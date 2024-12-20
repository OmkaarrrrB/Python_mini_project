import pandas as pd
import tkinter as tk
from tkinter import messagebox, ttk


# Function to load existing inventory data or create a new DataFrame
def load_inventory(file_name='inventory.csv'):
    try:
        return pd.read_csv(file_name)
    except FileNotFoundError:
        return pd.DataFrame(columns=["ProductID", "ProductName", "Quantity", "Price"])


# Function to save inventory data to a CSV file
def save_inventory(inventory, file_name='inventory.csv'):
    inventory.to_csv(file_name, index=False)


# Function to add a new product
def add_product():
    try:
        product_id = entry_product_id.get()
        product_name = entry_product_name.get()
        quantity = int(entry_quantity.get())
        price = float(entry_price.get())

        new_product = {
            "ProductID": product_id,
            "ProductName": product_name,
            "Quantity": quantity,
            "Price": price
        }

        inventory.loc[len(inventory)] = new_product
        save_inventory(inventory)
        refresh_tree_view()
        messagebox.showinfo("Success", "Product added successfully.")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid quantity and price.")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Function to update stock level
def update_stock():
    try:
        product_id = entry_update_product_id.get()
        new_quantity = int(entry_update_quantity.get())

        if product_id in inventory['ProductID'].values:
            inventory.loc[inventory['ProductID'] == product_id, 'Quantity'] = new_quantity
            save_inventory(inventory)
            refresh_tree_view()
            messagebox.showinfo("Success", "Stock updated successfully.")
        else:
            messagebox.showwarning("Warning", "Product ID not found.")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid quantity.")


# Function to generate reports and display in the tree view
def refresh_tree_view():
    # Clear existing rows in the tree
    for row in tree.get_children():
        tree.delete(row)

    # Populate tree view with current inventory data
    for index, row in inventory.iterrows():
        tree.insert("", "end", values=(row["ProductID"], row["ProductName"], row["Quantity"], row["Price"]))


# Function to create and display the main application window
def create_gui():
    global entry_product_id, entry_product_name, entry_quantity, entry_price
    global entry_update_product_id, entry_update_quantity
    global tree, inventory

    inventory = load_inventory()

    root = tk.Tk()
    root.title("Inventory Management System")

    # Add Product Section
    frame_add = tk.Frame(root)
    frame_add.pack(padx=10, pady=10)

    tk.Label(frame_add, text="Add Product").grid(row=0, columnspan=2)

    tk.Label(frame_add, text="Product ID").grid(row=1, column=0, sticky="e")
    entry_product_id = tk.Entry(frame_add)
    entry_product_id.grid(row=1, column=1)

    tk.Label(frame_add, text="Product Name").grid(row=2, column=0, sticky="e")
    entry_product_name = tk.Entry(frame_add)
    entry_product_name.grid(row=2, column=1)

    tk.Label(frame_add, text="Quantity").grid(row=3, column=0, sticky="e")
    entry_quantity = tk.Entry(frame_add)
    entry_quantity.grid(row=3, column=1)

    tk.Label(frame_add, text="Price").grid(row=4, column=0, sticky="e")
    entry_price = tk.Entry(frame_add)
    entry_price.grid(row=4, column=1)

    btn_add = tk.Button(frame_add, text="Add Product", command=add_product)
    btn_add.grid(row=5, columnspan=2)

    # Update Stock Section
    frame_update = tk.Frame(root)
    frame_update.pack(padx=10, pady=10)

    tk.Label(frame_update, text="Update Stock Level").grid(row=0, columnspan=2)

    tk.Label(frame_update, text="Product ID").grid(row=1, column=0, sticky="e")
    entry_update_product_id = tk.Entry(frame_update)
    entry_update_product_id.grid(row=1, column=1)

    tk.Label(frame_update, text="New Quantity").grid(row=2, column=0, sticky="e")
    entry_update_quantity = tk.Entry(frame_update)
    entry_update_quantity.grid(row=2, column=1)

    btn_update = tk.Button(frame_update, text="Update Stock", command=update_stock)
    btn_update.grid(row=3, columnspan=2)

    # Tree View for Inventory
    tree_frame = tk.Frame(root)
    tree_frame.pack(padx=10, pady=10)

    columns = ("ProductID", "ProductName", "Quantity", "Price")
    tree = ttk.Treeview(tree_frame, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center")

    tree.pack()

    refresh_tree_view()  # Initial population of the tree view

    root.mainloop()


if __name__ == "__main__":
    create_gui()
