def main(W, B):
    
    S ="wbwbwwbwbwbw"*(W+B)
    
    for i in range(len(S)):
      substring = S[i:i+W+B]
      if substring.count("w") == W and substring.count("b") == B:
          return print('Yes')
          exit()
    return print('No')
    
W, B = map(int,input().split()) 

main(W,B)