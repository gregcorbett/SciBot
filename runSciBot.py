"""This file runs the GameWindow."""


from src.GameWindow import GameWindow


def main():
    """Run the GameWindow."""
    gameWindow = GameWindow()
    gameWindow.start_rendering()
    gameWindow.choose_scenario()
    gameWindow.load_scenario()
    gameWindow.start_scenario()

if __name__ == "__main__":
    main()
