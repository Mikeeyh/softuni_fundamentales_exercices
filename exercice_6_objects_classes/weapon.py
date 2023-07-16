class Weapon:
    def __init__(self, bullet_counter):
        self.bullet_counter = bullet_counter
        self.bullets = [int(number) for number in range(1, self.bullet_counter)]

    def shoot(self):
        if len(self.bullets) > 0:
            self.bullets.pop(0)
            print("shooting...")
        else:
            print("no bullets left")

    def __repr__(self):
        return f"Remaining bullets: {len(self.bullets)}"


weapon = Weapon(5)
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
