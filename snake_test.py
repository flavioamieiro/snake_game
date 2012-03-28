import unittest
from snake_game import Snake, GameOver

class TestSnake(unittest.TestCase):

    def test_snake_initial_position(self):
        snake = Snake()
        self.assertEqual(snake.positions, [[5, 3], [5, 4], [5, 5]])

    def test_move_snake_down_from_initial_position(self):
        snake = Snake()
        snake.move_down()
        self.assertEqual(snake.positions, [[5, 4], [5, 5], [5, 6]])

if __name__ == '__main__':
    unittest.main()
