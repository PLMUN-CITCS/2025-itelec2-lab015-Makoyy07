# Filename: while_loop_sentinel.py

# Initialize the sum variable
total_sum = 0

# Start a while loop that continues indefinitely
while True:
    # Prompt the user for input
    user_input = input("Enter a number (or 'stop' to finish): ")
    
    # Check if the sentinel value 'stop' is entered
    if user_input.strip().lower() == "stop":
        break  # Exit the loop
    
    # Convert input to a number and add to total_sum (with error handling)
    try:
        number = float(user_input)
        total_sum += number
    except ValueError:
        print("Invalid input. Please enter a numeric value or 'stop'.")

# Print the final total sum
print("The total sum is:", total_sum)
