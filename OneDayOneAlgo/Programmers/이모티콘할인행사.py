from itertools import permutations, combinations, product
def solution(users, emoticons):
    answer = []
    discount = [10,20,30,40]
    n = len(emoticons)
    
    for elem in list(product(discount, repeat=n)):
        count_service = 0
        total_price = 0
        for user in users:
            percent, price = user
            count_price = 0
            for i in range(n):
                if elem[i] >= percent:
                    output_price = emoticons[i]*(100-elem[i])/100
                    count_price += output_price
            if count_price >= price:
                count_service += 1
            else:
                total_price += count_price
            
            
        answer.append([int(count_service), int(total_price)])
                
                
    
    
    
    answer.sort(key= lambda x : (-x[0],-x[1]))    
        
    
    return answer[0]


print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))