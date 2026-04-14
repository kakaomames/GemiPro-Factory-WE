import os
import re
import sys
import zipfile

def scan_jar_ultra_fast(target_dir="."):
    found_android_classes = set()
    # 探索対象のJARをリストアップ
    jars = [f for f in os.listdir(target_dir) if f.endswith(".jar")]
    
    if not jars:
        print("❌ No JAR files found.", file=sys.stderr)
        return

    # Androidクラス参照を見つけるための正規表現 (Landroid/view/View; 等)
    # バイナリの中から直接ぶっこ抜くため、少し広めに拾います
    pattern = re.compile(rb'android/[a-zA-Z0-9_/]+')

    for jar_path in jars:
        print(f"\n📦 Analyzing {jar_path}...", file=sys.stderr)
        try:
            with zipfile.ZipFile(jar_path, 'r') as z:
                all_files = [f for f in z.namelist() if f.endswith('.class')]
                total = len(all_files)
                
                for i, class_file in enumerate(all_files):
                    # 進捗バーの表示 (\r を使用)
                    percent = (i + 1) / total * 100
                    bar_len = 20
                    filled = int(bar_len * (i + 1) // total)
                    bar = '█' * filled + '-' * (bar_len - filled)
                    sys.stderr.write(f"\r|{bar}| {percent:3.1f}% Processing: {class_file[:30]:<30}")
                    sys.stderr.flush()

                    # クラスファイルをバイナリモードで読み込み、Constant Poolをスキャン
                    with z.open(class_file) as f:
                        content = f.read()
                        matches = pattern.findall(content)
                        for m in matches:
                            # android/view/View -> android.view.View に変換
                            found_android_classes.add(m.decode().replace('/', '.'))

            sys.stderr.write("\n✅ Done!\n")
        except Exception as e:
            print(f"\n❌ Error reading {jar_path}: {e}", file=sys.stderr)

    # 重複排除してソートして出力（これが dependencies.txt になる）
    for c in sorted(list(found_android_classes)):
        print(c)

if __name__ == "__main__":
    scan_jar_ultra_fast()
