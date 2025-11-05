import pandas as pd
from datetime import datetime, timedelta
from modules.record_handler import get_all

def get_week_range(data, weeks=1):
    """데이터에서 최근 n주간(기본 1주) 범위 가져오기"""
    dates = sorted(list(data.keys()))
    if not dates:
        return []
    latest_date = datetime.strptime(dates[-1], "%Y-%m-%d")
    start_date = latest_date - timedelta(days=(7 * weeks) - 1)
    return [d for d in dates if datetime.strptime(d, "%Y-%m-%d") >= start_date]

def weekly_report(weeks: int = 1):
    """최근 주간 리포트 데이터 반환 (dict)"""
    data = get_all()
    if not data:
        return None

    selected_dates = get_week_range(data, weeks)
    if not selected_dates:
        return None

    records = []
    for d in selected_dates:
        info = data[d]
        total = info.get("progress_hours", 0)
        focus = 0
        if info.get("final_report"):
            focus = info["final_report"].get("focus", 0)
        records.append({"date": d, "hours": total, "focus": focus})

    df = pd.DataFrame(records)
    if df.empty:
        return None

    avg_hours = round(df["hours"].mean(), 2)
    avg_focus = round(df["focus"].mean(), 2)
    max_focus_day = df.loc[df["focus"].idxmax()]["date"]
    best_focus = df["focus"].max()

    summary = {
        "range": (selected_dates[0], selected_dates[-1]),
        "avg_hours": avg_hours,
        "avg_focus": avg_focus,
        "best_day": max_focus_day,
        "best_focus": best_focus,
        "days": len(df)
    }

    return summary, df

def make_feedback(summary):
    """요약 정보 기반 간단 피드백 문장 생성"""
    if not summary:
        return "데이터가 충분하지 않습니다."

    avg_f = summary["avg_focus"]
    best_day = summary["best_day"]

    if avg_f >= 8:
        comment = "집중력이 아주 훌륭했던 주였습니다!"
    elif avg_f >= 6:
        comment = "꾸준한 패턴을 잘 유지했어요."
    else:
        comment = "조금 지쳐 보이는 한 주네요. 충분히 쉬어가는 타이밍이에요!"

    return (
        f"📅 {summary['range'][0]} ~ {summary['range'][1]} ({summary['days']}일간)\n"
        f"평균 공부시간 {summary['avg_hours']} 시간, 평균 집중도 {summary['avg_focus']}\n"
        f"🎯 가장 집중한 날: {best_day} ({summary['best_focus']}점)\n\n💬 {comment}"
    )
