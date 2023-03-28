
# enemy = [4, 2, 4, 5, 3, 3, 1]	
# n = 7
# k = 3

# answer = []
# def dfs(enemy, index, left_army, left_k):
    
#     if left_army < 0:
#         return None
    
#     if index == len(enemy)-1:
#         return answer.append(index+1)

#     if left_army - enemy[index] < 0 and left_k == 0:
#         return answer.append(index)
    
#     dfs(enemy, index+1, left_army-enemy[index], left_k)
#     if left_k != 0:
#         dfs(enemy, index+1, left_army, left_k-1) 
    
    
# dfs(enemy, 0, n, k)
# print(answer)


from heapq import heappop, heappush

def solution(n, k, enemy):
    answer, sumEnemy = 0, 0
    heap = []
    
    for e in enemy:
        heappush(heap, -e)
        sumEnemy += e
        if sumEnemy > n:
            if k == 0: break
            sumEnemy += heappop(heap) 
            k -= 1
        answer += 1
    return answer


solution(7,3,[4, 2, 4, 5, 3, 3, 1])