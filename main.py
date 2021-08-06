
#importing modules

import novalidation
import reversing
import conversion
import addition

#main method of the program

print ("\n^^^^^^^^^^^^^^^^^^^^^^^PROGRAM FOR ADDING BINARY NUMBERS^^^^^^^^^^^^^^^^^^^^^^^^\n")
             
def main_method():
    '''Returns the final output of the program'''
    while True:
        firstNo=novalidation.checkNumber("Enter the first number: ")
        binaryFirstNo=conversion.convert(firstNo)
        real_binaryfirst=reversing.reverse(binaryFirstNo)
       
        secondNo=novalidation.checkNumber("Enter the second number: ") 
        binary_number2=conversion.convert(secondNo)
        real_binarysecond=reversing.reverse(binary_number2)
        
        reversed_result=addition.final_calculation(real_binaryfirst[0],real_binarysecond[0])
        real_result=reversing.reverse(reversed_result)  
        rr=real_result[0]
        reducedList=[]
        finalResult=''
        rr2=real_result[1]
            
        ##Final output
        print ("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("\t\t\t output")
        print ("--------------------------------------------------------------------------------")
  
        print("You have entered ---> \tFirst Number : ",firstNo,"\tSecond Number : ",secondNo)
        
        check=False
        for i in range(0,len(rr)):
            if rr[i]>0:
                check=True
            if check==True:
                reducedList.append(rr[i])
        
        for element in reducedList:
            finalResult += str(element)

        if len(finalResult)>8:
            print("\n")
            error = "ERROR!!!THIS IS NOT 8 BIT NUMBER."
            print(error)
        else:
            print("\nFirst Number in binary is : ",real_binaryfirst[1],"\nSecond Number in binary is :",real_binarysecond[1])
            print("\n\t         ",real_binaryfirst[1],"\n\t       + ",real_binarysecond[1],"\n\t         __________\n\t\t ",rr2[1:])

            print ("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("Binary sum of ",firstNo," and ",secondNo,"is : ",finalResult)
            print ("--------------------------------------------------------------------------------")
  
        continuos=input("\n\nDo you really want to run this application?. Type yes to continue: ")
        if continuos.upper()=="YES":
            continue           
        else:
            print ("\n*********************************************************************************")
            print("Hope you enjoy this application.")
            print ("**********************************************************************************")
            break
            
if __name__=='__main__':
    main_method()

