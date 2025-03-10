import duckdb
import os
import requests
from datetime import datetime, timedelta

SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")  

def send_alert(message):
    """Prints alert to console and optionally sends to Slack."""
    print(message)  # Console alert
    if SLACK_WEBHOOK_URL:
        requests.post(SLACK_WEBHOOK_URL, json={"text": message})

def check_balance_changes(db_path="my_database.db"):
    """Checks for >50% total balance change in DuckDB between yesterday and the day before."""
    con = duckdb.connect(db_path)
    # Get yesterday and the day before yesterday's dates
    yesterday = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')
    day_before_yesterday = (datetime.today() - timedelta(days=2)).strftime('%Y-%m-%d')

    query = f"""
    WITH daily_totals AS (
        SELECT 
            transaction_date_day,
            SUM(total_amount) AS total_balance
        FROM my_database.main.fact_daily_balances
        WHERE transaction_date_day IN ('{yesterday}', '{day_before_yesterday}')
        GROUP BY transaction_date_day
    )
    SELECT 
        MAX(CASE WHEN transaction_date_day = '{yesterday}' THEN total_balance END) AS yesterday_balance,
        MAX(CASE WHEN transaction_date_day = '{day_before_yesterday}' THEN total_balance END) AS day_before_balance
    FROM daily_totals;
    """
    
    result = con.execute(query).fetchone()
    yesterday_balance, day_before_balance = result
    if yesterday_balance is None or day_before_balance is None:
        print("⚠️ Not enough data for comparison.")
        return

    # Calculate % change
    balance_change_pct = ((yesterday_balance - day_before_balance) / day_before_balance) * 100

    # Alert if change is greater than 50%
    if abs(balance_change_pct) > 0:
        alert_msg = (
            f"⚠️ Alert! Total balance changed {balance_change_pct:.2f}% "
            f"from {day_before_balance} to {yesterday_balance} between {day_before_yesterday} and {yesterday}."
        )
    send_alert(alert_msg)

    con.close()

if __name__ == "__main__":
    check_balance_changes()
