import arcade
import math
#hecho por chatgpt
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


def draw_elmo():
    # Eyes
    arcade.draw_circle_filled(400, 400, 55, arcade.color.BLACK)
    arcade.draw_circle_filled(200, 400, 55, arcade.color.BLACK)
    arcade.draw_circle_filled(400, 400, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(200, 400, 50, arcade.color.WHITE)
    # Nose
    arcade.draw_ellipse_filled(300, 300, 130, 210, arcade.color.BLACK)
    arcade.draw_ellipse_filled(300, 300, 120, 200, arcade.color.ORANGE)


def draw_pupilas(x1, y1, x2, y2):
    # Pupils
    arcade.draw_circle_filled(x1, y1, 25, arcade.color.BLACK)
    arcade.draw_circle_filled(x2, y2, 25, arcade.color.BLACK)


# Variables
pupila_centro_derecha = (400, 400)  # Center of the right eye
pupila_centro_izquierda = (200, 400)  # Center of the left eye
radius_x = 18  # Horizontal radius of the eye movement
radius_y = 15  # Vertical radius (to match eye shape)
angle = 0  # Angle for circular motion
direction = 1  # 1 = Right, -1 = Left
speed = 0.05  # Speed of the movement


def on_draw(delta_time):
    global angle, direction

    arcade.start_render()
    draw_elmo()

    # Move pupils along a circular path that hugs the edges of the eyes
    pupila_derecha_x = pupila_centro_derecha[0] + math.sin(angle) * radius_x
    pupila_derecha_y = pupila_centro_derecha[1] + math.cos(angle) * radius_y

    pupila_izquierda_x = pupila_centro_izquierda[0] + math.sin(angle) * radius_x
    pupila_izquierda_y = pupila_centro_izquierda[1] + math.cos(angle) * radius_y

    draw_pupilas(pupila_derecha_x, pupila_derecha_y, pupila_izquierda_x, pupila_izquierda_y)

    arcade.finish_render()

    # Update angle to create smooth motion
    angle += speed * direction

    # Reverse direction when reaching limits
    if angle >= math.pi / 2 or angle <= -math.pi / 2:
        direction *= -1  # Change direction


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Draw Elmo")
    arcade.set_background_color(arcade.color.RED)
    arcade.schedule(on_draw, 1 / 60)  # Smoother animation
    arcade.run()


main()
