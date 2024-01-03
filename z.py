with open("z") as file:
    line_list = []
    line_count = 0
    for line in file:
        letter_list = []
        for letter in line:
            if letter.isprintable() and not letter.isspace():
                letter_list.append(letter)
        if len(letter_list) != 0:
            words = []

            for x in range(0, len(letter_list), 5):  #modify number to match desired strig length
                word = letter_list[x: x + 5]         #modify number to match desired strig length
                words.append(word)

            line_list.append(words)
        line_count += 1

#edit desired grouping fashion

groups = [
       "abcd",
       "ef",
#      "f",
#      "f",
#      "f",
#      "f",
]
result = []

for la in line_list:
    gr = {}
    for word in la:
        # word.sort()
        counter = []
        for group in groups:
            count = 0
            for n in range(len(group)):
                count += word.count(group[n])
            #if count != 0:
            counter.append(count)
        # gr["".join(word)] = " ".join(sorted(counter, reverse=True))
        gr["".join(word)] = sorted(counter, reverse=True)
    result.append(gr)

for value in result:
    for word, score in value.items():
        print(word, end=" ")
        for number in score:
            print(number, end=" ")
        print("\t", end="")
    print()
print(f"Line count = {line_count}")