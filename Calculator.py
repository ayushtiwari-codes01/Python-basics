while True:
    print("\nSimple Calculator")
    

    num1 = float(input("Enter the first number: "))
    operator = input("Enter the operator (+,-,/,*,**): ")
    num2 = float(input("Enter the second number: "))

    if operator == "+":
        print("Result:", num1 + num2)
    
    elif operator == "-":
        print("Result:", num1 - num2)
    
    elif operator == "/":
        if num2 == 0:
            print("Cannot divided by Zero")
        else:
            print("Result:", num1 / num2)
                          
    elif operator == "*":
       print("Result:", num1 * num2)
                              
    elif operator =="**":
       print("Result:", num1 ** num2)
                                  
    else:
        print("invalid operator")
                                      
    again = input("Do you want to calculate again? (yes/no): ")
                                      
    if again.lower() != "yes":
        print("Calculate Closed.")
        break