weights = [100,180,360,100,270]
from collections import Counter   
from itertools import combinations, permutations
    # 그냥 다 돌면 중복된 것들도 돌아야하니까 모아서 키값만 순회하려고 이렇게 모아두었다.   
weight_cnt = Counter(weights)
dists = [2,3,4]
combination_list = list(permutations(dists, 2))
print(weight_cnt)

answer = 0 
    # 그래서 key 값을 순회를 하는데, 
for key in weight_cnt:
        # 여기는 count를 했을 중복된 key이 있을 때 당연히 value가 1보다 클 거니까 실행될 수 있도록 조건을 걸어준다. 
    if weight_cnt[key] > 1 : 
            # n개를 활용하여 2개를 뽑는 경우의 수를 아래 처럼 적어줄 수 있다. 
            # 중복은 고려하지 않는다. 
            # 모르겠으면, 컴비네이션 손으로 계산을 해봐 
        answer += weight_cnt[key] * ( weight_cnt[key] - 1 ) // 2 
        # combination을 순회하면서 이제 곱해볼거야 
        # x * a = y * b 를 변경하여서 y를 구하는 식으로 작성을 한다. 
    for i, j in combination_list:
        expection = key * i / j 
            # 그렇게 구한 expectation이 weight_cnt에 있으면, 그 수만큼 곱해준다. 
        if expection in weight_cnt:
            answer += weight_cnt[key] * weight_cnt[expection]
    weight_cnt[key] = 0 

print(answer)
