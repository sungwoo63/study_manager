import json
from datetime import datetime
from pathlib import Path

# 데이터 파일 경로
DATA_PATH = Path("data/study_log.json")

def load_data():
    """기존 데이터 불러오기"""
    if DATA_PATH.exists():
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_data(data):
    """데이터 저장"""
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def record_study_session(hours, mood, focus):
    """새로운 공부 세션 기록"""
    data = load_data()
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data[date] = {
        "hours": hours,
        "mood": mood,
        "focus": focus
    }

    save_data(data)
    print(f"✅ 기록 완료: {date} | {hours}시간 | 집중도: {focus}")
