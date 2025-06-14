questions = [
    ["What is the capital of India?", "Mumbai", "Delhi", "Kolkata", "Chennai",2],
    ["Which planet is known as the Red Planet?", "Earth", "Venus", "Mars", "Jupiter",3],
    ["Who wrote the national anthem of India?", "Bankim Chandra Chatterjee", "Sarojini Naidu", "Rabindranath Tagore", "Mahatma Gandhi",3],
    ["Which gas do plants absorb from the atmosphere?", "Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen",3],
    ["What is the smallest prime number?", "0", "1", "2", "3",2]
]


for question in questions:
    print(question[0])
    print(f"1. {question[1]}")
    print(f"2. {question[2]}")
    print(f"3. {question[3]}")
    print(f"4. {question[4]}")

    ans = int(input("Entyer correct Option (1-4): "))

    if ans == question[5]:
        print("Correct Answer!\n")
    else:
        print("Incorrect, better luck next time!!!\n")    
    
  