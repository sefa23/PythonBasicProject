def add(num1,num2):
    topp=num1+num2
    return topp
def extraction(num1,num2):
    ext=num1-num2
    return ext
def impact(num1,num2):
    imp=num1*num2
    return imp
def division(num1,num2):
    div=num1/num2
    return div
while 1==1:
    print("--------------")
    print("--CALCULATOR--")
    print("--------------")
    number1=int(input("1.NUMBER"))
    number2=int(input("2.NUMBER"))
    operation=input("Select Operation:")
    if operation=="+":
        print(number1,operation,number2,"=",add(number1,number2))
    elif operation=="-":
        print(number1,operation,number2,"=",extraction(number1,number2))
    elif operation=="*":
        print(number1, operation, number2, "=", impact(number1, number2))
    elif operation=="/":
        print(number1, operation, number2, "=", division(number1, number2))
    elif operation=="Q" or operation=="q":
        print("exitt.......")
        break
    else:
        print("EROR")


