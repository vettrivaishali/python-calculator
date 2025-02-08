def calculator():
    while True:
        print("You have sucessfully entered into vaishu's calculator")
        print("HERE ARE THE LIST OF OPERATIONS WE HAVE: ")
        print("1.Addition (+)")
        print("2.Subraction (-)")
        print("3.Multiplication (*)")
        print("4.Division (/)")
        print("5.Exit...")
        num1=int(input("ENTER YOUR FIRST NUMBER:"))
        num2=int(input("ENTER YOUR SECOND NUMBER:"))

        choice=int(input("ENTER YOUR CHOICE NUMBER FROM NUMBER 1 TO 5 : "))
        if choice==1:
            print("The addition of two numbers is : ",num1+num2)
        elif choice==2:
            print("The subraction of two numbers is : ",num1-num2)
        elif choice==3:
            print("The multiplication of two numbers is : ",num1*num2)
        elif choice==4:
            print("The division of two numbers is : ",num1/num2)
        elif choice==5:
            print("You have successfully exited the program")
            break
        else:
            print("please Enter the valid choice")
        
calculator()
