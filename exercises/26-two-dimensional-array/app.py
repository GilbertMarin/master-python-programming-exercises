import random
test = []
def array_2d(x, y):
    for i in range (0,x):
        for j in range (0,y):
            test[i][j]=int(random.randint(97,122))
    return test
print(array_2d(3,5))            