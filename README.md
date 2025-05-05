# To visit the URL Click on this link:
[link text](http://18.203.67.253:8000/docs) 

# 🛒 Shop API – FastAPI + MySQL (AWS RDS)

This project is a simple REST API built using **FastAPI** and connected to a **MySQL database on AWS RDS**. It allows querying useful business data like top customers, monthly sales, and more.

---

## 🔗 Live API Access

You can test the API endpoints directly from the browser or using Postman:

📍 **Swagger UI**:  
http://YOUR_PUBLIC_EC2_IP:8000/docs

Replace `YOUR_PUBLIC_EC2_IP` with your EC2's public IPv4 address (e.g. `http://18.203.67.253:8000/docs`)

---

## ⚙️ How It Works

- **Backend Framework**: FastAPI
- **Database**: MySQL hosted on AWS RDS
- **Host**: EC2 instance (Ubuntu)
- **Running in background**: using `tmux` and `uvicorn`

---

## 📦 API Endpoints

Here are the implemented routes:

| Endpoint                 | Description                             |
|--------------------------|-----------------------------------------|
| `/top-customers`         | Get top customers by spending           |
| `/monthly-sales`         | Show sales report for each month        |
| `/products-never-ordered`| List products that were never ordered   |
| `/average-order-value`   | Average order value by country          |
| `/frequent-buyers`       | Customers with more than 1 order        |

Test them easily in the Swagger UI: `/docs`

---


---

## 🔐 Environment Variables

Your sensitive information (DB host, user, password, name) is stored in a `.env` file and **should not be pushed to GitHub**.

Example:
```env
DB_HOST=your-db-name.rds.amazonaws.com
DB_USER=admin
DB_PASSWORD=yourpassword
DB_NAME=shop
```
## ▶️ How to Start the App (on EC2)
```
# Activate your environment
source .venv/bin/activate

# Start the API on port 8000
uvicorn main:app --host 0.0.0.0 --port 8000

```

### To keep it running in the background:
```
tmux new -s api
uvicorn main:app --host 0.0.0.0 --port 8000
# Then press CTRL+B then D to detach
```
