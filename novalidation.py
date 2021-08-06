
#function to check if the value is valid or not
def novalidation(string):
    '''Returns the novalidation of the given input'''
    num=input(string)
    try:
        number=int(num)
        return number
    except ValueError:
       #Error if string value or empty value is entered
        print("ERROR!!!^^^^Please input a valid number^^^^^^")
    return novalidation(string)    


#function to check if the value is valid or not

def checkNumber(string):
    '''Returns the number after checking under novalidation function'''
    while True:
        number=int(novalidation(string))
        if (number>=0 and number<=255):
            break
        else:
            print("Please choose number between 0 and 255")
            continue
    return number    
    
