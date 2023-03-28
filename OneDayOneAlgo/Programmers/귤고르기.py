from collections import Counter
def solution(k, tangerine):
    answer = 0
    dict = {}
    cnt = 0
    for elem in tangerine:
        if not elem in dict:
            dict[elem] = 1
        else:
            dict[elem] += 1
            
    sorted_dict = sorted(dict.items(), key = lambda x : x[1], reverse=True)
    
    for key, value in sorted_dict:
        cnt += 1
        answer += value
        if answer >= k:
            break
        
        
    return cnt
        
    
    




print(solution(6,[1, 3, 2, 5, 4, 5, 2, 3]))