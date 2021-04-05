arr = ['0100','0011','1010','1001']

def divisibles(num):
    for i in num:
        if (int(i) % 5 == 0):
            return i

print(divisibles(arr))            