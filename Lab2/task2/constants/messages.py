TERMINAL_COMMANDS = {
    "add": "add elements to the container",
    "remove": "remove element from the container",
    "find": "find element in the container",
    "list": "list all elements of the container",
    "grep": "check if element suitable for provided regEx  is present in the container",
    "save": "save container to the file",
    "load": "load container from the file",
    "switch": "switch to another user",
    "exit": "exit the terminal"
}

LOAD_PROMPT = "Load {}'s data? [y][n]: "
SAVE_PROMPT = "Save {}'s data before switching? [y][n]: "
EXIT_PROMPT = "Save {}'s data before exiting? [y][n]: "
TERMINAL_GREETING = "$$$Terminal started$$$\n\nHelper:\n"

for command, description in TERMINAL_COMMANDS.items():
    TERMINAL_GREETING += f"{command}: {description}\n"
