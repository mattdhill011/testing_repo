print("Hello, World")


for n in range(1,100):
    if n % 10 == 1:
        cardinal = "st"
    elif n % 10 == 2:
        cardinal = "nd"
    elif n % 10 == 3:
        cardinal = "rd"
    else:
        cardinal = "th"
    
    print(f"This is the {n}{cardinal} test")
