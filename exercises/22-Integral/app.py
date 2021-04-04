integral = {}


def integrales(x):
    for i in range(x):
        i=i+1
        integral[i]=i*i
    return integral


num = int(input("Indica el número que desea agregar al diccionario")) 
print(integrales(num))    