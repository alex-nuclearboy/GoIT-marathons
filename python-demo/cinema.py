import turtle

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800

HEADER_HEIGHT_OFFSET = 250
TURTLE_WIDTH_OFFSET = -50

DIAMETER = 50
OFFSET = 25

COLUMNS = 15
ROWS = 7

MAIN_WINDOW = None
SEATS = []

BKG_COLOR = "#F3F5BB"
FREE_SEAT_COLOR = "#29A006"
SOLD_SEAT_COLOR = "#ED1D1A"
PEN_COLOR = "#EDB31A"

main_pen = turtle.Turtle()
main_pen.shape('blank')

main_text = turtle.Turtle()
main_text.shape('blank')

screen_text = turtle.Turtle()
screen_text.shape('blank')


def setup_window():
    main_window = turtle.Screen()
    main_window.title("GOIT CINEMA")
    main_window.setworldcoordinates(
        0, main_window.window_height(), main_window.window_width(), 0)
    main_window.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
    main_window.bgcolor(BKG_COLOR)

    return main_window


def draw_cinema_screen(main_window):
    main_window.tracer(False)

    screen_width = 0.8 * WINDOW_WIDTH
    screen_height = 0.1 * HEADER_HEIGHT_OFFSET
    screen_start_x = (WINDOW_WIDTH - screen_width) / 2 - 120
    screen_start_y = (HEADER_HEIGHT_OFFSET - screen_height) / 2 - 80

    main_pen.penup()
    main_pen.setpos(screen_start_x, screen_start_y)
    main_pen.pendown()
    main_pen.fillcolor("#c0c0c0")
    main_pen.begin_fill()

    for _ in range(2):
        main_pen.forward(screen_width)
        main_pen.left(90)
        main_pen.forward(screen_height)
        main_pen.left(90)

    main_pen.end_fill()

    text_x = WINDOW_WIDTH / 2 - 150
    text_y = 60
    screen_text.penup()
    screen_text.setpos(text_x, text_y)
    screen_text.color("black")
    screen_text.write("SCREEN", align="center", font=("vergana", 18))

    main_window.tracer(True)


def text_printer(main_window):
    main_window.tracer(False)
    main_text.clear()

    total_seats = COLUMNS * ROWS

    sold_count = sum(1 for line in SEATS for _, _, state in line if state)

    free_seats = total_seats - sold_count

    display_data = [
        ("Seats amount:", total_seats, 130),
        ("Sold:", sold_count, 170),
        ("Free:", free_seats, 210)
    ]

    for text, count, pos_y in display_data:
        main_text.penup()
        main_text.setpos(-80, pos_y)
        main_text.pendown()
        main_text.write(f"{text} {count}", font=("vergana", 25))

    main_window.tracer(True)


def draw_seat(main_window, pos_x, pos_y, pen_color, fill_color):
    main_window.tracer(False)

    main_pen.pencolor(pen_color)
    main_pen.fillcolor(fill_color)
    main_pen.begin_fill()

    main_pen.penup()
    render_pos_x = TURTLE_WIDTH_OFFSET + pos_x * (DIAMETER + OFFSET)
    render_pos_y = pos_y * (DIAMETER + OFFSET) + HEADER_HEIGHT_OFFSET
    main_pen.setpos(render_pos_x, render_pos_y)
    main_pen.pendown()
    main_pen.circle(DIAMETER // 2)
    main_pen.end_fill()

    main_window.tracer(True)

    return (render_pos_x, render_pos_y)


def vec_len(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def on_click(x, y, order):
    for row in range(ROWS):
        for column in range(COLUMNS):
            place_x, place_y, _ = SEATS[row][column]
            if vec_len(x, y, place_x, place_y) <= DIAMETER // 2:
                if order:
                    color = SOLD_SEAT_COLOR
                else:
                    color = FREE_SEAT_COLOR
                draw_seat(MAIN_WINDOW, column, row, PEN_COLOR, color)
                SEATS[row][column] = (place_x, place_y, order)
                
                text_printer(MAIN_WINDOW)


def on_click_mouse_1(x, y):
    on_click(x, y, order=True)


def on_click_mouse_2(x, y):
    on_click(x, y, order=False)


def main():
    global MAIN_WINDOW

    MAIN_WINDOW = setup_window()

    draw_cinema_screen(MAIN_WINDOW)

    for y in range(ROWS):
        SEATS.append([])
        for x in range(COLUMNS):
            render_pos_x, render_pos_y = draw_seat(
                MAIN_WINDOW, x, y, PEN_COLOR, FREE_SEAT_COLOR)
            SEATS[y].append((render_pos_x, render_pos_y, False))

    text_printer(MAIN_WINDOW)

    MAIN_WINDOW.onclick(on_click_mouse_1, btn=1)
    MAIN_WINDOW.onclick(on_click_mouse_2, btn=3)

    MAIN_WINDOW.mainloop()


if __name__ == "__main__":
    main()
