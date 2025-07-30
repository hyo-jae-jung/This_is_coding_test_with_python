# https://programmers.co.kr/learn/courses/30/lessons/60062

n = 12
weak = [1,5,6,10]
dist = [1,2,3,4]

# n = 12
# weak = [1,3,4,9,10]
# dist = [3,5,7]

def solution(n, weak, dist):
    
    weak.sort()
    dist.sort()

    scalar = []
    for i in range(1,len(weak)):
        scalar.append((i-1,weak[i] - weak[i-1]))
    scalar.append((len(weak)-1,n - weak[-1] + weak[0]))

    scalar_sort = sorted(scalar,key=lambda x:-x[1])

    l = len(scalar)
    I = scalar_sort[0][0]
    
    s = set()
    for i,_ in scalar_sort:
        ii = (scalar_sort[0][0]+1)%l
        s.add(i)    
        tmp = []
        distance = 0
        while ii != I:
            if ii not in s:
                distance+=scalar[ii][1]
            else:
                if distance:
                    tmp.append(distance)
                    distance = 0
            ii = (ii+1)%l
        else:
            if distance:
                tmp.append(distance)

        tmp.sort()
        d = dist.copy()
        cnt = 0
        while True:
            tt = tmp.pop()
            dd = d.pop()
            if dd >= tt:
                cnt+=1
            else:
                tmp.append(tt)

            if not tmp:
                return cnt
            
            if not d:
                break

    return -1

print(solution(n,weak,dist))
