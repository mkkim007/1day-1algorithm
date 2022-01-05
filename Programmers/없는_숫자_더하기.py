def solution(numbers):
    A = set([1,2,3,4,5,6,7,8,9])
    B = set(numbers)
    C = A - B
    
    answer = sum(C)
    return answer

# 다른사람 코드

def solution2(numbers):
    return 45 - sum(numbers)