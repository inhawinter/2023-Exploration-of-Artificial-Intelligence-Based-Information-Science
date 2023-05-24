# week10_class_object04

class PrettyMixin:
    def dump(self):
        # print(f'{self.name} pokemon')
        import pprint
        pprint.pprint(vars(self))


class Pokemon(PrettyMixin):
    def __init__(self, input_name, hp, level):
        self.__name = input_name
        self.hp = hp
        self.level = level

    @property
    def name(self):
        print("getter executed!")
        return self.__name

    @name.setter
    def name(self, input_name):
        print("setter executed!")
        self.__name = input_name


    def info(self):
        print("================")
        print(f"Name : {self.__name}")
        print(f"Hp : {self.hp}")
        print(f"Level : {self.level}")
        print("================")


if __name__ == "__main__":
    p1 = Pokemon("pikachu", 35, 1)
    p2 = Pokemon("squirtle", 40, 1)
    p2.info()  # Pokemon.info(p2)
    p1.dump()
    p2.dump()
    p2.level = 2  # direct access
    p2.info()
    print(p2.__name)  # hidden but it isn't private like other oop language
    """
        print(p2.__name)
          ^^^^^^^^^
        AttributeError: 'Pokemon' object has no attribute '__name'. Did you mean: 'name'?
    """


