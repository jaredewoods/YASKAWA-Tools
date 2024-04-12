import tkinter as tk
from tkinter import ttk
import pandas as pd
import re

# Load the data
file_path = 'KLA Error Codes.csv'  # Make sure to use the correct path
try:
    df = pd.read_csv(file_path, header=None, names=['Alarm', 'SubCode', 'Message', 'Cause'])
    print("Data loaded successfully.")
except Exception as e:
    print(f"Failed to load data: {e}")


# Function to shift focus to next widget
def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return "break"  # Prevents the default behavior of the event


# Function to look up the error code, with modified text formatting for the cause
def look_up_error(event=None):
    alarm_code = alarm_code_entry.get()
    sub_code = sub_code_entry.get()
    print(f"Looking up alarm code: {alarm_code}, sub-code: {sub_code}")

    error = df[(df['Alarm'] == alarm_code) & (df['SubCode'] == sub_code)]
    if not error.empty:
        message = error.iloc[0]['Message']
        cause = error.iloc[0]['Cause']
    else:
        error = df[df['Alarm'] == alarm_code]
        if not error.empty:
            message = error.iloc[0]['Message']
            cause = error.iloc[0]['Cause']
        else:
            message = "Error code not found."
            cause = ""

    # New text formatting for cause
    cause = cause.replace(" - ", "\n- ")
    # Replace "ï" with "\n\t"
    cause = cause.replace("ï", "\n*")
    # Regex to match hexadecimal subcodes followed by a colon and preceded by a non-whitespace character
    cause = re.sub(r'(?<=\S)\s([0-9A-F]{2}:)', r'\n\1', cause, flags=re.IGNORECASE)

    # Update the message and cause text widgets
    message_text.delete('1.0', tk.END)
    message_text.insert(tk.END, message)

    cause_text.delete('1.0', tk.END)
    cause_text.insert(tk.END, cause)

    print(f"Message: {message}")
    print(f"Cause: {cause}")

# Setting up the GUI
root = tk.Tk()
root.title("KLA Alarm Code Search")

# Define the options for the dropdown
alarm_code_syntax_options = ['KLA Alarm Code', 'NXC100 Standard', 'AMAT NXC100', 'AMAT Amj']

# Create and place the dropdown (Combobox)
alarm_code_syntax_combobox = ttk.Combobox(root, values=alarm_code_syntax_options, state='readonly')
alarm_code_syntax_combobox.grid(column=2, row=0, padx=5, pady=2, sticky="")
alarm_code_syntax_combobox.set('KLA Alarm Code')  # Set the default value

label_width = 9

# Layout adjustments and debugging print statements
alarm_code_label = ttk.Label(root, text="ALARM", width=label_width)
alarm_code_label.grid(column=0, row=0, pady=2, padx=5, sticky="e")
alarm_code_entry = ttk.Entry(root, width=6)
alarm_code_entry.grid(column=1, row=0, pady=2, padx=5, sticky="")

sub_code_label = ttk.Label(root, text="SUBCODE", width=label_width)
sub_code_label.grid(column=0, row=1, pady=2, padx=5, sticky="e")
sub_code_entry = ttk.Entry(root, width=6)
sub_code_entry.grid(column=1, row=1, pady=2, padx=5)

lookup_button = ttk.Button(root, text="SEARCH", command=look_up_error, width=label_width)
lookup_button.grid(column=0, row=2, columnspan=2, padx=5, pady=2, sticky="ew")

message_text = tk.Text(root, height=2, width=30, wrap=tk.WORD)
message_text.grid(column=2, row=1, columnspan=2, rowspan=3, pady=2, padx=5, sticky="nesw")

cause_text = tk.Text(root, height=30, width=60, wrap=tk.WORD)
cause_text.grid(column=0, row=4, columnspan=4, pady=2, padx=5, sticky="ew")

# Bind Return key to the lookup function
alarm_code_entry.bind("<Return>", focus_next_widget)
sub_code_entry.bind("<Return>", look_up_error)
lookup_button.bind("<Return>", look_up_error)

root.mainloop()
