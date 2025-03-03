import arcade

arcade.open_window(600, 600, "Drawing Example")

arcade.set_background_color((arcade.csscolor.SKY_BLUE))
arcade.start_render()

arcade.draw_lrbt_rectangle_filled(0, 599, 0, 300, arcade.csscolor.GREEN)

arcade.draw_rect_filled(100, 320, arcade.csscolor.SIENNA)

arcade.finish_render()
arcade.run()