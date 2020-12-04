n=0
ans=1
def gcd(m, n):
    return m if n == 0 else gcd(n, m % n)

m = int(input("輸入第一個數字："))
n = int(input("輸入第二個數字："))
print("\n最大公因數是: ", gcd(m, n))
