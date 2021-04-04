# Your code here
x = int(input("coloca el numero para buscar su factorial"))
fac = 1
for i in range(x, 0, -1):
    fac=fac*i    
print(fac)