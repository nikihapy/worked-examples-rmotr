def conditional_multiplication(a_condition, number):
    if a_condition==true:
        return number*10
    else: 
        return number

result=conditional_multiplication(True,20)
print result
result=conditional_multiplication(False,5)
print result
