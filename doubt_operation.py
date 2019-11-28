text = input("Enter message: ")
operation = input("Select option 1 or 2: ")


def remove_text(txt):
    final_list = []
    for num in txt:
        if num not in final_list:
            final_list.append(num)
    return final_list


if operation == "1":
    for char in text:
        if (char != " ") & (not char.isalpha()):
            text = text.replace(char, "")

    words = text.split()
    words.sort()
    print("The sorted words are:")
    print(remove_text(words))


if operation == "2":
    for char in text:
        if not char.isalpha():
            text = text.replace(char, "")
    letter = {}
    for x in text:
        if x in letter:
            letter[x] += 1
        else:
            letter[x] = 1
    print("The number of each letter  :\n " + str(letter))
