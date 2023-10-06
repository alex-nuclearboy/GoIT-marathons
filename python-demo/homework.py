import turtle

SCREEN_WIDTH = 1200
SCREEN_HIGH = 800

main_turtle = turtle.Turtle()
main_turtle.shape("blank")


def setup_screen():
    main_screen = turtle.Screen()
    main_screen.title("Python Homework")
    main_screen.cv._rootwindow.resizable(False, False)
    main_screen.setup(SCREEN_WIDTH, SCREEN_HIGH)

    return main_screen


def draw_circle(main_screen, pos_x, pos_y, pen_color, fill_color):
    main_screen.tracer(False)

    main_turtle.pencolor(pen_color)
    main_turtle.fillcolor(fill_color)
    main_turtle.pendown()

    main_turtle.begin_fill()

    main_turtle.penup()
    main_turtle.setposition(pos_x, pos_y)
    main_turtle.pendown()

    main_turtle.circle(50)

    main_turtle.end_fill()

    main_screen.tracer(True)


def main():
    main_screen = setup_screen()
    draw_circle(main_screen, 350, 200, "#ffb900", "#0000FF")
    draw_circle(main_screen, -350, 200, "#ffb900", "#0000FF")
    draw_circle(main_screen, 350, -200, "#ffb900", "#0000FF")

    # main_screen.onclick()

    main_screen.mainloop()


if __name__ == "__main__":
    main()
