def solution(c, r):
    c = int(ord(c)) - int(ord('a')) + 1

    steps = [(-2,-1), (-1,-2), (1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]
    ans = 0
    for step in steps :
        
        next_r = r+step[0]
        next_c = r+step[1]

        if next_r>=1 and next_r<=8 and next_c>=1 and next_c<=8 :
            ans+=1

    return ans
