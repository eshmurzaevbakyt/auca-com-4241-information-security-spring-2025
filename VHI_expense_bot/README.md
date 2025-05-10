# VHI Expense Bot

This project is a personal expense tracking utility designed for users covered under a Voluntary Health Insurance (VHI) system. It allows users to log their medical expenses via a terminal interface or Telegram bot and receive a weekly summary report.

The project was developed as part of the **Information Security** course and is designed to improve transparency and responsibility in personal healthcare expense management.

---

## 📌 Features

- Add medical expenses (labs, medication, etc.) via terminal or Telegram
- Expenses stored in a local `JSON` database (`data/expenses.json`)
- Weekly expense reports are sent automatically via Telegram
- Categorize expenses and include payment method and notes
- Telegram bot support with `/add` command for quick entry
- Compatible with **Windows Task Scheduler** or **Linux cron** for scheduling

---

## 🧠 Project Structure

| File / Folder         | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| `expenses.py`          | Core logic for adding, viewing, deleting, and saving expenses              |
| `main.py`              | Telegram bot entry point for adding expenses via the `/add` command        |
| `send_report.py`       | Script that sends a weekly summary to your Telegram via bot API            |
| `config.py`            | Stores your `BOT_TOKEN` and `CHAT_ID` (Telegram credentials)               |
| `data/expenses.json`   | Local file database where all expenses are stored in JSON format           |
| `README.md`            | Project documentation (this file)                                          |

---

## ⚙️ How It Works

1. **Add an Expense**
   - Via terminal: run `expenses.py` and choose “Add new expense”
   - Via Telegram: send `/add <category> <amount> <YYYY-MM-DD>`, e.g.,  
     `/add Labs 1500 2024-05-10`

2. **View or Delete**
   - Terminal allows viewing and deleting previously entered expenses.

3. **Weekly Report**
   - `send_report.py` checks the last 7 days of expenses and sends a total summary to your Telegram.
   - Can be scheduled via **Task Scheduler** or **cron job**.

---

## 🛠️ Technologies Used

- **Python 3.10+**
- `python-telegram-bot`
- `requests` for API calls to Telegram
- `json` and `datetime` for local data handling
- **Windows Task Scheduler** or **Linux cron** (for scheduling report)

---

## 🛠️ Setup Instructions

1. **Install dependencies:**

   ```bash
   pip install python-telegram-bot requests

Demo Recording:
https://drive.google.com/file/d/1MmMg7C0TPpJBLGv2OsRRtVAWE4zfC6NE/view?usp=sharing
