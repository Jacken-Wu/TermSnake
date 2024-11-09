from src.world import World
from src.db import DB
import time
import curses


def main(stdscr):
    DB.init_table()

    stdscr.clear()
    stdscr.nodelay(True)
    curses.curs_set(0)

    world = World(stdscr)
    world.draw_frame(stdscr)

    while True:
        world.draw_score(stdscr)
        stdscr.refresh()

        time_start = time.time()
        time_end = time.time()
        key = -1

        refresh_time = 0.3 - (world.get_score() / 200)
        if refresh_time < 0.05:
            refresh_time = 0.05

        while time_end - time_start < refresh_time:
            key = stdscr.getch()
            if key == curses.KEY_UP:
                world.set_direction(World.UP)
            elif key == curses.KEY_DOWN:
                world.set_direction(World.DOWN)
            elif key == curses.KEY_LEFT:
                world.set_direction(World.LEFT)
            elif key == curses.KEY_RIGHT:
                world.set_direction(World.RIGHT)
            elif key == ord('q'):
                break
            time_end = time.time()

        if key == ord('q'):
            break

        is_game_over = world.snake_move(stdscr)
        if is_game_over:
            world.draw_game_over(stdscr)
            stdscr.refresh()
            key = -1
            while key == -1:
                key = stdscr.getch()
            break
        world.generate_food(stdscr)


curses.wrapper(main)
