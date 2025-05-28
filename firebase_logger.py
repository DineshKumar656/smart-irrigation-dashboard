import requests
import datetime
from config import FIREBASE_URL

def log_data(temp, humidity, rainfall, irrigate):
    timestamp = datetime.datetime.now().isoformat()
    data = {
        "timestamp": timestamp,
        "temperature": temp,
        "humidity": humidity,
        "rainfall": rainfall,
        "irrigate": irrigate
    }

    try:
        response = requests.post(FIREBASE_URL, json=data)
        if response.status_code == 200:
            print("✅ Data logged to Firebase.")
        else:
            print(f"❌ Firebase logging failed. Status code: {response.status_code}")
    except Exception as e:
        print(f"⚠️ Firebase log error: {e}")

def fetch_past_data():
    try:
        response = requests.get(FIREBASE_URL)
        if response.status_code == 200:
            data = response.json()
            if not data:
                return []
            records = sorted(data.values(), key=lambda x: x.get("timestamp", ""))
            return records
        else:
            print("❌ Failed to fetch Firebase data")
            return []
    except Exception as e:
        print(f"⚠️ Error fetching data: {e}")
        return []
