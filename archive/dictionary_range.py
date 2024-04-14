import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

# Your JSON data as a Python dictionary
json_data = {
    "4474": {
        "0001 or 0002": {
            "Message": "WRONG CONTROL GROUP AXIS",
            "Location of Defect": None,
            "Signal of Defect": None,
            "Cause": "The CALL/JUMP destination job could not be executed. An attempt was made to call or jump to a job whose control group cannot be controlled. The sub code stands for the related control-group.",
            "Potential Causes": [],
            "Sub-Code Description": None
        }
    },
    "4496": {
        "0001:000D": {
            "Message": "PARAMETER ERROR",
            "Location of Defect": None,
            "Signal of Defect": None,
            "Cause": "This alarm occurs when an abnormal parameter is detected in the arithmetic process.",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor."
        }
    },
    "4508": {
        "0000:0010": {
            "Message": "SPECIFIED ERROR (COORDINATE)",
            "Location of Defect": "COORDINATE",
            "Signal of Defect": "master tool coordinate system",
            "Cause": "An invalid coordinate system was specified. The specified coordinate system does not exist.",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the coordinate system."
        },
        "0000": {
            "Message": "SPECIFIED ERROR (COORDINATE)",
            "Location of Defect": "COORDINATE",
            "Signal of Defect": "H-LINK type cylindrical coordinate system",
            "Cause": "An invalid coordinate system was specified. The specified coordinate system does not exist.",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the coordinate system."
        }
    },
    "4513": {
        "0001:001F": {
            "Message": "EXCESSIVE SEGMENT (SAFETY1)",
            "Location of Defect": None,
            "Signal of Defect": "LOW",
            "Cause": "At the safety speed 1, the manipulator motion speed exceeded the speed limit value (LOW level).",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the axis."
        }
    }
}


def update_sub_codes(event):
    code = alarm_code_combobox.get()
    sub_code_combobox.set('')
    sub_code_combobox['values'] = ()

    if code in json_data and 'Sub-Codes' in json_data[code]:
        sub_codes = list(json_data[code]['Sub-Codes'].keys())

        # Expand numeric ranges into sub-codes
        expanded_sub_codes = []
        for sub_code in sub_codes:
            if '-' in sub_code:
                start, end = map(int, sub_code.split('-'))
                expanded_sub_codes.extend(str(i).zfill(4) for i in range(start, end + 1))
            else:
                expanded_sub_codes.append(sub_code)

        sub_code_combobox['values'] = expanded_sub_codes


def show_alarm_data():
    code = alarm_code_combobox.get()
    sub_code = sub_code_combobox.get()

    info_display.delete(1.0, tk.END)  # Clears previous data
    sub_info_display.delete(1.0, tk.END)  # Clears previous data

    if code in json_data:
        if 'Message' in json_data[code]:
            info_display.insert(tk.END, json_data[code]['Message'])

    if code in json_data and 'Sub-Codes' in json_data[code]:
        for key in json_data[code]['Sub-Codes']:
            if '-' in key:
                start, end = map(int, key.split('-'))
                if start <= int(sub_code) <= end:
                    sub_info = json_data[code]['Sub-Codes'][key]
                    if 'Sub-Message' in sub_info:
                        sub_info_display.insert(tk.END, sub_info['Sub-Message'])
            else:
                if sub_code == key:
                    sub_info = json_data[code]['Sub-Codes'][key]
                    if 'Sub-Message' in sub_info:
                        sub_info_display.insert(tk.END, sub_info['Sub-Message'])


root = tk.Tk()
root.title("Alarm Code Lookup")

frame = ttk.Frame(root)
frame.grid(column=0, row=0)

alarm_code_label = ttk.Label(frame, text="Alarm Code:")
alarm_code_label.grid(column=0, row=0)

alarm_code_combobox = ttk.Combobox(frame, values=list(json_data.keys()), width=10)
alarm_code_combobox.grid(column=1, row=0)
alarm_code_combobox.bind('<<ComboboxSelected>>', update_sub_codes)

sub_code_label = ttk.Label(frame, text="Sub-code:")
sub_code_label.grid(column=0, row=1)

sub_code_combobox = ttk.Combobox(frame, width=10)
sub_code_combobox.grid(column=1, row=1)

button = ttk.Button(frame, text="Show Code", width=10, command=show_alarm_data)
button.grid(column=2, row=0)

info_label = ttk.Label(frame, text="Common Information:")
info_label.grid(column=0, row=2)

info_display = scrolledtext.ScrolledText(frame, height=5, width=50, wrap=tk.WORD)
info_display.grid(column=1, row=2, columnspan=2)

sub_info_label = ttk.Label(frame, text="Sub-code Information:")
sub_info_label.grid(column=0, row=3)

sub_info_display = scrolledtext.ScrolledText(frame, height=5, width=50, wrap=tk.WORD)
sub_info_display.grid(column=1, row=3, columnspan=2)

root.mainloop()
