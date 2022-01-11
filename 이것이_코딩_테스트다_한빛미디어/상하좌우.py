def solution(n, action):
    act = {"L":-1,"R":+1,"U":-1,"D":+1}
    ans =[1,1]
    temp =[1,1]
    
    for i in action :
        if i=="L" or i=="R" :
            temp[1] = temp[1] + act[i]
        else :
             temp[0] = temp[0] + act[i]


        if temp[0]<=5 and temp[0]>=1 and temp[1]<=5 and temp[1]>=1 :
            ans = temp.copy()  # 주의...
        temp = ans.copy() # 주의 ...


    return ans
