def gcd(n, m):
    while m != 0:
        n, m = m, n % m
    print(n)

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    gcd(n, m)