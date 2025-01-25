import os

# Starting message
def main():
    print("=" * 40)
    print("Welcome to Your Personal Finance Tracker")
    print("=" * 40)
    print("Features Available:")
    print("1. Add Income or Expense")
    print("2. View Transactions")
    print("3. Generate Reports (Coming Soon)")
    print("4. Exit")
    print("=" * 40)

    while True:
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            print("Feature to add income/expense is under development!")
        elif choice == "2":
            print("Feature to view transactions is under development!")
        elif choice == "3":
            print("Reports will be available soon!")
        elif choice == "4":
            print("Thank you for using the Personal Finance Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from options 1-4.")

if __name__ == "__main__":
    main()