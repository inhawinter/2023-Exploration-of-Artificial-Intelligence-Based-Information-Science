class Pokemon:
    pass


if __name__ == "__main__":
    pikachu = Pokemon()  # instance creation
    eevee = Pokemon()  # instance creation

    pikachu.level = 1
    pikachu.hp = 35
    pikachu.nemesis = eevee

    print(pikachu.hp)
    print(pikachu.nemesis)
    print(pikachu)
    print(eevee.hp)