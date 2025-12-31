from pydantic import BaseModel


class PainZone(BaseModel):
    zone_id: str
    total_shortage: float
    avg_shortage: float
    shortage_hours: int


class WorstHour(BaseModel):
    hour: int
    demand_gap: float
