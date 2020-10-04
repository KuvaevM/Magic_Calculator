def memory_re_allocation(filled_size, total_size):
    if filled_size>total_size*2/3:
        return 'Память перевыделилась'
    return 'Память осталась прежней'


def most_popular_item(text):
    max = 0
    frequent_element = ''
    for i in text:
        counter = 0
        for j in text:
            if i == j:
                counter = counter+1
        if(max<counter):
            max = counter
            frequent_element = i
    return frequent_element


def most_popular_word(text):
    list_of_words = text.split()
    max = 0
    frequent_word = ''
    for i in list_of_words:
        counter = 0
        for j in list_of_words:
            if i == j:
                counter = counter+1
        if(max<counter):
            max = counter
            frequent_word = i
    return frequent_word


if __name__ == '__main__':
    print(most_popular_item('0rrrrrrrrrrrrrrrrrryyuyroooooo0000000000000000000000000000000000000000000ooo     '))