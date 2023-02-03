#import the pygame & sys modules to workspace
import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship

import game_functions as gf

#creating an empty pygame window
def run_game():
    """Initialize game and create a screen object"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")

    #create an instance to store game statistics and create a scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # To make a ship
    ship = Ship(ai_settings, screen)
    #A group to store bullets in
    bullets = Group()
    aliens = Group()

    #create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    #color set
    bg_color = (0,0,255)

    #game loop
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button,
             ship, aliens, bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship,
                 aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb,ship,
                 aliens,bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship,
             aliens, bullets, play_button)
        
run_game()

#to access the events detected by pygame
pygame.event.get()

print(len(bullets))