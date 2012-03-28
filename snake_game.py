#!/usr/bin/env python3

class Map(object):
    grid = [
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

    def update(self, positions, char='O'):
        for pos in positions:
            x = pos[0]
            y = pos[1]
            self.grid[y][x] = char

    def draw(self):
        for row in self.grid:
            for cell in row:
                print(cell, end='')
            print('\n')



class Snake(object):
    def __init__(self):
        self.positions = [[5, 3], [5, 4], [5, 5]]

    def move_down(self):
        for n, pos in enumerate(self.positions):
            pos[1] += 1
            self.positions[n] = pos

if __name__ == '__main__':
    snake = Snake()
    snake_map = Map()
    while True:
        snake.move_down()
        snake_map.update(snake.positions)
        snake_map.draw()
