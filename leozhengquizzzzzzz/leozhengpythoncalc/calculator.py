score = 0
print("Welcome to the Chess Quiz")
qs1 = input("1. What Country does Mr. Veldkamp Live in?")
print("Q1 Answer: " + qs1)
if qs1 == "Canada" or qs1 == "canada":
    print("Correct")
    score += 1
else:
    print("Incorrect")

qs2 = input("2. Who's the guy who's nose grows when he lies?")
print("Q2 Answer: " + qs2)
if qs2 == "Pinocchio" or qs2 == "pinocchio":
    print("Correct")
    score += 1
else:
    print("Incorrect")

qs3 = input("3. Whats the big rock that orbits the Earth called?")
print("Q3 Answer: " + qs3)
if qs3 == "The Moon" or qs3 == "Moon" or qs3 == "the Moon" or qs3 == "the moon" or qs3 == "moon":
    print("Correct")
    score += 1
else:
    print("Incorrect")

qs4 = input("4. What country was sushi invented in?")
print("Q4 Answer: " + qs4)
if qs4 == "China" or qs4 == "china":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print("Your score is " + str(score) + " / 4 (" + str(score / 4 * 100) + "%)")
if score > 2:
    print("Good Job!")
else:
    print("You need to study!")
