def decimalToBase(n, b):
    digits = []
    while n > 0:
        digits.insert(0, str(n % b))
        n = n / b
    return "".join(digits)

def baseToDecimal(n1, b):
    n = 0
    for d in str(n1):
        n = b * n + int(d)
    return n
    
def subtract(x, y, b):
    if b==10:
        return int(x) - int(y)
    
    dx=baseToDecimal(x, b)
    dy=baseToDecimal(y, b)
    dz=dx-dy
    return decimalToBase(dz, b)

def solution(n, b):
    arr=[]
    while True:
        x = "".join(sorted(str(n), reverse=True))
        y = "".join(sorted(str(n)))
        z = subtract(x, y, b)
        
        z_len = len(str(z))
        x_len = len(str(x))
        
        if z_len != x_len:
            z = z * pow(10, (x_len-z_len))
        
        for index, item in enumerate(arr):
            if item == z:
                return index + 1
        arr = [z] + arr
        n = z

print(solution(1211, 10))
        
    
    
