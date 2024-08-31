
name = input("Enter your name: ")


print("Hello, " + name + "! Let's explore your favorite numbers:")


num1 = int(input("Enter your first favorite number: "))
num2 = int(input("Enter your second favorite number: "))
num3 = int(input("Enter your third favorite number: "))


numbers = [num1, num2, num3]

for num in numbers:
    if num % 2 == 0:
        print("The number", num, "is even.")
    else:
        print("The number", num, "is odd.")


for num in numbers:
    print("The number", num, "and its square:", (num, num ** 2))


total_sum = num1 + num2 + num3
print("\nAmazing! The sum of your favorite numbers is:", total_sum)


is_prime = True
if total_sum > 1:
    for i in range(2, total_sum):
        if total_sum % i == 0:
            is_prime = False
            break
else:
    is_prime = False

if is_prime:
    print("Wow,", total_sum, "is a prime number!")
else:
    print(total_sum, "is not a prime number.")