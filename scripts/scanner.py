import subprocess
import re
import sys
import os

def scan_jar(jar_path):
    if not os.path.exists(jar_path): return
    
    # JAR内の全クラス名を取得
    class_list = subprocess.check_output(["jar", "tf", jar_path]).decode().split()
    found = set()

    for cf in class_list:
        if not cf.endswith(".class"): continue
        cls = cf.replace(".class", "").replace("/", ".")
        try:
            output = subprocess.check_output(["javap", "-p", "-v", "-cp", jar_path, cls]).decode()
            # Android APIの参照を抽出
            matches = re.findall(r'L(android/[\w/]+);', output)
            for m in matches:
                found.add(m.replace("/", "."))
        except:
            continue

    for c in sorted(list(found)):
        print(c)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        scan_jar(sys.argv[1])
