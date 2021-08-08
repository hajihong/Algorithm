import sys
input = sys.stdin.readline

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

word = list(input())
sum = 0

for i in word:
    for j in dial:
        if i in j:
            sum += dial.index(j) + 3

print(sum)