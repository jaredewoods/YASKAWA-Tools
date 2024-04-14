import tkinter as tk
from tkinter import messagebox
import json

# Error Codes Database (simplified version for illustration)
error_codes_db = {
    {
        "0020": {
            "Message": "CPU COMMUNICATION ERROR",
            "Cause": "An error occurred in communications between boards when the control power turned ON due to:",
            "Sub-Codes": {
                "0001": {
                    "Location of Defect": "NCP30"
                },
                "0032": {
                    "Location of Defect": "AXC01"
                }
            },
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the defective board.",
            "Potential Causes": [
                "Insertion of the circuit board is not completed.",
                "Defective circuit board.",
                "Corrupt memory on the CF"
            ]
        },
        "0021": {
            "Message": "COMMUNICATION ERROR (SERVO)",
            "Cause": "The communications CPU for the AXC01 detected an error when the control power turned ON due to:",
            "Sub-Codes": {
                "0032": {}
            },
            "Location of Defect": "SERVO",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": [
                "Defective connection of communication cable for servopack",
                "Defective connection of terminal connector",
                "Defective circuit board",
                "Corrupt memory on the CF"
            ]
        },
        "0030": {
            "Message": "ROM ERROR",
            "Cause": "The system program of AXC01 is damaged",
            "Sub-Codes": {
                "0032": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "0060": {
            "Message": "COMMUNICATION ERROR (I/O MODULE)",
            "Cause": "An error was detected in communications with an I/O module board (NIF30) when the control power turned ON.",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": "I/O MODULE",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "0100": {
            "Message": "MEMORY ERROR (JOB MNG DATA)",
            "Cause": "An error was detected in communications with the AXC01. The sub code stands for the alarm factor.",
            "Sub-Codes": {
                "0001": {
                    "Potential Causes": [
                        "Abnormal AXC01 serial communication Watch Dog value."
                    ]
                },
                "0002": {
                    "Potential Causes": [
                        "AXC01 serial communication watch dog missed one scan cycle."
                    ]
                }
            },
            "Location of Defect": "JOB MNG DATA",
            "Signal of Defect": None,
            "Sub-Code Description": None
        },
        "0200": {
            "Message": "MEMORY ERROR (PARAMETER FILE)",
            "Cause": "The parameter file is damaged due to:",
            "Sub-Codes": {
                "0000:005F": {}
            },
            "Location of Defect": "PARAMETER FILE",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": [
                "corrupt memory on the CF"
            ]
        },
        "0210": {
            "Message": "MEMORY ERROR (SYSTEM CONFIGDATA)",
            "Cause": "The system configuration information data are damaged due to:",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": "SYSTEM CONFIGDATA",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": [
                "corrupt memory on the CF",
                "corrupt memory on the NCP30"
            ]
        },
        "0220": {
            "Message": "MEMORY ERROR (JOB MNG DATA)",
            "Cause": "The management data of job files are damaged due to:",
            "Sub-Codes": {
                "0001": {},
                "0002": {},
                "0003": {}
            },
            "Location of Defect": "JOB MNG DATA",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": [
                "corrupt memory on the CF",
                "corrupt memory on the NCP30"
            ]
        },
        "0230": {
            "Message": "MEMORY ERROR (LADDER PRG FILE)",
            "Cause": "The concurrent I/O ladder program is damaged due to:",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": "LADDER PRG FILE",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": [
                "corrupt memory on the CF",
                "corrupt memory on the NCP30"
            ]
        },
        "0270": {
            "Message": "MEMORY ERROR (SYSTEM DATA FILE)",
            "Cause": "The system configuration data is damaged due to:",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": "SYSTEM DATA FILE",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": [
                "corrupt memory on the CF",
                "corrupt memory on the NCP30"
            ]
        },
        "0300": {
            "Message": "VERIFY ERROR (SYSTEM CONFIGDATA)",
            "Cause": "The setting of concurrent I/O parameter is incorrect due to:",
            "Sub-Codes": {
                "0002": {},
                "0003": {},
                "0004": {},
                "0008": {}
            },
            "Location of Defect": "SYSTEM CONFIGDATA",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": [
                "corrupt memory on the CF",
                "corrupt memory on the NCP30"
            ]
        },
        "0310": {
            "Message": "VERIFY ERROR (CMOS MEMORY SIZE)",
            "Cause": "The CMOS memory capacity is different from its initial setting.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": "CMOS MEMORY SIZE",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "0320": {
            "Message": "VERIFY ERROR (I/O MODULE)",
            "Cause": "The function of the connected I/O module is different from the set function.",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": "I/O MODULE",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "0330": {
            "Message": "VERIFY ERROR (SENSOR FUNCTION)",
            "Cause": "Inconsistency was detected in the application setting parameters.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": "SENSOR FUNCTION",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "0400": {
            "Message": "PARAMETER TRANSMISSION ERROR",
            "Cause": "An error occurred during the parameter/ file transfer to the AXC01 due to:",
            "Sub-Codes": {
                "0032": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": [
                "Defective connection of communication cable for servopack",
                "Defective connection of terminal connector",
                "Defective circuit board",
                "Corrupt memory on the CF"
            ]
        },
        "0410": {
            "Message": "MODE CHANGE ERROR",
            "Cause": "An error occurred during startup sequence processing with the AXC01, and the system did not startup normally.",
            "Sub-Codes": {
                "0032": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "0500": {
            "Message": "SEGMENT PROC NOT READY",
            "Cause": "Motion command processing was not completed within the specified time.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "0510": {
            "Message": "SOFTWARE VERSION UNMATCH",
            "Cause": "The combination of the main system program and the AXC01 system program are incorrect.",
            "Sub-Codes": {
                "0032": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "0900": {
            "Message": "WATCHDOG TIMER ERROR(NCP 30)",
            "Cause": "An insertion error of the NCP30 circuit board or defective circuit board",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": "NCP30",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "0950": {
            "Message": "CPU ERROR",
            "Cause": "The servo board #1 is defective. \u00ef An error was detected in the CPU of servo board #1.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "1001": {
            "Message": "ROM ERROR",
            "Cause": "An error is found at the sum check of the system programs for the AXC01.",
            "Sub-Codes": {
                "0001:0018": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the alarm factor.",
            "Potential Causes": []
        },
        "1030": {
            "Message": "MEMORY ERROR (PARAMETER FILE)",
            "Cause": "This alarm occurs when there is a mismatch between the parameter file data and the CF data.",
            "Sub-Codes": {
                "0000": {
                    "Signal of Defect": "RCD,RCxG parameter error"
                },
                "0001": {
                    "Signal of Defect": "ROxG parameter error"
                },
                "0002": {
                    "Signal of Defect": "SVD,SVxG parameter error"
                },
                "0003": {
                    "Signal of Defect": "SVMxG parameter error"
                },
                "0004": {
                    "Signal of Defect": "S1CxG,S2C,S3C,S4C parameter error"
                },
                "0005": {
                    "Signal of Defect": "S1D,S2D,S3D,S4D parameter error"
                },
                "0006": {
                    "Signal of Defect": "CIO parameter error"
                },
                "0007": {
                    "Signal of Defect": "FD parameter error"
                },
                "0008": {
                    "Signal of Defect": "A1P parameter error"
                },
                "0009": {
                    "Signal of Defect": "RS parameter error"
                },
                "000A": {
                    "Signal of Defect": "S1E parameter error"
                },
                "000B": {
                    "Signal of Defect": "SVxB parameter error"
                },
                "000C": {
                    "Signal of Defect": "AMCxG parameter error"
                },
                "000D": {
                    "Signal of Defect": "SVPxG parameter error"
                },
                "000E": {
                    "Signal of Defect": "MFxG parameter error"
                },
                "000F": {
                    "Signal of Defect": "SVxS parameter error"
                }
            },
            "Location of Defect": "PARAMETER FILE",
            "Sub-Code Description": "The sub code stands for the parameter type.",
            "Potential Causes": [
                "Another possibility is corrupt CF data or corrupt memory."
            ]
        },
        "1031": {
            "Message": "MEMORY ERROR (MOTION1)",
            "Cause": "The file data used by MOTION are damaged.",
            "Sub-Codes": {
                "0001:0030": {}
            },
            "Location of Defect": "MOTION1",
            "Signal of Defect": "The macro definition file",
            "Sub-Code Description": "The sub code stands for the defective data.",
            "Potential Causes": []
        },
        "1050": {
            "Message": "SET:UP PROCESS ERROR (SYSCON)",
            "Cause": "The motion instruction did not start up.",
            "Sub-Codes": {
                "0001:0002": {}
            },
            "Location of Defect": "SYSCON",
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the alarm factor",
            "Potential Causes": []
        },
        "1051": {
            "Message": "SET-UP PROCESS ERROR (MOTION)",
            "Cause": "This alarm is caused by an incomplete set up of the MOTION program file.",
            "Sub-Codes": {
                "0001:000C": {}
            },
            "Location of Defect": "MOTION1",
            "Signal of Defect": None,
            "Sub-Code Description": "The subcode shows the software internal process.",
            "Potential Causes": []
        },
        "1100": {
            "Message": "SYSTEM ERROR",
            "Cause": "An unknown alarm was detected because of noise or control error.",
            "Sub-Codes": {
                "0000:FFFF": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the detected error code.",
            "Potential Causes": []
        },
        "1101": {
            "Message": "SYSTEM ERROR (SYSTEM 1)",
            "Cause": "An error occurred during the system control check due to a software bugs or invalid NCP30 RAM data.",
            "Sub-Codes": {
                "0000:00FF": {}
            },
            "Location of Defect": "SYSTEM 1",
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the alarm factor",
            "Potential Causes": []
        },
        "1102": {
            "Message": "SYSTEM ERROR (SYSTEM 2)",
            "Cause": "An error occurred during the system control check due to a software bugs or invalid NCP30 RAM data.",
            "Sub-Codes": {
                "0000:00FF": {}
            },
            "Location of Defect": "SYSTEM 2",
            "Signal of Defect": None,
            "Sub-Code Description": "The subcode shows the software internal process.",
            "Potential Causes": []
        },
        "1103": {
            "Message": "SYSTEM ERROR (EVENT)",
            "Cause": "An error occurred during the system event data control check due to a software bugs or invalid NCP30 RAM data.",
            "Sub-Codes": {
                "0000:0008": {}
            },
            "Location of Defect": "EVENT",
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the detected error code.",
            "Potential Causes": []
        },
        "1104": {
            "Message": "SYSTEM ERROR (CIO)",
            "Cause": "This alarm is caused by an invalid CIO parameter.",
            "Sub-Codes": {
                "0080": {}
            },
            "Location of Defect": "CIO",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": [
                "Other possible causes are a corrupt CF memory or NCP30 memory."
            ]
        },
        "1105": {
            "Message": "SYSTEM ERROR (SERVO)",
            "Cause": "The status setting to base block is different from that of base block signal reading from JL056.",
            "Sub-Codes": {
                "07D0": {
                    "Sub-Code Description": None
                },
                "2710": {
                    "Sub-Code Description": None
                },
                "0000:8027": {
                    "Sub-Code Description": "The sub code stands for the alarm factor."
                }
            },
            "Location of Defect": "SERVO",
            "Signal of Defect": None,
            "Potential Causes": []
        },
        "1200": {
            "Message": "HIGH TEMPERATURE",
            "Cause": "The temperature inside the controller (CPS power supply unit) is too high.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": "CPS PSU",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "1202": {
            "Message": "FAULT",
            "Cause": "An error occurred in the NCP30 due to:",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": "NCP30",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": [
                "Defective board",
                "Incorrect connection",
                "software control error"
            ]
        },
        "1204": {
            "Message": "COMMUNICATION ERROR ( MODULE)",
            "Cause": "Communications and power supply error occurred in the NIF30 due to:",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": "MODULE",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": [
                "Loose X33 connector",
                "Invalid CIO parameter",
                "Corrupt memory in the NCP30"
            ]
        },
        "1207": {
            "Message": "BROKEN B_ON RELAY FUSE (NIF30)",
            "Cause": "The brake relay fuse was blown.",
            "Sub-Codes": {
                "0001:0003": {}
            },
            "Location of Defect": "NIF30",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "1208": {
            "Message": "BROKEN S_ON RELAY FUSE (NIF30)",
            "Cause": "The servo-ON relay fuse was blown.",
            "Sub-Codes": {
                "0001:0003": {}
            },
            "Location of Defect": "NIF30",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "1209": {
            "Message": "EXTERNAL WDT BROKEN (NIF30)",
            "Cause": "This alarm is caused by a failure of the external WDT (watch dog timer) circuit on the NIF30 board.",
            "Sub-Codes": {
                "0001:0003": {}
            },
            "Location of Defect": "NIF30",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "1210": {
            "Message": "SERIAL COMMUNICATION TOGGLE CHECK ERROR (NIF30)",
            "Cause": "This alarm is caused by a failure a serial communication toggle check circuit on the NIF30 board.",
            "Sub-Codes": {
                "0001:0003": {}
            },
            "Location of Defect": "NIF30",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": [
                "Possible causes are a defective circuit or electrical noise."
            ]
        },
        "1211": {
            "Message": "INPUT COMPARISON ERROR (NIF30)",
            "Cause": "The signal does not have a match signal as a result the mutual check of a dual signal.",
            "Sub-Codes": {
                "0001": {
                    "Signal of Defect": "PBESP signal"
                },
                "0002": {
                    "Signal of Defect": "PPESP signal"
                },
                "0004": {
                    "Signal of Defect": "EXESP signal"
                },
                "0020": {
                    "Signal of Defect": "SAF_F signal"
                },
                "0080": {
                    "Signal of Defect": "EXSVON signal"
                },
                "0200": {
                    "Signal of Defect": "FORCE signal"
                },
                "0400": {
                    "Signal of Defect": "DSW signal"
                },
                "1000": {
                    "Signal of Defect": "EXDSW signal"
                },
                "8000": {
                    "Signal of Defect": "FST signal"
                }
            },
            "Location of Defect": "NIF30",
            "Sub-Code Description": "The sub code stands for the defective signal.",
            "Potential Causes": [
                "This alarm can be caused by an error the user wiring, a damaged NIF30 board or electrical noise."
            ]
        },
        "1212": {
            "Message": "PLD MUTUAL MONITOR ERROR (NIF30)",
            "Cause": "The input comparison error occurred.",
            "Sub-Codes": {
                "0001:0003": {}
            },
            "Location of Defect": "NIF30",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "1213": {
            "Message": "MUTUAL WDT ERROR (NIF30)",
            "Cause": "The input comparison error occurred.",
            "Sub-Codes": {
                "0001:0003": {}
            },
            "Location of Defect": "NIF30",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "1214": {
            "Message": "PBESP RELAY STICKING",
            "Cause": "The emergency stop button of teach pendant PBESP is melted and stuck.",
            "Sub-Codes": {
                "0001:0003": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "1215": {
            "Message": "PPESP RELAY STICKING",
            "Cause": "The emergency stop button of programming pendant PPESP is melted and stuck.",
            "Sub-Codes": {
                "0001:0003": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "1216": {
            "Message": "EXESP RELAY STICKING",
            "Cause": "The external emergency stop button EXESP is melted and stuck.",
            "Sub-Codes": {
                "0001:0003": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "1217": {
            "Message": "S_ON RELAY STICKING",
            "Cause": "The servo-ON relay is melted and stuck.",
            "Sub-Codes": {
                "0001:0003": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "1218": {
            "Message": "B_ON RELAY STICKING",
            "Cause": "The brake relay is melted and stuck.",
            "Sub-Codes": {
                "0001:0003": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "1219": {
            "Message": "ANOTHER PLD EXT WDT ERROR (NIF BOARD)",
            "Cause": "The watchdog timer checking the safety circuit is incorrect.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": "NIF30",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "1300": {
            "Message": "SERVO CPU SYNCHRONIZING ERROR",
            "Cause": "The connection between the NCP30 and the AXC01 is abnormal.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": [
                "The cable between the NCP30 and the AXC01 is incomplete",
                "The connection of the terminal connector is incomplete.",
                "The NCP30 is defective.",
                "The AXC01 is defective."
            ]
        },
        "1301": {
            "Message": "COMMUNICATION ERROR (SERVO)",
            "Cause": "The communication between the NCP30 and the AXC01 is abnormal",
            "Sub-Codes": {
                "0001": {
                    "Signal of Defect": "Watch dog error"
                },
                "0002": {
                    "Signal of Defect": "JL040 alarm"
                },
                "0003": {
                    "Signal of Defect": "Communication status error"
                }
            },
            "Location of Defect": "SERVO",
            "Sub-Code Description": "The sub code stands for the alarm factor.",
            "Potential Causes": [
                "The cable between the NCP30 and the AXC01 is improper.",
                "The connection of the terminal connector is incomplete.",
                "The NCP30 defect",
                "The AXC01 defect"
            ]
        },
        "1302": {
            "Message": "COMMUNICATION ERROR (SERVO I/O)",
            "Cause": "The communication between the AXC01 and the NTU30 is abnormal.",
            "Sub-Codes": {
                "0001": {
                    "Signal of Defect": "Interruption detected"
                },
                "0002": {
                    "Signal of Defect": "Status error"
                },
                "006E": {
                    "Signal of Defect": "Communication loop back error"
                },
                "006F": {
                    "Signal of Defect": "MechatroLink data reception error"
                }
            },
            "Location of Defect": "SERVO I/O",
            "Sub-Code Description": "The sub code stands for the alarm factor",
            "Potential Causes": [
                "The AXC01 is abnormal",
                "The NTU30 is abnormal.",
                "The cable between the AXC01 and the NTU30 is abnormal."
            ]
        },
        "1303": {
            "Message": "ARITHMETIC ERROR (SERVO)",
            "Cause": "An error occurred in control arithmetic process or parameter arithmetic process.",
            "Sub-Codes": {
                "0000:FFFF": {}
            },
            "Location of Defect": "SERVO",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "1304": {
            "Message": "EX-AXIS BOARD NOT INSTALLED",
            "Cause": "The external board (AXD01) is not mounted although an external axis is specified.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "1306": {
            "Message": "AMPLIFIER TYPE MISMATCH",
            "Cause": "The type of the amplifier displayed in axis data is different from the type in the system configuration.",
            "Sub-Codes": {
                "0001:01FF": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for Physical axis.",
            "Potential Causes": [
                "The type of the amplifier is not correct.",
                "The type of the amplifier is different from the type in the system configuration.",
                "Defective amplifier",
                "Defective AXC01"
            ]
        },
        "1307": {
            "Message": "ENCODER TYPE MISMATCH",
            "Cause": "The type of the encoder displayed in the axis data is different form the type of the encoder set in the system configuration.",
            "Sub-Codes": {
                "0001:01FF": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for Physical axis.",
            "Potential Causes": [
                "The type of the encoder is not correct.",
                "System configuration is not correct.",
                "Defective encoder",
                "Defective AXC01",
                "Defective connection of encoder cable"
            ]
        },
        "1308": {
            "Message": "CONVERTER TYPE MISMATCH",
            "Cause": "The converter model set in the system configuration is different from that of the one mounted.",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "1309": {
            "Message": "HARDWARE ERROR (CONVERTER)",
            "Cause": "Converter hardware is incorrect.",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": "CONVERTER",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "1310": {
            "Message": "CHARGE ERROR (CONVERTER)",
            "Cause": "The voltage of main DC circuit did not rise above DC40V.",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": "CONVERTER",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "1311": {
            "Message": "A/D DETECTION ERROR (CONVERTER)",
            "Cause": "Abnormal current data is detected.",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": "CONVERTER",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "1312": {
            "Message": "ID ERROR (CONVERTER)",
            "Cause": "Converter type mismatch is detected by servo control board during power-up.",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": "CONVERTER",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "1325": {
            "Message": "COMMUNICATION ERROR (ENCODER)",
            "Cause": "Communication error occurred between the encoder and the AXC01 due to:",
            "Sub-Codes": {
                "0001:001F": {}
            },
            "Location of Defect": "ENCODER",
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the defective axis.",
            "Potential Causes": [
                "Misconnection of encoder",
                "Noise from external devices",
                "Incorrect motor type",
                "Defective servo control circuit board or encoder"
            ]
        },
        "1326": {
            "Message": "DEFECTIVE ENCODER ABSOLUTE DATA",
            "Cause": "The encoder data error is detected at power-up. The encoder data exceeds preset limit value. The sub code stands for the defective axis.",
            "Sub-Codes": {
                "0001:001F": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "1328": {
            "Message": "DEFECTIVE SERIAL ENCODER",
            "Cause": "Encoder internal data error is detected in serial communication between the controller and the encoder. The sub code stands for the defective axis.",
            "Sub-Codes": {
                "0001:001F": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "1329": {
            "Message": "DEFECTIVE SERIAL ENCODER COMMAND",
            "Cause": "Encoder command execution error is detected in serial communication between the controller and the encoder. The sub code stands for the defective axis.",
            "Sub-Codes": {
                "0001:001F": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "1330": {
            "Message": "MICRO PROGRAM TRANSMIT ERROR",
            "Cause": "Defective servo control circuit board (Occurred only when the control power supply turned ON.) The sub code stands for the defective axis.",
            "Sub-Codes": {
                "0001:001F": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "1343": {
            "Message": "COMMUNICATION ERROR (CONVERTER)",
            "Cause": "Serial communication error between the AXC01 and the COBCB030GAA.",
            "Sub-Codes": {
                "0065": {
                    "Signal of Defect": "Communication status error"
                },
                "0066": {
                    "Signal of Defect": "Command timeout"
                },
                "0067": {
                    "Signal of Defect": "Transmission error"
                },
                "0068": {
                    "Signal of Defect": "Check sum error of received data"
                },
                "0069": {
                    "Signal of Defect": "Error code reception"
                },
                "006A": {
                    "Signal of Defect": "Received command error"
                }
            },
            "Location of Defect": "CONVERTER",
            "Sub-Code Description": "The sub code stands for the alarm factor.",
            "Potential Causes": []
        },
        "1352": {
            "Message": "SERIAL CORRECTION FAILED",
            "Cause": "An error was detected in bit shifting compensation.",
            "Sub-Codes": {
                "0001:001F": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the defective axis.",
            "Potential Causes": []
        },
        "1355": {
            "Message": "SERIAL ENC MULTITURN LIMIT ERR",
            "Cause": "The NXC100 checks the multiple rotation number of the encoder. This alarm occurs when the parameter of the multiple rotation number is not set to the appropriate value.",
            "Sub-Codes": {
                "0001:001F": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the defective axis.",
            "Potential Causes": []
        },
        "1360": {
            "Message": "PA NOT INSTALLED",
            "Cause": "The prealigner is not mounted although use of the prealigner has been selected.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "1500": {
            "Message": "PLD INTERNAL MUTUAL MONITOR ERROR (SERVO I/O)",
            "Cause": "PLD internal mutual monitoring error is sent from the TU circuit board.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": "SERVO I/O",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "1501": {
            "Message": "SVMX RELAY STICKING (SERVO I/O)",
            "Cause": "PLD internal mutual monitoring error is sent from the TU circuit board.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": "SERVO I/O",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "1502": {
            "Message": "TACTOR STICKING (SERVO I/O)",
            "Cause": "PLD internal mutual monitoring error is sent from the TU circuit board.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": "SERVO I/O",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "1503": {
            "Message": "INPUT COMPARISON ERROR (SERVO I/O)",
            "Cause": "PLD internal mutual monitoring error is sent from the TU circuit board.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": "SERVO I/O",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "1504": {
            "Message": "TUSON RELAY BREAKDOWN (SERVO I/O)",
            "Cause": "PLD internal mutual monitoring error is sent from the TU circuit board.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": "SERVO I/O",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "1505": {
            "Message": "B_ON RELAY FUSE BREAKDOWN (SERVO I/O)",
            "Cause": "PLD internal mutual monitoring error is sent from the TU circuit board.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": "SERVO I/O",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "1506": {
            "Message": "MAIN TACTOR RELAY FUSE BREAKDOWN (SERVO I/O)",
            "Cause": "PLD internal mutual monitoring error is sent from the TU circuit board.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": "SERVO I/O",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "1507": {
            "Message": "S_ON RELAY FUSE BREAKDOWN (SERVO I/O)",
            "Cause": "PLD internal mutual monitoring error is sent from the TU circuit board.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": "SERVO I/O",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "1508": {
            "Message": "MUTUAL WDT ERROR (SERVO I/O)",
            "Cause": "PLD internal mutual monitoring error is sent from the TU circuit board.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": "SERVO I/O",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "1509": {
            "Message": "EXTERNAL WDT OVER (SERVO I/O)",
            "Cause": "PLD internal mutual monitoring error is sent from the TU circuit board.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": "SERVO I/O",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "1510": {
            "Message": "EXTERNAL WDT BREAKDOWN (SERVO I/O)",
            "Cause": "PLD internal mutual monitoring error is sent from the TU circuit board.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": "SERVO I/O",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "1511": {
            "Message": "SERIAL COMMUNICATION TOGGLE CHECK ERROR (SERVO I/O)",
            "Cause": "PLD internal mutual monitoring error is sent from the TU circuit board.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": "SERVO I/O",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "1514": {
            "Message": "OVERHEAT (AMPLIFIER)",
            "Cause": "Amplifier overheated.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": "AMPLIFIER",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "4000": {
            "Message": "MEMORY ERROR (TOOL FILE)",
            "Cause": "The memory for the tool file is damaged.",
            "Sub-Codes": {
                "0000:0017": {}
            },
            "Location of Defect": "TOOLFILE",
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for tool file number.",
            "Potential Causes": []
        },
        "4004": {
            "Message": "MEMORY ERROR (HOME POS FILE)",
            "Cause": "The memory for the home positioning file is damaged.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": "HOME POS FILE",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "4005": {
            "Message": "MEMORY ERROR (SECOND HOME POS)",
            "Cause": "The memory for the second home position file is damaged.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": "SECOND HOME POS FILE",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "4026": {
            "Message": "MEMORY ERROR(CONDITION FILE)",
            "Cause": "The memory for the condition file is damaged. The sub code is a file number. in which checksum error happened.",
            "Sub-Codes": {
                "0000:0099": {}
            },
            "Location of Defect": "CONDITION FILE",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "4100": {
            "Message": "OVERRUN (ROBOT AXIS)",
            "Cause": "NXC100 received robot overrun signal. The signal is disabled at default, so the possible causes are wiring defects or board defects.",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": "ROBOT AXIS",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "4101": {
            "Message": "OVERRUN (EXTERNAL AXIS)",
            "Cause": "NXC100 received external unit overrun signal. The signal is disabled at default, so the possible causes are wiring defects or board defects.",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": "EXTERNAL AXIS",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "4102": {
            "Message": "SYSTEM DATA HAS BEEN CHANGED",
            "Cause": "This alarm occurs when a servo on command is executed without a power cycle after changing system parameters.",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "4109": {
            "Message": "DC24V POWER SUPPLY FAILURE (I/ O)",
            "Cause": "This alarm is caused by no 24vdc power at the controller x33 connector.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": "I/O MODULE",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "4110": {
            "Message": "SHOCK SENSOR ACTIVATION",
            "Cause": "NXC100 received the robot shock sensor signal. The signal is disabled at default, so the possible causes are wiring defects or board defects.",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "4111": {
            "Message": "BRAKE FUSE BREAKDOWN",
            "Cause": "This alarm occurs when the brake output relay fuse for NTU30 is broken. The possible causes are NTU30 board defects, or, less often, contact failure or noise.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "4119": {
            "Message": "FAN ERROR (IN CONTROL BOX)",
            "Cause": "The rotation speed of in-panel cooling fan decreased.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": "IN CONTROL BOX",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "4200": {
            "Message": "SYSTEM ERROR (FILE DATA)",
            "Cause": "The error occurs in the file data access (file edition, CF operation)",
            "Sub-Codes": {
                "0001:0023": {}
            },
            "Location of Defect": "FILE DATA",
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the alarm factor.",
            "Potential Causes": [
                "Software bugs",
                "Invalid NCP30 RAM memory"
            ]
        },
        "4201": {
            "Message": "SYSTEM ERROR (JOB)",
            "Cause": "The error occurs in the MOTION job access. (job edition, CF operation)",
            "Sub-Codes": {
                "0001": {
                    "Signal of Defect": "Parameter error",
                    "Potential Causes": []
                },
                "0002": {
                    "Signal of Defect": "Access time over",
                    "Potential Causes": []
                },
                "0003": {
                    "Signal of Defect": "Access error",
                    "Potential Causes": []
                },
                "0004": {
                    "Signal of Defect": "Job name error\nInvalid character is used for the job name.",
                    "Potential Causes": []
                },
                "0005": {
                    "Signal of Defect": "Existing job open\nThe job name already exists in the memory at the new job creation.",
                    "Potential Causes": []
                },
                "0006": {
                    "Signal of Defect": "The area (memory) of the registered job exceeds the available range.",
                    "Potential Causes": []
                },
                "0007": {
                    "Signal of Defect": "The job which does not exist in the memory is selected for display.",
                    "Potential Causes": []
                },
                "0008": {
                    "Signal of Defect": "The edit-lock job is specified for edition.",
                    "Potential Causes": []
                },
                "0009": {
                    "Signal of Defect": "Handle value illegality",
                    "Potential Causes": []
                },
                "000A": {
                    "Signal of Defect": "System error",
                    "Potential Causes": []
                },
                "000B": {
                    "Signal of Defect": "Sequence number error",
                    "Potential Causes": []
                },
                "000C": {
                    "Signal of Defect": "Step number error",
                    "Potential Causes": []
                },
                "000D": {
                    "Signal of Defect": "The job specified for search does not exist in the memory.",
                    "Potential Causes": []
                },
                "000E": {
                    "Signal of Defect": "Invalid command exists in the job.\n(Software unmatch, or data unmatch by software update)",
                    "Potential Causes": []
                },
                "0010": {
                    "Signal of Defect": "Opened handle shortage",
                    "Potential Causes": []
                },
                "0011": {
                    "Signal of Defect": "Write impossibility by multi open",
                    "Potential Causes": []
                },
                "0012": {
                    "Signal of Defect": "The command number exceeds 9999 at the command insertion to the job.",
                    "Potential Causes": []
                },
                "0013": {
                    "Signal of Defect": "The step number exceeds 999 at the step insertion to the job.",
                    "Potential Causes": []
                },
                "0014": {
                    "Signal of Defect": "A job was newly created with the same name of the undefined job already specified in the memory.",
                    "Potential Causes": []
                },
                "0063": {
                    "Signal of Defect": "Job memory destruction",
                    "Potential Causes": [
                        "Software bugs or invalid NCP30 RAM memory."
                    ]
                }
            },
            "Location of Defect": "JOB",
            "Sub-Code Description": "The sub code stands for the alarm factor."
        },
        "4202": {
            "Message": "SYSTEM ERROR (JOB)",
            "Cause": "The error occurs in the MOTION job access. (job edition, CF operation)",
            "Sub-Codes": {
                "0001": {
                    "Signal of Defect": "Parameter error",
                    "Potential Causes": []
                },
                "0002": {
                    "Signal of Defect": "Access time over",
                    "Potential Causes": []
                },
                "0003": {
                    "Signal of Defect": "Access error",
                    "Potential Causes": []
                },
                "0004": {
                    "Signal of Defect": "Job name error\nInvalid character is used for the job name.",
                    "Potential Causes": []
                },
                "0005": {
                    "Signal of Defect": "Existing job open\nThe job name already exists in the memory at the new job creation.",
                    "Potential Causes": []
                },
                "0006": {
                    "Signal of Defect": "The area (memory) of the registered job exceeds the available range.",
                    "Potential Causes": []
                },
                "0007": {
                    "Signal of Defect": "The job which does not exist in the memory is selected for display.",
                    "Potential Causes": []
                },
                "0008": {
                    "Signal of Defect": "The edit-lock job is specified for edition.",
                    "Potential Causes": []
                },
                "0009": {
                    "Signal of Defect": "Handle value illegality",
                    "Potential Causes": []
                },
                "000A": {
                    "Signal of Defect": "System error",
                    "Potential Causes": []
                },
                "000B": {
                    "Signal of Defect": "Sequence number error",
                    "Potential Causes": []
                },
                "000C": {
                    "Signal of Defect": "Step number error",
                    "Potential Causes": []
                },
                "000D": {
                    "Signal of Defect": "The job specified for search does not exist in the memory.",
                    "Potential Causes": []
                },
                "000E": {
                    "Signal of Defect": "Invalid command exists in the job.\n(Software unmatch, or data unmatch by software update)",
                    "Potential Causes": []
                },
                "0010": {
                    "Signal of Defect": "Opened handle shortage",
                    "Potential Causes": []
                },
                "0011": {
                    "Signal of Defect": "Write impossibility by multi open",
                    "Potential Causes": []
                },
                "0012": {
                    "Signal of Defect": "The command number exceeds 9999 at the command insertion to the job.",
                    "Potential Causes": []
                },
                "0013": {
                    "Signal of Defect": "The step number exceeds 999 at the step insertion to the job.",
                    "Potential Causes": []
                },
                "0014": {
                    "Signal of Defect": "A job was newly created with the same name of the undefined job already specified in the memory.",
                    "Potential Causes": []
                },
                "0063": {
                    "Signal of Defect": "Job memory destruction",
                    "Potential Causes": [
                        "Software bugs or invalid NCP30 RAM memory."
                    ]
                }
            },
            "Location of Defect": "JOB",
            "Sub-Code Description": "The sub code stands for the alarm factor."
        },
        "4203": {
            "Message": "SYSTEM ERROR (POSITION DATA)",
            "Cause": "The error occurs in the MOTION position data access. (During play-back / operating)",
            "Sub-Codes": {
                "0001": {
                    "Signal of Defect": "Lack of area Uncompleted initialization (Defect)"
                },
                "0002": {
                    "Signal of Defect": "All axes number are 0. Uncompleted initialization (Defect)"
                },
                "0003": {
                    "Signal of Defect": "Keeping the position on the axes number 0 is unable. Uncompleted initialization (Defect)"
                },
                "0004": {
                    "Signal of Defect": "The total number of the keeping position is exceeded. Uncompleted initialization (Defect)"
                },
                "0005": {
                    "Signal of Defect": "The area is exceeds the system setting. Uncompleted initialization (Default)"
                },
                "0006": {
                    "Signal of Defect": "New acquisition file destruction CMOS memory destruction"
                },
                "0007": {
                    "Signal of Defect": "The registrable position area (memory) is exceeded."
                },
                "0008": {
                    "Signal of Defect": "Position data destruction CMOS memory destruction"
                },
                "0009": {
                    "Signal of Defect": "Controlling information destruction CMOS memory destruction"
                },
                "000A": {
                    "Signal of Defect": "Illegal position number CMOS memory destruction"
                },
                "000B": {
                    "Signal of Defect": "Unregisterable position data"
                },
                "000C": {
                    "Signal of Defect": "Undefined position"
                },
                "000D": {
                    "Signal of Defect": "Undefined control group"
                },
                "000E": {
                    "Signal of Defect": "Uncompleted initialization"
                },
                "000F": {
                    "Signal of Defect": "The number of axes for the control groups exceeded the limit."
                },
                "0010": {
                    "Signal of Defect": "An error occurred in exclusive control."
                },
                "0011": {
                    "Signal of Defect": "An error occurred in exceptional control."
                }
            },
            "Location of Defect": "POSITION DATA",
            "Sub-Code Description": "Data stands for the alarm factor.",
            "Potential Causes": []
        },
        "4204": {
            "Message": "SYSTEM ERROR (POSITION DATA)",
            "Cause": "The error occurs in the MOTION position data access. (During play-back / operating)",
            "Sub-Codes": {
                "0001": {
                    "Signal of Defect": "Lack of area Uncompleted initialization (Defect)"
                },
                "0002": {
                    "Signal of Defect": "All axes number are 0. Uncompleted initialization (Defect)"
                },
                "0003": {
                    "Signal of Defect": "Keeping the position on the axes number 0 is unable. Uncompleted initialization (Defect)"
                },
                "0004": {
                    "Signal of Defect": "The total number of the keeping position is exceeded. Uncompleted initialization (Defect)"
                },
                "0005": {
                    "Signal of Defect": "The area is exceeds the system setting. Uncompleted initialization (Default)"
                },
                "0006": {
                    "Signal of Defect": "New acquisition file destruction CMOS memory destruction"
                },
                "0007": {
                    "Signal of Defect": "The registrable position area (memory) is exceeded."
                },
                "0008": {
                    "Signal of Defect": "Position data destruction CMOS memory destruction"
                },
                "0009": {
                    "Signal of Defect": "Controlling information destruction CMOS memory destruction"
                },
                "000A": {
                    "Signal of Defect": "Illegal position number CMOS memory destruction"
                },
                "000B": {
                    "Signal of Defect": "Unregisterable position data"
                },
                "000C": {
                    "Signal of Defect": "Undefined position"
                },
                "000D": {
                    "Signal of Defect": "Undefined control group"
                },
                "000E": {
                    "Signal of Defect": "Uncompleted initialization"
                },
                "000F": {
                    "Signal of Defect": "The number of axes for the control groups exceeded the limit."
                },
                "0010": {
                    "Signal of Defect": "An error occurred in exclusive control."
                },
                "0011": {
                    "Signal of Defect": "An error occurred in exceptional control."
                }
            },
            "Location of Defect": "POSITION DATA",
            "Sub-Code Description": "Data stands for the alarm factor.",
            "Potential Causes": []
        },
        "4207": {
            "Message": "SYSTEM ERROR (MOTION)",
            "Cause": "A system error (Command-related processing FATAL error) occurred in MOTION due to",
            "Sub-Codes": {
                "0001:07D0": {}
            },
            "Location of Defect": "MOTION1",
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the software internal error code.",
            "Potential Causes": [
                "Software bugs",
                "invalid NCP30 RAM memory"
            ]
        },
        "4208": {
            "Message": "SYSTEM ERROR (ARITH)",
            "Cause": "A system error occurred in the path control section due to",
            "Sub-Codes": {
                "0001:002B": {}
            },
            "Location of Defect": "ARITH",
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the software internal error code.",
            "Potential Causes": [
                "Software bugs",
                "invalid NCP30 RAM memory"
            ]
        },
        "4209": {
            "Message": "OFFLINE SYSTEM ERROR (ARITH)",
            "Cause": "A system error occurred in the offline position-data preparation section due to",
            "Sub-Codes": {
                "0064:0070": {}
            },
            "Location of Defect": "ARITH",
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the software internal error code.",
            "Potential Causes": [
                "Software bugs",
                "invalid NCP30 RAM memory"
            ]
        },
        "4210": {
            "Message": "SYSTEM ERROR (Local variable)",
            "Cause": "An error occurred in local variable control process due to",
            "Sub-Codes": {
                "0001:000B": {}
            },
            "Location of Defect": None,
            "Signal of Defect": "Local Variable",
            "Sub-Code Description": "The sub code stands for the software internal error code.",
            "Potential Causes": [
                "Software bugs",
                "invalid NCP30 RAM memory"
            ]
        },
        "4220": {
            "Message": "SERVO POWER OFF FOR JOB",
            "Cause": "The servo power is not supplied to Manipulator.",
            "Sub-Codes": {
                "0001": {},
                "0002": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "4223": {
            "Message": "SERVO POWER OFF FOR JOB",
            "Cause": "A safety circuit signal error occurred in I/O unit. The sub code stands for the defective signal.",
            "Sub-Codes": {
                "0002": {
                    "Signal of Defect": "ON_EN"
                },
                "0003": {
                    "Signal of Defect": "OVSPD"
                }
            },
            "Location of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "4301": {
            "Message": "SAFE CIRCUIT SIGNAL DISAGREEMENT (SERVO)",
            "Cause": "An error occurred in the contactor due to a defective contactor unit (NTU30) circuit board (AXC01).",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": "SERVO",
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the defective converter No.",
            "Potential Causes": [
                "The contactor of contactor unit did not turn ON at servo ON.",
                "The signal from the contactor turned OFF while the servo was ON.",
                "The signal from the contactor remains ON when the servo turned OFF at emergency stop.",
                "The contactor turned ON while the servo was OFF for emergency stop."
            ]
        },
        "4302": {
            "Message": "CONTACTOR ERROR",
            "Cause": "The brake relay signal did not turn ON when the servo turned ON.",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the defective power-on unit No.",
            "Potential Causes": [
                "The brake relay signal turned OFF while the servo was ON.",
                "The brake signal remains ON when the servo turned OFF at emergency stop.",
                "The brake signal turned ON while the servo was OFF for emergency stop.",
                "Defective NTU30 power-on unit Defective AXC01 circuit board"
            ]
        },
        "4303": {
            "Message": "BRAKE CIRCUIT ERROR",
            "Cause": "No response of charge completion was sent from the converter when the servo turned ON.",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the defective converter No.",
            "Potential Causes": [
                "The SERVO READY signal turned OFF while the servo was ON.",
                "The SERVO READY signal remains ON when the servo turned OFF at emergency stop.",
                "The SERVO READY signal turned ON while the servo was OFF for emergency stop.",
                "The primary power supply voltage is too low.",
                "The voltage dropped.",
                "Defective servo control and/or converter."
            ]
        },
        "4304": {
            "Message": "CONVERTER INPUT POWER ERROR",
            "Cause": "No response of primary power supply input was sent from the converter when the servo turned ON.",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the defective converter No.",
            "Potential Causes": [
                "The READY 1 signal remains ON when the servo turned OFF at emergency stop.",
                "The READY 1 signal turned ON while the servo was OFF for emergency stop.",
                "Incorrect wiring or voltage drop of primary power supply",
                "Defective servo control and/or converter."
            ]
        },
        "4305": {
            "Message": "CONVERTER CIRCUIT CHARGE ERROR",
            "Cause": "No response (READY 2 signal) of charge completion was sent from the converter when the servo turned ON.",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the defective converter No.",
            "Potential Causes": [
                "The READY 2 signal turned OFF while the servo was ON.",
                "The READY 2 signal remains ON when the servo turned OFF at emergency stop.",
                "The READY 2 signal turned ON while the servo was OFF for emergency stop.",
                "Incorrect wiring and/or voltage drop of primary power supply",
                "Defective servo control circuit board, converter, and/or amplifier"
            ]
        },
        "4306": {
            "Message": "AMPLIFIER READY SIGNAL ERROR",
            "Cause": "No response \"Power ON\" was sent from the amplifier when the servo turned ON.",
            "Sub-Codes": {
                "0001-001F": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the defective axis.",
            "Potential Causes": [
                "The amplifier READY signal turned OFF while the servo was ON.",
                "The amplifier READY signal remains ON when the servo turned OFF at emergency stop.",
                "The amplifier READY signal turned ON while the servo was OFF for emergency stop.",
                "Defective servo control circuit board, converter, and/or amplifier."
            ]
        },
        "4307": {
            "Message": "SERVO ON SPEED ERROR",
            "Cause": "The motion speed of the encoder before the dynamic brake turns OFF in servo ON sequence exceeded the threshold for a certain period.",
            "Sub-Codes": {
                "0001:001F": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the defective axis.",
            "Potential Causes": [
                "The servo power supply turned ON while the manipulator (motor and encoder) was moving."
            ]
        },
        "4308": {
            "Message": "VOLTAGE DROP (CONVERTER)",
            "Cause": "The DC power voltage supplied to the SERVOPACK amplifier dropped below 143V due to",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": "CONVERTER",
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the defective converter No.",
            "Potential Causes": [
                "Low voltage of the primary power supply",
                "Open phase",
                "Defective converter",
                "Defective servo control circuit board"
            ]
        },
        "4311": {
            "Message": "ENCODER BACK-UP ERROR",
            "Cause": "Encoder resetting (initialization) not completed .",
            "Sub-Codes": {
                "0001:001F": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the defective axis.",
            "Potential Causes": [
                "The position data in the encoder was lost due to the voltage drop of encoder backup battery."
            ]
        },
        "4313": {
            "Message": "SERIAL ENCODER OVER HEAT",
            "Cause": "The temperature of the encoder exceeded 100 \u00c5~C.",
            "Sub-Codes": {
                "0001:001F": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": [
                "Encoder thermister failure"
            ]
        },
        "4315": {
            "Message": "COLLISION DETECT",
            "Cause": "Crashed FOUP as FOUP access motion path exceeded given allowable range of position or motion.",
            "Sub-Codes": {
                "0001:001F": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the defective axis.",
            "Potential Causes": [
                "External force Interfering with external devices"
            ]
        },
        "4318": {
            "Message": "SERIAL ENCODER CORRECT LIMITATION OVER",
            "Cause": "The speed feedback value of the serial encoder exceeded the allowable limit.",
            "Sub-Codes": {
                "0001:001F": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the defective axis.",
            "Potential Causes": []
        },
        "4320": {
            "Message": "OVER LOAD (CONTINUE)",
            "Cause": "The motor torque continuously exceeded the rated torque for a certain period due to:",
            "Sub-Codes": {
                "0001:001F": {}
            },
            "Location of Defect": None,
            "Signal of Defect": "CONTINUE",
            "Sub-Code Description": "The sub code stands for the defective axis.",
            "Potential Causes": [
                "The motor tends to be overheated and this brings damages to the motor.",
                "Mis-wiring and disconnection of the U, V, W lines of the motor.",
                "Improper type of the motor.",
                "External force.",
                "Interfering with external devices.",
                "Defective AXC01 circuit boards.",
                "Defective amplifier.",
                "Defective motor (Encoder)"
            ]
        },
        "4321": {
            "Message": "OVER LOAD (INSTANT)",
            "Cause": "The torque a several times as much as the rated torque has been applied to the motor due to:",
            "Sub-Codes": {
                "0001:001F": {}
            },
            "Location of Defect": None,
            "Signal of Defect": "INSTANT",
            "Sub-Code Description": "The sub code stands for the defective axis.",
            "Potential Causes": [
                "The motor tends to be overheated and this brings damages to the motor.",
                "Mis-wiring and disconnection of the U, V, W lines of the motor.",
                "Improper type of the motor.",
                "External force.",
                "Interfering with external devices.",
                "Defective AXC01 circuit boards.",
                "Defective amplifier.",
                "Defective motor (Encoder)"
            ]
        },
        "4322": {
            "Message": "AMPLIFIER OVER LOAD (CONTINUE)",
            "Cause": "The current a several times as much as the rated current has continuously flown in the amplifier for a certain period due to:",
            "Sub-Codes": {
                "0001:001F": {}
            },
            "Location of Defect": None,
            "Signal of Defect": "CONTINUE",
            "Sub-Code Description": "The sub code stands for the defective axis.",
            "Potential Causes": [
                "The motor tends to be overheated and this brings damages to the motor.",
                "Mis-wiring and disconnection of the U, V, W lines of the motor.",
                "Improper type of the motor.",
                "External force.",
                "Interfering with external devices.",
                "Defective AXC01 circuit boards.",
                "Defective amplifier.",
                "Defective motor (Encoder)"
            ]
        },
        "4323": {
            "Message": "AMPLIFIER OVER LOAD (INSTANT)",
            "Cause": "The current a several times as much as the rated current has flown in the amplifier for a certain period due to:",
            "Sub-Codes": {
                "0001:001F": {}
            },
            "Location of Defect": None,
            "Signal of Defect": "INSTANT",
            "Sub-Code Description": "The sub code stands for the defective axis.",
            "Potential Causes": [
                "The motor tends to be overheated and this brings damages to the motor.",
                "Mis-wiring and disconnection of the U, V, W lines of the motor.",
                "Improper type of the motor.",
                "External force.",
                "Interfering with external devices.",
                "Defective AXC01 circuit boards.",
                "Defective amplifier.",
                "Defective motor (Encoder)"
            ]
        },
        "4326": {
            "Message": "SPEED ERROR",
            "Cause": "The speed exceeded the limit due to",
            "Sub-Codes": {
                "0001:001F": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the defective axis.",
            "Potential Causes": [
                "Mis-wiring of the UVW lines of the motor",
                "The motor type is improper.",
                "The motor is shifted by the external force.",
                "Defective AXC01 circuit boards",
                "Defective motor (Encoder)"
            ]
        },
        "4327": {
            "Message": "MOTOR ROTATION ERROR",
            "Cause": "The motor is out of control. This alarm occurs when the motor is operated reversing to the instruction of the correct turning direction.",
            "Sub-Codes": {
                "0001:001F": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the defective axis.",
            "Potential Causes": [
                "Mis-wiring of the UVW lines of the motor",
                "The motor type is improper.",
                "The motor is shifted by the external force.",
                "Defective AXC01 circuit boards",
                "Defective motor (Encoder)"
            ]
        },
        "4328": {
            "Message": "SERVO TRACKING ERROR",
            "Cause": "The axis deviated from the specified position and motion path beyond the allowable range.",
            "Sub-Codes": {
                "0001:001F": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the defective axis.",
            "Potential Causes": [
                "Mis-wiring of the UVW lines of the motor",
                "The motor type is improper.",
                "The motor is shifted by the external force.",
                "Defective AXC01 circuit boards",
                "Defective motor (Encoder)"
            ]
        },
        "4334": {
            "Message": "OVER VOLTAGE (CONVERTER)",
            "Cause": "The DC voltage supplied to the amplifier exceeded 420V due to",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": "CONVERTER",
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the defective converter No.",
            "Potential Causes": [
                "Overloaded",
                "The primary power supply is too high. (220V+10%)",
                "Converter failure - Defective servo control circuit board"
            ]
        },
        "4335": {
            "Message": "EARTH FAULT",
            "Cause": "Ground fault of the motor power line occurred due to",
            "Sub-Codes": {
                "0001:001F": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the defective axis.",
            "Potential Causes": [
                "Motor failure",
                "Ground fault of motor line or lead cables",
                "Defective servo control circuit board",
                "Defective SERVOPACK"
            ]
        },
        "4337": {
            "Message": "OVER CURRENT (AMPLIFIER)",
            "Cause": "Ground fault of the motor power line occurred due to",
            "Sub-Codes": {
                "0001:001F": {}
            },
            "Location of Defect": "AMPLIFIER",
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the defective axis.",
            "Potential Causes": [
                "Motor failure",
                "Ground fault of motor line or lead cables",
                "Defective servo control circuit board",
                "Defective amplifier",
                "Overheating of amplifier"
            ]
        },
        "4339": {
            "Message": "INPUT POWER OVER VOLTAGE (CONV)",
            "Cause": "The SERVOPACK primary power supply voltage exceeded 242V.",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": "CONVERTER",
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the defective converter No.",
            "Potential Causes": []
        },
        "4340": {
            "Message": "TEMPERATURE ERROR (CONVERTER)",
            "Cause": "The temperature of the servo pack (converter) is too high.",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": "CONVERTER",
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the defective converter No.",
            "Potential Causes": []
        },
        "4353": {
            "Message": "DEFECTIVE TAUGHT POINT (ENDLESS)",
            "Cause": "Endless motion impossible The standard position of pre-aligner is not unmatch. *The feedback pulse value exceeded the maximum value (maximum number of pulses \u2248}536870912)",
            "Sub-Codes": {
                "0001:001F": {}
            },
            "Location of Defect": "ENDLESS",
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the defective axis.",
            "Potential Causes": []
        },
        "4360": {
            "Message": "WAFER ALIGNMENT ERROR (SERVO)",
            "Cause": "An error occurred in communications with the prealigner.",
            "Sub-Codes": {
                "0001": {
                    "Signal of Defect": "Serial communication timeout"
                },
                "0002": {
                    "Signal of Defect": "Sampling buffer overflow"
                },
                "0003": {
                    "Signal of Defect": "Data number not refreshed"
                }
            },
            "Location of Defect": "SERVO",
            "Sub-Code Description": "The sub code stands for the alarm factor.",
            "Potential Causes": []
        },
        "4400": {
            "Message": "NOT READY (ARITH)",
            "Cause": "The arithmetic process for motion control did not complete within regulated time due to",
            "Sub-Codes": {
                "0001:0006": {}
            },
            "Location of Defect": "ARITH",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": [
                "Software bugs",
                "Invalid NCP30 RAM memory The sub code stands for the alarm factor."
            ]
        },
        "4401": {
            "Message": "SEQUENCE TASK CONTROL ERROR",
            "Cause": "An error occurred in job execution process due to",
            "Sub-Codes": {
                "0001:006A": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": [
                "Software bugs",
                "Invalid NCP30 RAM memory The sub code stands for the alarm factor."
            ]
        },
        "4402": {
            "Message": "UNDEFINED COMMAND (ARITH)",
            "Cause": "An undefined command was issued to the path control section due to",
            "Sub-Codes": {
                "0": {}
            },
            "Location of Defect": "ARITH",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": [
                "Software bugs",
                "Invalid NCP30 RAM memory The sub code stands for the alarm factor."
            ]
        },
        "4404": {
            "Message": "ARITHMETIC ERROR (MOTION)",
            "Cause": "This alarm occurs when the path calculating process in the calculation section hasn't succeeded normally.",
            "Sub-Codes": {
                "0001": {
                    "Signal of Defect": "MOVL was instructed for the position where the 1st arm was aligned with 2nd arm."
                },
                "0007": {
                    "Signal of Defect": "Teaching position \u2248iMIN, IM1, IM2,, IM3, RDY, STA\u2248j was specified out of the motion range."
                }
            },
            "Location of Defect": "MOTION",
            "Sub-Code Description": "The sub code stands for the alarm factor.",
            "Potential Causes": [
                "The teaching position (MIN, IM1, IM2,, IM3, RDY, STA) for the motion command where the alarm has occurred may have an error."
            ]
        },
        "4405": {
            "Message": "SELECT ERROR (PARAMETER)",
            "Cause": "A parameter error occurred in the path control section.",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": "PARAMETER FILE",
            "Signal of Defect": "Selection error of motion system parameter",
            "Sub-Code Description": "The sub code stands for the alarm factor.",
            "Potential Causes": []
        },
        "4406": {
            "Message": "GROUP AXIS CONTROL ERROR",
            "Cause": "An internal control error occurred in a coordinated motion.",
            "Sub-Codes": {
                "0008": {
                    "Signal of Defect": "Occupation control error"
                },
                "0009": {
                    "Signal of Defect": "Jog operation occupation control specification error"
                }
            },
            "Location of Defect": None,
            "Sub-Code Description": "The sub code stands for the alarm factor.",
            "Potential Causes": []
        },
        "4413": {
            "Message": "IMPOSSIBLE LINEAR MOTION (S/ L)",
            "Cause": "This alarm occurs when the form (folded direction) of 1st and 2nd axes at start point and end point are different in the execution of MOVJ instructions.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": None,
            "Signal of Defect": "S/L",
            "Sub-Code Description": None,
            "Potential Causes": [
                "The teaching position for the motion command where the alarm has occurred may have an error."
            ]
        },
        "4414": {
            "Message": "EXCESSIVE SEGMENT (LOW SPEED)",
            "Cause": "The manipulator motion speed exceeded the limit (LOW level).",
            "Sub-Codes": {
                "0001:001F": {}
            },
            "Location of Defect": None,
            "Signal of Defect": "LOW SPEED",
            "Sub-Code Description": "The sub code stands for the defective axis.",
            "Potential Causes": []
        },
        "4415": {
            "Message": "EXCESSIVE SEGMENT (HIGH SPEED)",
            "Cause": "The manipulator motion speed exceeded the limit (HIGH level).",
            "Sub-Codes": {
                "0001:001F": {}
            },
            "Location of Defect": None,
            "Signal of Defect": "HIGH SPEED",
            "Sub-Code Description": "The sub code stands for the defective axis.",
            "Potential Causes": []
        },
        "4416": {
            "Message": "PULSE LIMIT (MIN.)",
            "Cause": "The manipulator exceeded its motion limit (pulse limit) in the negative (-) direction.",
            "Sub-Codes": {
                "0001:001F": {}
            },
            "Location of Defect": None,
            "Signal of Defect": "MIN.",
            "Sub-Code Description": "The sub code stands for the defective axis.",
            "Potential Causes": []
        },
        "4417": {
            "Message": "PULSE LIMIT (MAX.)",
            "Cause": "The manipulator exceeded its motion limit (pulse limit) in the positive (+) direction.",
            "Sub-Codes": {
                "0001:001F": {}
            },
            "Location of Defect": None,
            "Signal of Defect": "MAX.",
            "Sub-Code Description": "The sub code stands for the defective axis.",
            "Potential Causes": []
        },
        "4420": {
            "Message": "SPECIAL SOFTLIMIT (MIN.)",
            "Cause": "The manipulator exceeded its motion limit (special software limit) in the negative (-) direction.",
            "Sub-Codes": {
                "0001:001F": {}
            },
            "Location of Defect": None,
            "Signal of Defect": "MIN.",
            "Sub-Code Description": "The sub code stands for the defective axis.",
            "Potential Causes": []
        },
        "4421": {
            "Message": "SPECIAL SOFTLIMIT (MAX.)",
            "Cause": "The manipulator exceeded its motion limit (special software limit) in the positive (+) direction.",
            "Sub-Codes": {
                "0001:001F": {}
            },
            "Location of Defect": None,
            "Signal of Defect": "MAX.",
            "Sub-Code Description": "The sub code stands for the defective axis.",
            "Potential Causes": []
        },
        "4422": {
            "Message": "MECHANICAL INTERFERENCE (MIN.)",
            "Cause": "The manipulator exceeded its minimum- angle motion limit. (Mechanical interference)",
            "Sub-Codes": {
                "0001:001F": {}
            },
            "Location of Defect": None,
            "Signal of Defect": "MIN.",
            "Sub-Code Description": "The sub code stands for the defective axis.",
            "Potential Causes": []
        },
        "4423": {
            "Message": "MECHANICAL INTERFERENCE (MAX.)",
            "Cause": "The manipulator exceeded its maximum- angle motion limit. (Mechanical interference)",
            "Sub-Codes": {
                "0001:001F": {}
            },
            "Location of Defect": None,
            "Signal of Defect": "MAX.",
            "Sub-Code Description": "The sub code stands for the defective axis.",
            "Potential Causes": []
        },
        "4426": {
            "Message": "PULSE MECHANICAL LIMIT (MIN.)",
            "Cause": "The manipulator exceeded its motion limit (mechanical limit) in the negative (- ) direction.",
            "Sub-Codes": {
                "0001:001F": {}
            },
            "Location of Defect": None,
            "Signal of Defect": "MIN.",
            "Sub-Code Description": "The sub code stands for the defective axis.",
            "Potential Causes": []
        },
        "4427": {
            "Message": "PULSE MECHANICAL LIMIT (MAX.)",
            "Cause": "The manipulator exceeded its motion limit (mechanical limit) in the positive (+) direction.",
            "Sub-Codes": {
                "0001:001F": {}
            },
            "Location of Defect": None,
            "Signal of Defect": "MAX.",
            "Sub-Code Description": "The sub code stands for the defective axis.",
            "Potential Causes": []
        },
        "4428": {
            "Message": "SEGMENT CONTROL ERROR",
            "Cause": "An error occurred in the real-time processing section that controls the arithmetic section due to",
            "Sub-Codes": {
                "0001:0009": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": [
                "Software bugs",
                "Invalid NCP30 RAM memory The sub code stands for the alarm factor."
            ]
        },
        "4429": {
            "Message": "WRONG SPECIFIED CONTROL GROUP",
            "Cause": "An error occurred in the manipulator information at job execution due to",
            "Sub-Codes": {
                "0001:0013": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": [
                "Software bugs",
                "Invalid NCP30 RAM memory The sub code stands for the alarm factor."
            ]
        },
        "4430": {
            "Message": "CPU COMMUNICATION ERROR",
            "Cause": "An error occurred in the manipulator information at job execution due to",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": [
                "Software bugs",
                "Invalid NCP30 RAM memory The sub code stands for the alarm factor."
            ]
        },
        "4431": {
            "Message": "JHM ERROR",
            "Cause": "Data error occurred in job control process due to",
            "Sub-Codes": {
                "0001:0006": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": [
                "Software bugs",
                "Invalid NCP30 RAM memory The sub code stands for the alarm factor."
            ]
        },
        "4432": {
            "Message": "INSTRUCTION INTERPRETER ERROR",
            "Cause": "An error occurred in instruction interpretation/ execution process due to",
            "Sub-Codes": {
                "0001:0009": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": [
                "Software bugs",
                "Invalid NCP30 RAM memory The sub code stands for the alarm factor."
            ]
        },
        "4433": {
            "Message": "UNDEFINED GLOBAL VARIABLE",
            "Cause": "The global variable is not defined.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": None,
            "Signal of Defect": "byte type",
            "Sub-Code Description": "The sub code stands for the variable type.",
            "Potential Causes": []
        },
        "4434": {
            "Message": "UNDEFINED GLOBAL VARIABLE",
            "Cause": "The global variable is not defined.",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": None,
            "Signal of Defect": "integer type",
            "Sub-Code Description": "The sub code stands for the variable type.",
            "Potential Causes": []
        },
        "4435": {
            "Message": "UNDEFINED GLOBAL VARIABLE",
            "Cause": "The global variable is not defined.",
            "Sub-Codes": {
                "0002": {
                    "Signal of Defect": "double-precision integer type"
                },
                "0007": {
                    "Signal of Defect": "byte type"
                }
            },
            "Location of Defect": None,
            "Sub-Code Description": "The sub code stands for the variable type.",
            "Potential Causes": []
        },
        "4436": {
            "Message": "UNDEFINED GLOBAL VARIABLE",
            "Cause": "The global variable is not defined.",
            "Sub-Codes": {
                "0003": {}
            },
            "Location of Defect": None,
            "Signal of Defect": "real type",
            "Sub-Code Description": "The sub code stands for the variable type.",
            "Potential Causes": []
        },
        "4437": {
            "Message": "UNDEFINED GLOBAL VARIABLE",
            "Cause": "The global variable is not defined.",
            "Sub-Codes": {
                "0004": {}
            },
            "Location of Defect": None,
            "Signal of Defect": "character string type",
            "Sub-Code Description": "The sub code stands for the variable type.",
            "Potential Causes": []
        },
        "4438": {
            "Message": "UNDEFINED GLOBAL VARIABLE",
            "Cause": "The global variable is not defined.",
            "Sub-Codes": {
                "0005": {
                    "Signal of Defect": "robot-axis position type",
                    "Sub-Code Description": "The sub code stands for the variable type."
                },
                "0000": {
                    "Signal of Defect": None,
                    "Sub-Code Description": None
                }
            },
            "Location of Defect": None,
            "Potential Causes": []
        },
        "4439": {
            "Message": "UNDEFINED GLOBAL VARIABLE",
            "Cause": "The global variable is not defined.",
            "Sub-Codes": {
                "0006": {
                    "Signal of Defect": "base-axis position type",
                    "Sub-Code Description": "The sub code stands for the variable type."
                },
                "0000": {
                    "Signal of Defect": None,
                    "Sub-Code Description": None
                }
            },
            "Location of Defect": None,
            "Potential Causes": []
        },
        "4440": {
            "Message": "UNDEFINED GLOBAL VARIABLE",
            "Cause": "The global variable is not defined.",
            "Sub-Codes": {
                "0007": {
                    "Signal of Defect": "station-axis position type",
                    "Sub-Code Description": "The sub code stands for the variable type."
                },
                "0000": {
                    "Signal of Defect": None,
                    "Sub-Code Description": None
                }
            },
            "Location of Defect": None,
            "Potential Causes": []
        },
        "4441": {
            "Message": "LACK OF LOCAL VARIABLE AREA",
            "Cause": "An error occurred when memory area for local variable was obtained. Memory area is lacking because too many local variables in the job are used.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "4444": {
            "Message": "UNSUCCESSFUL FINE POSITIONING",
            "Cause": "When PL = 0 or an external servo turned OFF, the number of the servo error pulses did not fall in the limit range that had been set in a parameter, within the specified time.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "4445": {
            "Message": "DATA PRESET ERROR",
            "Cause": "Data error occurred at job prereading reinterpretation due to",
            "Sub-Codes": {
                "0001:00FF": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": [
                "Software bugs",
                "Invalid NCP30 RAM memory The sub code stands for the alarm factor."
            ]
        },
        "4446": {
            "Message": "OVER VARIABLE LIMIT",
            "Cause": "The value for the binary (0/1) data type variable exceeded the limit.",
            "Sub-Codes": {
                "0001": {},
                "0002": {},
                "0004": {},
                "0006": {},
                "0008": {},
                "8002": {},
                "8003": {},
                "8004": {},
                "8005": {},
                "8006": {},
                "8007": {},
                "8008": {},
                "800C": {},
                "800D": {},
                "800E": {},
                "800F": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "4449": {
            "Message": "UNMATCHED D POSNVAR DATA ERROR",
            "Cause": "The storage destination data (pulse/ Cartesian) is different from the storage source data.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "4450": {
            "Message": "FILE NO. ERROR",
            "Cause": "This alarm occurs when the interpretation/ execution process detects abnormal internal data due to",
            "Sub-Codes": {
                "0001:000E": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the alarm factor.",
            "Potential Causes": [
                "Software bugs",
                "Invalid NCP30 RAM memory"
            ]
        },
        "4452": {
            "Message": "STACK MORE THAN 8 (JOB CALL)",
            "Cause": "An attempt was made to add more than eight stacks in the job call stack.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": None,
            "Signal of Defect": "JOB CALL",
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "4453": {
            "Message": "OVER VARIABLE NO.",
            "Cause": "The variable number (the variable number which an attempt was made to use for subcode) is out of range.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "4459": {
            "Message": "EXCESSIVE INSTRUCTION EQUATION",
            "Cause": "An error occurred in expression operation. The operation is impossible because the expression is too long.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "4460": {
            "Message": "ZERO DIVIDED OCCURRENCE",
            "Cause": "An error occurred in operation instruction. Zero division occurred.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "4466": {
            "Message": "OFFLINE UNDEFINED COMMAND (ARITH)",
            "Cause": "An undefined command was issued to the offline position-data preparation section due to",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": None,
            "Signal of Defect": "ARITH",
            "Sub-Code Description": None,
            "Potential Causes": [
                "Software bugs",
                "Invalid NCP30 RAM memory"
            ]
        },
        "4473": {
            "Message": "ARITHMETIC ALARM RESET ERROR",
            "Cause": "The alarm occurred in the calculation section could not be reset due to",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": [
                "Software bugs",
                "Invalid NCP30 RAM memory"
            ]
        },
        "4474": {
            "Message": "WRONG CONTROL GROUP AXIS",
            "Cause": "The CALL/JUMP destination job could not be executed. An attempt was made to call or jump to a job whose control group cannot be controlled. The sub code stands for the related control-group.",
            "Sub-Codes": {
                "0001 or 0002": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "4475": {
            "Message": "CANNOT EXECUTE JOB (NO ROBOT)",
            "Cause": "An attempt was made to execute a job without robot axis. The robot axis is not designated for the control-group of the job at execution of a work instruction that uses a manipulator.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": None,
            "Signal of Defect": "NO ROBOT",
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "4496": {
            "Message": "PARAMETER ERROR",
            "Cause": "This alarm occurs when an abnormal parameter is detected in the arithmetic process.",
            "Sub-Codes": {
                "0001:000D": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the alarm factor.",
            "Potential Causes": []
        },
        "4498": {
            "Message": "CANNOT EXECUTE JOB (NO GRP AXIS)",
            "Cause": "An error occurred in a job without control group. An attempt was made to execute an instruction that could not be executed in a job without control group.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": None,
            "Signal of Defect": "NO GRP AXIS",
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "4499": {
            "Message": "UNDEFINED POSITION VARIABLE",
            "Cause": "The position type variable is not registered. An attempt was made to use the position type variable that was not set.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the variable number.",
            "Potential Causes": []
        },
        "4501": {
            "Message": "OUT OF RANGE (PARALLEL PROCESS)",
            "Cause": "The number of tasks exceeded the limit. An error occurred in the multi-task control process for the independent control function.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": None,
            "Signal of Defect": "PARALLEL PROCESS",
            "Sub-Code Description": "The sub code stands for the task number.",
            "Potential Causes": []
        },
        "4507": {
            "Message": "REFP POS ERROR (SEARCH MOTION)",
            "Cause": "Incorrect teaching point for search detection \u00ef The search start point and the motion target point are the same, or the distance between the two points is too short.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": None,
            "Signal of Defect": "SEARCH MOTION",
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "4508": {
            "Message": "SPECIFIED ERROR (COORDINATE)",
            "Cause": "An invalid coordinate system was specified. The specified coordinate system does not exist.",
            "Sub-Codes": {
                "0000:0010": {
                    "Signal of Defect": "master tool coordinate system"
                },
                "0000": {
                    "Signal of Defect": "H-LINK type cylindrical coordinate system"
                }
            },
            "Location of Defect": "COORDINATE",
            "Sub-Code Description": "The sub code stands for the coordinate system.",
            "Potential Causes": []
        },
        "4513": {
            "Message": "EXCESSIVE SEGMENT (SAFETY1)",
            "Cause": "At the safety speed 1, the manipulator motion speed exceeded the speed limit value (LOW level).",
            "Sub-Codes": {
                "0001:001F": {}
            },
            "Location of Defect": None,
            "Signal of Defect": "LOW",
            "Sub-Code Description": "The sub code stands for the axis.",
            "Potential Causes": []
        },
        "4514": {
            "Message": "EXCESSIVE SEGMENT (SAFETY1)",
            "Cause": "At the safety speed 1, the manipulator motion speed exceeded the speed limit value (HIGH level).",
            "Sub-Codes": {
                "0001:001F": {}
            },
            "Location of Defect": None,
            "Signal of Defect": "HIGH",
            "Sub-Code Description": "The sub code stands for the axis.",
            "Potential Causes": []
        },
        "4515": {
            "Message": "EXCESSIVE SEGMENT (SAFETY2)",
            "Cause": "At the safety speed 2, the manipulator motion speed exceeded the speed limit value (LOW level).",
            "Sub-Codes": {
                "0001:001F": {}
            },
            "Location of Defect": None,
            "Signal of Defect": "LOW",
            "Sub-Code Description": "The sub code stands for the axis.",
            "Potential Causes": []
        },
        "4516": {
            "Message": "EXCESSIVE SEGMENT (SAFETY2)",
            "Cause": "At the safety speed 2, the manipulator motion speed exceeded the speed limit value (HIGH level).",
            "Sub-Codes": {
                "0001:001F": {}
            },
            "Location of Defect": None,
            "Signal of Defect": "HIGH",
            "Sub-Code Description": "The sub code stands for the axis.",
            "Potential Causes": []
        },
        "4517": {
            "Message": "SEARCH MONITOR SET ERROR (SERVO)",
            "Cause": "An error occurred in search/monitoring mode settings in servo section due to",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": "SERVO",
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the related control-group",
            "Potential Causes": [
                "Software bugs",
                "Invalid NCP30 RAM memory"
            ]
        },
        "4518": {
            "Message": "SEARCH MON RELEASE ERROR",
            "Cause": "An error occurred in search/monitoring mode releasing in servo section due to",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": [
                "Software bugs",
                "Invalid NCP30 RAM memory"
            ]
        },
        "4521": {
            "Message": "WRONG JOB TYPE",
            "Cause": "\u00ef A robot job was started from the concurrent job at CALL/JUMP instruction execution.",
            "Sub-Codes": {
                "0000:0001": {},
                "0000:1001": {},
                "1000:0001": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "4524": {
            "Message": "CANNOT EXECUTE INST (CONCUR JOB)",
            "Cause": "There was an unexecutable instruction such as move instruction in the concurrent job.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": None,
            "Signal of Defect": "CONCUR JOB",
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "4525": {
            "Message": "SPECIFIED JOB EXECUTION IMPOSSIBILITY",
            "Cause": "An error occurred at startup of multisystem job. The specified job could not be executed.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "4528": {
            "Message": "SYNTAX ERROR",
            "Cause": "An error occurred in the instruction syntax. The function and the corresponding instruction data is inconsistent in the system software",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the box number",
            "Potential Causes": []
        },
        "4537": {
            "Message": "OFFLINEMAIL BOX PROCESSING ERROR",
            "Cause": "An error occurred in mail box control in the offline processing section due to",
            "Sub-Codes": {
                "0001:0003": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the alarm factor.",
            "Potential Causes": [
                "Software bugs",
                "Invalid NCP30 RAM memory"
            ]
        },
        "4543": {
            "Message": "JOB CALL STACK ERROR",
            "Cause": "At job return, an attempt was made to fetch a data from an empty job call stack or to stack a data in the job call stack that is full.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "4544": {
            "Message": "MID$ ERROR",
            "Cause": "The first character of character string to be extracted is None at MID$ instruction execution.",
            "Sub-Codes": {
                "0001": {},
                "0002": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "4546": {
            "Message": "CANNOT EXECUTE SYSTEM JOB",
            "Cause": "The system job could not be executed. \u00ef An error in the system number of system job",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the system number",
            "Potential Causes": []
        },
        "4547": {
            "Message": "PRIMITIVE ERROR",
            "Cause": "The error occurred in the OS.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the error code from the OS.",
            "Potential Causes": []
        },
        "4548": {
            "Message": "CANNOT OPERATE SPECIFIED EVENT QUE",
            "Cause": "The specified event could not be operated at INIEVNT instruction execution.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "4549": {
            "Message": "INIEVNT NOT EXECUTED",
            "Cause": "INIEVNT instruction was not executed before having executed the event related process.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the system number",
            "Potential Causes": []
        },
        "4550": {
            "Message": "CANNOT EXECUTE INST (USER JOB)",
            "Cause": "The specified instruction in the user job could not be executed.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": None,
            "Signal of Defect": "USER JOB",
            "Sub-Code Description": "The sub code stands for the system number",
            "Potential Causes": []
        },
        "4599": {
            "Message": "SERVO COMMAND ERROR",
            "Cause": "An abnormal response was returned from the servo control section. The servo control processing has not completed.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "4606": {
            "Message": "GLOBAL VARIABLE AREA OVERFLOW",
            "Cause": "The memory area of global variable exceeded the limit value. An error occurred in the value of parameter that defines the number of global (user) variables.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "4628": {
            "Message": "DUPLICATE WRITE VARIABLE",
            "Cause": "In the command which returns multiple outputs, same variable is used for the setting value for outputs.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": None,
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "4800": {
            "Message": "WDT ERROR (CONVERTER)",
            "Cause": "Watchdog timer error in the converter. No response from the converter.",
            "Sub-Codes": {
                "0000": {}
            },
            "Location of Defect": "CONVERTER",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "9001": {
            "Message": "Manipulator / Pre-Aligner Secondary Power OFF [ W2]",
            "Cause": "This alarm occurs when the servos are off and a command is sent that requires the servo power to be on.",
            "Sub-Codes": {
                "0000:0004": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the alarm factor.",
            "Potential Causes": []
        },
        "9002": {
            "Message": "Manipulator Homing Not Completed [W2]",
            "Cause": "This alarm occurs if any motion command other than MABS or MRLK, MRLN, ISYS is received when the manipulator is not located in the ISYS position, MIN or, RDY positions.",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "9003": {
            "Message": "CRSM Command Inexecutable [W2]",
            "Cause": "This alarm occurs when the CHLT command has not been executed or the external HOLD signal is OPEN when CRSM command is requested from host.",
            "Sub-Codes": {
                "0001": {
                    "Signal of Defect": "CRSM command was received even though CHLT command hadn't been received."
                },
                "0002": {
                    "Signal of Defect": "CRSM command was received while external HOLD signal (EXHOLD) was OPEN"
                }
            },
            "Location of Defect": "W2",
            "Sub-Code Description": "The sub code stands for the alarm factor.",
            "Potential Causes": []
        },
        "9004": {
            "Message": "MTRS Command Not Completed [W2]",
            "Cause": "This alarm occurs if the manipulator is not located in ready position when MGET or MPUT or MPNT is requested.",
            "Sub-Codes": {
                "0001:001B": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the command in which the alarm is detected.",
            "Potential Causes": []
        },
        "9005": {
            "Message": "Execution Disabled Command [W2]",
            "Cause": "This alarm occurs if the requested command cannot be executed by the cause indicated by the sub code.",
            "Sub-Codes": {
                "0001": {
                    "Signal of Defect": "An unexecutable command for the specified unit was sent"
                },
                "0003": {
                    "Signal of Defect": "CSRV command (Servo ON) for manipulator was received during alarm occurrence."
                },
                "0004": {
                    "Signal of Defect": "CSRV command (Servo ON) for manipulator was received during emergency stop."
                },
                "0005": {
                    "Signal of Defect": "CSRV command (Servo ON) for pre-aligner was received in the system of which parameter was set to \"Pre-aligner setting: Disabled\"."
                },
                "0006": {
                    "Signal of Defect": "CSRV command (Servo ON) for pre-aligner was received during alarm occurrence."
                },
                "0007": {
                    "Signal of Defect": "CSRV command (Servo ON) for pre-aligner was received during emergency stop."
                },
                "0009": {
                    "Signal of Defect": "CLFT command was received even though the parameter of the system was set to \"Lifter existence: w/o lifter\" or \"Lifter control enable/disable: Disabled\"."
                },
                "000C": {
                    "Signal of Defect": "In the system of which Upper End-Effector is not Edge Grip, SPOS and SABS for mapping position were received."
                },
                "000D": {
                    "Signal of Defect": "ISYS command for pre-aligner was received even though the parameter of the system was set to \"Pre-aligner setting: Disabled\"."
                },
                "000E": {
                    "Signal of Defect": "SPRM and DPRM were received during Servo ON status."
                }
            },
            "Location of Defect": "W2",
            "Sub-Code Description": "The sub code stands for the alarm factor.",
            "Potential Causes": []
        },
        "9006": {
            "Message": "Disabled Point Motion [W2]",
            "Cause": "This alarm occurs when a point that the manipulator cannot move to is specified by MPNT command.",
            "Sub-Codes": {
                "0001:000D": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the alarm factor.",
            "Potential Causes": []
        },
        "9007": {
            "Message": "Execution Disabled for ISYS Command for Pre-Aligner [W2]",
            "Cause": "This alarm occurs if ISYS for the manipulator hasn't been completed when ISYS command is requested by the host of the pre-aligner.",
            "Sub-Codes": {
                "0001:0002": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the alarm factor.",
            "Potential Causes": []
        },
        "9008": {
            "Message": "Impossible to Read Mapping Data [W2]",
            "Cause": "This alarm occurs if RMAP command is received for a station at which mapping has not been executed.",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "9009": {
            "Message": "Uploading/Downloading [W2]",
            "Cause": "This alarm occurs if another command is received while uploading / downloading position data or parameters.",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "9010": {
            "Message": "Position Unregistered [W2]",
            "Cause": "This alarm occurs if the teaching for the specified station has not finished when a command is requested from host.",
            "Sub-Codes": {
                "0001:0031": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the alarm factor.",
            "Potential Causes": []
        },
        "9011": {
            "Message": "Incorrect Station Attribute [W2]",
            "Cause": "This alarm occurs in the following cases",
            "Sub-Codes": {
                "0001": {
                    "Signal of Defect": "Control method of swung wrist axis (Parameter i300 to i319) value of the corresponding station is set to other than 0/1/2."
                },
                "0002": {
                    "Signal of Defect": "Automatic ready position generation (Parameter i320 to i339) of the corresponding station is set to other than 0/1."
                },
                "0003": {
                    "Signal of Defect": "Number of via point (Parameter i340 to i359) value of the corresponding station is set to other than 0/1/2/3."
                },
                "0004": {
                    "Signal of Defect": "End-Effector Swappable position (Parameter i360 to i379) value of the corresponding station is set to 0 - 31."
                },
                "0005": {
                    "Signal of Defect": "The IM3 position, of the station which was defined as \"IM3: None\" in Number of via point (Parameter i340 to i359), was taught."
                },
                "0006": {
                    "Signal of Defect": "The IM2 position, of the station which was defined as \"IM2: None\" in Number of via point (Parameter i340 to i359), was taught."
                },
                "0007": {
                    "Signal of Defect": "The IM1 position, of the station which was defined as \"IM1: None\" in Number of via point (Parameter i340 to i359), was taught."
                }
            },
            "Location of Defect": "W2",
            "Sub-Code Description": "The sub code stands for the alarm factor.",
            "Potential Causes": [
                "Teaching is executed for the station which has an incorrect parameter setting.",
                "A via point, which is not defined in the station attribute parameter, is taught."
            ]
        },
        "9031": {
            "Message": "Unit Number Error [W2]",
            "Cause": "This alarm occurs when the command for the pre-aligner is received in pre-aligner unit disabled system. It also occurs if the command of which unit number is set to other than 1,2 is received.",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "9032": {
            "Message": "Undefined Command Error [W2]",
            "Cause": "This alarm occurs if an undefined command is received. In addition, this alarm occurs in case that a command is requested to a wrong unit.",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "9033": {
            "Message": "Message Parameter Error [W2]",
            "Cause": "This alarm occurs when the parameter attached to a command is not correct when a command is requested from host.",
            "Sub-Codes": {
                "0001:00BF": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the alarm factor.",
            "Potential Causes": []
        },
        "9035": {
            "Message": "CEMG Command Executed [A1]",
            "Cause": "This alarm occurs when the CEMG command is received while the unit is moving, and also after receiving CEMG command, the motion command is received before receiving CCLR command.",
            "Sub-Codes": {
                "0001:000B": {}
            },
            "Location of Defect": "A1",
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the alarm factor.",
            "Potential Causes": []
        },
        "9036": {
            "Message": "Access Permission Error 1 [W2]",
            "Cause": "Time-out of access permission signal 1 to the specified station occurs. The following cases can be the causes for this alarm",
            "Sub-Codes": {
                "0001:000C": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the command in which the alarm is detected.",
            "Potential Causes": [
                "The access permission signal 1 is not input.",
                "Incorrect wiring between the host and the controller."
            ]
        },
        "9037": {
            "Message": "Access Permission Error 2 [W2]",
            "Cause": "Time-out of access permission signa2 1 to the specified station occurs. The following cases can be the causes for this alarm",
            "Sub-Codes": {
                "0001:000C": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the command in which the alarm is detected.",
            "Potential Causes": [
                "The access permission signal 1 is not input.",
                "Incorrect wiring between the host and the controller."
            ]
        },
        "9038": {
            "Message": "Access Permission Error 3 [W2]",
            "Cause": "Time-out of access permission signal 3 to the specified station occurs. The following cases can be the causes for this alarm",
            "Sub-Codes": {
                "0001:000C": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the command in which the alarm is detected.",
            "Potential Causes": [
                "The access permission signal 1 is not input.",
                "Incorrect wiring between the host and the controller."
            ]
        },
        "9039": {
            "Message": "Access Permission Error 4 [W2]",
            "Cause": "Time-out of access permission signal 4 to the specified station occurs. The following cases can be the causes for this alarm",
            "Sub-Codes": {
                "0001:000C": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the command in which the alarm is detected.",
            "Potential Causes": [
                "The access permission signal 1 is not input.",
                "Incorrect wiring between the host and the controller."
            ]
        },
        "9040": {
            "Message": "Access Permission Error 5 [W2]",
            "Cause": "Time-out of access permission signal 5 to the specified station occurs. The following cases can be the causes for this alarm",
            "Sub-Codes": {
                "0001:000C": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the command in which the alarm is detected.",
            "Potential Causes": [
                "The access permission signal 1 is not input.",
                "Incorrect wiring between the host and the controller."
            ]
        },
        "9041": {
            "Message": "Access Permission Error 6 [W2]",
            "Cause": "Time-out of access permission signal 6 to the specified station occurs. The following cases can be the causes for this alarm",
            "Sub-Codes": {
                "0001:000C": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the command in which the alarm is detected.",
            "Potential Causes": [
                "The access permission signal 1 is not input.",
                "Incorrect wiring between the host and the controller."
            ]
        },
        "9042": {
            "Message": "Access Permission Error 7 [W2]",
            "Cause": "Time-out of access permission signal 7 to the specified station occurs. The following cases can be the causes for this alarm",
            "Sub-Codes": {
                "0001:000C": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the command in which the alarm is detected.",
            "Potential Causes": [
                "The access permission signal 1 is not input.",
                "Incorrect wiring between the host and the controller."
            ]
        },
        "9043": {
            "Message": "Access Permission Error 8 [W2]",
            "Cause": "Time-out of access permission signal 8 to the specified station occurs. The following cases can be the causes for this alarm",
            "Sub-Codes": {
                "0001:000C": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the command in which the alarm is detected.",
            "Potential Causes": [
                "The access permission signal 1 is not input.",
                "Incorrect wiring between the host and the controller."
            ]
        },
        "9046": {
            "Message": "Home Motion Disabled [W2]",
            "Cause": "This alarm occurs if the manipulator doesn't meet the requirements for the HOME command when MHOM or ISYS from host is executed.",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "9049": {
            "Message": "Home Motion Disabled [W2]",
            "Cause": "This alarm occurs if the manipulator doesn't meet the requirements for the HOME command when MHOM or ISYS from host is executed.",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "9050": {
            "Message": "Access Permission for Pre-Aligner Stage Error 1 [W2]",
            "Cause": "This alarm occurs if the command to move the manipulator to the pre-aligner station is executed while the pre-aligner is operating.",
            "Sub-Codes": {
                "0001:0003": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the alarm factor.",
            "Potential Causes": []
        },
        "9051": {
            "Message": "Pre-Aligner Station Access Interlock Error [W2]",
            "Cause": "This alarm occurs if the manipulator is instructed to access the pre-aligner while the pre-aligner is chucking a wafer. The following cases can be the causes for this alarm",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": [
                "The wafer is not released.",
                "The parameter setting value is incorrect.",
                "The foreign objects are blocking the chucking face.",
                "Vacuum air failure",
                "Pressure switch failure"
            ]
        },
        "9052": {
            "Message": "Wafer Presence Check Time-out [W2]",
            "Cause": "This alarm occurs when the pressure switch cannot detect a wafer within the time specified in the manipulator parameter I030/i031 (Set value at shipping: 200, Unit: 10ms). The causes for this alarm can be as follows:",
            "Sub-Codes": {
                "0001:0013": {}
            },
            "Location of Defect": "Lower end-effector",
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the timing when the alarm occurs.",
            "Potential Causes": [
                "Teaching Error",
                "Error in command sending order",
                "Parameter setting error",
                "Solenoid Valve Failure",
                "Vacuum Leak",
                "Pressure Switch Failure",
                "CDA Leak",
                "Grip sensor failure"
            ]
        },
        "9053": {
            "Message": "Wafer Absence Check Time-out [W2]",
            "Cause": "This alarm occurs when the pressure switch doesn't detect the absence of the wafer within the time specified in the manipulator parameter I030/i031 (Set value at shipping: 200, Unit: 10ms). The causes for this alarm can be as follows:",
            "Sub-Codes": {
                "0001:0015": {}
            },
            "Location of Defect": "Lower end-effector",
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the timing when the alarm occurs.",
            "Potential Causes": [
                "Teaching Error",
                "Error in command sending order",
                "Parameter setting error",
                "Solenoid Valve Failure",
                "Vacuum blockage",
                "Pressure Switch Failure"
            ]
        },
        "9054": {
            "Message": "Wafer Presence Check Time-out [W2]",
            "Cause": "This alarm occurs when the pressure switch cannot detect a wafer within the time specified in the manipulator parameter I030/i031 (Set value at shipping: 200, Unit: 10ms). The causes for this alarm can be as follows:",
            "Sub-Codes": {
                "0001:0013": {}
            },
            "Location of Defect": "Upper end-effector",
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the timing when the alarm occurs.",
            "Potential Causes": [
                "Teaching Error",
                "Error in command sending order",
                "Parameter setting error",
                "Solenoid Valve Failure",
                "Vacuum Leak",
                "Pressure Switch Failure",
                "CDA Leak",
                "Grip sensor failure"
            ]
        },
        "9055": {
            "Message": "Wafer Absence Check Time-out [W2]",
            "Cause": "This alarm occurs when the pressure switch doesn't detect the absence of the wafer within the time specified in the manipulator parameter I030/i031 (Set value at shipping: 200, Unit: 10ms). The causes for this alarm can be as follows:",
            "Sub-Codes": {
                "0001:0016": {}
            },
            "Location of Defect": "Upper end-effector",
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the timing when the alarm occurs.",
            "Potential Causes": [
                "Teaching Error",
                "Error in command sending order",
                "Parameter setting error",
                "Solenoid Valve Failure",
                "Vacuum blockage",
                "Pressure Switch Failure"
            ]
        },
        "9056": {
            "Message": "Wafer Drop Error [W2]",
            "Cause": "This alarm occurs when the pressure switch signal has changed its status from \"with wafer (ON)\" to \"without wafer (OFF)\" while a wafer is being transported. The causes for this alarm can be as follows:",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": "Lower end-effector",
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the timing when the alarm occurs.",
            "Potential Causes": [
                "Teaching Error",
                "Error in command sending order",
                "Parameter setting error",
                "Solenoid Valve Failure",
                "Vacuum Leak",
                "Pressure Switch Failure",
                "CDA Leak",
                "Grip sensor failure"
            ]
        },
        "9057": {
            "Message": "Wafer Drop Error [W2]",
            "Cause": "This alarm occurs when the pressure switch signal has changed its status from \"with wafer (ON)\" to \"without wafer (OFF)\" while a wafer is being transported. The causes for this alarm can be as follows:",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": "Upper end-effector",
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the timing when the alarm occurs.",
            "Potential Causes": [
                "Teaching Error",
                "Parameter setting error",
                "Solenoid Valve Failure",
                "Vacuum Leak",
                "Pressure switch failure",
                "CDA Leak",
                "CDA Leak"
            ]
        },
        "9059": {
            "Message": "CCD Data Error [W2]",
            "Cause": "This alarm occurs if the data valid for alignment calculation (The pixel position for wafer edge detection  3 to 2047) is less than 75 % out of all sampling data. The following cases can be the causes for this alarm",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": [
                "The wafer size and the ready position don't correspond with each other",
                "The teaching position for the manipulator is not correct",
                "The standard position of the pre-aligner is not correct.",
                "There is dust or dirt or scratch on the lens of the linear sensor or the filter",
                "The wafer is deviated while sampling the data.",
                "The linear sensor is broken"
            ]
        },
        "9061": {
            "Message": "Wafer Center Detection Error [W2]",
            "Cause": "This alarm occurs when the center of the wafer cannot be detected. The following cases can be the causes for this alarm",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": [
                "The wafer is deformed",
                "The dust is attached to the wafer edge.",
                "There is dust or dirt or scratches on the lens of the linear sensor or the filter.",
                "The wafer has shifted while the data is being sampled.",
                "The linear sensor is broken."
            ]
        },
        "9062": {
            "Message": "Excessive Wafer Eccentricity [W2]",
            "Cause": "This alarm occurs when the eccentricity of the wafer exceeds 5mm as the result of the alignment. The followings can be the causes for this alarm",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": [
                "Teaching error for the manipulator",
                "Incorrect standard position (300mm ready position) of the pre-aligner"
            ]
        },
        "9063": {
            "Message": "Notch/ Orientation Flat Detection Error [W2]",
            "Cause": "This alarm occurs if the notch or the oriental flat cannot be detected. The following cases can be the causes for this alarm",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": [
                "The wafer is deformed.",
                "Dust is attached to the wafer edge.",
                "The wafer is chipped.",
                "There is dust or dirt or scratches on the lens of the linear sensor or the filter.",
                "The wafer shifted while the data is being sampled.",
                "The linear sensor is broken."
            ]
        },
        "9065": {
            "Message": "Mapping Sensor Error [W2]",
            "Cause": "This alarm occurs if the mapping sensor signal is ON (shielded) at the mapping start position. The followings can be the causes for this alarm",
            "Sub-Codes": {
                "0001:0002": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": [
                "Teaching error",
                "The sensor is shielded by something",
                "The deviation of the source axis",
                "Mapping sensor error"
            ]
        },
        "9067": {
            "Message": "Mapping Calibration Not Executed [W2]",
            "Cause": "This alarm occurs if the number of the wafers detected by MMCA command is not the following number",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": [
                "Simple mode (B variable B041=0): 2 wafers",
                "All slot mode (B variable B041=1): Slot number"
            ]
        },
        "9068": {
            "Message": "Mapping Data Error [W2]",
            "Cause": "This alarm also occurs if a wafer has been detected at the height where there is no slot by MMAP command.",
            "Sub-Codes": {
                "0001:0004": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the alarm factor,",
            "Potential Causes": []
        },
        "9070": {
            "Message": "Non-Host Mode Error [W2]",
            "Cause": "This alarm occurs if a command is received from the host when the mode is not set to host-mode. The causes for this alarm can be as follows:",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": [
                "Mode setting mistake",
                "Teaching pendant failure",
                "Teaching pendant dummy connector is broken",
                "NIF30 board failure"
            ]
        },
        "9073": {
            "Message": "Command in Execution Error [W2]",
            "Cause": "This alarm occurs when another command from the host is received while executing a command.",
            "Sub-Codes": {
                "0001:0007": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "9076": {
            "Message": "Message Length Error [W2]",
            "Cause": "This alarm occurs when receiving a command with a different length specified for each command, or when receiving the command with a message longer than 1024 characters, or when receiving an MACR instruction longer than 64 characters.",
            "Sub-Codes": {
                "0001:0003": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the alarm factor.",
            "Potential Causes": []
        },
        "9077": {
            "Message": "Checksum Error [W2]",
            "Cause": "This alarm occurs when the checksum value in the received message differs from the checksum value of the received message. The causes for this alarm can be as follows:",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": [
                "Message error",
                "Wrong parameter setting",
                "Loosing of a connector",
                "Noise",
                "Communication cable failure",
                "NCP30 board failure"
            ]
        },
        "9083": {
            "Message": "Plunger motion Time-out [W2]",
            "Cause": "This alarm occurs if the sensor flag of the plunger doesn't shade a wafer grip sensor within the time specified by the manipulator parameter I021 (Set value at shipping: 80, Unit 10ms). The causes for this alarm can be as follows::",
            "Sub-Codes": {
                "0001:000F": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": "Lower end-effector",
            "Sub-Code Description": "The sub code stands for the timing when the alarm occurs.",
            "Potential Causes": [
                "The plunger motion speed has decelerated.",
                "CDA leak",
                "Solenoid valve failure",
                "Sensor flag has been deformed",
                "Wafer grip sensor failure",
                "Parameter setting error"
            ]
        },
        "9084": {
            "Message": "Plunger motion Time-out [W2]",
            "Cause": "This alarm occurs if the sensor flag of the plunger doesn't shade a wafer grip sensor within the time specified by the manipulator parameter I021 (Set value at shipping: 80, Unit 10ms). The causes for this alarm can be as follows::",
            "Sub-Codes": {
                "0001:000F": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": "Upper end-effector",
            "Sub-Code Description": "The sub code stands for the timing when the alarm occurs.",
            "Potential Causes": [
                "The plunger motion speed has decelerated.",
                "CDA leak",
                "Solenoid valve failure",
                "Sensor flag has been deformed",
                "Wafer grip sensor failure",
                "Parameter setting error"
            ]
        },
        "9085": {
            "Message": "Pre-Aligner Lifter motion Time-out [W2]",
            "Cause": "This alarm occurs if the lifter motion is not completed within 2 seconds after the instruction is output toward pre-aligner lifter. The causes for this alarm can be as follows:",
            "Sub-Codes": {
                "0001:0006": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the timing when the alarm occurs.",
            "Potential Causes": [
                "Compressed dry air error",
                "Solenoid valve error",
                "Lifter sensor error",
                "Lifter sensor position deviation"
            ]
        },
        "9087": {
            "Message": "Servo ON Failure [W2]",
            "Cause": "This alarm occurs when the servo is not turned ON within 2 seconds after the servo ON instruction is output. This alarm is caused by the other error occurrence.",
            "Sub-Codes": {
                "0001:0004": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "9088": {
            "Message": "CCD or Pressure Sensor Error [W2]",
            "Cause": "This alarm occurs only when executing the ISYS command of pre-aligner. The pre-aligner moves to 300mm ready position first. And then if the pressure switch detects a wafer and the linear sensor doesn't detect a wafer, the pre-aligner moves to the 200mm ready position. In the case that the linear sensor cannot detect a wafer at 200mm ready position, this alarm occurs. The causes for this alarm can be as follows:",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": [
                "Compressed dry air error",
                "Wafer deviation",
                "Screening of chucking opening by foreign object",
                "Vacuum piping obstruction",
                "Pressure switch failure",
                "Pressure switch failure"
            ]
        },
        "9089": {
            "Message": "Pre-Aligner Station Access Intaerlock Error [W2]",
            "Cause": "This alarm occurs if the manipulator with a straight-type end-effector tries to access the pre-aligner when it is not located in the upper end position. The causes for this alarm can be as bellows",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": [
                "Operation mistake",
                "Parameter setting error",
                "CDA leak",
                "Lifter sensor position deviation",
                "Lifter sensor failure"
            ]
        },
        "9090": {
            "Message": "Pre-Aligner Station Access Intaerlock Error [W2]",
            "Cause": "This alarm occurs when putting a wafer on the pre-aligner even though the linear sensor is detecting a wafer . The causes for this alarm can be as follows:",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": [
                "Operation mistake",
                "Parameter setting error",
                "CDA leak",
                "Lifter sensor position deviation",
                "Lifter sensor failure"
            ]
        },
        "9091": {
            "Message": "No Pre-Aligner Wafer [W2]",
            "Cause": "This alarm occurs if the wafer cannot be chucked with in the time specified in the pre-aligner parameter i030 (set value at shipping: 100, unit: 10ms ) when executing MALN and MACA. The causes for this alarm can be as follows:",
            "Sub-Codes": {
                "0001:0002": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": [
                "There is no wafer on the pre-aligner",
                "Vacuum leak",
                "Pressure switch failure"
            ]
        },
        "9092": {
            "Message": "Emergency Stop [A1]",
            "Cause": "This alarm occurs when",
            "Sub-Codes": {
                "0001": {
                    "Signal of Defect": "CCHK command was received during emergency stop."
                },
                "0002": {
                    "Signal of Defect": "CCLR command was received during emergency stop."
                },
                "0003": {
                    "Signal of Defect": "CSRV command (Servo ON) for manipulator was received during emergency stop."
                },
                "0004": {
                    "Signal of Defect": "Emergency stop was requested while servo ON processing for manipulator was being executed."
                },
                "0005": {
                    "Signal of Defect": "CSRV command (Servo ON) for pre-aligner was received during emergency stop."
                },
                "0006": {
                    "Signal of Defect": "Emergency stop was requested while servo ON processing for pre-aligner was being executed."
                },
                "0007": {
                    "Signal of Defect": "CLFT command was received during emergency stop."
                },
                "0008": {
                    "Signal of Defect": "Emergency stop for the manipulator was received."
                },
                "0009": {
                    "Signal of Defect": "Emergency stop for the pre-aligner was received."
                },
                "0010": {
                    "Signal of Defect": "Emergency stop for the pre-aligner was received."
                },
                "0011": {
                    "Signal of Defect": "HRST command was received during emergency stop."
                },
                "000A": {
                    "Signal of Defect": "MACR command was received during emergency stop."
                },
                "000B": {
                    "Signal of Defect": "MACR command was received during emergency stop."
                },
                "000C": {
                    "Signal of Defect": "Motion command was received during emergency stop."
                },
                "000D": {
                    "Signal of Defect": "ISYS command was received during emergency stop."
                },
                "000E": {
                    "Signal of Defect": "Control command other than CEMG, CCLR, and HRST was received during emergency stop."
                },
                "000F": {
                    "Signal of Defect": "Emergency stop for the manipulator was received."
                }
            },
            "Location of Defect": "A1",
            "Sub-Code Description": "The sub code stands for the alarm factor.",
            "Potential Causes": [
                "There is no wafer on the pre-aligner",
                "Emergency stop button on teaching pendant is pressed",
                "External emergency stop signal is OPEN",
                "A command is requested under the status that the emergency stop on teaching pendant is being pressed",
                "the teaching pendant dummy connector is not connected",
                "external emergency stop signal is OPEN"
            ]
        },
        "9093": {
            "Message": "Pre-Aligner Lifter Position Error [W2}",
            "Cause": "This alarm occurs if alignment or calibration is requested when the pre-aligner lifter, of which setting is \"Set pre-aligner lifter\" and \"No pre-aligner lifter control\", is not located in the lower end position.",
            "Sub-Codes": {
                "0001:0004": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "9094": {
            "Message": "Pre-Aligner Wafer Chuck Time-out [W2]",
            "Cause": "This alarm occurs if the wafer cannot be chucked within the time specified in the pre-aligner parameter i030 (set value at shipping: 100, unit: 10ms) when executing CCHK command. The causes for this alarm can be as follows::",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": [
                "No wafer is on the pre-aligner",
                "Vacuum leaking",
                "Pressure switch failure"
            ]
        },
        "9095": {
            "Message": "Pre-Aligner Wafer Release Time-out Error [W2]",
            "Cause": "This alarm occurs if the chuck/release operation cannot be executed within the time specified in the pre-aligner parameter I030 (set value at shipping: 100, unit: 10ms) when executing CCHK command. The causes of this alarm are",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": [
                "Blockage of vacuum air",
                "Solenoid valve failure",
                "Pressure Switch system failure"
            ]
        },
        "9096": {
            "Message": "CCD or Pressure Sensor Error [W2]",
            "Cause": "This alarm occurs if the linear sensor detects the wafer even though the pressure switch is not detecting any wafer when executing ISYS command. The causes for this alarm can be as follows:",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": [
                "Blockage of vacuum air",
                "There is dust or dirt or scratches on the lens of the linear sensor or the filter.",
                "Linear sensor failure",
                "Vacuum leak",
                "Pressure switch failure"
            ]
        },
        "9097": {
            "Message": "User Task Stopped [W2]",
            "Cause": "The alarm also occurs if the user task cannot start up by CCLR or MABS, MRLK, MRLR, ISYS.",
            "Sub-Codes": {
                "0001:0007": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the command in which the alarm is detected.",
            "Potential Causes": []
        },
        "9098": {
            "Message": "System Error [F]",
            "Cause": "Failure in error number: detects the error as an undefined error, \"0000\", though the system error signal is on.",
            "Sub-Codes": {
                "0001:0005": {}
            },
            "Location of Defect": "F",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "9100": {
            "Message": "MACRO Accept Error [W2]",
            "Cause": "A new transfer command is sent during the process of another transfer command",
            "Sub-Codes": {
                "0001": {
                    "Signal of Defect": "Manipulator"
                },
                "0002": {
                    "Signal of Defect": "Pre-aligner"
                }
            },
            "Location of Defect": "W2",
            "Sub-Code Description": "The sub code stands for the unit in which the alarm is detected.",
            "Potential Causes": []
        },
        "9101": {
            "Message": "Position Calculation Error [W2]",
            "Cause": "This alarm occurs if the route calculated during teaching a position or during a system motion command is outside the motion range of the manipulator. The causes are When instructing teaching position, \u00ef Blockage of vacuum air \u00ef Position name is instructed incorrectly. (such as STA) \u00ef End-Effector is instructed incorrectly. (1/ 2) \u00ef Parameter error R460 to R479 and R480 to R499 When moving to relative position, \u00ef The motion distance instruction is out of the operation range. When executing a transport system command. \u00ef Parameter error R120 to R319 (Transfer offset)",
            "Sub-Codes": {
                "0001:0023": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": None,
            "Sub-Code Description": "Sub code differs depending on the command at alarm occurrence.",
            "Potential Causes": []
        },
        "9102": {
            "Message": "System JOB Not Registered [F]",
            "Cause": "This alarm occurs if any system JOB is registered.",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": "F",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "9103": {
            "Message": "System JOB Not Started [F]",
            "Cause": "System JOB is stopped because of other alarm occurrences.",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": "F",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "9104": {
            "Message": "SAFE Signal OPEN [A1]",
            "Cause": "This alarm occurs in the following cases \u00ef Fence signal (both SAFF1 and 2 ) is open while the manipulator or prealigner is moving \u00ef CCLR, CSRV, MACR, ISYS or motion command is received in the status that fence signal ( both SAFF1 and 2 ) is open.",
            "Sub-Codes": {
                "0001:000C": {}
            },
            "Location of Defect": "A1",
            "Signal of Defect": None,
            "Sub-Code Description": "Sub code differs depending on the command at alarm occurrence.",
            "Potential Causes": []
        },
        "9105": {
            "Message": "EXSVON Signal OPEN [A1]",
            "Cause": "This alarm occurs in the following cases \u00ef External servo power ON signal (EXSVON) is open while the manipulator or pre-aligner is moving \u00ef CCLR, CSRV, MACR, ISYS or motion command is received in the status that external servo power ON signal is open.",
            "Sub-Codes": {
                "0001:000C": {}
            },
            "Location of Defect": "A1",
            "Signal of Defect": None,
            "Sub-Code Description": "Sub code differs depending on the command at alarm occurrence.",
            "Potential Causes": []
        },
        "9106": {
            "Message": "EXHOLD Signal OPEN [W2]",
            "Cause": "This alarm occurs if CCLR, MACR, ISYS or motion command is received in the status that external hold signal (EXHOLD) is open.",
            "Sub-Codes": {
                "0001:000A": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": None,
            "Sub-Code Description": "Sub code differs depending on the command at alarm occurrence.",
            "Potential Causes": []
        },
        "9107": {
            "Message": "Controller Battery Error [W2]",
            "Cause": "This alarm occurs when the voltage of the battery for memory backup of the controller becomes lower than 2.8V. In case of the occurrence of this alarm, the alarm code is sent by the completion response for the first command after the alarm occurrence.",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        },
        "9108": {
            "Message": "Serial Encoder Battery Error [W2]",
            "Cause": "This alarm occurs when the voltage of the battery for backup of the encoder becomes lower than 2.8V. In case of the occurrence of this alarm, the alarm code is sent by the completion response for the first command after the alarm occurrence.",
            "Sub-Codes": {
                "0001:001F": {}
            },
            "Location of Defect": "W2",
            "Signal of Defect": None,
            "Sub-Code Description": "The sub code stands for the defective axis.",
            "Potential Causes": []
        },
        "9109": {
            "Message": "Hardware Reset Error [A1]",
            "Cause": "No response for HRST command.",
            "Sub-Codes": {
                "0001": {}
            },
            "Location of Defect": "A1",
            "Signal of Defect": None,
            "Sub-Code Description": None,
            "Potential Causes": []
        }
    }
}


def search_errors():
    alarm_code = entry_alarm_code.get().strip()
    sub_code = entry_sub_code.get().strip()

    if alarm_code not in error_codes_db:
        messagebox.showinfo("Error", "Alarm not found. View database?")
        return

    result = error_codes_db[alarm_code]
    if not sub_code or sub_code not in result['Sub-Codes']:
        display_info = f"Alarm Code: {alarm_code}\n" + json.dumps(result, indent=4)
    else:
        display_info = f"Alarm Code: {alarm_code}, Sub-Code: {sub_code}\n" + json.dumps(result['Sub-Codes'][sub_code],
                                                                                        indent=4)

    text_area.config(state=tk.NORMAL)
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, display_info)
    text_area.config(state=tk.DISABLED)


root = tk.Tk()
root.title("Error Code Lookup")

tk.Label(root, text="Enter Alarm Code:").grid(row=0, column=0)
entry_alarm_code = tk.Entry(root)
entry_alarm_code.grid(row=0, column=1)

tk.Label(root, text="Enter Sub-Code:").grid(row=1, column=0)
entry_sub_code = tk.Entry(root)
entry_sub_code.grid(row=1, column=1)

submit_button = tk.Button(root, text="Search", command=search_errors)
submit_button.grid(row=2, column=1)

text_area = tk.Text(root, state=tk.DISABLED, width=80, height=20)
text_area.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
