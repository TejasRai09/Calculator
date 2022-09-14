
# Add
def sum(n1,n2):
  return n1+n2

# Subtract
def subtract(n1,n2):
  return n1-n2  

#  Multiply
def multiply(n1,n2):
  return n1*n2

# Divide

def divide(n1,n2):
  return n1/n2
mathematical_operations = {}
mathematical_operations["+"] = sum
mathematical_operations["-"] = subtract
mathematical_operations["*"] = multiply
mathematical_operations["/"] = divide




def TEJ_CALC(): 
        stop = True      
        num1 = float(input("What is the first number: "))
        for operation in mathematical_operations:
            print(operation)
        operation_symbol = input("Pick a operation from above list ")
        num2 = float(input("What is the second number: "))
        Answer1 = mathematical_operations[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {Answer1}")
        while stop:
            yes_or_no = input("Type 'yes' for contuinuing 'no' to start fresh: ")
            if yes_or_no == "no":
                # print("THANKS FOR USING TEJ CALCULATOR")
                stop = False
                TEJ_CALC()
            else:
                num3 = int(input("What is the other number: "))
                operation_symbol = input("Pick a operation from above list ")
                Answer2 = mathematical_operations[operation_symbol](Answer1,num3)
                print(f"{Answer1} {operation_symbol} {num3} = {Answer2}")
                Answer1 = Answer2
                
                


        # final_answer += Answer1
        # print(f"The value of {num1} {operation_symbol} {num2} is : {final_answer}")
        # num3 = int(input("What is the first number: "))
        # operation_symbol = input("Pick a operation from above list ")
        # Answer2 = mathematical_operations[operation_symbol](Answer1,num3)
        # print(f"The value of {Answer1} {operation_symbol} {num3} is : {Answer2}")
TEJ_CALC()



