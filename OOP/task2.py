class Monster:
    def __init__(self, name="Неизвестная тварь", hp=100, dmg=10):
        self.name = name
        self.hp = hp
        self.dmg = dmg

        print(f"Монстр: {self.name}")
        print(f"HP: {self.hp}")
        print(f"DMG: {self.dmg}")
        print()


name1, hp1, dmg1 = input().split()
m1 = Monster(name1, int(hp1), int(dmg1))

name2, hp2, dmg2 = input().split()
m2 = Monster(name2, int(hp2), int(dmg2))

