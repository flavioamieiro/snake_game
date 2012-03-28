#!/usr/bin/env python3

import copy
import time
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
    def __init__(self):
        self.positions = [[5, 3], [5, 4], [5, 5]]

    def move_down(self):
        for n, pos in enumerate(self.positions):
            pos[1] += 1
            self.positions[n] = pos


class Game(object):
    def __init__(self):
        self.snake = Snake()
        self.map = Map()

    def play(self):
        self.map.update(self.snake.positions)
        self.map.draw()

        while True:
            sys.stdout.write('\n')
            self.snake.move_down()
            try:
                self.map.update(self.snake.positions)
            except IndexError:
                raise GameOver("You've hit a wall. Your game is over!\n")
            self.map.draw()
            time.sleep(1)


if __name__ == '__main__':
    game = Game()
    try:
        game.play()
    except GameOver as exc:
        sys.stdout.write(str(exc))
