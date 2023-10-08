largest = None
smallest = None

while True:
    input_str = input("Enter an integer number (or 'done' to exit): ")

    if input_str.lower() == 'done':
        break

    try:
        number = int(input_str)

        if largest is None or number > largest:
            largest = number

        if smallest is None or number < smallest:
            smallest = number
    except ValueError:
        print("Invalid input. Please enter a valid integer or 'done'.")

if largest is not None and smallest is not None:
    print("Largest:", largest)
    print("Smallest:", smallest)
else:
    print("No valid numbers were entered.")


# numbers = []
#
# while True:
#     user_input = input("Enter an integer number ('done' to finish): ")
#
#     if user_input == 'done':
#         break
#
#     try:
#         number = int(user_input)
#         numbers.append(number)
#     except ValueError:
#         print("Invalid input. Please enter a valid integer or 'done'.")
#
# if numbers:
#     largest = max(numbers)
#     smallest = min(numbers)
#     print("Largest:", largest)
#     print("Smallest:", smallest)
# else:
#     print("No valid numbers entered.")
