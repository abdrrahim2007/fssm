#Exercice_1
def produit_recrusive(a,b):
    if b == 0:
        return 0
    else:
        return a + produit_recrusive(a,b-1)
  
recrusive = produit_recrusive(3,4)
print(recrusive)

def produit_iterative(a,b):
    iterative = 0

    for num in range(b):
        iterative += a
    return iterative

iterative = produit_iterative(2,5)
print(iterative)

#Exercice_2
def fact_iter(a):
    if a == 0:
        return 1
    fact = 1
    for i in range(a):
        fact *= a-i
    return fact
print(fact_iter(51))

def fact_recru(a):
    if a == 0:
        return 1
    else:
        return a * fact_recru(a - 1)

print(fact_recru(5)) 

#Exercice_3
def feb_iter(n):
    if n <= 1:
        return n
    a,b = 0,1
    for i in range(2,n+1):
        res = a+b
        a = b
        b = res
    return res

print(feb_iter(6))   

def feb_recu_naive(n):
    if n <= 1:
        return n
    else:
        return feb_recu_naive(n-1) + feb_recu_naive(n-2)
print(feb_recu_naive(6))

def feb_recu_memo(n):
    memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    else:
        return feb_recu_naive(n-1) + feb_recu_naive(n-2)
print(feb_recu_memo(6))

#Exercice_4

def check_palindrome(x):
    if len(x) <= 1:
        return True
    if x[0] != x[-1]:
        return False
    else:
        return check_palindrome(x[1:-1])
print(check_palindrome(x="radar"))
print(check_palindrome("hello"))

#Exercice_5
def permute(x):
    all_permuted = []
    if len(x) <=1:
        return [x]
    else:
        for i in range(len(x)):
            char = x[i]
            other = x[:i] + x[i+1:]

            for per in permute(other):
                all_permuted.append(char + per)
        return all_permuted
print(permute("abc"))

#Exercice_6

def power(a,n):
    if n == 1:
        return a
    else:
        return a* power(a,n-1)
print(power(3,5))

#Exercice_7

def num_chifr(n):
    if n < 10:
        return 1
    else:
        return 1 + num_chifr(n//10)
print(num_chifr(123888999945))         
