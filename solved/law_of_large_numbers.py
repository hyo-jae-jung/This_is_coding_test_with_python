from multiprocessing import shared_memory


N,M,K = map(int,input().split())
natural_numbers = [int(i) for i in input().split()]
natural_numbers.sort(reverse=True)

share = M//(K+1)
rest = M%(K+1)

answer = natural_numbers[0]*K*share + natural_numbers[1]*share + natural_numbers[0]*rest

print(answer)