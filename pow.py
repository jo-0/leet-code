# 50. Pow(x, n)
# https://leetcode.com/problems/powx-n/

def pow(x: float, n: int) -> float:
    if (n == 0) or (x == 1):
        return 1.0
    if (x == 0) or (x > 0 and x < 0.01):
        return 0.0
    signed = True if (n < 0) else False
    res = x
    for _ in range(1, abs(n)):
        res = res * x

    return (1 / res) if signed else res


# print("Pow = ", pow(x=2.00000, n=10))
# print("Pow = ", pow(x=2.10000, n=3))
# print("Pow = ", pow(x=2.00000, n=-2))
# print("Pow = ", pow(x=0.00001, n=2147483647))
# print("Pow = ", pow(x=2, n=-2147483647))
print("Pow = ", pow(x=-1, n=2148364))
# print("Pow = ", pow(x=0.05930, n=2))
