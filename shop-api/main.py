from fastapi import FastAPI
from db import get_connection

app = FastAPI()

@app.get("/top-customers")
def top_customers():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c.name, SUM(oi.quantity * oi.unit_price) AS total_spent
        FROM customers c
        JOIN orders o ON c.customer_id = o.customer_id
        JOIN order_items oi ON o.order_id = oi.order_id
        GROUP BY c.name
        ORDER BY total_spent DESC;
    """)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return [{"name": r[0], "total_spent": float(r[1])} for r in rows]

