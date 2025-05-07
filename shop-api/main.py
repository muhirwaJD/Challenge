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


@app.get("/monthly-sales")
def monthly_sales():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT DATE_FORMAT(order_date, '%Y-%m') AS month, 
               SUM(oi.quantity * oi.unit_price) AS sales
        FROM orders o
        JOIN order_items oi ON o.order_id = oi.order_id
        WHERE status IN ('Shipped', 'Delivered')
        GROUP BY month
        ORDER BY month;
    """)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return [{"month": r[0], "sales": float(r[1])} for r in rows]


@app.get("/products-never-ordered")
def products_never_ordered():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT p.name
        FROM products p
        LEFT JOIN order_items oi ON p.product_id = oi.product_id
        WHERE oi.product_id IS NULL;
    """)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return [{"product_name": r[0]} for r in rows]


@app.get("/average-order-value-by-country")
def avg_order_value_by_country():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c.country, AVG(order_total) AS avg_order_value
        FROM (
            SELECT o.order_id, c.country, SUM(oi.quantity * oi.unit_price) AS order_total
            FROM orders o
            JOIN customers c ON o.customer_id = c.customer_id
            JOIN order_items oi ON o.order_id = oi.order_id
            GROUP BY o.order_id, c.country
        ) AS sub
        GROUP BY country;
    """)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return [{"country": r[0], "avg_order_value": float(r[1])} for r in rows]


@app.get("/frequent-buyers")
def frequent_buyers():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c.name, COUNT(o.order_id) AS order_count
        FROM customers c
        JOIN orders o ON c.customer_id = o.customer_id
        GROUP BY c.name
        HAVING order_count > 1;
    """)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return [{"name": r[0], "orders": r[1]} for r in rows]

