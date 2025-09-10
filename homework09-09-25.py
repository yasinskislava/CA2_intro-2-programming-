total = 0
for i in range(10):
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = str(input("Enter the operation (+, -, *, /, **, //, %): "))
    ans = int(input("Enter the expected result: "))
    if c == '+' and a + b == ans:
        total+=1
    elif c == '-' and a - b == ans:
        total+=1
    elif c == '*' and a * b == ans:
        total+=1
    elif c == '/' and b != 0 and a / b == ans:
        total+=1
    elif c == '**' and a ** b == ans:
        total+=1
    elif c == '//' and b != 0 and a // b == ans:
        total+=1
    elif c == '%' and b != 0 and a % b == ans:
        total+=1
    print("  ")
print("You got", total, "out of 10 correct.")

    
