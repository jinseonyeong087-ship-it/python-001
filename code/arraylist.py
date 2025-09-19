# ✅ 파이썬 버전: list CRUD (과일)
# ─────────────────────────────────────────────────────────────────────────────
# [자바와 큰 차이]
# 1) 파이썬은 컬렉션으로 기본 내장 list를 사용 (java.util.ArrayList 필요 없음)
# 2) 동적 타이핑: 타입 선언/제너릭(<String>) 없음. 원하면 타입 힌트(list[str])를 쓸 수는 있음.
# 3) 추가: add가 아니라 append 사용. (자바: list.add("사과") / 파이썬: list.append("사과"))
# 4) 조회: get(index) 메서드가 아니라 대괄호 인덱싱 사용. (자바: list.get(0) / 파이썬: list[0])
# 5) 수정: set(index, value) 대신 인덱싱 대입. (자바: list.set(1,"오렌지") / 파이썬: list[1]="오렌지")
# 6) 삭제(인덱스): 자바 remove(int)와 같은 역할은 pop(index). pop은 '삭제된 요소'를 반환함.
#    - 파이썬 remove(value)는 '값으로 삭제' (자바 remove(Object)와 동일 의미) → 둘 다 처음 등장하는 1개만 삭제.
# 7) 포함 여부: contains 대신 'in' 키워드. (자바: list.contains("바나나") / 파이썬: "바나나" in list)
# 8) 반복/람다: 파이썬은 리스트 내포(list comprehension)와 lambda/filter 등 풍부한 내장 문법을 제공.
# 9) 예외: 인덱스 범위 오류는 IndexError (자바는 IndexOutOfBoundsException).
# 10) 동기화: 둘 다 기본은 비동기화. 자바는 Collections.synchronizedList(...)로 감쌀 수 있고,
#     파이썬은 threading.Lock 등으로 임계영역 보호를 직접 구현.
# 11) 성능 감각: 내부는 동적 배열로 유사. 중간 삽입/삭제는 비용 큼(O(n)), 끝에 append는 보통 O(1) 평균.

from typing import List  # 타입 힌트(선택사항). 자바의 제너릭처럼 '강제'가 아니라 '도움' 용도.

# 타입 힌트 예시(선택): 자바의 List<String> 느낌을 주고 싶을 때 사용 가능.
fruits: List[str] = []

# ──────── C (Create) : 추가 ────────
# 자바: list.add("사과")
# 파이썬: list.append("사과")
fruits.append("사과")
fruits.append("바나나")
fruits.append("포도")
print("추가 후:", fruits)  # ['사과', '바나나', '포도']

# ──────── R (Read) : 조회 ────────
# 자바: list.get(0)
# 파이썬: list[0]  (get 메서드 없음, 대괄호로 직접 접근)
print("0번 인덱스:", fruits[0])  # 사과

# 자바: list.contains("바나나")
# 파이썬: "바나나" in fruits
print("포함 여부(바나나):", "바나나" in fruits)  # True

# 전체 출력은 동일하게 가능(자바는 toString 오버라이드 출력 형식, 파이썬은 리터럴 형태로 출력)
print("전체 과일:", fruits)  # ['사과', '바나나', '포도']

# ──────── U (Update) : 수정 ────────
# 자바: list.set(1, "오렌지")
# 파이썬: 인덱싱 대입
fruits[1] = "오렌지"
print("수정 후:", fruits)  # ['사과', '오렌지', '포도']

# ──────── D (Delete) : 삭제 ────────
# 1) 인덱스로 삭제
# 자바: list.remove(0)  → 인덱스 기반 삭제 (주의: 자바는 오버로드 때문에 int/객체 구분!)
# 파이썬: list.pop(0)  → 인덱스 삭제 + 삭제된 요소 반환
removed = fruits.pop(0)
print("삭제된 요소(인덱스 0):", removed)  # '사과'
print("현재:", fruits)  # ['오렌지', '포도']

# 2) 값으로 삭제 (첫 번째 매칭만 삭제)
# 자바: list.remove("포도") → boolean 반환(성공/실패)
# 파이썬: list.remove("포도") → 실패 시 ValueError 예외 발생 (자바는 false 반환)
fruits.remove("포도")
print("값 삭제 후:", fruits)  # ['오렌지']

# 3) 전체 삭제
# 자바: list.clear()
# 파이썬: list.clear()
fruits.clear()
print("전체 삭제 후 비었나?", len(fruits) == 0)  # True

# ──────── 보너스: 조건 삭제/필터링 패턴 ────────
# 자바: list.removeIf(x -> x.startsWith("포"))
# 파이썬: 리스트 내포로 필터링된 새 리스트 만들기 (원본 변경 X)
fruits = ["사과", "포도", "파인애플", "바나나"]
fruits = [x for x in fruits if not x.startswith("파")]  # "파"로 시작하는 과일 제거
print("조건 필터링 후:", fruits)  # ['사과', '포도', '바나나']

# ──────── 예외 차이 간단 데모 ────────
# 자바: 인덱스 초과 → IndexOutOfBoundsException
# 파이썬: 인덱스 초과 → IndexError
try:
    _ = fruits[999]
except IndexError as e:
    print("파이썬 인덱스 예외 타입:", type(e).__name__)  # IndexError
