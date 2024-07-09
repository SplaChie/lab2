from builder.hero_builder import HeroBuilder
from builder.enemy_builder import EnemyBuilder


def main():
    # Створення героя
    hero_builder = HeroBuilder()
    hero = (hero_builder
            .set_height("6 feet")
            .set_build("Athletic")
            .set_hair_color("Blonde")
            .set_eye_color("Blue")
            .set_clothing("Armor")
            .add_inventory("Sword")
            .add_inventory("Shield")
            .build())

    print(hero)

    # Створення ворога
    enemy_builder = EnemyBuilder()
    enemy = (enemy_builder
             .set_height("5.8 feet")
             .set_build("Muscular")
             .set_hair_color("Black")
             .set_eye_color("Red")
             .set_clothing("Dark Cloak")
             .add_inventory("Dagger")
             .add_inventory("Poison")
             .build())

    print(enemy)


if __name__ == "__main__":
    main()
