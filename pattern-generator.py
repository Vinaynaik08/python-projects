from math import comb

def show_menu():
    print("\nChoose a pattern to print:")
    print("1. Square of Stars")
    print("2. Right-Angled Triangle")
    print("3. Inverted Triangle")
    print("4. Pyramid")
    print("5. Number Triangle")
    print("6. Pascal's Triangle")
    print("7. Hollow Square")

# 1. Square of Stars
def square_of_stars(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()

# 2. Right-Angled Triangle
def right_triangle(n):
    for i in range(1, n+1):
        for j in range(i):
            print("*", end=" ")
        print()

# 3. Inverted Triangle
def inverted_triangle(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()

# 4. Pyramid
def pyramid(n):
    for i in range(n):
        print(" " * (n - i - 1), end="")
        for j in range(2*i + 1):
            print("*", end="")
        print()

# 5. Number Triangle
def number_triangle(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()

# 6. Pascal's Triangle
def pascals_triangle(n):
    for i in range(n):
        print(" " * (n - i - 1), end="")
        for j in range(i + 1):
            print(comb(i, j), end=" ")
        print()

# 7. Hollow Square
def hollow_square(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

# Main Program
def main():
    show_menu()
    choice = int(input("Enter your choice (1-7): "))
    n = int(input("Enter number of rows: "))

    print("\nGenerated Pattern:\n")
    if choice == 1:
        square_of_stars(n)
    elif choice == 2:
        right_triangle(n)
    elif choice == 3:
        inverted_triangle(n)
    elif choice == 4:
        pyramid(n)
    elif choice == 5:
        number_triangle(n)
    elif choice == 6:
        pascals_triangle(n)
    elif choice == 7:
        hollow_square(n)
    else:
        print("Invalid choice!")

# Run it
main()
