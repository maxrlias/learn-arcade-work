# Import the "arcade" library
import arcade

# Open up a window.
arcade.open_window(600, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# Get ready to draw
arcade.start_render()

# Draw the ground
arcade.draw_lrbt_rectangle_filled(0, 600, 0, 300, arcade.csscolor.GREEN)

# Draw a tree trunk
arcade.draw_rectangle_filled(100, 320, 20, 60, arcade.csscolor.DARK_GREEN)

# Draw a house (brown rectangle outline)
arcade.draw_rectangle_outline(300, 300, 350, 200, arcade.csscolor.BROWN, 3)

# Draw an oval outline
arcade.draw_ellipse_outline(300, 300, 350, 200, arcade.csscolor.RED, 3)

# Finish drawing
arcade.finish_render()

# Keep the window open
arcade.run()
