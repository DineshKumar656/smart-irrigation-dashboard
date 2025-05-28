# telegram_notifier.py

import requests
from config import BOT_TOKEN, CHAT_ID

def send_alert(bot_token=BOT_TOKEN, chat_id=CHAT_ID, message="No message provided"):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML"
    }

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("✅ Telegram alert sent.")
        else:
            print(f"❌ Failed to send Telegram alert. Status code: {response.status_code}")
    except Exception as e:
        print(f"⚠️ Telegram error: {e}")
