from model.vacationer import Vacationer

def main():
    print("Hello, world!")
    user_name = input("What is your full name? ")
    user_dob = input("What is your birthdate (mm/dd/yyyy)? ")

    setUser(user_name, user_dob)

def setUser(name, dob):
    organizer = Vacationer(name,dob)
    print("Hello, " + organizer.name)
    print("Your birthdate is: " + organizer.dob)

# Treats the main function as the base function
if __name__ == "__main__":
    main()