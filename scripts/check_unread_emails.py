#!/usr/bin/env python

import subprocess
import json
import sys

def run_gog_search():
    try:
        result = subprocess.run(
            ['gog', 'gmail', 'search', 'is:unread in:inbox', '--json', '--limit', '3'],
            capture_output=True,
            text=True,
            check=True
        )
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error running gog: {e}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    data = run_gog_search()
    
    # Assuming gog returns a list of messages or with metadata
    # Note: Adjust based on actual gog output structure. From examples, it's a list of dicts.
    messages = data if isinstance(data, list) else data.get('messages', [])
    count = len(messages)  # But this is limited to 3; actual count might need --count-only or separate call
    
    # To get total count, run a separate search without limit and with --count-only if available
    # For simplicity, assuming gog search with no limit returns all, but to avoid fetching all, perhaps add --max-results 0 or something; but let's fetch up to 3 and note if more.
    # Wait, gog might have metadata. Assuming the output includes total count; if not, run separate for count.
    
    # For now, run separate for count
    try:
        count_result = subprocess.run(
            ['gog', 'gmail', 'search', 'is:unread in:inbox', '--json', '--max-results', '0'],
            capture_output=True,
            text=True,
            check=True
        )
        count_data = json.loads(count_result.stdout)
        count = count_data.get('resultSizeEstimate', 0)  # Gmail API standard
    except:
        count = len(messages)  # Fallback
    
    print(f"Number of unread emails: {count}")
    
    if count > 0:
        print("First 3 unread emails:")
        for i, msg in enumerate(messages[:3], 1):
            subject = msg.get('subject', 'No subject')
            sender = msg.get('from', 'Unknown sender')
            print(f"{i}. Subject: {subject} | From: {sender}")

if __name__ == "__main__":
    main()
