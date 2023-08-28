def find_indexes(word, letter):
    index_list = []

    for i in range(len(word)):
        if word[i] == letter:
            index_list.append(i)

    return index_list