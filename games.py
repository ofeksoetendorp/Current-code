class Games:

    def snake(self):
        import turtle
        import random

        w = 500
        h = 500
        food_size = 10
        delay = 100

        offsets = {
            "up": (0, 20),
            "down": (0, -20),
            "left": (-20, 0),
            "right": (20, 0)
        }

        def reset():
            global snake, snake_dir, food_position, pen
            snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
            snake_dir = "up"
            food_position = get_random_food_position()
            food.goto(food_position)
            move_snake()

        def move_snake():
            global snake_dir

            new_head = snake[-1].copy()
            new_head[0] = snake[-1][0] + offsets[snake_dir][0]
            new_head[1] = snake[-1][1] + offsets[snake_dir][1]

            if new_head in snake[:-1]:
                reset()
            else:
                snake.append(new_head)

                if not food_collision():
                    snake.pop(0)

                if snake[-1][0] > w / 2:
                    snake[-1][0] -= w
                elif snake[-1][0] < - w / 2:
                    snake[-1][0] += w
                elif snake[-1][1] > h / 2:
                    snake[-1][1] -= h
                elif snake[-1][1] < -h / 2:
                    snake[-1][1] += h

                pen.clearstamps()

                for segment in snake:
                    pen.goto(segment[0], segment[1])
                    pen.stamp()

                screen.update()

                turtle.ontimer(move_snake, delay)

        def food_collision():
            global food_position
            if get_distance(snake[-1], food_position) < 20:
                food_position = get_random_food_position()
                food.goto(food_position)
                return True
            return False

        def get_random_food_position():
            x = random.randint(- w / 2 + food_size, w / 2 - food_size)
            y = random.randint(- h / 2 + food_size, h / 2 - food_size)
            return (x, y)

        def get_distance(pos1, pos2):
            x1, y1 = pos1
            x2, y2 = pos2
            distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
            return distance

        def go_up():
            global snake_dir
            if snake_dir != "down":
                snake_dir = "up"

        def go_right():
            global snake_dir
            if snake_dir != "left":
                snake_dir = "right"

        def go_down():
            global snake_dir
            if snake_dir != "up":
                snake_dir = "down"

        def go_left():
            global snake_dir
            if snake_dir != "right":
                snake_dir = "left"

        screen = turtle.Screen()
        screen.setup(w, h)
        screen.title("Snake")
        screen.bgcolor("blue")
        screen.setup(500, 500)
        screen.tracer(0)

        pen = turtle.Turtle("square")
        pen.penup()

        food = turtle.Turtle()
        food.shape("square")
        food.color("yellow")
        food.shapesize(food_size / 20)
        food.penup()

        screen.listen()
        screen.onkey(go_up, "Up")
        screen.onkey(go_right, "Right")
        screen.onkey(go_down, "Down")
        screen.onkey(go_left, "Left")

        reset()
        turtle.done()


    def tictactoe(self):
        print(20 * ' ', "   reference:    ")
        print(20 * ' ', '     |    |      ')
        print(20 * ' ', '  1  | 2  | 3    ')
        print(20 * ' ', "-----+----+----- ")
        print(20 * ' ', "     |    |      ")
        print(20 * ' ', "  4  | 5  | 6    ")
        print(20 * ' ', "-----+----+----- ")
        print(20 * ' ', "     |    |      ")
        print(20 * ' ', "  7  | 8  | 9    \n")

        def display_board():
            print()
            print('                               reference:')
            print('     |    |     ', 10 * ' ', '     |    |   ', )
            print('  ' + board[1] + '  | ' + board[2] + '  | ' + board[3] + '   ', 10 * ' ', '  1  | 2  | 3  ')
            print('-----+----+-----', 10 * ' ', "-----+----+-----")
            print('     |    |     ', 10 * ' ', "     |    |     ")
            print('  ' + board[4] + '  | ' + board[5] + '  | ' + board[6] + '   ', 10 * ' ', "  4  | 5  | 6   ")
            print('-----+----+-----', 10 * ' ', "-----+----+-----")
            print('     |    |     ', 10 * ' ', "     |    |      ")
            print('  ' + board[7] + '  | ' + board[8] + '  | ' + board[9] + '   ', 10 * ' ', "  7  | 8  | 9    \n\n")

        def human_input(mark):
            while True:
                inp = input(f"[HUMAN] '{mark}' Enter your choice:")
                if inp.isdigit() and int(inp) < 10 and int(inp) > 0:
                    inp = int(inp)
                    if board[inp] == " ":
                        return inp
                    else:
                        print(f"[HUMAN] '{mark}' place already taken.")
                else:
                    print(f"[HUMAN] '{mark}' Enter valid option (1 - 9).")

        def winning(mark, board):
            winning_place = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
            for win_place in winning_place:
                if board[win_place[0]] == board[win_place[1]] == board[win_place[2]] == mark:
                    return True

        def win_move(i, board, mark):
            temp_board = list(board)
            temp_board[i] = mark
            if winning(mark, temp_board):
                return True
            else:
                return False

        def cpu_input(cpu, human, board):
            for i in range(1, 10):
                if board[i] == ' ' and win_move(i, board, cpu):
                    return i
            for i in range(1, 10):
                if board[i] == ' ' and win_move(i, board, human):
                    return i
            for i in [5, 1, 7, 3, 2, 9, 8, 6, 4]:
                if board[i] == ' ':
                    return i

        def new_game():
            while True:
                nxt = input('[HUMAN] Do you want to play again?(y/n):')
                if nxt in ['y', 'Y']:
                    again = True
                    break
                elif nxt in ['n', 'N']:
                    again = False
                    break
                else:
                    print('Enter correct input')
            if again:
                print('__________NEW GAME__________')
                main_game()
            else:
                return False

        def win_check(human, cpu):
            winning_place = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
            for win_place in winning_place:
                if board[win_place[0]] == board[win_place[1]] == board[win_place[2]] == human:
                    print('[HUMAN] wins the match!')
                    if not new_game():
                        return False
                elif board[win_place[0]] == board[win_place[1]] == board[win_place[2]] == cpu:
                    print('[CPU] wins the match!')
                    if not new_game():
                        return False
            if ' ' not in board:
                print('MATCH DRAW!!')
                if not new_game():
                    return False
            return True

        def user_choice():
            while True:
                inp = input('[HUMAN]Choose your mark[x/o]: ')
                if inp in ['x', 'X']:
                    print('[HUMAN]You choose "X".\n[HUMAN]You play first.')
                    return 'x', 'o'
                elif inp in ['O', 'o']:
                    print('[HUMAN] You choose "O".\n[HUMAN] CPU plays first.')
                    return 'o', 'x'
                else:
                    print('[HUMAN] Enter correct input!')

        def main_game():
            global board
            play = True
            board = ['', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            human, cpu = user_choice()
            display_board()
            while play:
                if human == 'x':
                    x = human_input(human)
                    board[x] = human
                    display_board()
                    play = win_check(human, cpu)
                    if play:
                        o = cpu_input(cpu, human, board)
                        print(f'[CPU] Entered:{o}')
                        board[o] = cpu
                        display_board()
                        play = win_check(human, cpu)
                else:
                    x = cpu_input(cpu, human, board)
                    print(f'[CPU] Entered:{x}')
                    board[x] = cpu
                    display_board()
                    play = win_check(human, cpu)
                    if play:
                        o = human_input(human)
                        board[o] = human
                        display_board()
                        play = win_check(human, cpu)

        main_game()
    def pong(self):
        import turtle

        wn = turtle.Screen()
        wn.title("Pong")
        wn.bgcolor("black")
        wn.setup(width=800, height=600)
        wn.tracer()

        # paddle A
        paddle_a = turtle.Turtle()
        paddle_a.speed(0)
        paddle_a.shape("square")
        paddle_a.color("white")
        paddle_a.shapesize(stretch_wid=5, stretch_len=1)
        paddle_a.penup()
        paddle_a.goto(-350, 0)

        # bot paddle
        paddle_b = turtle.Turtle()
        paddle_b.speed(0)
        paddle_b.shape("square")
        paddle_b.color("white")
        paddle_b.shapesize(stretch_wid=5, stretch_len=1)
        paddle_b.penup()
        paddle_b.goto(350, 0)

        # ball
        ball = turtle.Turtle()
        ball.speed(0)
        ball.shape("circle")
        ball.color("white")
        ball.penup()
        ball.goto(0, 0)
        ball.dx = 8
        ball.dy = 8

        # paddle movement
        def paddle_a_up():
            y = paddle_a.ycor()
            y += 20
            paddle_a.sety(y)

        def paddle_a_down():
            y = paddle_a.ycor()
            y += -20
            paddle_a.sety(y)

        # keyboard binding
        wn.listen()
        wn.onkeypress(paddle_a_up,"w")
        wn.onkeypress(paddle_a_down,"s")

        # score
        score_a = 0
        score_b = 0

        # scoring
        pen = turtle.Turtle()
        pen.speed(0)
        pen.color("white")
        pen.penup()
        pen.hideturtle()
        pen.goto(0, 260)
        pen.write("Human : 0   Bot : 0", align="center",
                  font=("courier", 24, "normal"))

        # bot
        def bot():
            if ball.xcor() > 0 and ball.dx == 8:
                paddle_b.goto(350, ball.ycor())
            else:
                pass





        while True:
            wn.update()

            # move the ball
            ball.setx(ball.xcor() + ball.dx)

            ball.sety(ball.ycor() + ball.dy)

            bot()

            # border
            if ball.ycor() > 290:
                ball.sety(290)
                ball.dy *= -1

            if ball.ycor() < -290:
                ball.sety(-290)
                ball.dy *= -1

            if ball.xcor() > 390:
                ball.goto(0, 0)
                ball.dx *= -1
                score_a += 1
                pen.clear()
                pen.write(f"Human : {score_a}   Bot : {score_b} ",
                          align="center", font=("courier", 24, "normal"))

            if ball.xcor() < -390:
                ball.goto(0, 0)
                ball.dy *= -1
                score_b += 1
                pen.clear()
                pen.write(f"Human : {score_a}   Bot : {score_b} ",
                          align="center", font=("courier", 24, "normal"))

            # paddle and ball collision
            if (ball.xcor() > 340) and (ball.xcor() < 350) and (
                    ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() + 40 > paddle_b.ycor() - 40):
                ball.setx(340)
                ball.dx *= -1

            if (ball.xcor() < -340) and (ball.xcor() > -350) and (
                    ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() + 40 > paddle_a.ycor() - 40):
                ball.setx(-340)
                ball.dx *= -1

            # Maximum score is 15 but you can increase it here
            if score_a >= 15:
                break
            elif score_b >= 15:
                break
            else:
                continue
        turtle.done()

