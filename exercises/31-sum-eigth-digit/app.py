arr = []

def evennums(num):
    for i in range(num):
        if (int(i)>= 1000 and int(i)<=3000):
            if (num%100==0):
                arr.append(num[i])
    return arr

print(evennums([1001, 2468]))                


#(num//100)+(num%100)//10+num%10            