def main():
    print("Hello, world!")
    user_name = input("What is your full name? ")
    user_addr_st = input("What is your street address? ")
    #user_addr_zipcode = input("What is the zip code? ")
    user_dob = input("What is your birthdate (mm/dd/yyyy)? ")

    setUser(user_name, user_addr_st, user_dob)

def setUser(name, address, dob):
    print("Hello, " + name)
    print("You live at: " + address)
    print("Your birthdate is: " + dob)

# Treats the main function as the base function
if __name__ == "__main__":
    main()