#!/usr/bin/env python3

import copy
import time
import tty, termios
import sys

class GameOver(Exception):
    pass

class Map(object):
    initial_grid = [
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ]

    def __init__(self):
        self.grid = copy.deepcopy(self.initial_grid)

    @property
    def width(self):
        return len(self.grid[0])

    @property
    def height(self):
        return len(self.grid)

    def clear(self):
        self.grid = copy.deepcopy(self.initial_grid)

    def update(self, positions, char='O'):
        self.clear()
        for pos in positions:
            x = pos[0]
            y = pos[1]
            self.grid[y][x] = char

    def draw(self):
        for row in self.grid:
            for cell in row:
                sys.stdout.write(cell)
            sys.stdout.write('\n')


class Snake(object):
    def __init__(self, initial_positions=None, direction='down'):
        self.positions = copy.deepcopy(initial_positions) or [[5, 3], [5, 4], [5, 5]]
        self.direction = direction

    def direction_conflicts(self, new_direction):
        conflicts = {
            'left': 'right',
            'right': 'left',
            'down': 'up',
            'up': 'down',
        }
        return conflicts[self.direction] == new_direction

    def move(self, new_direction):
        # we should keep the old direction if the new one conflicts
        # with it, but still move it
        if self.direction_conflicts(new_direction):
            new_direction = self.direction

        tail = self.positions.pop(0) # remove the 'tail'
        previous_head = self.positions[-1]

        if new_direction == 'up':
            new_head = [previous_head[0], (previous_head[1] - 1)]

        if new_direction == 'down':
            new_head = [previous_head[0], (previous_head[1] + 1)]

        elif new_direction == 'left':
            new_head = [(previous_head[0] - 1), previous_head[1]]

        elif new_direction == 'right':
            new_head = [(previous_head[0] + 1), previous_head[1]]

        self.positions.append(new_head)
        self.direction = new_direction


class Game(object):
    def __init__(self):
        self.snake = Snake()
        self.map = Map()

    @property
    def invalid_position(self):
        for pos in self.snake.positions:
            # negative indexes are not allowed (this takes care of the
            # snake going out through the top and the left of the map)
            if (pos[0] < 0) or (pos[1] < 0):
                return True

            # we should not have a part of the snake through the
            # bottom of the map
            elif (pos[0] >= self.map.height):
                return True

            # we should not have a part of the snake through the right
            # of the map
            elif (pos[1] >= self.map.width):
                return True

        return False

    def read_key(self):
        """
        Read a key from stdin without having to press enter. This
        means putting the tty in Raw mode, and then setting it back to
        it's original state so we can print stuff out without problems.

        man 3 termios has more details on how this works.
        """
        # get current tty attributes so we can restore them later
        old_tty_attr = termios.tcgetattr(sys.stdin)

        # set the tty to raw mode (input is available character by
        # character, echoing is disabled and special processing of
        # term input and output is disabled.
        tty.setraw(sys.stdin)

        # get the key
        key = sys.stdin.read(1)

        # return to old attributes after everything from fd was read
        # (TCSADRAIN)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_tty_attr)

        return key

    def play(self):
        self.map.update(self.snake.positions)
        self.map.draw()

        while True:
            sys.stdout.write('\n')

            keymap = {
                'h': 'left',
                'j': 'down',
                'k': 'up',
                'l': 'right',
            }

            key = self.read_key()
            try:
                new_direction = keymap[key]
            except KeyError:
                new_direction = self.snake.direction

            self.snake.move(new_direction)

            if self.invalid_position:
                raise GameOver("You've hit a wall. Your game is over!\n")

            self.map.update(self.snake.positions)
            self.map.draw()


if __name__ == '__main__':
    game = Game()
    try:
        game.play()
    except GameOver as exc:
        sys.stdout.write(str(exc))
