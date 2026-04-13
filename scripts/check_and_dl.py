import requests
import os
import base64
import sys

AOSP_BASE_URL = "https://android.googlesource.com/platform/frameworks/base/+/master/core/java/"
URL_SUFFIX = "?format=TEXT"
MIN_SIZE = 10000 
VENDOR_DIR = "vendor/java"

# Web版があるAPI（DLスキップ対象）
WEB_BRIDGE_LIST = [
    "android.hardware.camera",
    "android.location.Location"
]

def download_aosp_java(class_list):
    if not os.path.exists(VENDOR_DIR):
        os.makedirs(VENDOR_DIR)

    for full_name in class_list:
        if any(api in full_name.lower() for api in WEB_BRIDGE_LIST):
            print(f"🌐 {full_name}: Web APIブリッジ対象。DLスキップ。")
            continue

        file_path = full_name.replace(".", "/") + ".java"
        url = f"{AOSP_BASE_URL}{file_path}{URL_SUFFIX}"
        local_path = os.path.join(VENDOR_DIR, file_path)
        
        if not os.path.exists(os.path.dirname(local_path)):
            os.makedirs(os.path.dirname(local_path))

        try:
            head = requests.head(url, allow_redirects=True)
            if head.status_code != 200:
                print(f"⚠️ {full_name}: 取得不可 ({head.status_code})")
                continue

            resp = requests.get(url)
            raw_content = base64.b64decode(resp.text)
            
            if len(raw_content) < MIN_SIZE:
                print(f"⚠️ {full_name}: サイズ異常。無視します。")
                continue

            with open(local_path, "wb") as f:
                f.write(raw_content)
            print(f"🔥 {full_name}: DL完了！")

        except Exception as e:
            print(f"❌ {full_name}: エラー: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            classes = [line.strip() for line in f if line.strip() and not line.startswith("#")]
        download_aosp_java(classes)
