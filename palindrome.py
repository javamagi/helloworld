def is_palindrome(s):
    # Convert to string in case input is a number
    s = str(s)
    # Check if string equals its reverse
    return s == s[::-1]

# Example usage
user_input = input("Enter a string or number: ")
if is_palindrome(user_input):
    print(f'"{user_input}" is a palindrome!')
else:
    print(f'"{user_input}" is not a palindrome.')
