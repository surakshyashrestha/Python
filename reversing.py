#function to reverse the list. 

def reverse(list):
    '''Returns the reversed number list'''
    real_string=""
    list.reverse()
    for i in range(len(list)):
        real_string+=str(list[i])
    return [list,real_string]


