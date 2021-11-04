## 매우 비효율적으로 짰던 첫번째 시도
def solution1(phone_book):
    for i in phone_book :
        phone_book.remove(i)
        for j in phone_book :
            if i==j[:len(i)] :
                return False
    return True

## 두번째 시도
def solution(phone_book):
    phone_book.sort()
    for idx, n in enumerate(phone_book[:len(phone_book)-1]) :
        if n == phone_book[idx+1][:len(n)] :
            return False
    return True

## 다른사람 코드
def solution(phoneBook):
    phoneBook = sorted(phoneBook)
    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):       ## 처음보는 녀석,,, 
            return False
    return True
