import sqlite3

conn = sqlite3.connect("finance_data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS financials (
    company TEXT,
    revenue INTEGER,
    ebitda INTEGER,
    net_income INTEGER
)
""")

cursor.execute("INSERT INTO financials VALUES ('IBM', 60000000, 15000000, 8000000)")
cursor.execute("INSERT INTO financials VALUES ('AAPL', 120000000, 30000000, 22000000)")

conn.commit()
conn.close()