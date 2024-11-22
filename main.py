from math import gcd

def pollard_rho( n , f=lambda x: (x**2 + 1) %n): 
    
    c = 1 
    a= c 
    b = c 
    
    while True: 
        a = f(a)
        b = f(f(b))
        d = gcd(abs(a-b),n )
        if d == n : 
            return None
        if d > 1:
            return d 

n = 1359331
factor = pollard_rho(n)
if factor: 
    print(f"Нетривиалный делитель числа {n}: {factor}.")
    print(f"Другой делитель: {n // factor},")
else: 
    print(f"Не удалось найти делитель для чтсла {n}.")
    
    