a,b,c = map(int,input().split())

sum = 0
#memo = {}
def rec(x): #x는 b
    if x == 1:
        return a%c
    else:
        tmp = rec(x//2)
        if x%2 == 0: #짝수
            return (tmp * tmp)%c
        else: 
            return (tmp* tmp *a)%c

sum = rec(b)
print(sum)

