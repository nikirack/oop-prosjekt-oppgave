from ui import Menu, info, win

def play_game() -> None:
    win("Starting game...")

def show_balance() -> None:
    info("You have 1000 credits.")

def settings() -> None:
    info("Opening settings...")

menu = Menu(
    title="Main Menu",
    options={
        1: "Play Game",
        2: "Show Balance",
        3: "Settings",
        4: "Statistics",
    },
)

choice: str = menu.ask()

match choice:
    case "0":
        print("Exiting...")
    case "1":
        print("Starting game...")
    case "2":
        print("Showing balance...")
    case "3":
        print("Opening settings...")
    case "4":
        print("Showing statistics...")