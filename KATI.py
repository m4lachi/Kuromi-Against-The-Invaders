import glfw
from OpenGL.GL import *
import time
import math
import random

# Initialize game state variables
level = 1
max_levels = 3 
enemy_speed = 0.20  
speed_increase = 0.05 

# Initialize player position at the bottom of the screen
px, py = 400, 570
scaleFactor =.35

# Initialize bullet properties
bullets = [] 
bullet_speed = 5

# Initialize enemy properties at the top of the screen
num_rows = 4
num_columns = 12
enemy_speed = .25

def draw_rect(x, y, width, height):
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)
    glEnd()

def draw_player():
    # Draw the face
    glColor3f(1, 1, 1) 
    draw_rect(px-40*scaleFactor, py-110*scaleFactor, 120*scaleFactor, 80*scaleFactor)
    
    #draw outline
    glColor3f(0, 0, 0) 
    draw_rect(px - 30*scaleFactor, py-120*scaleFactor, 100*scaleFactor, 10*scaleFactor)
    glColor3f(0, 0, 0) 
    draw_rect(px-40*scaleFactor, py-110*scaleFactor, 20*scaleFactor, 10*scaleFactor)
    glColor3f(0, 0, 0) 
    draw_rect(px+60*scaleFactor, py-110*scaleFactor, 20*scaleFactor, 10*scaleFactor)
    glColor3f(0, 0, 0) 
    draw_rect(px-50*scaleFactor, py-100*scaleFactor, 20*scaleFactor, 40*scaleFactor)
    glColor3f(0, 0, 0) 
    draw_rect(px+70*scaleFactor, py-100*scaleFactor, 20*scaleFactor, 40*scaleFactor)
    glColor3f(0, 0, 0) 
    draw_rect(px+60*scaleFactor, py-60*scaleFactor, 50*scaleFactor, 10*scaleFactor)
    glColor3f(0, 0, 0) 
    draw_rect(px-70*scaleFactor, py-60*scaleFactor, 50*scaleFactor, 10*scaleFactor)
    glColor3f(0, 0, 0) 
    draw_rect(px+10*scaleFactor, py-60*scaleFactor, 20*scaleFactor, 10*scaleFactor)
    glColor3f(0, 0, 0) 
    draw_rect(px-80*scaleFactor, py-50*scaleFactor, 200*scaleFactor, 40*scaleFactor)
    glColor3f(0, 0, 0) 
    draw_rect(px-90*scaleFactor, py-10*scaleFactor, 60*scaleFactor, 10*scaleFactor)
    glColor3f(0, 0, 0) 
    draw_rect(px+70*scaleFactor, py-10*scaleFactor, 60*scaleFactor, 10*scaleFactor)
    glColor3f(0, 0, 0) 
    draw_rect(px-100*scaleFactor, py+.01*scaleFactor, 40*scaleFactor, 10*scaleFactor)
    glColor3f(0, 0, 0) 
    draw_rect(px+100*scaleFactor, py+.01*scaleFactor, 40*scaleFactor, 10*scaleFactor)
    glColor3f(0, 0, 0) 
    draw_rect(px+130*scaleFactor, py+10*scaleFactor, 20*scaleFactor, 20*scaleFactor)
    glColor3f(0, 0, 0) 
    draw_rect(px-110*scaleFactor, py+10*scaleFactor, 20*scaleFactor, 20*scaleFactor)

    #Draw eyes
    glColor3f(0, 0, 0) 
    draw_rect(px-10*scaleFactor, py-90*scaleFactor, 10*scaleFactor, 10*scaleFactor)
    glColor3f(0, 0, 0) 
    draw_rect(px-20*scaleFactor, py-80*scaleFactor, 20*scaleFactor, 10*scaleFactor)
    glColor3f(0, 0, 0) 
    draw_rect(px+40*scaleFactor, py-90*scaleFactor, 10*scaleFactor, 10*scaleFactor)
    glColor3f(0, 0, 0) 
    draw_rect(px+40*scaleFactor, py-80*scaleFactor, 20*scaleFactor, 10*scaleFactor)

    #draw nose
    glColor3f(0.8, 0.6, 0.9) 
    draw_rect(px+10*scaleFactor, py-100*scaleFactor, 20*scaleFactor, 10*scaleFactor)

    #draw Symbol
    glColor3f(0.8, 0.6, 0.9) 
    draw_rect(px+10*scaleFactor, py-50*scaleFactor, 20*scaleFactor, 10*scaleFactor)
    glColor3f(0.8, 0.6, 0.9) 
    draw_rect(px+1*scaleFactor, py-40*scaleFactor, 40*scaleFactor, 20*scaleFactor)

def draw_bullets():
    glColor3f(0.8, 0.6, 0.9)  
    for bullet_x, bullet_y in bullets:
        draw_rect(bullet_x, bullet_y, 3, 10)

def draw_enemy(enemy_x, enemy_y):
    
    glColor3f(1.0, 0.4, 0.4)  
    draw_rect(enemy_x, enemy_y, 20, 20)

    glColor3f(1, 1, 1)
    draw_rect(enemy_x+12.5, enemy_y+10.5, 5, 2.5)
    draw_rect(enemy_x+2.5, enemy_y+10.5, 5, 2.5)
    draw_rect(enemy_x+2.5, enemy_y+8, 2.5, 2.5)
    draw_rect(enemy_x+15, enemy_y+8, 2.5, 2.5)
    draw_rect(enemy_x+5, enemy_y+12.5, 2.5, 2.5)
    draw_rect(enemy_x+12.5, enemy_y+12.5, 2.5, 2.5)

def reset_enemies():
    global enemies, num_rows, num_columns, level

    if level <= 5:
        increase_speed()
        return square_formation()
    elif level >5 and level <=8:
        increase_speed()
        return heart_formation()
    elif level >= 9:
        increase_speed()
        return pyramid_formation()

def increase_speed():
    global enemy_speed
    enemy_speed += speed_increase

def pyramid_formation():
    formations = []
    pyramid_size = 15

    formations.append([(j * 2 * pyramid_size + 100, i * pyramid_size + 50) for j in range(3) for i in range(3)])
    formations.append([(j * 2 * pyramid_size + 200, i * pyramid_size + 50) for j in range(3) for i in range(3)])
    formations.append([(j * 2 * pyramid_size + 300, i * pyramid_size + 50) for j in range(3) for i in range(3)])
    formations.append([(j * 2 * pyramid_size + 400, i * pyramid_size + 50) for j in range(3) for i in range(3)])
    formations.append([(j * 2 * pyramid_size + 500, i * pyramid_size + 50) for j in range(3) for i in range(3)])
    formations.append([(j * 2 * pyramid_size + 600, i * pyramid_size + 50) for j in range(3) for i in range(3)])

    formations.append([(j * 2 * pyramid_size + 150, i * pyramid_size + 150) for j in range(3) for i in range(3)])
    formations.append([(j * 2 * pyramid_size + 250, i * pyramid_size + 150) for j in range(3) for i in range(3)])
    formations.append([(j * 2 * pyramid_size + 350, i * pyramid_size + 150) for j in range(3) for i in range(3)])
    formations.append([(j * 2 * pyramid_size + 450, i * pyramid_size + 150) for j in range(3) for i in range(3)])
    formations.append([(j * 2 * pyramid_size + 550, i * pyramid_size + 150) for j in range(3) for i in range(3)])

    formations.append([(j * 2 * pyramid_size + 200, i * pyramid_size + 250) for j in range(3) for i in range(3)])
    formations.append([(j * 2 * pyramid_size + 300, i * pyramid_size + 250) for j in range(3) for i in range(3)])
    formations.append([(j * 2 * pyramid_size + 400, i * pyramid_size + 250) for j in range(3) for i in range(3)])
    formations.append([(j * 2 * pyramid_size + 500, i * pyramid_size + 250) for j in range(3) for i in range(3)])

    return formations

def heart_formation():
    enemies = []

    for t in range(0, 360, 10):
        # Parametric equations for a heart shape
        x = 10 *16 * math.sin(math.radians(t))**3
        y = 10 * (13 * math.cos(math.radians(t)) - 5 * math.cos(2 * math.radians(t)) - 2 * math.cos(3 * math.radians(t)) - math.cos(4 * math.radians(t)))
        
        # Offset to center the heart on the screen
        x_offset = 400
        y_offset = 100

        enemies.append((x + x_offset, -y + y_offset))

    for t in range(0, 360, 20):
        # Parametric equations for a heart shape
        x = 4 *16 * math.sin(math.radians(t))**3
        y = 4 * (13 * math.cos(math.radians(t)) - 5 * math.cos(2 * math.radians(t)) - 2 * math.cos(3 * math.radians(t)) - math.cos(4 * math.radians(t)))
        
        # Offset to center the heart on the screen
        x_offset = 100
        y_offset = 125

        enemies.append((x + x_offset, -y + y_offset))

    for t in range(0, 360, 20):
        # Parametric equations for a heart shape
        x = 4 *16 * math.sin(math.radians(t))**3
        y = 4 * (13 * math.cos(math.radians(t)) - 5 * math.cos(2 * math.radians(t)) - 2 * math.cos(3 * math.radians(t)) - math.cos(4 * math.radians(t)))
        
        # Offset to center the heart on the screen
        x_offset = 700
        y_offset = 125

        enemies.append((x + x_offset, -y + y_offset))

    return [enemies]

def square_formation():
    enemies = []

    for i in range(num_rows):
        for j in range(num_columns):
            enemy_x = j * 60 + 50
            enemy_y = i * 80 + 25
            enemies.append((enemy_x, enemy_y))

    return [enemies]

enemies = square_formation()

def collision(obj1, obj2):
    return (
        obj1[0] < obj2[0] + 20 and
        obj1[0] + 40 > obj2[0] and
        obj1[1] < obj2[1] + 20 and
        obj1[1] + 10 > obj2[1]
    )

def key_callback(window, key, scancode, action, mods):
    global bullets, px, py

    if action == glfw.PRESS:
        if key == glfw.KEY_A and px > 0:
            px -= 20
        elif key == glfw.KEY_D and px < 760:
            px += 20
        elif key == glfw.KEY_SPACE:
            bullets.append((px+5, py-50))

def game_loop():
    global bullets, enemies, px, py, level

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        draw_player()

        all_enemies_killed = all(not enemies[i] for i in range(len(enemies)))

        if all_enemies_killed:
            level += 1
            print(f"Level {level}")
            increase_speed()
            enemies = reset_enemies()

        for i in range(len(enemies)):
            for j in range(len(enemies[i])):
                enemy_x, enemy_y = enemies[i][j]
                draw_enemy(enemy_x, enemy_y)

        # Check if any enemy has passed the player
        for i in range(len(enemies)):
            for j in range(len(enemies[i])):
                enemy_x, enemy_y = enemies[i][j]
                if enemy_y + 20 > py:
                    print("Game Over! Enemy passed the player.")
                    glfw.set_window_should_close(window, True)

        # Check Collisions
        for i in range(len(enemies)):
            for j in reversed(range(len(enemies[i]))):
                for k in reversed(range(len(bullets))):
                    if collision(bullets[k], enemies[i][j]):
                        enemies[i].pop(j)
                        bullets.pop(k)
                        break
        

        bullets = [bullet for bullet in bullets if bullet[1] > 0]  # Remove bullets on hit and those out of the screen

        # Update bullet positions
        updated_bullets = []
        for bullet_x, bullet_y in bullets:
            bullet_y -= bullet_speed
            if bullet_y > 0:
                updated_bullets.append((bullet_x, bullet_y))

        bullets = updated_bullets

        # Update enemy positions after collision and bullet updates
        for i in range(len(enemies)):
            for j in range(len(enemies[i])):
                enemy_x, enemy_y = enemies[i][j]
                enemies[i][j] = (enemy_x, enemy_y + enemy_speed)

        draw_bullets()

        glfw.swap_buffers(window)
        glfw.poll_events()
        time.sleep(0.02)

# Initialize GLFW
if not glfw.init():
    print("Failed to initialize GLFW")
    glfw.terminate()
    exit()

glfw.window_hint(glfw.MAXIMIZED, glfw.TRUE)

# Create a windowed mode window and its OpenGL context
window = glfw.create_window(1910, 1070, "Kuromi Against The Invaders", None, None)
if not window:
    print("Failed to create GLFW window")
    glfw.terminate()
    exit()

# Make the window's context current
glfw.make_context_current(window)

# Set the clear color
glClearColor(0.06, 0.08, 0.2, 0.5)

# Set the orthographic projection matrix
glOrtho(0, 800, 600, 0, -1, 1)

# Set the keyboard callback function
glfw.set_key_callback(window, key_callback)

# Run the game loop
game_loop()

# Terminate GLFW
glfw.terminate()
