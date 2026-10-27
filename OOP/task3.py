class Monster:
    def __init__(self, name="Неизвестная тварь", hp=100, dmg=10) -> None:
        self.name = name
        self.hp = hp
        self.dmg = dmg

        print(f"Монстр: {self.name}")
        print(f"HP: {self.hp}")
        print(f"DMG: {self.dmg}")
        print()


name1, hp1, dmg1 = input().split()
m1 = Monster(name=name1, hp=int(hp1), dmg=int(dmg1))

name2, hp2, dmg2 = input().split()
m2 = Monster(name=name2, hp=int(hp2), dmg=int(dmg2))

while m1.hp > 0 and m2.hp > 0:
    m2.hp -= m1.dmg
    if m2.hp < 0:
        m2.hp = 0
    print(f"{m1.name} наносит удар! У {m2.name} осталось {m2.hp} HP")

    if m2.hp == 0:
        break

    m1.hp -= m2.dmg
    if m1.hp < 0:
        m1.hp = 0
    print(f"{m2.name} наносит удар! У {m1.name} осталось {m1.hp} HP")

if m1.hp > 0:
    print(f"Победил {m1.name}!")
else:
    print(f"Победил {m2.name}!")
