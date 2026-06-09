# Juice & Coffee — AI-powered Dashboard

This project contains a Streamlit dashboard for a coffee & juice shop, including a data generator that creates one year of realistic sales data.

Getting started

1. Create a Python environment (recommended).
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Generate the dataset:

```bash
python generate_data.py
```

4. Run the dashboard:

```bash
streamlit run app.py
```

Files

- `generate_data.py`: Generates `data/sales_2025.csv` with one year of orders.
- `app.py`: Streamlit dashboard with KPIs, charts, heatmap, and Prophet forecasting.
- `requirements.txt`: Python dependencies.

Notes

- Forecasting uses `prophet`. Installation may require build tools on some platforms.
- If you want a larger or smaller dataset, change `target_rows` in `generate_data.py`.
