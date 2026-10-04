def calculate_basic(a, b):
    addition = a + b
    multiplication = a * b
    return addition, subtraction

# Example usage:
add_result, sub_result = calculate_basic(10, 5)

print(f"Addition result: {add_result}")       # Outputs: 15
print(f"Subtraction result: {sub_result}")    # Outputs: 5
