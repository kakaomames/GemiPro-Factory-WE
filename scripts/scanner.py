import subprocess
import re
import sys
import os

def scan_jar_dependencies(jar_path):
    if not os.path.exists(jar_path):
        print(f"Error: {jar_path} not found.")
        return []

    print(f"📦 {jar_path} を解析中...")
    
    # javapを使ってJAR内の全ての参照先をダンプ
    # -p (全メンバ), -v (定数プール)
    try:
        # まずはJAR内のクラス一覧を取得
        classes_output = subprocess.check_output(["jar", "tf", jar_path]).decode()
        class_files = [c for c in classes_output.split() if c.endswith(".class")]
        
        found_android_classes = set()

        for cf in class_files:
            # 各クラスファイルをjavapで解析
            cmd = ["javap", "-p", "-v", "-cp", jar_path, cf.replace(".class", "")]
            output = subprocess.check_output(cmd).decode()
            
            # Landroid/view/View; 形式の文字列を探す
            matches = re.findall(r'L(android/[\w/]+);', output)
            for m in matches:
                found_android_classes.add(m.replace("/", "."))

        # 整理して出力
        sorted_classes = sorted(list(found_android_classes))
        for c in sorted_classes:
            print(c)
            
        return sorted_classes

    except Exception as e:
        print(f"❌ 解析エラー: {e}")
        return []

if __name__ == "__main__":
    if len(sys.argv) > 1:
        scan_jar_dependencies(sys.argv[1])
    else:
        print("Usage: python scanner.py <path_to_jar>")
