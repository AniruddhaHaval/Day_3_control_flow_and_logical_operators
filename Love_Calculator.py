your_name = input("Enter Your Name: ")
their_name = input("Enter their Name: ")

combine_name = (your_name + their_name).lower()

print(combine_name)

t = combine_name.count("t")
r = combine_name.count("r")
u = combine_name.count("u")
e = combine_name.count("e")

score_1 = t + r + u + e

l = combine_name.count("l")
o = combine_name.count("o")
v = combine_name.count("v")
e = combine_name.count("e")

score_2 = l + o + v + e

total_score = str(score_1) + str(score_2)

print(f"your score is {total_score} ")

