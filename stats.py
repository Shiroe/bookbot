def get_number_of_words(text):
    splitted = text.split()
    return len(splitted)


def get_all_characters_occurence(text):
    normalized = text.lower()
    table = {}
    for t in normalized:
        if t not in table:
            table[t] = 1
        else:
            table[t] += 1
    return table


def sort_on(items):
    return items["num"]


def get_characters_occurence_sorted(dictionary):
    arrDict = []
    for key in dictionary:
        if key.isalpha():
            print(f"KEY: {key}")
            arrDict.append({"char": key, "num": dictionary[key]})

    arrDict.sort(reverse=True, key=sort_on)
    return arrDict
