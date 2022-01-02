def solution(card):
    temp = min(card[0]);
    for i, a in enumerate(card[1:]):
        if min(a) > temp :
            temp = min(a)
    return temp
