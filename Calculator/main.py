try:
    a = int(input("Enter first number: "))
    b = int(input("enter second number: "))
    

    print("Press + for addition\nPress - for substraction\nPress * for multiplication\nPress / for division")

    o = input("Enter an operator: ")
   
    match o:
        case "+":
            print(f"The result is:{a + b}")
        case "-":
            print(f"The result is:{a - b} ")
        case "*":
            print(f"The result is:{a * b} ")
        case "/":
            print(f"The result is:{a / b} ")
        case default:
            print("Errore!!!")    
  

except:
    print("Enter valid number!")  
      