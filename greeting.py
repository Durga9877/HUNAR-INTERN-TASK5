def personalized_greeting(first_name, last_name):
    greeting = f"Hello, {first_name} {last_name}! Welcome!"
    return greeting
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
message = personalized_greeting(first_name, last_name)
print(message)
