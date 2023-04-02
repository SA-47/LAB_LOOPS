#part 1
for num in range(45, 211):
    if num == 100:
        continue
    print(num)
    if num == 205:
        break

#part 2
answer = input("What is the product of 7 * 24? ")
while answer != "168":
    print("Your answer is wrong. Please try again.")
    answer = input("What is the product of 7 * 24? ")
print("You answered this question correctly.")