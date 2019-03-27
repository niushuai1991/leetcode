
dic = dict()

def fib(n):
    if n in dic:
        return dic[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    num = fib(n-1) + fib(n-2)
    dic[n] = num
    return num

def fib2(n):
    if n <= 0:
        return n
    memo = dict()
    memo[0] = 0
    memo[1] = 1
    for i in range(2, n+1) :
        memo[i] = memo[i-1] + memo[i - 2]
    return memo[n]

print(fib2(50))

# https://blog.csdn.net/u013309870/article/details/75193592