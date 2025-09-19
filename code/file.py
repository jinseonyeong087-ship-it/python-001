# 파일을 UTF-8 인코딩으로 열고 한 줄씩 읽기
file_path = "test.txt"

try:
   with open("C:/jsy.python/python-001/test.txt", "r", encoding="utf-8") as f:

        for line in f:
            print(line, end="")  # 줄 끝 개행(\n)이 이미 포함돼 있으므로 end=""로 중복 방지
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
