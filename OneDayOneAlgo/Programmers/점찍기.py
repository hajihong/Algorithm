import math
def solution(k, d):
    answer = 0
    for i in range(0,d+1,k):
        for j in range(0,d+1,k):
            if math.sqrt(i**2+j**2) > d:
                break
            else:
                answer += 1
    
    return answer


print(solution(1,5))


