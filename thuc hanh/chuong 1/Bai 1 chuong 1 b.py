def fibonacci_iterative(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
n = int(input("Nhap vao so nguyen n: "))
if n < 0:
    print("So nguyen n phai lon hon hoac bang 0.")
else:
    print("So Fibonacci bac 1 cua", n, "la:", fibonacci_iterative(n))
