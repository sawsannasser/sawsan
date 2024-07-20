def display_menu():
    print("Menu:")
    print("1. Display a right-angle triangle of ones")
    print("2. Display a Palindromic Triangle")
    print("3. Help")
    print("4. Exit")

def display_right_angle_triangle(rows):
    for i in range(1, rows + 1):
        print("1 " * i)

def display_palindromic_triangle(rows):
    for i in range(1, rows + 1):
        # Print leading spaces
        print(" " * (rows - i), end="")
        # Print first half of the row
        for j in range(1, i + 1):
            print(j, end="")
        # Print second half of the row
        for j in range(i - 1, 0, -1):
            print(j, end="")
        print()

def show_help():
    print("Help Section:")
    print("1. Display a right-angle triangle of ones: This option will display a right-angle triangle made of ones.")
    print("2. Display a Palindromic Triangle: This option will display a palindromic triangle of numbers.")
    print("3. Help: Displays this help section.")
    print("4. Exit: Exits the program.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            rows = int(input("Enter the number of rows: "))
            display_right_angle_triangle(rows)
        elif choice == '2':
            rows = int(input("Enter the number of rows: "))
            display_palindromic_triangle(rows)
        elif choice == '3':
            show_help()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
