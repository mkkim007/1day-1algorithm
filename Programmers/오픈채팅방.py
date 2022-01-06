
def solution(record):
    answer = []
    user = {}
    
    for i in record :
        temp = i.split()
        if temp[0]=="Enter" or temp[0]=="Change" : user[temp[1]]=temp[2]  
    
    for i in record :
        temp = i.split()
        if temp[0]=="Enter" :
            answer.append(user[temp[1]]+"님이 들어왔습니다.")
            print()
        if temp[0]=="Leave" : 
            answer.append(user[temp[1]]+"님이 나갔습니다.")

    
   
    return answer

# 다른사람 풀이
def solution2(record):
    answer = []
    namespace = {}
    printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    for r in record:
        rr = r.split(' ')
        if rr[0] in ['Enter', 'Change']:
            namespace[rr[1]] = rr[2]

    for r in record:
        if r.split(' ')[0] != 'Change':
            answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])

    return answer


# 다른사람 풀이
def solution3(record):
    user_id = {EC.split()[1]:EC.split()[-1] for EC in record if EC.startswith('Enter') or EC.startswith('Change')}
    return [f'{user_id[E_L.split()[1]]}님이 들어왔습니다.' if E_L.startswith('Enter') else f'{user_id[E_L.split()[1]]}님이 나갔습니다.' for E_L in record if not E_L.startswith('Change')]

