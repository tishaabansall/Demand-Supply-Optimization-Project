from fastapi import FastAPI, Query
from app.services import run_gap_analysis, run_optimization
from app.schemas import PainZone, WorstHour
from typing import List

app = FastAPI(title="Demand–Supply Optimization API")


@app.get("/gap-analysis", response_model=dict[str, list])

def gap_analysis(
    zone: str | None = Query(default=None),
    hour: int | None = Query(default=None)
):
    result = run_gap_analysis()

    pain_zones = result["pain_zones"]
    worst_hours = result["worst_hours"]

    if zone:
        pain_zones = pain_zones[pain_zones["zone_id"] == zone]

    if hour:
        worst_hours = worst_hours[worst_hours["hour"] == hour]

    return {
        "pain_zones": pain_zones.to_dict(orient="records"),
        "worst_hours": worst_hours.to_dict(orient="records")
    }
