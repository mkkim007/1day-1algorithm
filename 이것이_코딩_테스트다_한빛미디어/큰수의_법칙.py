print("N, M, K를 입력하세요 :", end=" ")
n, m, k = map(int, input().split())

print("N개의 data를 입력하세요 :", end=" ")
data = list(map(int, input().split()))

data.sort()

first = data[n-1]
second = data[n-2]

ans = int(m/(k+1))*(first*k+second) + (m%(k+1))*first
print(ans)