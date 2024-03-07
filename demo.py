import tkinter as tk
import mysql.connector
from tkinter import ttk

# Function to fetch data from MySQL database based on the given value
def get_data(value):
    # Replace the following with your MySQL connection details
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'Sujoy@2212',
        'database': 'voter',
    }

    # Connect to the database
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # Fetch data from the database based on the value
    query = "SELECT * FROM voters WHERE Word_No = %s"
    cursor.execute(query, (value,))
    data = cursor.fetchall()

    # Close the connection
    cursor.close()
    connection.close()

    return data

# Function to generate the table based on the data
def generate_table():
    value = entry_value.get()
    if value:
        data = get_data(value)
        if data:
            # Clear any previous data in the treeview
            for row in tree.get_children():
                tree.delete(row)

            # Insert data into the treeview
            for row in data:
                tree.insert("", "end", values=row)

# Create the main application window
root = tk.Tk()
root.title("MySQL Table Generator")

# Create and place widgets
label_value = tk.Label(root, text="Enter a value:")
label_value.pack(pady=5)

entry_value = tk.Entry(root)
entry_value.pack(pady=5)

button_generate = tk.Button(root, text="Generate Table", command=generate_table)
button_generate.pack(pady=5)

# Create the table (treeview)
tree_columns = ("Id", "VoterID", "First_Name","Last_Name")  # Replace with your column names
tree = ttk.Treeview(root, columns=tree_columns, show="headings")

# Set column headings
for col in tree_columns:
    tree.heading(col, text=col)

tree.pack(pady=10)

root.mainloop()
