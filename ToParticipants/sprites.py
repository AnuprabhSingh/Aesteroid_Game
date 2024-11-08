import arcade
import math
from constants import *

# Constants to avoid cyclic imports


"""


This file defines three key classes for handling sprite behaviors within a space shooter game: TurningSprite, ShipSprite, and AsteroidSprite.
Classes:

    TurningSprite
        Represents a generic sprite that aligns its angle with its movement direction.
        The update() method calculates the angle based on its current velocity components.

    ShipSprite
        Manages the player's spaceship, handling movement, thrust, speed, and screen wrapping.
        Implements respawn functionality, where the ship becomes temporarily invulnerable after respawning.
        The update() method adjusts speed based on thrust and drag, updates position, and handles screen boundary wrapping.

    AsteroidSprite
        Represents asteroids in the game.
        Handles initialization and movement logic for asteroids as they float across the screen.


"""




class TurningSprite(arcade.Sprite):
    """ Sprite that sets its angle to the direction it is traveling in. """
    def update(self):
        """ Move the sprite """
        super().update()
        self.angle = math.degrees(math.atan2(self.change_y, self.change_x))


class ShipSprite(arcade.Sprite):
    """
    Sprite that represents our space ship.

    Derives from arcade.Sprite.
    """
    def __init__(self, filename, scale):
        """ Set up the space ship. """
        pass

    def respawn(self):
        """
        Called when we die and need to make a new ship.
        'respawning' is an invulnerability timer.
        """
        pass

    def update(self):
        """
        Update our position and other particulars.
        """
        if self.respawning:
            self.respawning += 1
            self.alpha = self.respawning
            if self.respawning > 250:
                self.respawning = 0
                self.alpha = 255
        if self.speed > 0:
            self.speed -= self.drag
            if self.speed < 0:
                self.speed = 0

        if self.speed < 0:
            self.speed += self.drag
            if self.speed > 0:
                self.speed = 0

        self.speed += self.thrust
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        if self.speed < -self.max_speed:
            self.speed = -self.max_speed

        self.change_x = -math.sin(math.radians(self.angle)) * self.speed
        self.change_y = math.cos(math.radians(self.angle)) * self.speed

        self.center_x += self.change_x
        self.center_y += self.change_y

        # If the ship goes off-screen, move it to the other side of the window
        if self.right < 0:
            self.left = SCREEN_WIDTH

        if self.left > SCREEN_WIDTH:
            self.right = 0

        if self.bottom < 0:
            self.top = SCREEN_HEIGHT

        if self.top > SCREEN_HEIGHT:
            self.bottom = 0

        """ Call the parent class. """
        super().update()


class AsteroidSprite(arcade.Sprite):
    """ Sprite that represents an asteroid. """

    def __init__(self, image_file_name, scale):
        pass
    def update(self):
        """ Move the asteroid around. """
        pass