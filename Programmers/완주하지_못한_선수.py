#나의 풀이
def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i,j in zip(participant, completion) : 
        if i != j :
            return i
    return participant.pop()



# 다른사람 풀이
import collections
def bestsolution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

# collection의 Counter 객체는 빼기가 가능하다.. 