# 장바구니 합계
"""
1. 장바구니 합계 함수 정의
2. 정보 입력
3. 함수 호출 및 출력
"""
def cart(*items: int, coupon: int = 0) -> int:
    """
    장바구니 합계 함수
    
    Args:
        *items (int): 임의 개수의 상품 가격
        coupon (int): 할인 쿠폰
    
    Returns:
        int: 총 합계
    """
    return max(sum(items) - coupon, 0)

# 정보 입력
raw = input().split()
pos = [t for t in raw if "=" not in t]
items = [int(x) for x in pos]
coupon = 0
for t in raw:
    if "=" in t:
        k, v = t.split("=", 1)
        if k == "coupon":
            coupon = int(v)


# 결과 출력
print(cart(*items, coupon=coupon))