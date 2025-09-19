# HashSetExample.py

# set 생성 (문자열 저장)
fruits = set()

# 값 추가
fruits.add("Apple")
fruits.add("Banana")
fruits.add("Orange")
fruits.add("Apple")  # 중복 → 무시됨

# 크기 출력
print("저장된 과일 개수:", len(fruits))

# 전체 요소 출력
print("저장된 과일:", fruits)

# 특정 값 포함 여부 확인
if "Banana" in fruits:
    print("Banana가 있습니다.")

# 값 삭제
fruits.discard("Orange")  # remove와 비슷하지만, 없으면 에러 안 남
print("Orange 삭제 후:", fruits)

# 모든 값 반복 출력
print("=== 반복문으로 출력 ===")
for fruit in fruits:
    print(fruit)

# 전체 비우기
fruits.clear()
print("비운 후:", fruits)
