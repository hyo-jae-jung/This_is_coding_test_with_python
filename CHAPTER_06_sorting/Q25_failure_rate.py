# https://programmers.co.kr/learn/courses/30/lessons/42889

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
# N = 5
# stages = [1, 2, 2, 2, 2, 2, 2, 1]
# N = 4
# stages = [4,4,4,4,4]

def solution(N, stages):
    
    l = len(stages)
    d = {}
    for i in range(N+2):
        d.update({i:0})
    
    for i in sorted(stages):
        d[i]+=1

    arr = [[0,0,0] for _ in range(N)]
    
    for i in range(N):
        arr[i][0] = i+1
        arr[i][1] = d[i+1]
        l-=d[i]
        arr[i][2] = l

    arr.sort(key=lambda x:(-x[1]/(x[2] if x[2] > 0 else 1),x[0]))
    answer = []
    for i,_,_ in arr:
        answer.append(i)
    return answer

print(solution(N,stages))
