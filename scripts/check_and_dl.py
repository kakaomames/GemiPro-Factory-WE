import requests
import os
import base64
import sys

# --- 設定変数 ---
AOSP_BASE_URL = "https://android.googlesource.com/platform/frameworks/base/+/master/core/java/"
URL_SUFFIX = "?format=TEXT"
MIN_SIZE = 10000  # 10KB未満は異常（メンテナンス画面等）とみなす
VENDOR_DIR = "vendor/java"

# WebカメラAPI等で代用するため、AOSPからDLしないリスト
WEB_BRIDGE_LIST = [
    "android.hardware.camera",
    "android.location.Location"
]

def download_aosp_java(class_list):
    if not os.path.exists(VENDOR_DIR):
        os.makedirs(VENDOR_DIR)

    for full_name in class_list:
        # Web代用リストに含まれているかチェック
        if any(api in full_name.lower() for api in WEB_BRIDGE_LIST):
            print(f"🌐 {full_name}: Web APIでブリッジするためDLをスキップし、Stubを使用します。")
            continue

        # パッケージ名をパスに変換
        file_path = full_name.replace(".", "/") + ".java"
        url = f"{AOSP_BASE_URL}{file_path}{URL_SUFFIX}"
        
        # 保存先の階層を作成
        local_path = os.path.join(VENDOR_DIR, file_path)
        local_dir = os.path.dirname(local_path)
        if not os.path.exists(local_dir):
            os.makedirs(local_dir)

        try:
            # 1. HEADリクエストで生存確認
            head = requests.head(url, allow_redirects=True)
            if head.status_code != 200:
                print(f"⚠️ {full_name}: 取得不可 (Status: {head.status_code})")
                continue

            # 2. GETリクエストで中身を確保
            resp = requests.get(url)
            raw_content = base64.b64decode(resp.text)
            content_size = len(raw_content)

            # 3. サイズバリデーション
            if content_size < MIN_SIZE:
                print(f"⚠️ {full_name}: サイズ異常 ({content_size} bytes)。壊れたデータの可能性があります。")
                continue

            # 4. 変更がある場合のみ上書き保存
            if os.path.exists(local_path):
                with open(local_path, "rb") as f:
                    if f.read() == raw_content:
                        print(f"✅ {full_name}: 変更なし。")
                        continue

            with open(local_path, "wb") as f:
                f.write(raw_content)
            print(f"🔥 {full_name}: DL完了！ ({content_size} bytes)")

        except Exception as e:
            print(f"❌ {full_name}: 通信エラーが発生しました: {e}")

if __name__ == "__main__":
    # 引数から依存関係リストを読み込む
    target_classes = []
    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        with open(sys.argv[1], "r") as f:
            target_classes = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    else:
        # 引数がない場合のテスト用デフォルト
        target_classes = ["android.view.View", "android.widget.Button"]

    download_aosp_java(target_classes)
