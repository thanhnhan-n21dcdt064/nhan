def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
n = int(input("Nhap vao so nguyen n: "))
if n < 0:
    print("So nguyen n phai lon hon hoac bang 0.")
else:
    print("So Fibonacci bac 1 cua", n, "la:", fibonacci_recursive(n))

