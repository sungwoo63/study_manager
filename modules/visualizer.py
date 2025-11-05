import matplotlib.pyplot as plt
import pandas as pd
from modules.record_handler import get_all
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import streamlit as st

plt.rcParams['font.family'] = 'Malgun Gothic'  # 한글 폰트
plt.rcParams['axes.unicode_minus'] = False      # 마이너스 깨짐 방지


def show_daily_summary(date=None):
    data = get_all()
    if not data:
        st.warning("⚠️ 데이터가 없습니다.")
        return

    if not date:
        date = sorted(list(data.keys()))[-1]

    info = data[date]
    goal = info.get("goal_hours", 0)
    actual = info.get("progress_hours", 0)
    rate = (actual / goal * 100) if goal else 0
    plans = info.get("plan_list", [])
    done = len([t for t in plans if t["done"]])
    complete_rate = (done / len(plans) * 100) if plans else 0

    fig, ax = plt.subplots(1, 2, figsize=(8, 4))
    ax[0].bar(["목표", "실제"], [goal, actual], color=["#FFB347", "#47B39C"])
    ax[0].set_title(f"공부시간 ({rate:.1f}%)")
    ax[1].bar(["계획수", "완료수"], [len(plans), done],
              color=["#87CEFA", "#1976D2"])
    ax[1].set_title(f"완료율 {complete_rate:.1f}%")
    plt.tight_layout()

    st.pyplot(fig)


def show_focus_trend():
    data = get_all()
    if not data:
        st.warning("⚠️ 데이터가 없습니다.")
        return

    rec = []
    for d, info in sorted(data.items()):
        if info.get("final_report"):
            rec.append({
                "date": d,
                "focus": info["final_report"]["focus"]
            })
    if not rec:
        st.warning("집중도 데이터가 없습니다.")
        return

    df = pd.DataFrame(rec)
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(df["date"], df["focus"], marker="o", color="#0077FF")
    ax.fill_between(df["date"], df["focus"], color="#CFE2FF", alpha=0.4)
    ax.set_title("집중도 추세")
    ax.set_ylim(0, 10)
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)

