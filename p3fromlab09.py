words_already_used = list()
k = 1
s1 = input("input the fist word")
s2 = s1[-2] + s1[-1]
s3 = s1[0] + s1[1]
words_already_used.append(s1)
while k:
    s1 = input(f"input a word starting with {s2}")
    s3 = s1[0] + s1[1]
    if s2 != s3:
        print("the word you entered doesnt start with the letters it should")
        k = 0
    s2 = s1[-2] + s1[-1]
    for x in words_already_used:
        if x == s1:
            print("the word was used before")
            k = 0
    words_already_used.append(s1)
print(words_already_used)

