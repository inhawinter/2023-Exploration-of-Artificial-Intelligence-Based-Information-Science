animal = 'fruitbat' # global variable


#def print_global():
#    print('inside print_global:', animal)

def change_and_print_global():
    """
    지역변수와 전역변수 실습
    :return: 없음
    """
    global animal
    student = '이우진'
    print('inside change_and_print_global:', animal)
    animal = 'wombat'
    print('after the change:', animal)
    print(locals())
    print(change_and_print_global.__name__)
    print(change_and_print_global.__doc__)


if __name__ == "__main__":

print('at the top level:', animal)
# print_global()
change_and_print_global()