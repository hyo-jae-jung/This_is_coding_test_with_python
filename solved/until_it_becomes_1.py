N,K = map(int,input().split())
count = 0
while N >= K:
    if N%K == 0:
        N//=K
        count+=1
    else:
        N-=1
        count+=1

count+=N-1 # 이게 2번 요지

print(count)

'''
요지는
1. 나누기가 숫자를 크게 줄이니 나누기를 먼저 많이 해라.
2. 숫자가 커지면 K보다 작아지는 N에 대한 빼기연산이 많아지니 해당 작업은 반복문이 아니라 연산으로 해결하기.
'''