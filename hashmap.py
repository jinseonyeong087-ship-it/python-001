import json
import os

file = "data.json"
obj = {"name": "Alice", "age": 25}

# JSON 파일로 저장
with open(file, "w", encoding="utf-8") as f:
    json.dump(obj, f, ensure_ascii=False, indent=2)
print("파일 저장 완료")

# JSON 파일 읽기
if os.path.exists(file):
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
    print("읽은 데이터:", data)
else:
    print("파일이 존재하지 않습니다.")
