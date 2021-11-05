# 첫번째 시도 
def solution(array, commands):
    answer = []
    for i, a in enumerate(commands) :
        ans = sorted(array[a[0]-1:a[1]])[a[2]-1]
        answer.append(ans)
    return answer