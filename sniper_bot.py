import json
import os
import time
import requests

# ✅ Telegram Bot Setup
BOT_TOKEN = '8401879582:AAGO2bD1lMfK_RF9IijnTcSgzXtur_-KNC4'
CHAT_ID = '-1002884824123'  # Your channel ID: 'Future signal'

# 🗂️ All .json files (USDINR, USDBRL, etc.)
def get_json_files():
    return [file for file in os.listdir() if file.endswith('.json')]

# 📤 Send signal to Telegram
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {'chat_id': CHAT_ID, 'text': message}
    try:
        requests.post(url, data=data)
    except Exception as e:
        print("Telegram error:", e)

# 🔍 Check signals in each file
def check_signals():
    for file in get_json_files():
        try:
            with open(file, 'r') as f:
                data = json.load(f)

            if data and isinstance(data, dict):
                signal = data.get("signal")
                timestamp = data.get("time")

                if signal:
                    pair = file.replace(".json", "")
                    msg = f"""📡 *SNIPER SIGNAL ALERT*

📊 Pair: `{pair}`
📈 Signal: *{signal.upper()}*
⏱ Time: `{timestamp}`

#sniper #quotex #{pair.lower()}"""

                    print(f"Sending: {pair} - {signal}")
                    send_telegram_message(msg)

        except Exception as e:
            print(f"Error in {file}:", e)

# 🔁 Continuous check every 15 sec
while True:
    check_signals()
    time.sleep(15)
