import ctypes
import time
import tkinter as tk

# ---- COMMANDS LISTS ----
WEATHER_CODES = {
    "Clear": "fw 001CC2A4",
    "Cloudy": "fw 001CC2A5",
    "Light Rain": "fw 001CC2AD",
    "Storm": "fw 001CC2AE",
    "Fog": "fw 001CC2A7",
    "Snow": "fw 001CC2B0"
}

TIME_COMMANDS = {
    "Midnight (00:00)": "set gamehour to 0",
    "Dawn (06:00)": "set gamehour to 6",
    "Noon (12:00)": "set gamehour to 12",
    "Sunset (18:00)": "set gamehour to 18",
    "+1 Hour": "advancetime 1",
    "+10 Minutes": "advancetime 0.1667"
}

AMMO_COMMANDS = {
    "10mm": "player.additem 0001F276 9999",
    "5mm": "player.additem 0001F66C 9999",
    ".308": "player.additem 0001F66B 9999",
    ".44": "player.additem 0009221C 9999",
    ".38": "player.additem 000E6B27 9999",
    ".45": "player.additem 0001F66A 9999",
    ".50": "player.additem 0001F279 9999",
    "Shotgun Shell": "player.additem 0001F673 9999",
    "5.56mm": "player.additem 0001F278 9999",
    "Fusion Core": "player.additem 00075FE4 9999",
    "Mini Nuke": "player.additem 000E6B2E 9999",
    "Missile": "player.additem 000E6B2D 9999",
    "Flamer Fuel": "player.additem 000CAC78 9999",
    "Cryo Cell": "player.additem 0018ABE2 9999",
    "Railway Spike": "player.additem 000FE269 9999",
    "Gamma Round": "player.additem 000DF279 9999",
    "Cannonball": "player.additem 0010E689 9999",
    "Plasma Cartridge": "player.additem 00100E44 9999"
}

MATERIAL_COMMANDS = {
    "Aluminum": "player.additem 0006907A 9999",
    "Copper": "player.additem 0006907B 9999",
    "Steel": "player.additem 000731A4 9999",
    "Wood": "player.additem 000731A3 9999",
    "Nuclear Material": "player.additem 00069086 9999",
    "Ceramic": "player.additem 000AEC5F 9999",
    "Rubber": "player.additem 00106D98 9999",
    "Gears": "player.additem 0006907E 9999",
    "Screws": "player.additem 00069081 9999",
    "Adhesive": "player.additem 001BF72E 9999",
    "Plastic": "player.additem 0006907C 9999",
    "Fiberglass": "player.additem 000AEC61 9999"
}

LEVEL_COMMANDS = {
    "+1 Level": "player.advlevel",
    "+10 Levels": "player.setlevel player.getlevel +10",
    "+50 Levels": "player.setlevel player.getlevel +50"
}

CARRY_WEIGHT_COMMANDS = {
    "+10 Carry Weight": "player.modav carryweight 10",
    "+100 Carry Weight": "player.modav carryweight 100",
    "+1000 Carry Weight": "player.modav carryweight 1000"
}

HEALTH_ITEMS_COMMANDS = {
    "10 Stimpak": "player.additem 00023736 10",
    "50 Stimpak": "player.additem 00023736 50",
    "100 Stimpak": "player.additem 00023736 100",
    "10 Radaway": "player.additem 00023737 10",
    "50 Radaway": "player.additem 00023737 50",
    "100 Radaway": "player.additem 00023737 100",
    "10 Rad-X": "player.additem 0002373B 10",
    "50 Rad-X": "player.additem 0002373B 50",
    "100 Rad-X": "player.additem 0002373B 100",
    "10 Jet": "player.additem 0002372E 10",
    "50 Jet": "player.additem 0002372E 50",
    "100 Jet": "player.additem 0002372E 100",
    "10 Buffout": "player.additem 00023731 10",
    "50 Buffout": "player.additem 00023731 50",
    "100 Buffout": "player.additem 00023731 100",
    "10 Psycho": "player.additem 00023730 10",
    "50 Psycho": "player.additem 00023730 50",
    "100 Psycho": "player.additem 00023730 100",
    "10 Mentats": "player.additem 0002372D 10",
    "50 Mentats": "player.additem 0002372D 50",
    "100 Mentats": "player.additem 0002372D 100"
}

FAST_TRAVEL_COMMANDS = {
    "Vault 111": "player.moveto 0001A9D7",
    "Diamond City": "player.moveto 0001A946",
    "Goodneighbor": "player.moveto 0001A88F",
    "Bunker Hill": "player.moveto 00014E1E",
    "Nuka-World Entrance": "player.moveto 00069F64",
    "Far Harbor": "player.moveto 000DEFF5"
}

# ---- FUNCTIONS ----
def press_key(hexKeyCode):
    ctypes.windll.user32.keybd_event(hexKeyCode, 0, 0, 0)
    ctypes.windll.user32.keybd_event(hexKeyCode, 0, 2, 0)

def send_command(command):
    press_key(0x29)
    time.sleep(0.5)

    for char in command:
        ctypes.windll.user32.keybd_event(ord(char), 0, 0, 0)
        ctypes.windll.user32.keybd_event(ord(char), 0, 2, 0)
        time.sleep(0.05)

    press_key(0x0D)
    time.sleep(0.5)
    press_key(0x29) 

def execute_command(command_dict, key):
    command = command_dict.get(key, "")
    if command:
        send_command(command)

# ---- USER INTERFACE ----
root = tk.Tk()
root.title("FO4 - AIO Mod Menu")
root.geometry("1920x1080")
root.configure(bg="#222")

sections = [
    ("Change Weather", WEATHER_CODES, 0, 0),
    ("Change Time", TIME_COMMANDS, 0, 1),
    ("Give Ammo (9999)", AMMO_COMMANDS, 1, 0),
    ("Give Materials (9999)", MATERIAL_COMMANDS, 1, 1),
    ("Level Up", LEVEL_COMMANDS, 2, 0),
    ("Increase Carry Weight", CARRY_WEIGHT_COMMANDS, 2, 1)
]


for title, command_dict, row, col in sections:
    frame = tk.Frame(root, bg="#333", padx=10, pady=10)
    frame.grid(row=row, column=col, padx=20, pady=20, sticky="nw")

    tk.Label(frame, text=title, fg="white", bg="#333", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=5)

    max_cols = 3
    for i, key in enumerate(command_dict.keys()):
        tk.Button(frame, text=key, font=("Arial", 12), width=20, height=2,
                  command=lambda k=key: execute_command(command_dict, k), bg="#555", fg="white").grid(row=(i // max_cols) + 1, column=i % max_cols, padx=5, pady=5)


frame_health = tk.Frame(root, bg="#333", padx=10, pady=10)
frame_health.grid(row=0, column=2, rowspan=3, padx=20, pady=20, sticky="nw")

tk.Label(frame_health, text="Health Items & Drugs", fg="white", bg="#333", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=5)

max_cols = 3
for i, key in enumerate(HEALTH_ITEMS_COMMANDS.keys()):
    tk.Button(frame_health, text=key, font=("Arial", 12), width=20, height=2,
              command=lambda k=key: execute_command(HEALTH_ITEMS_COMMANDS, k), bg="#555", fg="white").grid(row=(i // max_cols) + 1, column=i % max_cols, padx=5, pady=5)

frame_teleport = tk.Frame(root, bg="#333", padx=10, pady=10)
frame_teleport.grid(row=3, column=2, padx=20, pady=20, sticky="nw")

tk.Label(frame_teleport, text="Fast Travel Locations", fg="white", bg="#333", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=5)

max_cols = 3
for i, key in enumerate(FAST_TRAVEL_COMMANDS.keys()):
    tk.Button(frame_teleport, text=key, font=("Arial", 12), width=20, height=2,
              command=lambda k=key: execute_command(FAST_TRAVEL_COMMANDS, k), bg="#555", fg="white").grid(row=(i // max_cols) + 1, column=i % max_cols, padx=5, pady=5)
root.mainloop()
