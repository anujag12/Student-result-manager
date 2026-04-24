def main():
    # 1. Data Storage: Initialize an empty dictionary
    students = {}

    print("Welcome to the Student Result Manager!")

    # 2. Application State: A continuous loop for the menu
    while True:
        print("\n--- Main Menu ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Check Result")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        # 3. Logic & Control Flow
        if choice == '1':
            name = input("Enter the student's name: ").strip()
            
            # Edge Case Handling: Making sure marks are numbers
            try:
                marks = float(input(f"Enter marks for {name}: "))
                students[name] = marks
                print(f"Success! {name} has been added.")
            except ValueError:
                print("Invalid input. Please enter a numerical value for marks.")

        elif choice == '2':
            # Edge Case Handling: Check if the dictionary is empty
            if not students:
                print("No students found. The registry is currently empty.")
            else:
                print("\n--- Registered Students ---")
                for name, marks in students.items():
                    print(f"Name: {name} | Marks: {marks}")

        elif choice == '3':
            name = input("Enter the student's name to check result: ").strip()
            
            # Check if the student exists in our dictionary
            if name in students:
                marks = students[name]
                # Determine pass or fail (threshold >= 40)
                if marks >= 40:
                    print(f"Result: {name} PASSED with {marks} marks.")
                else:
                    print(f"Result: {name} FAILED with {marks} marks.")
            else:
                print(f"Error: No student found with the name '{name}'.")

        elif choice == '4':
            print("Exiting the Student Result Manager. Goodbye!")
            break # This breaks the while loop and ends the program

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# This ensures the script runs when executed directly
if __name__ == "__main__":
    main()