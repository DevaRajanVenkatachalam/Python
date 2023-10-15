Atm_card="card"
pin=4747
Money=1000
Temp=0
# Setting up the range of for loop
for outer_value in range(1,3):
    #Outer for loop denotes the person who use the ATM
    print("Welcome to Public Bank")
    print("Please insert your card")
    print("Enter your pin")
    if (Atm_card=="card")&(pin==4747):
        if outer_value==1:
            while Temp<=Money:
                print(f" count {Temp} Total Amount {Money}")
                Temp=Temp+100
                print(f" Take your cash {Money} Rupee ")
            else:
                print("Only one atempt is possible")
        elif(Atm_card=="card")|(pin==4747):
            print("Any one value is wrong")
        else:
            print("Both values are wrong")
        print("Thank you for using")




