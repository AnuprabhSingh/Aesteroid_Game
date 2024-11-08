import arcade
import math
from typing import cast
import random
from sprites import TurningSprite,ShipSprite,AsteroidSprite
from constants import *

"""

Class: MyGame

Handles the main game logic, including drawing, input handling, and game updates.
Methods:

    init
        Initializes the game window, sprite lists, and loads sound effects.

    start_new_game
        Sets up a new game by initializing player, asteroids, bullets, and lives.
        Resets the score and creates text objects.

    on_draw
        Clears the screen and draws all game elements and text.

    on_key_press
        Handles player input for shooting bullets and controlling ship movement.

    on_key_release
        Stops ship movement when arrow keys are released.

    split_asteroid
        Splits an asteroid into smaller pieces based on its size.
        Increases score and plays appropriate sound effects.

    on_update
        Updates positions of all game elements.
        Checks for collisions between bullets and asteroids.
        Handles player collision with asteroids, reduces lives, and manages game-over state.
        Updates the score and asteroid count text.
"""






class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        pass

    def start_new_game(self):
        """ Set up the game and initialize the variables. """
        pass

       

    def on_draw(self):
        """
        Render the screen.
        """
        pass

    def on_key_press(self, symbol, modifiers):
        """ Called whenever a key is pressed. """
        # Shoot if the player hit the space bar and we aren't respawning.
        pass

    def on_key_release(self, symbol, modifiers):
        """ Called whenever a key is released. """
        pass

    def split_asteroid(self, asteroid: AsteroidSprite):
        """ Split an asteroid into chunks. """
        pass

    def on_update(self, x):
        """ Move everything """

        if not self.game_over:
            self.asteroid_list.update()
            self.bullet_list.update()
            self.player_sprite_list.update()

            for bullet in self.bullet_list:
                asteroids = arcade.check_for_collision_with_list(bullet,
                                                                 self.asteroid_list)

                for asteroid in asteroids:
                    # expected AsteroidSprite, got Sprite instead
                    self.split_asteroid(cast(AsteroidSprite, asteroid))
                    asteroid.remove_from_sprite_lists()
                    bullet.remove_from_sprite_lists()

                # Remove bullet if it goes off-screen
                size = max(bullet.width, bullet.height)
                if bullet.center_x < 0 - size:
                    bullet.remove_from_sprite_lists()
                if bullet.center_x > SCREEN_WIDTH + size:
                    bullet.remove_from_sprite_lists()
                if bullet.center_y < 0 - size:
                    bullet.remove_from_sprite_lists()
                if bullet.center_y > SCREEN_HEIGHT + size:
                    bullet.remove_from_sprite_lists()

            if not self.player_sprite.respawning:
                asteroids = arcade.check_for_collision_with_list(self.player_sprite,
                                                                 self.asteroid_list)
                if len(asteroids) > 0:
                    if self.lives > 0:
                        self.lives -= 1
                        self.player_sprite.respawn()
                        self.split_asteroid(cast(AsteroidSprite, asteroids[0]))
                        asteroids[0].remove_from_sprite_lists()
                        self.ship_life_list.pop().remove_from_sprite_lists()
                        print("Crash")
                    else:
                        self.game_over = True
                        print("Game over")

        # Update the text objects
        self.text_score.text = f"Score: {self.score}"
        self.text_asteroid_count.text = f"Asteroid Count: {len(self.asteroid_list)}"
