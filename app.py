import streamlit as st
from modules.record_handler import (
    set_goal, add_progress, check_task, finish_day, get_today, get_all
)
from modules.feedback import feedback_today
from modules.visualizer import show_daily_summary, show_focus_trend
import io
import matplotlib.pyplot as plt
from modules.report import weekly_report, make_feedback
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

st.set_page_config(page_title="Smart Study Planner", layout="centered")

st.title("📘 Smart Study Planner Web")
st.caption("하루의 목표를 세우고, 공부 진행 상황을 기록하고, 마무리 리포트를 확인하세요.")

# 사이드바 메뉴
menu = st.sidebar.selectbox("메뉴 선택", [
    "오늘 목표 세우기",
    "공부 진행/체크",
    "하루 마무리",
    "오늘 피드백 보기",
    "시각화 보기",
    "누적 분석 보기",
    "📅 주간 리포트 보기"
])

from modules.record_handler import get_today, set_goal, get_all

if menu == "오늘 목표 세우기":
    st.header("🌞 오늘 목표 세우기")

    today_info = get_today()  # 오늘 데이터 불러오기
    if today_info:
        st.info("🔹 이미 오늘의 목표가 있습니다. 수정 후 '저장'을 누르면 갱신됩니다.")
        default_goal = today_info.get("goal_hours", 0.0)
        default_plans = ", ".join([p["task"] for p in today_info.get("plan_list", [])])
    else:
        default_goal = 0.0
        default_plans = ""

    # 기존 값 표시 (수정 가능)
    goal = st.number_input("🎯 목표 공부시간(시간)", 0.0, 24.0, step=0.5, value=default_goal)
    plan_text = st.text_area("📝 공부 계획 (쉼표로 구분)", value=default_plans)

    plans = [p.strip() for p in plan_text.split(",") if p.strip()]

    if st.button("💾 목표 저장 / 수정"):
        set_goal(goal, plans)
        st.success("✅ 오늘의 목표가 저장(또는 수정)되었습니다.")


elif menu == "공부 진행/체크":
    st.header("⏱️ 공부 진행 현황")

    if st.button("+0.5h 추가"):
        add_progress(0.5)
        today = get_today()
        st.success(f"0.5 시간 추가 완료 ✅ 누적 {today['progress_hours']} h / 목표 {today['goal_hours']} h")
    if st.button("+1h 추가"):
        add_progress(1.0)
        today = get_today()
        st.success(f"1.0 시간 추가 완료 ✅ 누적 {today['progress_hours']} h / 목표 {today['goal_hours']} h")

    st.divider()
    st.subheader("🎯 완료 체크")
    today = get_today()
    if not today:
        st.info("오늘 목표를 먼저 세워주세요.")
    else:
        for t in today["plan_list"]:
            if st.checkbox(t["task"], t["done"]):
                check_task(t["task"])

elif menu == "하루 마무리":
    st.header("🌙 하루 회고")
    mood = st.text_input("오늘 기분")
    focus = st.slider("집중도", 1, 10, 7)
    completed = st.text_area("오늘 마무리한 과제 (쉼표로)").split(",")
    completed = [c.strip() for c in completed if c.strip()]
    comment = st.text_area("한 줄 코멘트")
    if st.button("🌙 마무리 저장"):
        finish_day(mood, focus, completed, comment)
        st.success("마무리 저장 완료!")

elif menu == "오늘 피드백 보기":
    now = get_today()
    st.header("📋 오늘의 피드백")
    if now:
        st.text(feedback_today(now))
    else:
        st.info("오늘의 데이터가 없습니다.")

elif menu == "시각화 보기":
    st.header("📊 시각화")
    col1, col2 = st.columns(2)
    if col1.button("오늘 요약 보기"): show_daily_summary()
    if col2.button("집중도 추세 보기"): show_focus_trend()

elif menu == "누적 분석 보기":
    st.header("📈 누적 분석")
    from modules.analyzer import analyze_data
    import matplotlib.pyplot as plt
    import pandas as pd
    from modules.record_handler import get_all

    st.write("원하는 통계를 선택하세요:")
    col1, col2 = st.columns(2)
    with col1:
        show_avg = st.button("📊 평균 분석 보기")
    with col2:
        show_focus_graph = st.button("🎯 집중도 추세 보기")

    # 평균 분석 버튼 눌렀을 때
    if show_avg:
        res = analyze_data()
        if not res:
            st.warning("데이터가 충분하지 않습니다.")
        else:
            st.success(f"총 {res['days']}일 기록 | 평균 공부 {res['avg_hours']}h | 평균 집중도 {res['avg_focus']}")
        st.divider()

    # 집중도 그래프 버튼 눌렀을 때
    if show_focus_graph:
        data = get_all()
        rec = []
        for d, info in sorted(data.items()):
            if info.get("final_report"):
                rec.append({
                    "date": d,
                    "focus": info["final_report"]["focus"]
                })
        if rec:
            df = pd.DataFrame(rec)
            fig, ax = plt.subplots(figsize=(8, 4))
            ax.plot(df["date"], df["focus"], marker="o", color="#0077FF")
            ax.set_title("집중도 추세")
            ax.set_ylim(0, 10)
            plt.xticks(rotation=45)
            plt.tight_layout()
            st.pyplot(fig)
        else:
            st.warning("⚠️ 집중도 데이터가 없습니다.")

    st.divider()

elif menu == "📅 주간 리포트 보기":
    st.header("📅 주간 학습 리포트")

    res = weekly_report()
    if not res:
        st.warning("데이터가 충분하지 않습니다.")
    else:
        summary, df = res
        fb = make_feedback(summary)
        st.text(fb)

        # --- 그래프 ---
        st.subheader("📈 공부시간 & 집중도 추세")
        fig, ax1 = plt.subplots(figsize=(8, 4))
        ax1.plot(df["date"], df["hours"], marker="o", color="#4CBB17", label="공부시간(h)")
        ax1.set_ylabel("공부시간(시간)")
        ax2 = ax1.twinx()
        ax2.plot(df["date"], df["focus"], marker="s", color="#0077FF", label="집중도(1~10)")
        ax2.set_ylabel("집중도")

        ax1.set_xticklabels(df["date"], rotation=45)
        fig.legend(loc="upper left")
        st.pyplot(fig)

    if st.button("🏠 메인으로 돌아가기"):
        st.experimental_rerun()
