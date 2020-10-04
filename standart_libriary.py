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


if __name__ == '__main__':
    print(most_popular_item('0rrrrrrrrrrrrrrrrrryyuyroooooo0000000000000000000000000000000000000000000ooo     '))