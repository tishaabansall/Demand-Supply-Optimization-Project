
## Demand–Supply Optimization Project

A Python project to analyze ride demand and optimize driver allocation across urban zones. Includes APIs to query demand gaps, pain zones, worst hours, and optimized driver movements, plus visualization of driver reallocations.

---

## Features

- **Gap Analysis**: Identify zones and hours with demand–supply gaps.
- **Pain Zones**: Rank zones with the highest shortage.
- **Worst Hours**: Identify peak hours with highest demand gaps.
- **Driver Optimization**: Simulate driver reallocation from surplus to deficit zones.
- **Visualization**: Plot driver movements per hour using bar charts.
- **FastAPI Backend**: Expose `/gap-analysis` and `/optimize` APIs for querying results.

---

## Tech Stack
- Python 3.13+
- Pandas
- NumPy
- Matplotlib
- FastAPI
- Uvicorn

---

## Installation
1. Clone the repository:
```bash
   git clone <your-repo-url>
   cd <your-repo-folder>
```
2.Install required libraries:
```bash
pip install pandas matplotlib
```
---

## Visualisation

1.Run the Python script:
```bash
   python visualize_movement.py
```
2.The script will display all available hours:
```bash
    Available hours:[0, 1, 2, ... , 23]
```
3.Enter the hour you want to visualize (e.g., 15 for 3 PM)

4.A bar chart will be displayed showing driver movements from source to destination zones.

---

## Running the Backend
Start the FastAPI server:
```bash
python -m uvicorn app.main:app --reload
```

## API Endpoints
1. Gap Analysis
```bash
GET /gap-analysis
```
Query by zone:
```bash
http://127.0.0.1:8000/gap-analysis?zone=Central
```
Returns JSON containing:

- gap_table: predicted demand vs available supply
- pain_zones: zones with highest shortages
- worst_hours: hours with highest demand gaps

2. Optimized Driver Allocation
```bash
GET /optimize
```

Query by hour:
```bash
http://127.0.0.1:8000/optimize?hour=9
```
Returns JSON with driver reallocations for the chosen hour:
- hour
- source_zone
- destination_zone
- drivers_moved

---

## Project Structure
```text
# Project Structure

UNTITLED (WORKSPACE)/
├── demand_supply/
│   ├── analysis/
│   │   ├── __init__.py
│   │   ├── gap_analysis.py
│   │   └── run_gap_analysis.py
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── schemas.py
│   │   └── services.py
│   ├── data/
│   │   ├── urban_logistics.csv
│   │   ├── with_predictions.csv
│   │   ├── zone_distances.csv
│   │   └── zone_request.csv
│   ├── forecast/
│   │   ├── baseline.py
│   │   └── ml_model.py
│   ├── optimization/
│   │   ├── __init__.py
│   │   ├── distances.py
│   │   ├── optimize_allocation.py
│   │   ├── reallocate.py
│   │   └── run_optimize_allocation.py
│   └── outputs/
│       ├── allocation_comparison.csv
│       └── optimized_allocation.csv
├── scripts/
│   ├── generate_data.py
│   ├── generate_zone_distances.py
|
└── compare_allocation.py
|
└── visualize_movement.py
```
---

## License

This project is open-source and free to use.