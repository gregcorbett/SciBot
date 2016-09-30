"""This file runs the GameWindow."""
import sys

from src.GameWindow import GameWindow


def main():
    """Run the GameWindow."""
    gameWindow = GameWindow()
    gameWindow.start_rendering()
    gameWindow.start_logic()

if __name__ == "__main__":
    main()
