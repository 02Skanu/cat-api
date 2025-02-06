import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
# TheCatAPI 키 설정
API_KEY = os.getenv("CAT_API_KEY")
URL = f"https://api.thecatapi.com/v1/images/search?api_key={API_KEY}"

# README 파일 경로
README_PATH = "README.md"

def get_cat_info():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        if data:
            cat_info = data[0]
            image_url = cat_info.get("url")
            breed_info = cat_info.get("breeds", [{}])[0]
            breed_name = breed_info.get("name", "Unknown")
            description = breed_info.get("description", "No description available.")
            wikipedia_url = breed_info.get("wikipedia_url", "No Wikipedia link available.")

            return {
                "image_url": image_url,
                "breed_name": breed_name,
                "description": description,
                "wikipedia_url": wikipedia_url
            }
    return None


def update_readme():
    cat_info = get_cat_info()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if cat_info:
        readme_content = f"""
# 나만 없어 고양이

![Cat Image]({cat_info['image_url']})

⏳ 업데이트 시간: {now} (KRW)

---
"""
    else:
        readme_content = f"""
# 진짜 없어

현재 고양이 정보를 가져올 수 없습니다.

⏳ 업데이트 시간: {now} (KRW)

---
"""

    with open(README_PATH, "w", encoding="utf-8") as file:
        file.write(readme_content)

if __name__ == "__main__":
    update_readme()
