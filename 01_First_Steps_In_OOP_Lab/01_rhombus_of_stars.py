def create_rhombus(n):
    for row in range(1, n + 1):
        print(f"{' ' * (n - row)}{'* ' * row}")

    for row in range(n - 1, 0, -1):
        print(f"{' ' * (n - row)}{'* ' * row}")


n = int(input())
create_rhombus(n)
