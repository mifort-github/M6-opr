numbers = []
running = "ne"

while running == "ne":
    numbers.append(float(input("vnesi število --> ")))
    print(numbers)
    running = input("konec? -->")
    
numbers.sort()
#numbers.reverse #največje število

print("najmanjše število je:", numbers[0])