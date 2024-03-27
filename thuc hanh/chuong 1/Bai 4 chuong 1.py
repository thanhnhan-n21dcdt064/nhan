def pascal(n):
    for line in range(0, n):
        # In ra so 1 o moi dau dong
        print("n=" + str(line), 1, end=" ")
        # Tinh toan va in ra so o giua
        for i in range(1, line):
            print(calculate_binomial_coefficient(line, i), end=" ")
        # In ra so 1 o cuoi moi dong
        if line > 0:
            print(1, end="")

        print() 
# Phuong thuc de tinh so nhi thuc
def calculate_binomial_coefficient(n, k):
    res = 1
    if k > n - k:
        k = n - k
    for i in range(k):
        res *= (n - i)
        res //= (i + 1)
    return res
# Nhap so nguyen duong n 
n = int(input("Nhap vao so nguyen duong n: "))
# In ra tam giac Pascal cho bac n
pascal(n)
