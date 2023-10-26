# Function to calculate simple interest
def calculate_simple_interest(principal, rate, time):
    # Convert rate to a percentage
    rate = rate / 100
    # Calculate simple interest
    simple_interest = (principal * rate * time)
    return simple_interest

# Input principal amount, rate of interest, and time
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time (in years): "))

# Calculate simple interest
interest = calculate_simple_interest(principal, rate, time)

# Display the result
print("Simple Interest: ", interest)
