# week06_function.py
def ishs(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)


nb = [9]
ishs(7)
ishs(8)
ishs(3, nb)
