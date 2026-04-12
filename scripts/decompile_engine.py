import subprocess
import os
import glob
import json

def run_decompile():
    print("📢 現場監督：作業を開始します。")
    
    # 対象APKの検索
    apk_list = glob.glob("apks/*.apk")
    if not apk_list:
        print("❌ ターゲット（APK）が見当たりません！")
        return
    
    target = apk_list[0]
    jar_editor = "tools/APKEditor.jar"
    
    # APK Editor での解体コマンド (shell=True で一気に！)
    # 隊員の持っている JAR の仕様に合わせてコマンドを調整してください
    print(f"🛠️ {target} を最新の APKEditor で解体中...")
    cmd = f"java -jar {jar_editor} d -i {target} -o temp_work"
    
    try:
        subprocess.run(cmd, shell=True, check=True)
        print("✨ 解体完了！")
        
        # 報告書の作成
        report = {
            "status": "completed",
            "apk": os.path.basename(target),
            "engine": "APKEditor + GitHub Actions",
            "message": "動けば正義。壊れなければ問題ない。"
        }
        
        with open("result.json", "w", encoding="utf-8") as f:
            json.dump(report, f, indent=4, ensure_ascii=False)
            
    except Exception as e:
        print(f"💥 事故発生：{e}")
        with open("result.json", "w") as f:
            json.dump({"status": "error", "message": str(e)}, f)

if __name__ == "__main__":
    run_decompile()
