from flask import Flask, render_template
from irrigation_logic import get_weather, should_irrigate
from firebase_logger import log_data, fetch_past_data
from telegram_notifier import send_alert
from config import BOT_TOKEN, CHAT_ID

app = Flask(__name__)

@app.route("/")
def home():
    try:
        temp, humidity, rainfall = get_weather()
        decision = should_irrigate(temp, humidity, rainfall)

        # Log to Firebase
        log_data(temp, humidity, rainfall, decision)

        # Send Telegram Alert
        msg = (
            f"🌾 Smart Irrigation Alert 🌾\n\n"
            f"🌡 Temperature: {temp}°C\n"
            f"💧 Humidity: {humidity}%\n"
            f"🌧 Rainfall: {rainfall} mm\n"
            f"🧠 AI Decision: {'Irrigate ✅' if decision else 'No Need ❌'}"
        )
        send_alert(BOT_TOKEN, CHAT_ID, msg)

    except Exception as e:
        print("❌ Error in processing:", e)
        temp = humidity = rainfall = 0
        decision = False

    # Fetch historical data
    past_data = fetch_past_data()
    print("📊 Fetched past data:", past_data)  # Debugging line

    return render_template(
        "index.html",
        temp=temp,
        humidity=humidity,
        rainfall=rainfall,
        decision=decision,
        past_data=past_data
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
