# linear dynamic programming
txt1 = ['A', 'B', 'E', 'G', 'E', 'C', 'E', 'E', 'G', 'E', 'G', 'E',
        'A', 'B', 'C', 'D', 'E', 'E', 'G', 'E', 'G', 'E', 'O', 'Y', 'Z']
dp = [1, ]
len1 = len(txt1)
j = 0
max1 = 1
while j < len1-1:
    if txt1[j] < txt1[j+1]:
        dp.append(dp[j]+1)
        if dp[-1] > max1:
            max1 = dp[-1]
    else:
        dp.append(1)
    j += 1
print('max length:%d' % (max1))
r = []
for k in range(dp.index(max1)-max1+1, dp.index(max1)+1):
    r.append(txt1[k])
print(r)
# ------------------------------------------------------------------
# stone
# (4, 5), 6, 7, 8, 6, 10, 2, 5, 7 ;j=0,i=1;0~1;(i-1)~(j+i)
# 4, (5, 6), 7, 8, 6, 10, 2, 5, 7 ;j=0;i=2;1~2
# ...
# 4, 5, 6, 7, 8, 6, 10, 2, (5, 7) ;j=0;i=9;8~9

# (4, 5, 6), 7, 8, 6, 10, 2, 5, 7 ;j=1;i=1;0~2
# 4, (5, 6, 7), 8, 6, 10, 2, 5, 7 ;j=1;i=2;1~3
# ...
# 4, 5, 6, 7, 8, 6, 10, (2, 5, 7) ;j=1;i=8;7~9

# ...

# (4, 5, 6, 7, 8, 6, 10, 2, 5), 7 ;j=7;i=1;0~8
# 4, (5, 6, 7, 8, 6, 10, 2, 5, 7) ;j=7;i=2;1~9

# ...

# (4, 5, 6, 7, 8, 6, 10, 2, 5, 7) ;j=8;i=1;0~9;(i-1)~(j+i)

# dp[j][i]; k=j; dp[j][k]
stones = [4, 5, 6, 7, 8, 6, 10, 2, 5, 7, 1, 1]
n = len(stones)
dp = [[0]*n for _ in range(n)]  # initialize a two-dimensional list


def StonesSum(substones):
    return sum(substones)


def StonesDP(stone):
    i = 1
    while i < n:
        j = 0
        while j < n and (j+i) < n:
            k = j
            while k < j+1:
                curCost = dp[j][k]+dp[k+1][j+1]+StonesSum(stone[j:(j+i+1)])
                print('i=%d j=%d,curCost %d,stonessum %d' %
                      (i, j, curCost, StonesSum(stone[j:(j+i+1)])))
                if dp[j][j+i] == 0:
                    dp[j][j+i] = curCost
                else:
                    dp[j][j+1] = min(dp[j][j+i], curCost)
                k += 1
            j += 1
        i += 1


StonesDP(stones)
for line in dp:
    print(line)
# ------------------------------------------------------------------
# Tree-like dynamic programming
triangle = [[5], [2, 3], [5, 6, 3], [6, 1, 2, 4]]


def minpath(t1):
    dp = []  # store local optimal solution
    for row in t1:
        dp.append([0]*len(row))  # initialization
    n = len(dp)
    dp[0][0] = t1[0][0]  # first the optimal solution is its own
    for i in range(n-1):
        len1 = len(t1[i][:])
        for j in range(len1):
            if dp[i+1][j] == 0 and j == 0:  # parent node(i,0)
                dp[i+1][j] = dp[i][j]+t1[i+1][j]  # left child node:j
                dp[i+1][j+1] = dp[i][j]+t1[i+1][j+1]  # right child node:j+1
            else:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j]+t1[i+1][j])
                dp[i+1][j+1] = dp[i][j]+t1[i+1][j+1]
    print('result:'+str(dp[n-1]))
    minValue = dp[n-1][0]
    bottomLength = len(dp[n-1])
    f = 1
    while f < bottomLength:
        if minValue > dp[n-1][f]:
            minValue = dp[n-1][f]
        f += 1
    print('triangle result:%d' % (minValue))


minpath(triangle)
# ------------------------------------------------------------------
vol_max = 5
values = [20, 10, 15, 25]
volumes = [3, 1, 2, 4]


def bagValue(volume, value, m):
    i_len = len(volume)
    dp = [[0]*(m+1)for _ in range(i_len)]
    for j in range(1, m+1):
        if volume[0] <= j:
            dp[0][j] = value[0]
    for i in range(1, i_len):
        for j in range(1, m+1):
            if j < volume[i]:
                dp[i][j] = dp[i][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-volume[i]]+value[i])
    for line in dp:
        print(line)
    return dp[-1][-1]


solve = bagValue(volumes, values, vol_max)
print('space %d value %d' % (vol_max, solve))
