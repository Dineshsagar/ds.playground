import pandas as pd
import openpyxl
import os
import tkinter as tk
from tkinter import filedialog

def main():
    # Create a root window (it will be hidden)
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    # Ask user to select a file
    file_path = filedialog.askopenfilename(
        title="Select a CSV or Excel file",
        filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx;*.xls")]
    )
    
    if not file_path:
        print("No file selected.")
        return
    
    # Check if file exists (though filedialog should ensure it)
    if not os.path.exists(file_path):
        print("File does not exist. Please check the path.")
        return
    
    # Determine file type
    if file_path.lower().endswith('.csv'):
        try:
            df = pd.read_csv(file_path)
            print("Contents of the CSV file:")
            print(df)
        except Exception as e:
            print(f"Error reading CSV file: {e}")
    elif file_path.lower().endswith(('.xlsx', '.xls')):
        try:
            df = pd.read_excel(file_path)
            print("Contents of the Excel file:")
            print(df)
        except Exception as e:
            print(f"Error reading Excel file: {e}")
    else:
        print("Unsupported file format. Please select a CSV or Excel file.")

if __name__ == "__main__":
    main()