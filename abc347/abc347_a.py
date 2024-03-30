# 標準入力から N と K を読み取る
N, K = map(int, input().split())

# 標準入力から数列 A を読み取る
A = list(map(int, input().split()))

# K の倍数である要素を見つけ、K で割る
result = [a // K for a in A if a % K == 0]

# 結果を空白で区切って出力する
print(*result)
