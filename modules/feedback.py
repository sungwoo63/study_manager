def feedback_today(today):
    if not today:
        return "⚠️ 오늘 기록이 없습니다."

    goal = today.get("goal_hours", 0)
    progress = today.get("progress_hours", 0)
    rate = round((progress / goal) * 100, 1) if goal else 0

    msg = f"🎯 목표 {goal}h / 누적 {progress}h ({rate}%)\n"

    plans = today.get("plan_list", [])
    done = len([t for t in plans if t["done"]])
    msg += f"☑️ 완료한 과제: {done}/{len(plans)}개\n"

    if today.get("final_report"):
        r = today["final_report"]
        msg += f"🙂 기분: {r['mood']} | 🎯 집중도: {r['focus']}\n"

        rate_final = round((r["actual_hours"]/goal)*100, 1) if goal else 0
        if r["focus"] >= 8:
            comment_line = "🔥 오늘 정말 집중이 잘 됐어요!"
        elif r["focus"] >= 6:
            comment_line = "💡 꾸준히 집중력을 유지했어요."
        else:
            comment_line = "😴 약간 산만했지만 내일 더 나아질 거예요!"

        msg += f"📊 최종 달성률 {rate_final}% | {comment_line}\n"

        if today.get("completed_tasks"):
            tasks = ", ".join(today["completed_tasks"])
            msg += f"🏁 마무리한 과제: {tasks}\n"

        if today.get("comment"):
            msg += f"📝 한줄 코멘트: {today['comment']}\n"

    return msg
