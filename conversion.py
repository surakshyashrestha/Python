#function to convert the decimal number into binary number.

def convert(number):
    '''Returns the decimal number into binary number'''
    #Creating an empty list
    reversed_binary=[]
    
    for i in range(1,9,1):
        remainder=number%2
        reversed_binary.append(remainder)
        number=number//2
        i+=1
    return reversed_binary







