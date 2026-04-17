# inheritance.py

# Parent Class
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def login(self):
        print(f"User {self.username} logged in.")

# Subclass (Inheritance)
class Admin(User):
    def __init__(self, username, email, permissions):
        # Use super() to call parent constructor
        super().__init__(username, email)
        self.permissions = permissions

    # Method Overriding
    def login(self):
        print(f"Admin {self.username} logged in with full access.")

    # Specialized Method
    def delete_user(self, user):
        print(f"Admin {self.username} deleted user {user.username}.")

# Polymorphism Task
user1 = User("albin", "albin@example.com")
admin1 = Admin("lealabs_admin", "admin@lealabs.com", ["delete", "modify", "add"])

users = [user1, admin1]

for u in users:
    u.login()  # Each responds differently

# Demonstrate specialized method
admin1.delete_user(user1)

# Trying to call delete_user() on User will cause an AttributeError
# user1.delete_user(admin1)  # Uncomment to see the error
