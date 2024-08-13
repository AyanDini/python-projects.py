print("Let's take a quiz!")


playing = input("DO you want to play? ")

if playing != "yes":
        quit()

print("okay! Let's play :)")
score = 0

answer = input("How many countries is in Africa? ")
if answer.lower() == "54":
    print('Correct!')
    score += 1
else: 
    print("Incorrect!")

answer = input("How many countries is in East Africa? ")
if answer.lower() == "20":
    print('Correct!')
    score += 1
else: 
    print("Incorrect!")

answer = input("How many countries is in North Africa? ")
if answer.lower() == "7":
    print('Correct!')
    score += 1
else: 
    print("Incorrect!")

answer = input("How many countries is in South Africa? ")
if answer.lower() == "1":
    print('Correct!')
    score += 1
else: 
    print("Incorrect!")

answer = input("How many countries is in  West Africa? ")
if answer.lower() == "17":
    print('Correct!')
    score +=1
else: 
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%.")