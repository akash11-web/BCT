# Step 1: Create an empty list to store user data
users_data = []

# Step 2: Create functions for sign-up, login, and delete functionality
def sign_up():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    
    # Step 3: Store data in a dictionary
    user_dict = {'name': name, 'email': email, 'password': password}
    
    # Add the user data to the users list
    users_data.append(user_dict)
    print(f"User {name} signed up successfully!")

def login():
    email = input("Enter your email to login: ")
    password = input("Enter your password to login: ")

    # Step 4: Check if the user data exists and matches
    for user in users_data:
        if user['email'] == email and user['password'] == password:
            print("Login successful!")
            return
    print("Login failed! Incorrect email or password.")

def delete_user():
    email = input("Enter the email of the user to delete: ")

    # Step 5: Delete user data if found
    global users_data
    users_data = [user for user in users_data if user['email'] != email]
    print(f"User with email {email} has been deleted.")

def display_users():
    # Step 6: Display user data in tabular form using pandas
    if users_data:
        df = pd.DataFrame(users_data)
        print("\nUsers Data:")
        print(df)
    else:
        print("No users to display.")

# Step 7: Main program to execute the functions
def main():
    while True:
        print("\nOptions:")
        print("1. Sign Up")
        print("2. Login")
        print("3. Display Users")
        print("4. Delete User")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            sign_up()
        elif choice == '2':
            login()
        elif choice == '3':
            display_users()
        elif choice == '4':
            delete_user()
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please select a valid option.")

# Running the program
main()
