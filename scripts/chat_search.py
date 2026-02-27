#!/usr/bin/env python3
"""
Search the Telegram message database.

Usage:
    python chat_search.py --query "docker setup"          # Full-text search all chats
    python chat_search.py --chat "Bots" --days 7          # Recent messages from a chat
    python chat_search.py --chat "Bots" --query "deploy"  # Search within a chat
    python chat_search.py --sender "Gustav" --days 3      # Messages from a person
    python chat_search.py --chats                         # List all tracked chats
    python chat_search.py --stats                         # Message counts per chat
"""

import argparse
import sqlite3
import sys
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path

# Ensure UTF-8 output regardless of locale
os.environ.setdefault("PYTHONIOENCODING", "utf-8")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

DEFAULT_DB = Path(__file__).parent.parent / "services" / "telegram-logger" / "messages.db"


def get_db(db_path: str) -> sqlite3.Connection:
    db = sqlite3.connect(db_path)
    db.row_factory = sqlite3.Row
    return db


def list_chats(db):
    rows = db.execute("SELECT chat_id, chat_name, chat_type, last_seen FROM chats ORDER BY last_seen DESC").fetchall()
    if not rows:
        print("No chats tracked yet.")
        return
    for r in rows:
        print(f"  {r['chat_name']:30s}  id={r['chat_id']}  type={r['chat_type']}  last={r['last_seen'][:10] if r['last_seen'] else '?'}")


def show_stats(db):
    rows = db.execute("""
        SELECT chat_name, COUNT(*) as cnt, MIN(timestamp) as first, MAX(timestamp) as last
        FROM messages GROUP BY chat_id ORDER BY cnt DESC
    """).fetchall()
    if not rows:
        print("No messages yet.")
        return
    for r in rows:
        first = r['first'][:10] if r['first'] else '?'
        last = r['last'][:10] if r['last'] else '?'
        print(f"  {r['chat_name']:30s}  {r['cnt']:6d} msgs  ({first} → {last})")


def search(db, query=None, chat=None, sender=None, days=None, limit=30, bots_only=False):
    conditions = []
    params = []

    if chat:
        conditions.append("m.chat_name LIKE ?")
        params.append(f"%{chat}%")

    if sender:
        conditions.append("m.sender_name LIKE ?")
        params.append(f"%{sender}%")

    if days:
        cutoff = (datetime.now(timezone.utc) - timedelta(days=days)).isoformat()
        conditions.append("m.timestamp > ?")
        params.append(cutoff)

    if bots_only:
        conditions.append("m.is_bot = 1")

    if query:
        # Use FTS5 for full-text search
        conditions.append("m.id IN (SELECT rowid FROM messages_fts WHERE messages_fts MATCH ?)")
        params.append(query)

    where = "WHERE " + " AND ".join(conditions) if conditions else ""
    params.append(limit)

    sql = f"""
        SELECT m.chat_name, m.sender_name, m.is_bot, m.text, m.timestamp, m.media_type
        FROM messages m
        {where}
        ORDER BY m.timestamp DESC
        LIMIT ?
    """

    rows = db.execute(sql, params).fetchall()
    if not rows:
        print("No messages found.")
        return

    # Print newest first but display in chronological order
    for r in reversed(rows):
        ts = r['timestamp'][:16].replace('T', ' ') if r['timestamp'] else '?'
        bot_tag = " [BOT]" if r['is_bot'] else ""
        name = r['sender_name'] or "Unknown"
        chat = r['chat_name'] or "?"
        text = (r['text'] or "").replace('\n', ' ')[:120]
        media = f" [{r['media_type']}]" if r['media_type'] and not text else ""
        print(f"[{ts}] [{chat}] {name}{bot_tag}: {text}{media}")


def main():
    parser = argparse.ArgumentParser(description="Search Telegram message database")
    parser.add_argument("--query", "-q", help="Full-text search query")
    parser.add_argument("--chat", "-c", help="Filter by chat name (partial match)")
    parser.add_argument("--sender", "-s", help="Filter by sender name (partial match)")
    parser.add_argument("--days", "-d", type=int, help="Only messages from last N days")
    parser.add_argument("--limit", "-l", type=int, default=30, help="Max results (default: 30)")
    parser.add_argument("--bots", action="store_true", help="Only show bot messages")
    parser.add_argument("--chats", action="store_true", help="List all tracked chats")
    parser.add_argument("--stats", action="store_true", help="Show message counts per chat")
    parser.add_argument("--db", default=str(DEFAULT_DB), help="Database path")
    args = parser.parse_args()

    if not Path(args.db).exists():
        print(f"Database not found: {args.db}")
        print("Has the telegram-logger service been started?")
        sys.exit(1)

    db = get_db(args.db)

    if args.chats:
        list_chats(db)
    elif args.stats:
        show_stats(db)
    else:
        search(db, query=args.query, chat=args.chat, sender=args.sender,
               days=args.days, limit=args.limit, bots_only=args.bots)


if __name__ == "__main__":
    main()
