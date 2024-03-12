n, k = map(int, input().split()) # 물품의 수 & 준서가 버틸 수 있는 무게
lst=[[0, 0]] # nested list  
for _ in range(n): # 물품의 수 만 큼 반복
    lst.append(list(map(int, input().split())))  # table을 구성 : 즉 조건들을 입력 받기 
dp=[[0 for _ in range(k+1)] for _ in range(n+1)] # dp 테이블 생성 (n+1 x k+1 크기)
for i in range(1, n+1): # 테스트 횟수만큼 
    for j in range(1, k+1): # value 즉 무게를 계산하기 위해  , k가 7이면 1~8
        weight = lst[i][0]
        value = lst[i][1]
        if j < weight:  # 현재 가방의 무게(j)가 물건의 무게(weight)보다 작으면
            dp[i][j] = dp[i - 1][j]  # 이전 상태(i-1)의 값 그대로 유지
        else: # 가방에 물건을 넣을 수 있는 경우
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)
            # 1. 이전 상태(i-1)의 값
            # 2. 물건을 넣지 않은 상태(i-1, j-weight)의 값 + 물건의 가치(value)
            # 두 가지 중 더 큰 값을 선택
print(dp[n][k])
