# xudingE5
import time

def focus_timer(focus_duration):
    print(f"开始专注... 设定时间为 {focus_duration} 分钟。")
    start_time = time.time()
    end_time = start_time + 60 * focus_duration

    while time.time() < end_time:
        # 在这里专注于你的任务...
        pass

    print("时间到！停止专注。")

# 设定专注时间为 20 分钟
focus_timer(20)
