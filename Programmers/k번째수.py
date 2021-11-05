# 첫번째 시도 
def solution(array, commands):
    answer = []
    for i, a in enumerate(commands) :
        ans = sorted(array[a[0]-1:a[1]])[a[2]-1]
        answer.append(ans)
    return answer


# 다른 사람 코드,,
def solution(array, commands):
    # 존경,,,
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))