# 🧠 Smart Study Manager  
> 개인의 학습 데이터를 기반으로 패턴을 분석하고 피드백을 제공하는 AI 기반 학습 관리 시스템  

---

## 📑 프로젝트 개요
**Smart Study Manager**는  
사용자의 공부 시간, 집중도, 기분 데이터를 기록하고  
이를 바탕으로 **자신의 학습 패턴을 분석**하여  
AI 기반 맞춤형 피드백을 제공하는 프로젝트입니다.  

이 프로젝트는 이후 개발될 **“Personal AI Manager (J.A.R.V.I.S)”**의  
첫 번째 단계인 ‘**기억(Memory) 시스템**’ 역할을 합니다.

---

## 🧩 주요 기능

| 기능 | 설명 |
|------|------|
| 🕒 **기록(Record)** | 날짜별 공부 시간, 기분, 집중도 기록 |
| 🔍 **분석(Analyze)** | pandas를 이용한 평균 집중도·학습시간 통계 |
| 💬 **피드백(Feedback)** | 규칙 기반 “AI 조언” 메시지 출력 |
| 📊 **시각화(Visualization)** | matplotlib으로 집중도 & 공부시간 변화 그래프 표시 |
| 💾 **데이터 저장** | JSON 기반 학습 데이터 자동 저장 / 불러오기 |

---

## 🛠️ 기술 스택

| 분류 | 사용 기술 |
|------|------------|
| 언어 | Python 3.11 |
| 데이터 처리 | pandas |
| 시각화 | matplotlib, seaborn |
| 구조 설계 | 모듈형 설계 (record / analyze / feedback / visualize) |
| 실행 환경 | VS Code, Git Bash |
| 버전 관리 | Git + GitHub |

---

## 🧱 프로젝트 구조

study_manager/
│
├── main.py # 메인 실행부
├── requirements.txt
├── README.md
│
├── data/
│ └── study_log.json # 학습 데이터 저장소
│
├── modules/
│ ├── init.py
│ ├── record_handler.py # 데이터 기록 / 저장
│ ├── analyzer.py # 데이터 분석
│ └── feedback.py # 피드백 생성
│
└── visualizer.py # 시각화 모듈

--- 

## 📸 실행 화면 예시 (콘솔)
=== Smart Study Manager ===

공부 기록 추가
데이터 분석 및 피드백 보기
종료
메뉴 선택: 1
오늘 공부시간(단위: 시간): 3
오늘 기분(한 단어로): 집중
오늘 집중도(1~10): 8
✅ 기록 완료: 2025-10-11 21:35 | 3시간 | 집중도: 8

=== Smart Study Manager ===
메뉴 선택: 2

📊 [학습 분석 결과]

총 학습일수: 1
평균 공부시간: 3시간
평균 집중도: 8
💬 AI 피드백: 멋져요! 현재 패턴을 유지하면서 스스로에게 보상하세요!

--- 

## 🚀 실행 방법 1️⃣ 필요한 라이브러리 설치 ```bash pip install -r requirements.txt
