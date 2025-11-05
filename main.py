from modules.record_handler import (
    set_goal, add_progress, check_task, finish_day, get_today, get_all
)
from modules.analyzer import analyze_data
from modules.feedback import feedback_today
import os, time
from modules.visualizer import show_daily_summary, show_focus_trend

def clear(): os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print("""
[1] 오늘 목표 세우기
[2] 공부시간 추가
[3] 목표 완료 체크
[4] 하루 마무리 (코멘트 작성)
[5] 오늘 현황 및 피드백 보기
[6] 누적 분석
[7] 시각화 보기 📊
[0] 종료
""")


def main():
    while True:
        clear()
        print("📘 SMART STUDY PLANNER v3.2")
        print("="*45)
        menu()
        sel = input("👉 메뉴 선택: ")

        if sel == "1":
            goal = float(input("🎯 목표 공부시간(시간): "))
            plans = [x.strip() for x in input("📝 공부 계획(쉼표로 구분): ").split(",") if x.strip()]
            set_goal(goal, plans)
            input("\n[Enter] 계속...")

        elif sel == "2":
            hrs = float(input("추가 공부시간(시간): "))
            add_progress(hrs)
            input("\n[Enter] 계속...")

        elif sel == "3":
            task = input("완료한 과제 이름: ")
            check_task(task)
            input("\n[Enter] 계속...")

        elif sel == "4":
            mood = input("🙂 오늘 기분: ")
            focus = int(input("🎯 집중도(1~10): "))
            completed = [c.strip() for c in input("🏁 오늘 마무리한 과제(쉼표로): ").split(",") if c.strip()]
            comment = input("📝 오늘 한줄 코멘트: ")
            finish_day(mood, focus, completed, comment)
            input("\n[Enter] 계속...")

        elif sel == "5":
            today = get_today()
            print("\n" + feedback_today(today))
            input("\n[Enter] 계속...")

        elif sel == "6":
            res = analyze_data()
            if not res:
                print("데이터가 충분하지 않습니다.")
            else:
                print(f"📈 {res['days']}일 기록 | 평균 공부 {res['avg_hours']}h | 집중도 {res['avg_focus']}")
            input("\n[Enter] 계속...")

        elif sel == "7":
            print("""
[1] 오늘 요약 보기
[2] 집중도 추세 보기
""")
            sub = input("👉 선택: ")
            if sub == "1":
                show_daily_summary()
            elif sub == "2":
                show_focus_trend()
            else:
                print("⚠️ 잘못된 입력입니다.")
            input("\n[Enter] 계속...")


        elif sel == "0":
            print("👋 종료합니다.")
            break

        else:
            print("⚠️ 잘못된 입력입니다.")
            time.sleep(1)

if __name__ == "__main__":
    main()
