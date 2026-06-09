"""Generate 1 year of realistic sales data for a coffee & juice shop.
Writes CSV to data/sales_2025.csv by default.
"""
import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

OUT_DIR = Path("data")
OUT_DIR.mkdir(exist_ok=True)
OUT_CSV = OUT_DIR / "sales_2025.csv"

MENU = [
    ("Espresso", "Coffee", 2.5),
    ("Americano", "Coffee", 3.0),
    ("Latte", "Coffee", 4.0),
    ("Cappuccino", "Coffee", 4.0),
    ("Cold Brew", "Coffee", 4.5),
    ("Mango Juice", "Juice", 3.5),
    ("Orange Juice", "Juice", 3.0),
    ("Green Detox", "Juice", 4.5),
    ("Berry Blast", "Juice", 4.0),
    ("Blueberry Muffin", "Bakery", 2.75),
    ("Croissant", "Bakery", 2.5),
    ("Bagel", "Bakery", 2.0),
    ("Ham Sandwich", "Savory", 5.5),
    ("Avocado Toast", "Savory", 6.0),
    ("Chai Tea", "Tea", 3.25),
    ("Matcha", "Tea", 4.25),
]

PAYMENT_METHODS = ["Card", "Cash", "Mobile Pay"]
CUSTOMER_TYPES = ["New", "Returning"]

def generate_year(start_date, end_date, target_rows=12000):
    rows = []
    order_id = 100000
    current = start_date
    # Generate variable number of orders per day to reach target_rows
    while current <= end_date:
        # More customers on weekends
        weekday = current.weekday()
        base_orders = 30 if weekday < 5 else 45
        orders_today = max(5, int(random.gauss(base_orders, base_orders * 0.25)))

        for _ in range(orders_today):
            order_id += 1
            # random order time between 6:00 and 20:00
            hour = random.choices(range(6, 21), weights=[1 if 8<=h<=10 or 12<=h<=14 or 16<=h<=18 else 0.6 for h in range(6,21)])[0]
            minute = random.randint(0, 59)
            second = random.randint(0, 59)
            ts = datetime.combine(current, datetime.min.time()) + timedelta(hours=hour, minutes=minute, seconds=second)

            # Each order has 1-3 different items
            line_items = random.randint(1, 3)
            for _ in range(line_items):
                item_name, category, price = random.choice(MENU)
                # quantity skewed towards 1
                quantity = random.choices([1,2,3], weights=[0.8,0.15,0.05])[0]
                total = round(price * quantity, 2)
                payment_method = random.choices(PAYMENT_METHODS, weights=[0.65, 0.25, 0.1])[0]
                customer_type = random.choices(CUSTOMER_TYPES, weights=[0.35, 0.65])[0]

                rows.append({
                    "date": ts.isoformat(sep=' '),
                    "order_id": str(order_id),
                    "item_name": item_name,
                    "category": category,
                    "quantity": quantity,
                    "price": f"{price:.2f}",
                    "total": f"{total:.2f}",
                    "payment_method": payment_method,
                    "customer_type": customer_type,
                })

        current += timedelta(days=1)

        # stop early if enough rows
        if len(rows) >= target_rows:
            break

    # If we undershot, add a bit more randomly until reaching target
    while len(rows) < target_rows:
        order_id += 1
        d = start_date + timedelta(days=random.randint(0, (end_date-start_date).days))
        hour = random.randint(6, 20)
        ts = datetime.combine(d, datetime.min.time()) + timedelta(hours=hour, minutes=random.randint(0,59))
        item_name, category, price = random.choice(MENU)
        quantity = random.choices([1,2,3], weights=[0.8,0.15,0.05])[0]
        total = round(price * quantity, 2)
        payment_method = random.choice(PAYMENT_METHODS)
        customer_type = random.choice(CUSTOMER_TYPES)
        rows.append({
            "date": ts.isoformat(sep=' '),
            "order_id": str(order_id),
            "item_name": item_name,
            "category": category,
            "quantity": quantity,
            "price": f"{price:.2f}",
            "total": f"{total:.2f}",
            "payment_method": payment_method,
            "customer_type": customer_type,
        })

    return rows


def write_csv(rows, path):
    fieldnames = ["date", "order_id", "item_name", "category", "quantity", "price", "total", "payment_method", "customer_type"]
    with open(path, "w", newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in rows:
            writer.writerow(r)


if __name__ == "__main__":
    start_date = datetime(2025, 1, 1).date()
    end_date = datetime(2025, 12, 31).date()
    print("Generating sales rows for", start_date, "->", end_date)
    rows = generate_year(start_date, end_date, target_rows=12000)
    print(f"Generated {len(rows)} rows — writing to {OUT_CSV}")
    write_csv(rows, OUT_CSV)
    print("Done.")
