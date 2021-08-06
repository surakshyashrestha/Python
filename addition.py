#function to carry out the binary calculation

#function for xor gate
def xorGate(higherNo,lesserNo):
    '''Returns the numbers of XOR Gate'''
    firstInput=~higherNo & lesserNo
    secondInput=higherNo & ~lesserNo
    carryIn=firstInput | secondInput
    return int(carryIn)
#to calculate the carry out
def to_carry(higherNo,lesserNo,carry):
    '''Returns the carryin number'''
    xorOne=higherNo ^ lesserNo
    q=higherNo & lesserNo
    r=carry & xorOne
    s=r | q 
    return int(s)
#to calculate the sum of the numbers
def final_calculation(higherNo,lesserNo):
    '''Returns the sum of the numbers'''
    result=[]
    carry=0
    higherNo.reverse()
    lesserNo.reverse()
    for i in range(len(higherNo)):
        sum1=higherNo[i] ^ lesserNo[i]
        result.append(sum1 ^ carry)
        carry=to_carry(higherNo[i],lesserNo[i],carry)
        i+=1
    result.append(carry)
    return result
