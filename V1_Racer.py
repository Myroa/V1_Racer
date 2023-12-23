import pygame
import sys
import math
import random
import time
import pygame.mixer

pygame.init()

#Constant#-----------------------------#
WIDTH, HEIGHT = 2000, 1000
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
CAR_WIDTH, CAR_HEIGHT = 50, 30
ACCELERATION = 0.1
FRICTION = 0.09
TURN_SPEED = 2.5
MAX_SPEED = 1
Vaild_Lap = True
times = [100]
high_Score = [1]
Sec = 0
tick_counter = 0
#------------------------------------#

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("V1 Racer")

#images
main_menu_bg = pygame.image.load("C:\Coding\Main-Menu-V1-Racer2.png")
main_menu_bg_rect = main_menu_bg.get_rect()

text_font = pygame.font.SysFont("microsofttaile", 200)
text_font2 = pygame.font.SysFont("microsofttaile", 100)

def Main_M_text(text, font, text_col, x_MM, y_MM):
    words_MM = font.render(text, True, text_col)
    screen.blit(words_MM, (x_MM, y_MM))
def Main_M_text2(text, font, text_col, x_MM, y_MM):
    words_MM = font.render(text, True, text_col)
    screen.blit(words_MM, (x_MM, y_MM))
def reset_StopWatch():
    global Sec
    times.append(Sec)
    Sec = 0 

start_button_rect = pygame.Rect(800, 400, 400, 100)
end_button_rect = pygame.Rect(800, 600, 400, 100)

def main_menu():
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and start_button_rect.collidepoint(event.pos):
                    K1_V1_map()
                if event.button == 1 and end_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        screen.blit(main_menu_bg, main_menu_bg_rect)
        # Draw "Start" button
        pygame.draw.rect(screen, WHITE, start_button_rect, 10)
        pygame.draw.rect(screen, WHITE, end_button_rect, 10)

        # Display title
        Main_M_text("V1 Racers", text_font, (255, 255, 255), 500, 100)
        Main_M_text2("Quit", text_font2, (255, 255, 255), 900, 590)
        Main_M_text2("Start", text_font2, (255, 255, 255), 900, 390)



        pygame.display.flip()
        clock.tick(FPS)

def K1_V1_map():
    global times, tick_counter, Sec, Vaild_Lap

    clock = pygame.time.Clock()

    # Load car image
    car_image = pygame.image.load("V1_e46_M3.png")
    car_image = pygame.transform.rotate(car_image, -90)

    # Load background image
    background_image = pygame.image.load("carbg.png")  # Replace "background.jpg" with your image file
    background_rect = background_image.get_rect()

    #Setup Stopwatch start/restart
    stopwatchblock = [
    pygame.Rect(1412, 783, 37, 160)
    ]

    # Obstacles
    obstacles = [
    pygame.Rect(1725, 630, 111, 110),
    pygame.Rect(1404, 519, 34, 27),
    pygame.Rect(1665, 208, 113, 92),
    pygame.Rect(856, 350, 50, 288),
    pygame.Rect(730, 488, 79, 152),
    pygame.Rect(310, 210, 228, 211),
    pygame.Rect(1170, 21, 382, 65),
    pygame.Rect(1220, 92, 199, 83),
    pygame.Rect(900, 8, 118, 38),
    pygame.Rect(531, 177, 181, 74),
    pygame.Rect(189, 415, 218, 242),
    ]

    #Create a font object
    font = pygame.font.Font(None, 36)

    # Car properties
    car_x, car_y = 1392, 870
    car_speed = 0
    car_angle = 0

    DRIFT_MULTIPLIER = 0.8
    DRIFT_TURN_SPEED = 2.0
    DRIFT_FRICTION = 0.1
    DRIFT_SLIDE_FACTOR = 0.5
    CAR_LENGTH = CAR_HEIGHT

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            main_menu()

        # Acceleration and friction
        if keys[pygame.K_w]:
            car_speed += ACCELERATION
        else:
            car_speed -= FRICTION if car_speed > 0 else -FRICTION
            car_speed = max(0, car_speed)
        if keys[pygame.K_s]:
            car_speed -= ACCELERATION * 1.5

        # Turning
        if keys[pygame.K_a]:
            car_angle += TURN_SPEED
        if keys[pygame.K_d]:
            car_angle -= TURN_SPEED

        # Update car position
        car_x += car_speed * math.cos(math.radians(car_angle))
        car_y -= car_speed * math.sin(math.radians(car_angle))

        if car_x >= 2000:
            car_x = 1975
            car_speed = 0
        elif car_x <= 0:
            car_x = 25
            car_speed = 0
        if car_y >= 1000:
            car_y = 975
            car_speed = 0
        elif car_y <= 0:
            car_y = 25
            car_speed = 0

        #increace tickcounter   
        tick_counter += 1
        # count seconds
        if tick_counter == 100:
            Sec += 1
            print("cycle complete")
            print("Your Times Are:", times)
            print("Your Last Score:", YLS)
            print("Your High Score:", lowest_num)
            print("Time Elapsed:", Sec)
            tick_counter = 0

        lowest_num = min(times)
        high_Score.append(lowest_num) 
            
        NTT = len(times) - 1
        YLS = times[NTT]

        lowest_num = min(times)
        high_Score.append(lowest_num) 

            #Create a text suface
        info_text = f"Time Elapsed: {Sec} seconds"
        info_surface = font.render(info_text, True, WHITE)
        
        info_text2 = f"High Score: {lowest_num}"
        info_surface2 = font.render(info_text2, True, WHITE)

        #Rect object for words
        info_rect = info_surface.get_rect()
        info_rect2 = info_surface2.get_rect()

        # deleting a fake times
        times = [x for x in times if x >= 5]

        #set Words postion
        info_rect.topleft = (10, 10)
        info_rect2.topleft = (10, 46)


        # Check collisions with obstacles
        car_rect = pygame.Rect(car_x, car_y, CAR_WIDTH, CAR_HEIGHT)
        for obstacle in obstacles:
            if car_rect.colliderect(obstacle):
                car_speed = 0.5
                Vaild_Lap = False
        if Vaild_Lap == False:
            info_surface = font.render(info_text, True, RED)
            YLS = 100
        for obstacle in stopwatchblock:
            if car_rect.colliderect(obstacle):
                reset_StopWatch()
                Vaild_Lap = True



        # Draw background
        screen.blit(background_image, background_rect)

        # Rotate car image
        rotated_car = pygame.transform.rotate(car_image, car_angle)

        # Draw car
        screen.blit(rotated_car, (car_x - rotated_car.get_width() / 2, car_y - rotated_car.get_height() / 2))

        # Draw obstacles
        for obstacle in obstacles:
            pygame.draw.rect(screen, WHITE, obstacle)

        #Draw Words
        screen.blit(info_surface, info_rect)
        screen.blit(info_surface2, info_rect2)

        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)
main_menu()