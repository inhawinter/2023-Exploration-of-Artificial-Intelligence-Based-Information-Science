# week10_class_object05

class Pokemon:
    pokemon_count = 0

    def __init__(self, input_name, hp, level):
        self.__name = input_name
        self.hp = hp
        self.level = level
        Pokemon.pokemon_count = Pokemon.pokemon_count + 1

    @staticmethod
    def intro():
        print("ISHS Pokemon Game")


    @classmethod
    def print_pokemon_count(cls):
        # print(f"pokemon population : {Pokemon.pokemon_count}")
        print(f"pokemon population : {cls.pokemon_count}")


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
    Pokemon.intro()
    p1 = Pokemon("pikachu", 35, 1)
    p2 = Pokemon("squirtle", 40, 1)
    p3 = Pokemon("charizard", 85, 36)
    print(Pokemon.pokemon_count)
    Pokemon.print_pokemon_count()