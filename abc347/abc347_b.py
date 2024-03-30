def count_unique_substrings(S):
    # 部分文字列を格納するセットを初期化
    substrings = set()

    # 文字列の全ての可能な部分文字列を生成し、セットに追加
    for i in range(len(S)):
        for j in range(i+1, len(S)+1):
            substrings.add(S[i:j])

    # セットのサイズ（重複しない部分文字列の数）を返す
    return len(substrings)

# 入力
S = input().strip()

# 部分文字列の種類の数を計算し出力
print(count_unique_substrings(S))
