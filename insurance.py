# Operational input step
user_input = input("Enter policy number: ")
policy = int(user_input)

# 2. Conditional statements using equality operators (==)
if policy == 1001:
    print("private")
elif policy == 1002:
    print("Commercial")
else:
    print("others")