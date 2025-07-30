# https://school.programmers.co.kr/learn/courses/30/lessons/42891?language=python3

food_times = [3,1,2]
k = 5

if sum(food_times) <= k:
    print(-1)
else:
    l = len(food_times)
    i,j = 0,0
    while bool(any(food_times)) and j < k:
        if food_times[i%l] > 0:
            food_times[i%l]-=1
            j+=1
        i+=1

    print(i%l+1)

