import requests
import json
import os

# API
url = "https://meowfacts.herokuapp.com/?lang=zho&count=3"

# 取得目前程式所在資料夾
base_dir = os.path.dirname(os.path.abspath(__file__))

# 設定輸出檔案路徑（固定在 main.py 同一層）
file_path = os.path.join(base_dir, "data.json")

# 發送請求
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    # 寫入 JSON
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print("資料抓取成功")
    print("檔案位置：", file_path)
else:
    print("抓取失敗:", response.status_code)
