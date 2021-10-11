import math
def isPrimeNumber(n):
    # so nguyen n < 2 khong phai la so nguyen to
    if (n < 2):
        return False

    # check so nguyen to khi n >= 2
    squareRoot = int(math.sqrt(n))
    for i in range(2, squareRoot + 1):
        if (n % i == 0):
            return False
    return True


[n,x] = [int(x) for x in input().split()]
dem = 0;  # đếm số số nguyên tố
i = 2;  # tìm số nguyên tố bắt dầu từ số 2
sb = "";
print(x,end=' ')
while (dem < n):
    if (isPrimeNumber(i)):
        x+=i
        sb = sb + str(x) + " ";
        dem = dem + 1;
    i = i + 1;
print(sb);