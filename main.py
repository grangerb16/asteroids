import pygame
import player 
import asteroid
import asteroidfield
import shot
from constants import *

def main():
    print("Starting Asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()    
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    asteroidfield.AsteroidField.containers = (updateable)
    asteroid.Asteroid.containers = (updateable, drawable, asteroids)
    player.Player.containers = (updateable, drawable)
    shot.Shot.containers = (shots, updateable, drawable)

    my_player = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    my_asteroidfield = asteroidfield.AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(pygame.Color(0,0,0))

        # my_player.update(dt)
        updateable.update(dt)

        # check collisions
        for ast in asteroids:
            if ast.collision(my_player):
                print("Game Over!")
                exit()

        for ast in asteroids:
            for bullet in shots:
                if ast.collision(bullet):
                    ast.kill()
                    bullet.kill()

        # my_player.draw(screen)
        for d in drawable:
            d.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()