def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def prime_factors(num):
    i = 2
    factors = []
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            factors.append(i)
    if num > 1:
        factors.append(num)
    return factors

def common_prime_divisors(m, n):
    factors_m = set(prime_factors(m))
    factors_n = set(prime_factors(n))
    return factors_m & factors_n


m = int(input("Nhập số nguyên thứ nhất : "))
n = int(input("Nhập số nguyên thứ hai : "))

# Hiển thị tất cả các ước nguyên tố chung
common_primes = common_prime_divisors(m, n)
print("Các ước nguyên tố chung:", common_primes)

# (GCD)
gcd_result = gcd(m, n)
print("Ước chung lớn nhất (GCD):", gcd_result)

# (LCM)
lcm_result = lcm(m, n)
print("Bội số chung nhỏ nhất (LCM):", lcm_result)
