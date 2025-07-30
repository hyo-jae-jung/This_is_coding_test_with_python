# https://school.programmers.co.kr/learn/courses/30/lessons/60059

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

def solution(key,lock):

    def rotate_90(m):
        N = len(m)
        ret = [[0] * N for _ in range(N)]

        for r in range(N):
            for c in range(N):
                ret[c][N-1-r] = m[r][c]
        return ret

    key_l = len(key)
    lock_l = len(lock)
    expend_l = 2*(lock_l-1) + key_l
    expends = []
    for _ in range(4):
        expend = [[0]*(expend_l) for _ in range(expend_l)]
        for i in range(key_l):
            for j in range(key_l):
                expend[i+lock_l-1][j+lock_l-1] = key[i][j]
        expends.append(expend)
        key = rotate_90(key)

    diff = expend_l - lock_l
    
    for expend in expends:
        for i in range(diff+1):
            for j in range(diff+1):
                    breaking = False
                    for k in range(lock_l):
                        if breaking:break
                        for l in range(lock_l):
                            if breaking:break
                            if expend[i+k][j+l] == lock[k][l]:
                                breaking = True
                    else:
                        if not breaking:
                            return True

    return False

print(solution(key,lock))
