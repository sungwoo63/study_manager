import pandas as pd
from modules.record_handler import load_data

def analyze_data():
    """저장된 학습 데이터를 pandas로 분석"""
    data = load_data()

    if not data:
        print("⚠️ 아직 기록된 데이터가 없습니다.")
        return None

    df = pd.DataFrame(data).T
    df["hours"] = df["hours"].astype(float)
    df["focus"] = df["focus"].astype(int)

    result = {
        "total_days": len(df),
        "avg_focus": round(df["focus"].mean(), 2),
        "avg_hours": round(df["hours"].mean(), 2),
        "max_focus_day": df["focus"].idxmax(),
        "min_focus_day": df["focus"].idxmin()
    }

    return result
