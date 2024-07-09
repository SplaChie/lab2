from prototype.virus import Virus


def main():
    # Створення вірусів і їх клонування
    parent_virus = Virus("Parent", 10, 2, "Type A")
    child_virus1 = Virus("Child1", 1, 0.5, "Type A")
    child_virus2 = Virus("Child2", 1.2, 0.6, "Type A")

    parent_virus.children.extend([child_virus1, child_virus2])

    cloned_virus = parent_virus.clone()

    print(parent_virus)
    for child in parent_virus.children:
        print(child)

    print(cloned_virus)
    for child in cloned_virus.children:
        print(child)


if __name__ == "__main__":
    main()
