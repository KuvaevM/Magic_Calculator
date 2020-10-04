def memory_re_allocation(filled_size, total_size):
    if filled_size>total_size*2/3:
        return 'Память перевыделилась'
    return 'Память осталась прежней'


