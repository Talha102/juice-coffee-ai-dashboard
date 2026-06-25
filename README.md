# ☕🧃 Juice & Coffee AI Dashboard

> A real-time sales analytics dashboard for a coffee and juice shop business — built to turn raw sales numbers into decisions, not just charts.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 🧐 What Problem Does This Solve?

If you ask most small cafe owners "what was your best-selling item last month?" or "which day of the week is your busiest?", the honest answer is usually a guess. The data to answer those questions properly exists — it's sitting in receipts, registers, and memory — it's just never been organized in a way that's quick to look at.

This dashboard takes raw sales data and turns it into a single screen that answers the questions a business owner actually asks every day: *How much did we make? What's selling? When are we busiest? What should we focus on?*

---

## ✨ Features

- **KPI Cards** — Total revenue, total orders, and best-selling item, visible the moment the dashboard loads
- **Date Range Filter** — Look at any custom time period, from a single day to the full sales history
- **Category Filter** — Break the view down by Coffee, Juice, or see everything combined
- **Daily Sales Trend Chart** — An interactive line chart showing revenue fluctuation day by day
- **Monthly Revenue Chart** — A higher-level view for spotting seasonal patterns month over month
- **Top 10 Items Chart** — Instantly see which products are actually driving the business
- **Clean, Dark, Professional UI** — Designed to look and feel like a real product dashboard, not a spreadsheet

---

## 🛠️ Built With

| Technology | Purpose |
|---|---|
| **Python 3.12** | Core language |
| **Streamlit** | Interactive web dashboard framework |
| **Pandas** | Data processing and aggregation |
| **Plotly** | Interactive, hover-friendly charts |

---

## 📁 Project Structure

```
juice-coffee-ai-dashboard/
│
├── app.py                  # Main Streamlit dashboard application
├── generate_data.py        # Generates a year of realistic sample sales data
├── requirements.txt        # Python dependencies
│
└── data/
    └── sales_2025.csv       # Sales records (date, item, quantity, revenue, etc.)
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or higher
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/Talha102/juice-coffee-ai-dashboard.git
cd juice-coffee-ai-dashboard

# Install dependencies
pip install -r requirements.txt

# Generate sample data (if not already present)
python generate_data.py

# Launch the dashboard
streamlit run app.py
```

The dashboard will open automatically in your browser at `http://localhost:8501`.

---

## 📊 Sample Data

The bundled dataset simulates roughly six months of daily sales for a combined coffee and juice menu — including items like Mango Juice, Orange Juice, Lemonade, Watermelon Juice, and classic coffee drinks — with realistic day-to-day variation so the charts tell a believable story rather than a flat line.

---

## 🔮 Roadmap — What's Next

- [ ] Add a sales forecasting page (predicting the next 30 days using Prophet or a similar model)
- [ ] Peak-hours heatmap (hour of day vs. day of week)
- [ ] Connect to live POS data instead of a static CSV
- [ ] Add a downloadable PDF/Excel report export
- [ ] Customer segmentation (new vs. returning) once that data is captured

---

## 🔗 Related Project

This dashboard is the analytics counterpart to **[InvenAI](https://github.com/Talha102/inventory-management-ai)** — a smart inventory management system built for the same kind of business. Together, they're designed to eventually form one connected view of a cafe's operations: what's selling (this project) and what needs to be restocked (InvenAI).

---

## 👤 About the Builder

Built by **Talha Akram** — combining hands-on cafe operations experience (including international experience at Ole & Steen, London) with a growing data science and AI skillset, to build tools that solve problems real small businesses actually face.

---

## 📝 License

This project is open for learning and adaptation. Built as part of an ongoing journey into AI-powered business tools for Pakistani small businesses.

---

*Made with ☕, 🧃, and a lot of `streamlit run app.py`*
