def number(x, y):
    for n in range(x, y+1):
        s = sum_of_divisors(n)
        if s < n:
            print(n, "la deficient")
        elif s == n:
            print(n, "la perfect")
        else:
            print(n, "la abundant")
# Phuong thuc đe tinh tong cac uoc so cua n
def sum_of_divisors(n):
    if n == 1:
        return 1
    divisor_sum = 1  # 1 la uoc so cua moi so nguyen duong
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisor_sum += i
            if i != n // i: 
                divisor_sum += n // i
    return divisor_sum
# Nhap hai so nguyen duong x va y tu nguoi dung
x = int(input("Nhap so nguyen duong x: "))
y = int(input("Nhap so nguyen duong y (y >= x): "))
# Kiem tra va in ra phan loai cua cac so tu x den y
print("Phan loai cac so tu", x, "den", y, ":")
number(x, y)
