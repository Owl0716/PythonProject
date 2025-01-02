TOP_VALUE =43.
def print_funtion(a, b):
    if a == TOP_VALUE+1:
        return
    if a >b:  # When A reaches 10, reset A and increment B
        print()
        print_funtion(1, b + 1)
        return
    print(f"{a}x{b}={a * b}", end=" ")  # Print the product
    print_funtion(a + 1, b)

# Start the recursion
print_funtion(1, 1)
