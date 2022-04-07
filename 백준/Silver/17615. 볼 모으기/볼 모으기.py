N = int(input())
S = input()

# 빨간색 count 저장
red = S.count('R')
# 파란색 count 저장
blue = N - red
# 빨강, 파랑 중 더 개수가 적은 것 저장
ans = min(red, blue)
cnt = 0

#반복문 돌면서, 연속적인 것 count
for i in range(N):
    if S[i] != S[0]:
        break
    cnt += 1

# 만약에 연속 count한게 빨간색이었다면, 위의 답 vs <전체 빨강 개수 - 앞에서부터 연속 빨강 개수> 중 적은 것 저장
if S[0] == 'R':
    ans = min(ans, red - cnt)
# 만약에 연속 count한게 빨간색이었다면, 위의 답- <전체 파랑 개수 - 앞에서부터 연속 파랑 개수> 중 적은 것 저장
else:
    ans = min(ans, blue - cnt)

cnt = 0
# 반복문 거꾸로 돌면서 끝에서 얼마나 연속되는지 저장
for i in range(N-1, -1, -1):
    if S[i] != S[N - 1]:
        break
    cnt += 1
#만약 연속 count했던게 빨강이었다면, 위의 값 vs <전체 빨강 개수 - 뒤에서부터 연속 빨강 개수> 
if S[N - 1] == 'R':
    ans = min(ans, red - cnt)
#만약 연속 count했던게 파랑이었다면, 위의 값 vs <전체 파랑 개수 - 뒤에서부터 연속 파랑 개수>
else:
    ans = min(ans, blue - cnt)
print(ans)

# 최소값을 구하기 위해서 계속해서 mid으로 답을 갱신해나간다.


"""
우선순위
1. <둘 중 최소> -> 빨강 개수 vs 파랑 개수
2. <둘 중 최소> -> 1번 vs "전체 빨강/파랑 개수 - 앞에서부터 세었을 때 연속된 빨강/파랑 개수"
3. <둘 중 최소> ->  2번 vs "전체 빨강/파랑 개수 - 뒤에서부터 세었을 때 연속된 빨강/파랑 개수"

전체 빨강/파랑 개수에서 앞/뒤에서 연속된 빨강/파랑 개수를 빼는 이유:
- 끝에서부터 연속되어 있다면 그 볼 무더기는 움직일 필요가 없는것들이고, 따로 떨어진것들만 무더기쪽으로 움직이면 되어서 이게 곧 횟수를 의미
"""