age = int(input("Enter age : "))
def vote(age):
    if age >= 18:
        print("Eligible for Voting!")
    else:
        print("Not Eligible for Voting!")

vote(age)