# ローカル動作確認用のスケジューラー（本番運用はVercel Cronを使用: api/rollover.py, vercel.json）

import schedule
import time
from main_workflow import run_cafe_beans_rollover

schedule.every().friday.at("12:00").do(run_cafe_beans_rollover)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)


