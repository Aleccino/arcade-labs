import arcade


def draw_elmo():
    # Ojos
    arcade.draw_circle_filled(400, 400, 55, arcade.color.BLACK)
    arcade.draw_circle_filled(200, 400, 55, arcade.color.BLACK)
    arcade.draw_circle_filled(400, 400, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(200, 400, 50, arcade.color.WHITE)
    # Nariz
    arcade.draw_ellipse_filled(300, 300, 130, 210, arcade.color.BLACK)
    arcade.draw_ellipse_filled(300, 300, 120, 200, arcade.color.ORANGE)

def draw_pupilas(x1, x2, y):
    # Pupilas
    arcade.draw_circle_filled(x1, y, 25, arcade.color.BLACK)
    arcade.draw_circle_filled(x2, y, 25, arcade.color.BLACK)

# Variables
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
pupilaDerecha = 370
pupilaIzquierda = 170
pupilaY = 400
direction_x = 1  # 1 = Derecha, -1 = Izquierda
movement_counter = 0  # Contador
MOVEMENT_LIMIT = 60  # Número de frames que se mueve hasta girar

def on_draw(delta_time):
    global pupilaDerecha, pupilaIzquierda, direction_x, movement_counter

    arcade.start_render()
    draw_elmo()

    if movement_counter < MOVEMENT_LIMIT:
        pupilaDerecha += direction_x
        pupilaIzquierda += direction_x
        movement_counter += 1
    else:
        direction_x *= -1  # Reverse
        movement_counter = 0  # Reset

    draw_pupilas(pupilaDerecha, pupilaIzquierda, pupilaY)
    arcade.finish_render()

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Draw Elmo")
    arcade.set_background_color(arcade.color.RED)
    arcade.schedule(on_draw, 1/50)
    arcade.run()

main()
