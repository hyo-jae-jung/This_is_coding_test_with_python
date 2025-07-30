# https://programmers.co.kr/learn/courses/30/lessons/60061

# n = 5
# build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

def solution(n, build_frame):
    ans = []
    
    ans.sort(key=lambda x:(x[0],x[1],x[2]))

    return ans

print(solution(n,build_frame))
