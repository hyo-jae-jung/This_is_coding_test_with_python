S = [
"aabbaccc",
"ababcdcdababcdcd",
"abcabcdede",
"abcabcabcabcdededededede",
"xababcdcdababcdcd",
]

def solution(s):
    max_length = len(s)
    result = max_length
    for each_length in range(1,max_length//2+1):
        total_s = ''
        each_a = ''
        cnt = 1
        for i in range(0,(max_length//each_length)*each_length,each_length):
            each_b = ''
            for j in range(i,i+each_length):
                each_b+=s[j]
            if each_a == each_b:
                cnt+=1
            else:
                total_s+=(str(cnt) if cnt > 1 else '') + each_a
                each_a = each_b
                cnt = 1
        else:
            total_s+=(str(cnt) if cnt > 1 else '') + each_a
            each_a = each_b
            cnt = 1

        if (r:=max_length%each_length) > 0:
            total_s+=s[-r:]   
        result = min(result,len(total_s))
    return result
        
for i in S:
    print(solution(i))
