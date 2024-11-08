import arcade
from game import MyGame

def main():
    """Start the game."""
    window = MyGame()
    window.start_new_game()
    arcade.run()

if __name__ == "__main__":
    main()
