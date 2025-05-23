import json
import requests
from datetime import datetime, timedelta
from config import BOT_TOKEN, CHAT_ID

def load_expenses():
    try:
        with open("data/expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def get_last_week_expenses(data):
    one_week_ago = datetime.now() - timedelta(days=7)
    weekly = [item for item in data if datetime.strptime(item["date"], "%Y-%m-%d") >= one_week_ago]
    return weekly

def format_report(expenses):
    if not expenses:
        return "No expenses were recorded this week."
    lines = [f"{item['date']}: {item['category']} — {item['amount']} сом" for item in expenses]
    total = sum(float(item["amount"]) for item in expenses)
    return f"Your weekly report:\n\n" + "\n".join(lines) + f"\n\nTotal: {total} сом"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    response = requests.post(url, data=payload)
    return response.status_code == 200

if __name__ == "__main__":
    expenses = load_expenses()
    weekly_expenses = get_last_week_expenses(expenses)
    report = format_report(weekly_expenses)
    success = send_telegram_message(report)
    
    if success:
        print("Report sent.")
    else:
        print("Failed to send report.")
        print("Full response from Telegram API:")
        print(report) 
