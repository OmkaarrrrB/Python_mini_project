# Inventory Management System

This project is a simple **Inventory Management System** developed using **Python**, **Tkinter**, and **Pandas**. It provides a user-friendly interface for managing product inventories and ensures data persistence through a CSV file.

## Features

- **Add New Products**:
  - Add products with unique IDs, names, quantities, and prices.
  - Validates inputs to ensure accurate data entry.

- **Update Stock Levels**:
  - Modify the stock quantity of existing products using their product ID.
  - Provides instant updates to the inventory.

- **View Inventory**:
  - Displays the current inventory in a tabular format using a `Treeview` widget.
  - Includes columns for Product ID, Product Name, Quantity, and Price.

- **Save and Load Data**:
  - Automatically loads existing inventory data from a CSV file (`inventory.csv`).
  - Saves any changes to the file, ensuring data is persistent across sessions.

## Requirements

- Python 3.6 or later
- Required libraries:
  - `pandas`
  - `tkinter` (comes pre-installed with Python)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/inventory-management-system.git
   ```

2. Navigate to the project directory:
   ```bash
   cd inventory-management-system
   ```

3. Install required dependencies:
   ```bash
   pip install pandas
   ```

4. Run the application:
   ```bash
   python inventory_management.py
   ```

## How to Use

1. **Adding Products**:
   - Enter the Product ID, Product Name, Quantity, and Price in the respective fields.
   - Click the "Add Product" button to save the product in the inventory.

2. **Updating Stock**:
   - Enter the Product ID and the new Quantity in the update section.
   - Click the "Update Stock" button to modify the quantity.

3. **Viewing Inventory**:
   - All products are displayed in the table format, showing their ID, Name, Quantity, and Price.
   - The table updates dynamically after any changes.

## File Structure

- `inventory_management.py`: Main application script.
- `inventory.csv`: File to store inventory data (automatically created if it doesn't exist).

## Contributing

Feel free to submit issues or pull requests for improvements and additional features. Contributions are always welcome!



---

Enjoy managing your inventory efficiently!

