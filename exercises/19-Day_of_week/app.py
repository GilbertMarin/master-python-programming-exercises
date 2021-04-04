#Complete the function to return the number of day of the week for k'th day of year. 
def day_of_week(k):
    if (k == 1):
        return 4
    if (k == 2):
        return 5
    if (k == 3):
        return 6        
    if (k == 4):
        return 7
    if (k == 5):
        return 1
    if (k == 6):
        return 2    
    else:
        return 3


#Invoke function day_of_week with an interger between 0 and 6 (number for days of week)
print(day_of_week(1))