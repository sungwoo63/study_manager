import pandas as pd
from modules.record_handler import get_all

def analyze_data():
    data = get_all()
    if not data:
        return None

    records = []
    for date, info in data.items():
        if info.get("final_report"):
            r = info["final_report"]
            records.append({
                "date": date,
                "goal": info["goal_hours"],
                "actual": r["actual_hours"],
                "focus": r["focus"],
                "mood": r["mood"]
            })

    if not records:
        return None

    df = pd.DataFrame(records)
    res = {
        "days": len(df),
        "avg_hours": round(df["actual"].mean(), 2),
        "avg_focus": round(df["focus"].mean(), 2)
    }
    return res
