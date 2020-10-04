def memory_re_allocation(filled_size, total_size):
    """Размер dict будет изменен, если он заполнен на две трети"""
    if filled_size > total_size*2/3:
        return 'Память перевыделилась'
    return 'Память осталась прежней'


def most_popular_item(text):
    """Ищется элемент, наиболее частый в строке"""
    maximum = 0
    frequent_element = ''
    for i in text:
        counter = 0
        for j in text:
            if i == j:
                counter = counter+1
        if maximum < counter:
            maximum = counter
            frequent_element = i
    return frequent_element


def most_popular_word(text):
    """Ищется слово наиболее популярное в тексте"""
    list_of_words = text.split()
    maximum = 0
    frequent_word = ''
    for i in list_of_words:
        counter = 0
        for j in list_of_words:
            if i == j:
                counter = counter+1
        if maximum < counter:
            maximum = counter
            frequent_word = i
    return frequent_word


def average_word_length(text):
    """Расчитывается средняя длина слов"""
    list_of_words = text.split()
    summary_length = 0
    word_count = len(list_of_words)
    for i in list_of_words:
        summary_length += len(i)
    return summary_length/word_count


def palindrom(alphabet, length):
    """Ищутся все палиндромы длины не более length из букв алфавита"""
    list_of_palindroms = []
    list_of_symbols = alphabet.split()
    for i in range(length):  # в список палиндромов добавляются первые половины палиндромов с чётной длиной и первые
        # половины с центральным элементом палиндромов с нечётной длиной
        list_of_palindroms.append([])
        if i == 0 or i == 1:
            for j in range(len(list_of_symbols)):
                list_of_palindroms[i].append(list_of_symbols[j])
        else:
            for j in list_of_palindroms[i-2]:
                for k in list_of_palindroms[0]:
                    list_of_palindroms[i].append(j+k)
    for i in range(length):  # к палиндромам добавляются недостающие зеркальные части
        for j in range(len(list_of_palindroms[i])):
            if i % 2 == 0:
                help_str = list_of_palindroms[i][j][:-1]
                reverse_str = help_str[::-1]
                list_of_palindroms[i][j] += reverse_str
            else:
                reverse_str = list_of_palindroms[i][j][::-1]
                list_of_palindroms[i][j] += reverse_str
    return list_of_palindroms


if __name__ == '__main__':
    print(average_word_length('0rrrrrrrrrrrrrrrrrryyuyroooo oo00000000000000 0 0 000000000000000000000000000ooo     '))
    print(palindrom('a b c', 5))
