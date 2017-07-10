
def column_to_number(letter):
    ''' Transfer the column letter to number. '''
    letters = ['0',
               'a', 'b', 'c', 'd', 'e', 'f', 'g',
               'h', 'i', 'j', 'k', 'l', 'm', 'n',
               'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z']
    print(letter, letters.index(letter))
    return letters.index(letter)


def collist_to_num(letter_list):
    ''' Transfer the column letter to number. '''
    col_to_num_list = []
    for letter in letter_list:
        col_to_num_list.append(column_to_number(letter))
    return col_to_num_list


def test():
    ''' test for col_to_num() and colist_to_num().'''
    letters_test = ['m', 's']
    # test for col_to_num().
    for letter_test in letters_test:
        num = column_to_number(letter_test)
    # test for colist_to_num().
    num2 = collist_to_num(letters_test)


if __name__ == '__main__':
    '''  '''
    print('---Begin--------')
    test()
    print('---End--------')
