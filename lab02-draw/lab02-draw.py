import arcade

arcade.open_window(width=600, height=600, window_title="Draw Elmo")

arcade.set_background_color(arcade.color.RED)

arcade.start_render()

#Ojos
arcade.draw_circle_filled(400, 400, 55, arcade.color.BLACK)
arcade.draw_circle_filled(200, 400, 55, arcade.color.BLACK)
arcade.draw_circle_filled(400, 400, 50, arcade.color.WHITE)
arcade.draw_circle_filled(200, 400, 50, arcade.color.WHITE)
#Pupilas
arcade.draw_circle_filled(380, 380, 25, arcade.color.BLACK)
arcade.draw_circle_filled(220, 380, 25, arcade.color.BLACK)
#Nariz
arcade.draw_ellipse_filled(center_x=300 , center_y= 300, width=130 , height=210 , color= arcade.color.BLACK)
arcade.draw_ellipse_filled(center_x=300 , center_y= 300, width=120 , height=200 , color= arcade.color.ORANGE)





arcade.finish_render()
arcade.run()