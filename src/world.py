import random


class World:

    UP = 0
    LEFT = 1
    DOWN = 2
    RIGHT = 3


    def __init__(self, stdscr):
        self.__width = (stdscr.getmaxyx()[1] - 10) // 2
        self.__height = stdscr.getmaxyx()[0] - 10
        __init_snake_head = (random.randint(5, self.__height - 5), random.randint(0, self.__width - 1))
        __init_snake_body = (__init_snake_head[0] + 1, __init_snake_head[1])
        __init_snake_tail = (__init_snake_head[0] + 2, __init_snake_head[1])
        self.__snake = [__init_snake_head, __init_snake_body, __init_snake_tail]
        stdscr.addstr(__init_snake_head[0] + 5, __init_snake_head[1] * 2 + 5, "■")
        stdscr.addstr(__init_snake_body[0] + 5, __init_snake_body[1] * 2 + 5, "■")
        stdscr.addstr(__init_snake_tail[0] + 5, __init_snake_tail[1] * 2 + 5, "■")
        self.__foods = []
        self.__direction = World.UP
        self.__score = 0

    def generate_food(self, stdscr):
        while len(self.__foods) < 3:
            food = (random.randint(0, self.__height - 1), random.randint(0, self.__width - 1))
            if food not in self.__snake and food not in self.__foods:
                self.__foods.append(food)
                stdscr.addstr(food[0] + 5, food[1] * 2 + 5, "*")

    def snake_move(self, stdscr):
        # 生成移动后的蛇头
        new_head = (0, 0)
        if self.__direction == World.UP:
            new_head = (self.__snake[0][0] - 1, self.__snake[0][1])
        elif self.__direction == World.DOWN:
            new_head = (self.__snake[0][0] + 1, self.__snake[0][1])
        elif self.__direction == World.LEFT:
            new_head = (self.__snake[0][0], self.__snake[0][1] - 1)
        elif self.__direction == World.RIGHT:
            new_head = (self.__snake[0][0], self.__snake[0][1] + 1)

        # 移动合法性检测，不能180度大掉头
        if new_head == self.__snake[1]:
            self.__direction = (self.__direction + 2) % 4
            new_head = (self.__snake[0][0] * 2 - self.__snake[1][0], self.__snake[0][1] * 2 - self.__snake[1][1])

        # 是否吃到食物
        if new_head in self.__foods:
            self.__score += 1
            self.__foods.remove(new_head)
        else:
            stdscr.addstr(self.__snake[-1][0] + 5, self.__snake[-1][1] * 2 + 5, " ")
            self.__snake.pop()
        
        self.__snake.insert(0, new_head)
        stdscr.addstr(new_head[0] + 5, new_head[1] * 2 + 5, "■")

        # 胜负判断
        if new_head[0] < 0 or new_head[0] >= self.__height or new_head[1] < 0 or new_head[1] >= self.__width:
            return True
        elif new_head in self.__snake[1:]:
            return True
        return False

    def set_direction(self, direction):
        self.__direction = direction

    def draw_frame(self, stdscr):
        stdscr.addstr(4, 4, "┌" + "-" * self.__width * 2 + "┐")
        for i in range(self.__height):
            stdscr.addstr(5 + i, 4, "│")
            stdscr.addstr(5 + i, 5 + self.__width * 2, "│")
        stdscr.addstr(self.__height + 5, 4, "└" + "-" * self.__width * 2 + "┘")
        stdscr.addstr(self.__height + 6, 4, "Use arrow keys to control the snake. Press 'q' to quit.".center(self.__width * 2 + 2))

    def draw_score(self, stdscr):
        stdscr.addstr(3, 4, f"Score: {str(self.__score)}".ljust(self.__width + 2))

    def get_score(self):
        return self.__score

    def draw_game_over(self, stdscr):
        stdscr.addstr(self.__height // 2 + 3, self.__width - 10, "┌" + "─" * 28 + "┐")
        stdscr.addstr(self.__height // 2 + 4, self.__width - 10, "│" + " " * 28 + "│")
        stdscr.addstr(self.__height // 2 + 5, self.__width - 10, "│" + " Game Over!".center(28) + "│")
        stdscr.addstr(self.__height // 2 + 6, self.__width - 10, "│" + " " * 28 + "│")
        stdscr.addstr(self.__height // 2 + 7, self.__width - 10, "└" + "─" * 28 + "┘")
