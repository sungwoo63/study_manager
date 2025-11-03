from modules.record_handler import record_study_session
from modules.analyzer import analyze_data
from modules.feedback import generate_feedback

def main_menu():
    print("\n=== Smart Study Manager ===")
    print("1. 공부 기록 추가")
    print("2. 데이터 분석 및 피드백 보기")
    print("0. 종료")

def main():
    while True:
        main_menu()
        choice = input("메뉴 선택: ")

        if choice == "1":
            hours = float(input("오늘 공부시간(단위: 시간): "))
            mood = input("오늘 기분(한 단어로): ")
            focus = int(input("오늘 집중도(1~10): "))
            record_study_session(hours, mood, focus)

        elif choice == "2":
            result = analyze_data()
            fb = generate_feedback(result)
            print(fb)

        elif choice == "0":
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 입력입니다. 다시 선택하세요.")

if __name__ == "__main__":
    main()
