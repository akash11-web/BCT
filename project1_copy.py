def signup():
    array = []
    n = int(input("Enter the number of users to register: "))
    
    for i in range(n):
        print(f"\nEnter user details for user {i+1}:")
        print("----------------------------------")
        user = {
            "name": input(f"Enter the name of user {i+1}: "),
            "email": input(f"Enter the email of user {i+1}: "),
            "password": input(f"Enter the password for user {i+1}: ")
        }
        array.append(user)
    
    return array

def login(array):  
    email_input = input("\nEnter your email to login: ")  
    password_input = input("Enter your password: ")  

    for user in array:  
        if user["email"] == email_input and user["password"] == password_input:  
            print("Login Successful!")  
            print(user)

     

    print("Login Failed! Invalid email or password.")  

def de(delete):
    if(delete==True):
        print("Account removed successfully")

 
# Main process
array = signup()
login(array)
delete = input("After login do you want to delete your details? Yes then enter True otherwise enter False: ")
de(delete)