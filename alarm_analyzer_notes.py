import base64
import tkinter as tk
from tkinter import ttk, messagebox, PhotoImage, font as tkFont

import pandas as pd

# Load the Excel workbook at work
# excel_path = r'G:\DATA\REPAIR\Semi-Conductor Section Info\Procedures & notes\Brian Shanders Notes\FORMS\Training Doc\RMA Failure History.xlsx'
# Load the Excel workbook at work
excel_path = '/Users/jaredwoods/PycharmProjects/RMA Failure History.xlsx'
data = pd.read_excel(excel_path, sheet_name='KLA Cont ')


# Embedded alarm dictionary with the specified alarm and sub-codes
alarm_dict = {
    "0020": {
        "0001": {
            "Message": "CPU COMMUNICATION ERROR",
            "Location of Defect": "NCP30",
            "Signal of Defect": "",
            "Cause": "An error occurred in communications between boards when the control power turned ON due to",
            "Potential Causes": [
                "Insertion of the circuit board is not completed",
                "Defective circuit board",
                "Corrupt memory on the CF "
            ],
            "Sub-Code Description": "The sub code stands for the defective board"
        },
        "0032": {
            "Message": "CPU COMMUNICATION ERROR",
            "Location of Defect": "AXC01",
            "Signal of Defect": "",
            "Cause": "An error occurred in communications between boards when the control power turned ON due to",
            "Potential Causes": [
                "Insertion of the circuit board is not completed",
                "Defective circuit board",
                "Corrupt memory on the CF"
            ],
            "Sub-Code Description": "The sub code stands for the defective board"
        }
    },
    "0021": {
        "0032": {
            "Message": "COMMUNICATION ERROR (SERVO)",
            "Location of Defect": "SERVO",
            "Signal of Defect": "",
            "Cause": "The communications CPU for the AXC01 detected an error when the control power turned ON due to",
            "Potential Causes": [
                "Defective connection of communication cable for servopack",
                "Defective connection of terminal connector",
                "Defective circuit board",
                "Corrupt memory on the CF"
            ],
            "Sub-Code Description": ""
        }
    },
    "0030": {
        "0032": {
            "Message": "ROM ERROR",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The system program of AXC01 is damaged",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "0060": {
        "0001": {
            "Message": "COMMUNICATION ERROR (I/O MODULE)",
            "Location of Defect": "I/O MODULE",
            "Signal of Defect": "",
            "Cause": "An error was detected in communications with an I/O module board (NIF30) when the control power turned ON",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "0100": {
        "0001": {
            "Message": "MEMORY ERROR (JOB MNG DATA)",
            "Location of Defect": "JOB MNG DATA",
            "Signal of Defect": "",
            "Cause": "An error was detected in communications with the AXC01",
            "Potential Causes": [
                "Abnormal AXC01 serial communication Watch Dog value"
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0002": {
            "Message": "MEMORY ERROR (JOB MNG DATA)",
            "Location of Defect": "JOB MNG DATA",
            "Signal of Defect": "",
            "Cause": "An error was detected in communications with the AXC01",
            "Potential Causes": [
                "AXC01 serial communication watch dog missed one scan cycle"
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        }
    },
    "0200": {
        "0000:005F": {
            "Message": "MEMORY ERROR (PARAMETER FILE)",
            "Location of Defect": "PARAMETER FILE",
            "Signal of Defect": "",
            "Cause": "The parameter file is damaged due to",
            "Potential Causes": [
                "corrupt memory on the CF"
            ],
            "Sub-Code Description": ""
        }
    },
    "0210": {
        "0000": {
            "Message": "MEMORY ERROR (SYSTEM CONFIGDATA)",
            "Location of Defect": "SYSTEM CONFIGDATA",
            "Signal of Defect": "",
            "Cause": "The system configuration information data are damaged due to",
            "Potential Causes": [
                "corrupt memory on the CF",
                "corrupt memory on the NCP30"
            ],
            "Sub-Code Description": ""
        }
    },
    "0220": {
        "0001": {
            "Message": "MEMORY ERROR (JOB MNG DATA)",
            "Location of Defect": "JOB MNG DATA",
            "Signal of Defect": "",
            "Cause": "The management data of job files are damaged due to",
            "Potential Causes": [
                "corrupt memory on the CF",
                "corrupt memory on the NCP30"
            ],
            "Sub-Code Description": ""
        },
        "0002": {
            "Message": "MEMORY ERROR (JOB MNG DATA)",
            "Location of Defect": "JOB MNG DATA",
            "Signal of Defect": "",
            "Cause": "The job files are damaged due to",
            "Potential Causes": [
                "corrupt memory on the CF",
                "corrupt memory on the NCP30"
            ],
            "Sub-Code Description": ""
        },
        "0003": {
            "Message": "MEMORY ERROR (JOB MNG DATA)",
            "Location of Defect": "JOB MNG DATA",
            "Signal of Defect": "",
            "Cause": "The management data of position data files are damaged due to",
            "Potential Causes": [
                "corrupt memory on the CF",
                "corrupt memory on the NCP30"
            ],
            "Sub-Code Description": ""
        }
    },
    "0230": {
        "0000": {
            "Message": "MEMORY ERROR (LADDER PRG FILE)",
            "Location of Defect": "LADDER PRG FILE",
            "Signal of Defect": "",
            "Cause": "The concurrent I/O ladder program is damaged due to",
            "Potential Causes": [
                "corrupt memory on the CF",
                "corrupt memory on the NCP30"
            ],
            "Sub-Code Description": ""
        }
    },
    "0270": {
        "0000": {
            "Message": "MEMORY ERROR (SYSTEM DATA FILE)",
            "Location of Defect": "SYSTEM DATA FILE",
            "Signal of Defect": "",
            "Cause": "The system configuration data is damaged due to",
            "Potential Causes": [
                "corrupt memory on the CF",
                "corrupt memory on the NCP30"
            ],
            "Sub-Code Description": ""
        }
    },
    "0300": {
        "0002": {
            "Message": "VERIFY ERROR (SYSTEM CONFIGDATA)",
            "Location of Defect": "SYSTEM CONFIGDATA",
            "Signal of Defect": "",
            "Cause": "The setting of concurrent I/O parameter is incorrect due to",
            "Potential Causes": [
                "corrupt memory on the CF",
                "corrupt memory on the NCP30"
            ],
            "Sub-Code Description": ""
        },
        "0003": {
            "Message": "VERIFY ERROR (SYSTEM CONFIGDATA)",
            "Location of Defect": "SYSTEM CONFIGDATA",
            "Signal of Defect": "",
            "Cause": "An invalid value is set for the segment clock due to",
            "Potential Causes": [
                "corrupt memory on the CF",
                "corrupt memory on the NCP30"
            ],
            "Sub-Code Description": ""
        },
        "0004": {
            "Message": "VERIFY ERROR (SYSTEM CONFIGDATA)",
            "Location of Defect": "SYSTEM CONFIGDATA",
            "Signal of Defect": "",
            "Cause": "Inconsistency was detected in axis related parameters due to",
            "Potential Causes": [
                "corrupt memory on the CF",
                "corrupt memory on the NCP30"
            ],
            "Sub-Code Description": ""
        },
        "0008": {
            "Message": "VERIFY ERROR (SYSTEM CONFIGDATA)",
            "Location of Defect": "SYSTEM CONFIGDATA",
            "Signal of Defect": "",
            "Cause": "The function designation for the concurrent I/O parameter is incorrect due to",
            "Potential Causes": [
                "corrupt memory on the CF",
                "corrupt memory on the NCP30"
            ],
            "Sub-Code Description": ""
        }
    },
    "0310": {
        "0000": {
            "Message": "VERIFY ERROR (CMOS MEMORY SIZE)",
            "Location of Defect": "CMOS MEMORY SIZE",
            "Signal of Defect": "",
            "Cause": "The CMOS memory capacity is different from its initial setting",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "0320": {
        "0001": {
            "Message": "VERIFY ERROR (I/O MODULE)",
            "Location of Defect": "I/O MODULE",
            "Signal of Defect": "",
            "Cause": "The function of the connected I/O module is different from the set function",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "0330": {
        "0000": {
            "Message": "VERIFY ERROR (SENSOR FUNCTION)",
            "Location of Defect": "SENSOR FUNCTION",
            "Signal of Defect": "",
            "Cause": "Inconsistency was detected in the application setting parameters",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "0400": {
        "0032": {
            "Message": "PARAMETER TRANSMISSION ERROR",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "An error occurred during the parameter/ file transfer to the AXC01 due to",
            "Potential Causes": [
                "Defective connection of communication cable for servopack",
                "Defective connection of terminal connector",
                "Defective circuit board",
                "Corrupt memory on the CF"
            ],
            "Sub-Code Description": ""
        }
    },
    "0410": {
        "0032": {
            "Message": "MODE CHANGE ERROR",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "An error occurred during startup sequence processing with the AXC01, and the system did not startup normally",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
}


# noinspection PyUnusedLocal
class AlarmAnalyzer:
    def __init__(self, master):
        self.subcode_description_text = None
        self.cause_text = None
        self.message_text = None
        self.signal_of_defect_text = None
        self.location_of_defect_text = None
        self.subcode_combo = None
        self.alarm_combo = None
        self.info_text = None
        self.details_button = None
        self.master = master
        master.title("KLA Alarm Analyzer")

        label_font = tkFont.Font(family="Arial", size=12)
        entry_font = tkFont.Font(family="Courier New", size=12)

        # Initialize UI components
        self.initialize_ui(label_font, entry_font)

    def initialize_ui(self, label_font, entry_font):
        print("Initializing UI components")
        base64_image = ("iVBORw0KGgoAAAANSUhEUgAAAHgAAAAvCAYAAAAo7w6dAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcw"
                        "AADsMAAA7DAcdvqGQAAAZLSURBVHhe7Zt1iDVVGIc/A7EbC+xuxcLEQrEDbBQTxUIRxf5HEVGxFWzFQsVWUOxCRcXAAhW7"
                        "wA7s+D2788rP95u7e6+7qMO+DzzcuXNmZu89Z8573nPm7qSiKIqiKIqiKIqimEBM0bx2meXlBnIR+Ya8WP4ii44zj7xGfi"
                        "v/MD+T88uiw2wk35HesO7Vsugo28gvJQ35hXyr2c7OIYuOsY6kcWnUveWsEhh/35bewNvLokMsLT+R98r52JFYWXoDHycn"
                        "PP1m0SvIhYc3h3hZ0ouCGeW6cpqhd8OQ/DwmCZVrsKPhU/nU8OZkLCaXHd78iwfk1PJ2+ZXcXX4j2+BzxfmnyGrkPrleeu"
                        "9gHAyo/LOll38ut5WwtfSyS2Uv7pR+LNKgJ8knZITkXlwp47yf5XsjyNSqaGB+6ZW+kIQZ5HXSyz6WhMvgeOnlx8o2GFP9"
                        "uPA5+a7sZ+pzhmy7RptEpULMJukNUTGvS6A3XSa90l6Qc0nnRunHbCUzc8qPpB/n7if74Rz5a2O+RuxHvs/MshAbS6+oBy"
                        "WNe5ftw/tk29Qk9/4FZIbx0o/5PW0vKPtlpsYjpF/zLBllWDTsL72ibpEPp33ny7bxkQb33k8SlNlSkjTFMdw4XC/e405y"
                        "UFiy9GtETgDrS/IKIs4HkinWbfIA6XDjMQQh4X8teaskihFxqIeDZYbp3Lnyefm+JCElknkHWFueLp+RlH/YbF8g8/BxiY"
                        "zPcYKkrnm9X14uxwQX94rKS4Mnyl7Z+CbSj6WXO2TfVHKUM8ddTZJY+Xk0+KA8K/0aS0kqOH+f7EMSppRk7bGf7D8WWLK7"
                        "SaDiiRQegUKuRUI6u8xJaZtHSmDI8/2vSW6aeM8sY0zk3pqlMXpxkPRjL5QON4eX02Mgfynmv4MwnWSVK85ne3rJ8BL7iC"
                        "Z7yMXlrs2+cE+5UtqHj0iWQb+3fXiFhDzb4O9yUz8queFmkVzDj/la9lp2XUYS4drK4iY6U44JphRx0R8koSzeI39oVdmG"
                        "T1twLxnwFMh7BHdlhHl6j/9d5OFCv6wo/Vwq95C0jxB+mEm2HmU04r72Hul1zBqARNHLCJPcFL7vBjm3DBaVp0o/hrDtOU"
                        "mu25PlUWkfOc3qkmhEchozmn8EiwZ+8RcljZCXBZnGEH4yzF39uBhbWBBhLPMypkkOd76XU4H9sqP0c6lIQpnvG0l6Yk78"
                        "lpRBntsfKj06YFti6PX2k8wrcjtLvwazghwVBpq/01NGgnHLeUUylvAFHe7CO4Y3/4Z/SXo/vXIqSWj0pOdumZOFJ5vXgM"
                        "SoX9ZsXoOnpScur0oapZd8FiJM8J2kcQJCp/OSJKQH1BE3vcOw472NME+i5uRVPDoIq3sBoZwhc9xgoPe753AZMO54GXov"
                        "pIJyOdly6Pt8KTPYXPq5g4zDeQq3qaTC4z1hztlQkkHjPpJo5EME4dvxuT0/LiBU5qhG2A/WkzRwTlCPlizg8LCE5MyTOm"
                        "5CoqXnEjfLcSWH0c2kQ1rv5ciaNOwgc1mbTCcCKoqkI/TjWKDotZrFeOQ93B8h/ibnlSx3+vUYl6lUxr0fm31Ixp6HpvOk"
                        "w/Qnyt5khzhG+jlIGGZlL3oqCVE+pk1+tEBd50SPqdG4whfxCidRcEj5vRy588lYyaC9x7ZJYuWJiGfPXCsfn8fpgOw8vj"
                        "zjmk9T+BvAuE8PiP1ZEj4eTvDZ6fFe5skhw5onhzdJYKp4lfTzQh6UAMNTr2OQm5hpWoRlVvC8fOBHoKM9TcpjNBXXRttY"
                        "zrGjjfHg1yT7ZV4M98gtZP6M9EiHX3fQw1iEIMSxtLqdDGgMIlFA/sBaOfnFtJLe8rhkbItxkydnnsywoMCNC4RNr2hCqT"
                        "8dY1rDZ+H69GDGzWulL/KwEMIxy0mWTPncjOMkgrzSmEDesMrw5hB8D47tLD7nYxwdDSqbCt5l6F0xGf30sH8TQn7gy3pt"
                        "kAhdJOnxTCWKDuCPDJlG9IIbk6kM68ij3QjF/wjGtmhgbFvcYIwl02VsrYf2HWMJ6Q1MI/LAAhhvmTow32Raw/px0UF8Yh"
                        "8yj+RnQGwTug+URUc5TeYGDunRPictOgih2FeKkAUAFvPzQksxCv3+bPa/gMd7LM4TsnkYwYOO+qeyoiiKoiiKoiiKoiiK"
                        "icmkSX8CyETzCVcLsyAAAAAASUVORK5CYII=")
        image_data = base64.b64decode(base64_image)
        image = PhotoImage(data=image_data)
        logo_label = tk.Label(self.master, image=image)
        logo_label.image = image  # Keep a reference!
        logo_label.grid(row=0, column=0, rowspan=2, pady=(20, 0), sticky='sew')

        ttk.Label(self.master, text="ALARM CODE", font=label_font, anchor="center", foreground="grey",
                  width=12).grid(row=0, column=1, sticky="", padx=5, pady=5)
        self.alarm_combo = ttk.Combobox(self.master, font=entry_font, width=7, height=25)
        self.alarm_combo.grid(row=1, column=1, pady=0)
        self.alarm_combo['values'] = list(alarm_dict.keys())  # Use real alarm codes here
        self.alarm_combo.bind('<<ComboboxSelected>>', self.update_subcodes)

        ttk.Label(self.master, text="TECH NOTES", font=label_font, anchor="center", foreground="grey").grid(row=0, column=3, padx=5, pady=5, sticky='nsew')
        self.details_button = ttk.Button(self.master, text="Details", command=self.show_tech_notes, state='disabled')
        self.details_button.grid(row=1, column=3, padx=5, pady=0, sticky='')
        print("UI components initialized")

        separator = ttk.Separator(self.master, orient='horizontal')
        separator.grid(row=2, columnspan=4, sticky='ew', padx=5, pady=(10, 15))

        # Setup comboboxes for Alarm and Sub-Code
        self.setup_comboboxes(label_font, entry_font)

        # Setup individual fields for Message, Location, Signal, and Cause
        self.setup_fields(label_font, entry_font)

        # Create and configure styles
        style = ttk.Style()
        style.configure("TButton", font=entry_font, padding=6)
        style.map("TButton",
                  foreground=[('disabled', 'gray'), ('active', 'black')],
                  background=[('disabled', 'lightgray'), ('active', 'green'), ('!disabled', 'lightgreen')])

        # Use the styled button
        self.details_button = ttk.Button(self.master, text="Details", command=self.show_tech_notes, style="TButton")
        self.details_button.grid(row=1, column=3, padx=5, pady=0, sticky='')
        self.details_button['state'] = 'disabled'  # Initialize button as disabled

    def setup_comboboxes(self, label_font, entry_font):
        style = ttk.Style()
        style.configure("Grey.TLabel", foreground="grey")
        #
        # # Label and combobox for KLA Alarm
        # ttk.Label(self.master, text="ALARM CODE", font=label_font, style="Grey.TLabel", anchor="center",
        #           width=12).grid(row=0, column=1, sticky="", padx=5, pady=5)
        # self.alarm_combo = ttk.Combobox(self.master, font=entry_font, width=7, height=25)
        # self.alarm_combo.grid(row=1, column=1, pady=0)
        # self.alarm_combo['values'] = list(alarm_dict.keys())
        # self.alarm_combo.bind('<<ComboboxSelected>>', self.update_subcodes)

        # Label and combobox for Sub-Code
        ttk.Label(self.master, text=" SUB-CODE", font=label_font, style="Grey.TLabel", width=10, anchor="center").grid(
            row=0, column=2, pady=5)
        self.subcode_combo = ttk.Combobox(self.master, font=entry_font, width=9)
        self.subcode_combo.grid(row=1, column=2, padx=5, pady=0)
        self.subcode_combo.bind('<<ComboboxSelected>>', self.display_info)

    def setup_fields(self, label_font, entry_font):
        # Sub-Code Description
        ttk.Label(self.master, text="SUB-CODE\n   DETAIL", font=label_font, anchor="center",
                  foreground="grey").grid(row=6, column=0, padx=5, sticky='nsew')
        self.subcode_description_text = tk.Text(self.master, height=2, width=40, font=entry_font, padx=5, wrap=tk.WORD)
        self.subcode_description_text.grid(row=6, column=1, columnspan=3, padx=(0, 10), sticky='EW')

        # Location of Defect
        ttk.Label(self.master, text="   FAULT\nLOCATION", font=label_font, anchor="center", foreground="grey").grid(
            row=7, column=0, padx=5, sticky='nsew')
        self.location_of_defect_text = tk.Text(self.master, height=2, width=40, font=entry_font, padx=5, wrap=tk.WORD)
        self.location_of_defect_text.grid(row=7, column=1, columnspan=3, padx=(0, 10), sticky='EW')

        # Signal of Defect
        ttk.Label(self.master, text=" FAULT\nSIGNAL", font=label_font, anchor="center", foreground="grey").grid(
            row=8, column=0, padx=5, pady=5, sticky='new')
        self.signal_of_defect_text = tk.Text(self.master, height=4, width=40, font=entry_font, padx=5, wrap=tk.WORD)
        self.signal_of_defect_text.grid(row=8, column=1, columnspan=3, padx=(0, 10), sticky='EW')

        # Message
        ttk.Label(self.master, text="   FAULT\nMESSAGE", font=label_font, anchor="center",
                  foreground="grey").grid(row=9, column=0, padx=5, pady=5, sticky='new')
        self.message_text = tk.Text(self.master, height=2, width=40, font=entry_font, padx=5, wrap=tk.WORD)
        self.message_text.grid(row=9, column=1, columnspan=3, padx=(0, 10), sticky='EW')

        # Possible Causes
        ttk.Label(self.master, text="POTENTIAL\n  CAUSES", font=label_font, anchor="center", foreground="grey").grid(
            row=10, column=0, padx=5, pady=5, sticky='new')
        self.info_text = tk.Text(self.master, height=18, width=40, font=entry_font, padx=5, wrap=tk.WORD)
        self.info_text.grid(row=10, column=1, columnspan=3, padx=(0, 10), pady=(0, 10), sticky='EW')

    def update_subcodes(self, event):
        print("Alarm code selected:", self.alarm_combo.get())
        alarm_code = self.alarm_combo.get()
        sub_codes = list(alarm_dict[alarm_code].keys())
        self.subcode_combo['values'] = sub_codes
        print("Sub-codes updated:", sub_codes)

        if sub_codes:
            self.subcode_combo.set(sub_codes[0])
            self.display_info(None)
        else:
            self.subcode_combo.set('')
            self.info_text.delete(1.0, tk.END)

        # Enable or disable the details button based on the availability of tech notes
        if alarm_code and self.check_tech_notes(alarm_code):
            self.details_button['state'] = 'normal'
            print("Details button enabled")
        else:
            self.details_button['state'] = 'disabled'
            print("Details button disabled")

    def display_info(self, event):
        print("Displaying information for sub-code:", self.subcode_combo.get())
        sub_code = self.subcode_combo.get()
        if not sub_code:
            return

        details = alarm_dict[self.alarm_combo.get()][sub_code]
        self.subcode_description_text.delete(1.0, tk.END)
        self.subcode_description_text.insert(tk.END, details.get('Sub-Code Description', ''))
        self.location_of_defect_text.delete(1.0, tk.END)
        self.location_of_defect_text.insert(tk.END, details.get('Location of Defect', ''))
        self.signal_of_defect_text.delete(1.0, tk.END)
        self.signal_of_defect_text.insert(tk.END, details.get('Signal of Defect', ''))
        self.message_text.delete(1.0, tk.END)
        self.message_text.insert(tk.END, details.get('Message', ''))

        self.info_text.delete(1.0, tk.END)
        causes = details.get('Cause', '') + "\n"
        potential_causes = details.get('Potential Causes', [])
        if potential_causes:
            causes += "\n".join(f"• {cause}" for cause in potential_causes)
        self.info_text.insert(tk.END, causes)

    def check_tech_notes(self, alarm_code):
        print("Checking tech notes for alarm code:", alarm_code)
        # Ensure the DataFrame and columns exist
        if 'Error Code 1' not in data.columns or 'Error Code 2' not in data.columns or 'Error Code 3' not in data.columns:
            print("Required columns are missing from the data.")
            return False

        # Convert error codes in the DataFrame to strings and strip whitespace
        data['Error Code 1'] = data['Error Code 1'].astype(str).str.strip()
        data['Error Code 2'] = data['Error Code 2'].astype(str).str.strip()
        data['Error Code 3'] = data['Error Code 3'].astype(str).str.strip()

        # Check if there are any matching records for the given alarm code
        has_records = not data[(data['Error Code 1'] == alarm_code) |
                               (data['Error Code 2'] == alarm_code) |
                               (data['Error Code 3'] == alarm_code)].empty

        print("Records found:", has_records)
        return has_records

    def show_tech_notes(self):
        print("Showing tech notes for alarm code:", self.alarm_combo.get())
        alarm_code = self.alarm_combo.get()
        if not alarm_code:
            messagebox.showerror("Error", "No alarm code selected. Please select an alarm code.")
            return

        try:
            results = self.search_alarm_code(alarm_code)
            self.open_results_window(results)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to search for alarm code. Error: {str(e)}")

    @staticmethod
    def search_alarm_code(alarm_code):
        try:
            # Ensure the DataFrame and columns exist
            if 'Error Code 1' not in data.columns or 'Error Code 2' not in data.columns or 'Error Code 3' not in data.columns:
                raise ValueError("Required columns are missing from the data.")

            data['Error Code 1'] = data['Error Code 1'].astype(str).str.strip()
            data['Error Code 2'] = data['Error Code 2'].astype(str).str.strip()
            data['Error Code 3'] = data['Error Code 3'].astype(str).str.strip()

            filtered_data = data[(data['Error Code 1'] == alarm_code) |
                                 (data['Error Code 2'] == alarm_code) |
                                 (data['Error Code 3'] == alarm_code)]
            return filtered_data
        except Exception as e:
            # Log the error or handle it as necessary
            raise e  # Re-raise the exception for the calling method to handle

    def open_results_window(self, results):
        if results.empty:
            messagebox.showinfo("Search Results", "No records found for this alarm code.")
            return

        results_window = tk.Toplevel(self.master)
        results_window.title("Search Results")
        listbox = tk.Listbox(results_window, width=80, height=10)
        listbox.pack(padx=10, pady=10)

        for _, row in results.iterrows():
            display_text = f"{row['RMA Number']} - {row['Serial Number']} - {row['Model Type']} - {row['Revison Type']} - {row['Part Number']}"
            listbox.insert(tk.END, display_text)

        listbox.bind('<<ListboxSelect>>', lambda event: self.show_detail(results, event))

    @staticmethod
    def show_detail(results, event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            selected_row = results.iloc[index]
            details = f"Solution: {selected_row['Solution']}\n\nSummary: {selected_row['Eval Summary']}"
            messagebox.showinfo("Detailed Info", details)


# Main application logic
root = tk.Tk()
app = AlarmAnalyzer(root)
root.mainloop()
