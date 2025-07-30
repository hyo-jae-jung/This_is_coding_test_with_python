# https://programmers.co.kr/learn/courses/30/lessons/60060

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

def solution(words, queries):

    words.sort()
    words_arranged_by_count = {}

    for i in words:
        if not words_arranged_by_count.get(l:=len(i)):
            words_arranged_by_count.update({l:[]})
        words_arranged_by_count[l].append(i)
        
    rev_words = []
    for i in words:
        tmp = ''
        for j in range(len(i)-1,-1,-1):
            tmp+=i[j]
        rev_words.append(tmp)

    rev_words.sort()
    rev_words_arranged_by_count = {}

    for i in rev_words:
        if not rev_words_arranged_by_count.get(l:=len(i)):
            rev_words_arranged_by_count.update({l:[]})
        rev_words_arranged_by_count[l].append(i)

    from bisect import bisect_left

    answer = []
    for i in queries:
        start,end = '',''
        if not words_arranged_by_count.get(len(i)):
            answer.append(0)
        else:
            if i[-1] == '?':
                for j in i:
                    if j == '?':
                        start+='a'
                        end+='z'
                    else:
                        start+=j
                        end+=j
                answer.append(bisect_left(words_arranged_by_count[len(i)],end) - bisect_left(words_arranged_by_count[len(i)],start))
            else:
                for j in range(len(i)-1,-1,-1):
                    if i[j] == '?':
                        start+='a'
                        end+='z'
                    else:
                        start+=i[j]
                        end+=i[j]
                answer.append(bisect_left(rev_words_arranged_by_count[len(i)],end) - bisect_left(rev_words_arranged_by_count[len(i)],start))

    return answer

print(solution(words, queries))