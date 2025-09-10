for i in range(5):
    a = str(input("Enter your name: "))
    b = int(input("Enter your age: "))
    print(f"Hello {a}")
    print(f"You will be {b+2} years old in 2 years")
    print(f"You entered {b}, which means you have lived {b//10} decades and {b%10} years")