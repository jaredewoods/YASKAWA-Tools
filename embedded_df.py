import tkinter as tk
from tkinter import ttk
import pandas as pd

# DataFrame data
data_dict = {
    'Alarm': ['4200', '4201', '4202', '4203', '4204', '4207', '4208', '4209', '4210', '4220', '4220', '4223', '4301'],
    'Sub-Code': ['0001-0023', '0001-0063', '0001-0063', '0001-0011', '0001-0011', '0001-07D0', '0001-002B', '0064-0070', '0001-000B', '0001', '0002', '0002-0003', '0001'],
    'Message': [
        'SYSTEM ERROR (FILE DATA)',
        'SYSTEM ERROR (JOB)',
        'SYSTEM ERROR (JOB)',
        'SYSTEM ERROR (POSITION DATA)',
        'SYSTEM ERROR (POSITION DATA)',
        'SYSTEM ERROR (MOTION)',
        'SYSTEM ERROR (ARITH)',
        'OFFLINE SYSTEM ERROR (ARITH)',
        'SYSTEM ERROR (Local variable)',
        'SERVO POWER OFF FOR JOB',
        'SERVO POWER OFF FOR JOB',
        'SERVO POWER OFF FOR JOB',
        'SAFE CIRCUIT SIGNAL DISAGREEMENT (SERVO)'
    ],
    'Cause': [
        'The error occurs in the file data access (file edition CF operation) due to:\n- Software bugs\n- Invalid NCP30 RAM memory \n\nThe sub code stands for the alarm factor:',
        'The error occurs in the MOTION job access. job edition, CF operation)\n\nThe sub code stands for the alarm factor:\n01: Parameter error\n02: Access time over\n03: Access error',
        'The error occurs in the MOTION job access. (job edition, CF operation)\n\nThe sub code stands for the alarm factor:\n01: Parameter error\n02: Access time over\n03: Access error',
        'The error occurs in the MOTION position data access.\n- Invalid NC parameter setting value.\n\nThe sub code stands for the alarm factor:\n01: Invalid parameter (axis parameter)\n11: Invalid parameter (robot parameter)',
        'The error occurs in the position data access.\n- Invalid NC parameter setting value.\n\nThe sub code stands for the alarm factor:',
        'A system error (Command-related processsing FATAL error) occurred in motion control process due to:\n- Software bugs\n- Invalid NCP30 RAM memory \n\nThe sub code stands for the software internal error code:',
        'A system error occurred in the path control section of the motion control system due to:\n- Software bugs\n- Invalid NCP30 RAM memory \n\nThe sub code stands for the software internal error code:',
        'A system error occurred in the offline position data handling due to:\n- Software bugs\n- Invalid NCP30 RAM memory \n\nThe sub code stands for the software internal error code:',
        'An error occurred in local variable control process due to:\n- Software bugs\n- Invalid NCP30 RAM memory \n\nThe sub code stands for the software internal error code:',
        'The servo power is not supplied to Manipulator.\n\nThe sub code stands for the alarm factor:',
        'The servo power is not supplied to Prealigner.\n\nThe sub code stands for the alarm factor:',
        'A safety circuit signal error occurred in I/O unit. The sub code stands for the defective signal.\n\nThe sub code stands for the alarm factor:\n02: ON_EN\n03: OVSPD',
        'An error occurred in the contactor due to a defective contactor unit (NTU30) circuit board (AXC01). The contactor of contactor unit did not turn ON at servo ON. The signal from the contactor turned OFF while the servo was ON. The signal from the contactor remains ON when the servo turned OFF at emergency stop. The contactor turned ON while the servo was OFF for emergency stop.\n\nThe sub code stands for the defective converter No.'
    ]
}

# Recreate DataFrame from the dictionary
df_alarms = pd.DataFrame(data_dict)


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


# Define lookup function and focus_next_widget function
def look_up_error(event=None):
    message_text.delete("1.0", tk.END)
    cause_text.delete("1.0", tk.END)
    alarm = alarm_code_entry.get()
    result = df_alarms[df_alarms['Alarm'] == alarm]
    if not result.empty:
        message_text.insert(tk.END, result.iloc[0]['Message'])
        cause_text.insert(tk.END, result.iloc[0]['Cause'])
    else:
        message_text.insert(tk.END, "Not found")
        cause_text.insert(tk.END, "The alarm code is not found.")


def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return("break")


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
