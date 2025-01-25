import sqlite3

# Initialize database connection
def initialize_database():
    conn = sqlite3.connect("finance_tracker.db")  # Create the database file
    cursor = conn.cursor()

    # Create transactions table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL NOT NULL,
        category TEXT NOT NULL,
        transaction_type TEXT NOT NULL,
        date TEXT NOT NULL,
        description TEXT
    )
    """)

    # Create categories table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    """)

    conn.commit()  # Save changes
    conn.close()   # Close connection
    print("Database initialized successfully!")

# Run the initializer
if __name__ == "__main__":
    initialize_database()