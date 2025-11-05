import json
from datetime import datetime
from pathlib import Path

DATA_PATH = Path("data/study_log.json")

def _load():
    if not DATA_PATH.exists():
        return {}
    try:
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

def _save(data):
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# 1️⃣ 아침: 목표 세우기
def set_goal(goal_hours: float, plan_list: list):
    data = _load()
    today = datetime.now().strftime("%Y-%m-%d")

    data[today] = {
        "goal_hours": goal_hours,
        "plan_list": [{"task": t, "done": False} for t in plan_list],
        "progress_hours": 0.0,
        "completed_tasks": [],
        "comment": "",
        "final_report": None
    }
    _save(data)
    print(f"✅ {today} 목표가 등록되었습니다!")

# 2️⃣ 공부 중: 공부 시간 추가 / 체크리스트 완료 처리
def add_progress(hours: float):
    data = _load()
    today = datetime.now().strftime("%Y-%m-%d")
    if today not in data:
        print("⚠️ 오늘 목표를 먼저 세워주세요.")
        return

    info = data[today]
    info["progress_hours"] += hours
    progress_rate = round((info["progress_hours"] / info["goal_hours"]) * 100, 1)
    _save(data)

    print(f"⏱️ 공부시간 누적: {info['progress_hours']}h / 목표 {info['goal_hours']}h ({progress_rate}%)")

def check_task(task_name: str):
    data = _load()
    today = datetime.now().strftime("%Y-%m-%d")
    if today not in data:
        print("⚠️ 오늘의 계획이 없습니다.")
        return

    for task in data[today]["plan_list"]:
        if task["task"] == task_name:
            task["done"] = True
            print(f"☑️ '{task_name}' 완료 처리되었습니다.")
            break
    else:
        print("⚠️ 해당 항목을 찾을 수 없습니다.")
    _save(data)

# 3️⃣ 마무리: 완료 목록 + 코멘트 기록 (시간 입력 X)
def finish_day(mood: str, focus: int, completed: list, comment: str):
    data = _load()
    today = datetime.now().strftime("%Y-%m-%d")
    if today not in data:
        print("⚠️ 오늘의 계획이 없습니다.")
        return

    info = data[today]
    info["completed_tasks"] = completed
    info["comment"] = comment

    info["final_report"] = {
        "actual_hours": info["progress_hours"],
        "mood": mood,
        "focus": focus
    }
    _save(data)
    print("🌙 하루 마무리가 저장되었습니다!")

# 보기
def get_today():
    today = datetime.now().strftime("%Y-%m-%d")
    return _load().get(today)

def get_all():
    return _load()
