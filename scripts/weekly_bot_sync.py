#!/usr/bin/env python3
"""
Weekly Bot Sync - Sends status check to all bots in Bots chat.
Runs every Monday at 19:00 (cron).
"""

import subprocess
import sys
from datetime import datetime

def send_sync_message():
    """Send weekly sync request to all bots."""
    
    message = """🧙‍♂️ **Weekly Bot Sync - Monday 19:00**

Time to share what we've learned this week! I need:

@Admiral_Clawberg_bot (Luma):
  • Key achievements this week?
  • Any blockers or issues?
  • Top learnings to remember?

@Palaistina:
  • What have you been working on?
  • Major discoveries or changes?
  • Anything needing attention?

@RobotSam:
  • Status update?
  • Anything important happened?
  • What's next?

Format: Keep it concise (bullets work great). This helps us all stay aligned. 📊"""

    try:
        result = subprocess.run(
            [
                "message",
                "action=send",
                "channel=telegram",
                "target=-1003817355698",
                f"message={message}"
            ],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode == 0:
            print(f"[{datetime.now().isoformat()}] ✅ Weekly sync sent successfully")
            return True
        else:
            print(f"[{datetime.now().isoformat()}] ❌ Failed to send: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"[{datetime.now().isoformat()}] ❌ Error: {e}")
        return False

if __name__ == "__main__":
    success = send_sync_message()
    sys.exit(0 if success else 1)
