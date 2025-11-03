import matplotlib.pyplot as plt
import pandas as pd
from modules.record_handler import load_data

def show_graph():
    data = load_data()
    if not data:
        print("📊 아직 시각화할 데이터가 없습니다.")
        return

    df = pd.DataFrame(data).T
    df["focus"] = df["focus"].astype(int)
    df["hours"] = df["hours"].astype(float)

    df.plot(y=["focus", "hours"], kind="bar", figsize=(10, 5))
    plt.title("집중도 & 공부시간 변화")
    plt.xlabel("날짜")
    plt.ylabel("값")
    plt.show()
