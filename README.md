Here’s your full `README.md` file, ready to copy-paste or create in your project:

---

```markdown
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

## 📂 Folder Structure

```

shop-api/
├── main.py              # Main FastAPI app
├── db.py                # DB connection config
├── .env                 # Environment variables (hidden)
├── requirements.txt     # Python dependencies
├── shop-queries.sql     # SQL to create and seed DB
└── README.md            # This file

````

---

## 🔐 Environment Variables

Your sensitive information (DB host, user, password, name) is stored in a `.env` file and **should not be pushed to GitHub**.

Example:
```env
DB_HOST=your-db-name.rds.amazonaws.com
DB_USER=admin
DB_PASSWORD=yourpassword
DB_NAME=shop
````

---

## ▶️ How to Start the App (on EC2)

```bash
# Activate your environment
source .venv/bin/activate

# Start the API on port 8000
uvicorn main:app --host 0.0.0.0 --port 8000
```

To keep it running in the background:

```bash
tmux new -s api
uvicorn main:app --host 0.0.0.0 --port 8000
# Then press CTRL+B then D to detach
```

---

## 📸 Screenshots

Find all screenshots for database setup, queries, and API responses in the `screenshots/` folder.

---

## 📤 Deployment Notes

* The EC2 instance must allow inbound traffic on port **8000**.
* The RDS MySQL DB must allow the EC2 to connect (correct VPC, SG, credentials).
* Use `tmux` or `screen` to keep the app running in background.

---

## 🧑‍🏫 Facilitator Notes

Dear facilitator,
You can access the API live via the Swagger UI link above and run the different GET endpoints as listed.
Let me know if login or DB access is needed — I'm happy to provide.

---

````

### ✅ What to do next:

1. Create the file:
   ```bash
   vi README.md
````

2. Paste the content and save (`:wq`)

3. Commit it:

   ```bash
   git add README.md
   git commit -m "Add project README"
   git push
   ```
