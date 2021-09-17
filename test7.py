score = int(input("Enter score: "))
G = ""
if 90 <= score <= 100:
    G = "A"
elif 80 <= score:
    G = "B"
elif 70 <= score:
    G = "C"
else:
    print ("Your score is", score, ", Grade is F")
print("Your score is", score, ", Grade is", G)