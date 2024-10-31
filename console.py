import sys

# Available commands
commands = {
    'help': 'List available commands.',
    'status': 'Check the current status of the ship.',
    'logs': 'View past log entries.',
    'exit': 'Exit the console.'
}

# Sample ship status and logs
ship_status = {
    "oxygen_level": "Stable",
    "power_core": "Functioning at 95%",
    "external_temperature": "-270°C",
    "alien_presence": "Unknown anomaly detected",
}

logs = [
    "[Log 1] Cryo-chamber malfunction in sector 7B...",
    "[Log 2] Security breach reported in Class 3 quarters...",
    "[Log 3] Research log: Psychron experiment showing adverse effects on humans...",
]

def show_help():
    print("Available commands:")
    for command, description in commands.items():
        print(f"{command} - {description}")

def show_status():
    print("Ship Status:")
    for stat, value in ship_status.items():
        print(f"{stat}: {value}")

def show_logs():
    print("Accessing logs:")
    for entry in logs:
        print(entry)

def main():
    print("Welcome to the Nebula-5 Console.")
    print("Type 'help' for a list of commands.")
    
    while True:
        user_input = input("Enter command: ").strip().lower()
        
        if user_input == "help":
            show_help()
        elif user_input == "status":
            show_status()
        elif user_input == "logs":
            show_logs()
        elif user_input == "exit":
            print("Exiting console. Goodbye.")
            sys.exit()
        else:
            print("Unknown command. Type 'help' for a list of commands.")

if __name__ == "__main__":
    main()
