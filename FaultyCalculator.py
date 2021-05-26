# Design a Calculator That will correctly solve all problem except the following
# 45 * 3 = 555, 56+9 = 77 56/6 = 4
#without  Any Class/Function

print("Type '+' for Addition")
print("Type '-' for Addition")
print("Type '/' for Addition")
print("Type '*' for Addition")
print("Type '%' for Addition")
print("Type '**' for Addition")
#print("Type '' for Addition")

useAgain = "Yes"
while useAgain == "Yes":
    varOperater = input("Enter Operator : ")

    var1 = int(input("Enter Number 1 : "))
    var2 = int(input("Enter Number 2 : "))

    if var1 == 45 and var2 == 3 and varOperater == '*':
        print("555")
    elif var1 == 56 and var2 == 9 and varOperater == '+':
        print("77")
    elif var1 == 56 and var2 == 6 and varOperater == '/':
        print("4")
#if var1 == 45 and var2 == 3 and varOperater == '*':
#if var1 == 45 and var2 == 3 and varOperater == '*':
    elif varOperater == '+':
        print(var1 + var2)
    elif varOperater == '-':
        print(var1 - var2)
    elif varOperater == '/':
        print(var1 / var2)
    elif varOperater == '*':
        print(var1 * var2)
    elif varOperater == '%':
        print(var1 % var2)
    elif varOperater == '**':
        print(var1 ** var2)

    useAgain = input("Use Again (Yes/No) : ")

