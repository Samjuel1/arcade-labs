import arcade

arcade.open_window(800, 600, "Drawing Example")

arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0, 800, 600, 0, arcade.color.SKY_BLUE)

arcade.draw_circle_filled(400, -1500, 1650, (53,104,45),1000,500)

arcade.draw_lrtb_rectangle_filled(275,525,350,100, (247,105,97))

arcade.draw_lrtb_rectangle_filled(105,155,180,100,(255,223,196))

arcade.draw_lrtb_rectangle_outline(105,155,180,100,(0,0,0),2)

arcade.draw_circle_filled(130,208,35,(255,223,196))

arcade.draw_circle_outline(130,208,35,(0,0,0),2)

arcade.draw_circle_filled(118,215,8,(255,255,255))

arcade.draw_circle_outline(118,215,8,(0,0,0))

arcade.draw_circle_filled(142,215,8,(255,255,255))

arcade.draw_circle_outline(142,215,8,(0,0,0))

arcade.draw_circle_filled(118,215,4,(0,170,228),350,1000)

arcade.draw_circle_filled(118,215,3,(0,0,0))

arcade.draw_circle_filled(142,215,4,(0,170,228),350,1000)

arcade.draw_circle_filled(142,215,3,(0,0,0))

arcade.draw_arc_outline(130,200,100,100,(255,0,0),90,0,50)

arcade.draw_arc_filled(130,199,30,30,(255,0,0),0,180,180)

arcade.draw_lrtb_rectangle_filled(129,131,210,204,(161,130,98))

arcade.finish_render()
arcade.run()