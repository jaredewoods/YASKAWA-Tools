import tkinter as tk
from tkinter import messagebox
import pandas as pd

# Path to the Excel file
excel_path = (r'G:\DATA\REPAIR\Semi-Conductor Section Info\Procedures & notes\Brian Shanders Notes\FORMS\Training '
              r'Doc\RMA Failure History.xlsx')

# Load the Excel workbook
workbook = pd.ExcelFile(excel_path)

# Print all sheet names to find the one you need
print("Available sheets in the workbook:", workbook.sheet_names)

# Assuming you know the sheet name now, specify it in read_excel()
sheet_name = 'KLA Cont '  # Replace 'YourSheetName' with the actual name of the sheet
data = pd.read_excel(excel_path, sheet_name=sheet_name)
print(f"Data from {sheet_name} loaded successfully.")


# Function to search for the alarm code in specified columns and return matches
def search_alarm_code(alarm_code):
    print(f"Searching for alarm code: {alarm_code}")
    alarm_code = str(alarm_code).strip()  # Convert to string and strip whitespace

    # Ensure all error code data are strings and stripped of whitespace for accurate comparison
    data['Error Code 1'] = data['Error Code 1'].astype(str).str.strip()
    data['Error Code 2'] = data['Error Code 2'].astype(str).str.strip()
    data['Error Code 3'] = data['Error Code 3'].astype(str).str.strip()

    # Filtering the data where any of the error code columns match the alarm code
    filtered_data = data[(data['Error Code 1'] == alarm_code) |
                         (data['Error Code 2'] == alarm_code) |
                         (data['Error Code 3'] == alarm_code)]

    print(f"Found {len(filtered_data)} matches.")
    results = filtered_data[['RMA Number', 'Serial Number', 'Model Type', 'Revison Type', 'Part Number']]
    return results


# Function to show summary of selected RMA
def show_summary(event):
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        rma_number = event.widget.get(index)
        print(f"Selected RMA Number: {rma_number}")
        selected_row = data.loc[data['RMA Number'] == int(rma_number.split(' - ')[0])]
        solution = selected_row['Solution'].values[0]
        summary = selected_row['Eval Summary'].values[0]

        message = f"Solution:\n{solution}\n\nSummary:\n{summary}"
        messagebox.showinfo("RMA Summary", message)


# Set up the main application window
root = tk.Tk()
root.title("RMA Alarm Code Search")

entry_label = tk.Label(root, text="Enter 4-digit Alarm Code:")
entry_label.pack()

# Entry Box for alarm code
alarm_code_entry = tk.Entry(root)
alarm_code_entry.pack(padx=10, pady=5)
alarm_code_entry.focus_set()  # Focus on entry box by default


# Bind Enter key to search function
def on_enter(event):
    on_search_clicked()


alarm_code_entry.bind('<Return>', on_enter)

results_listbox = tk.Listbox(root, width=80)  # Adjust width as needed
results_listbox.pack(padx=10, pady=5)
results_listbox.bind('<<ListboxSelect>>', show_summary)


def on_search_clicked():
    print("Search button clicked.")
    results_listbox.delete(0, tk.END)
    alarm_code = alarm_code_entry.get()
    print(f"Entered alarm code: {alarm_code}")
    results = search_alarm_code(alarm_code)
    if results.empty:
        print("No results found.")
    for _, row in results.iterrows():
        display_text = f"{row['RMA Number']} - {row['Serial Number']} - {row['Model Type']} - {row['Revison Type']} - {row['Part Number']}"
        print(f"Adding to listbox: {display_text}")
        results_listbox.insert(tk.END, display_text)


search_button = tk.Button(root, text="Search", command=on_search_clicked)
search_button.pack(pady=5)

print("Starting the application...")
root.mainloop()
