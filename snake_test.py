import unittest
from snake_game import Snake, Game, GameOver

class TestSnake(unittest.TestCase):

    def test_snake_initial_position(self):
        snake = Snake()
        self.assertEqual(snake.positions, [[5, 3], [5, 4], [5, 5]])

    def test_move_snake_down_from_initial_position(self):
        snake = Snake()
        snake.move_down()
        self.assertEqual(snake.positions, [[5, 4], [5, 5], [5, 6]])



class TestGame(unittest.TestCase):
    def test_end_game_if_the_snake_hits_a_wall(self):
        game = Game()
        game.snake.positions = [[5, 7], [5, 8], [5, 9]]
        with self.assertRaises(GameOver):
            game.play()

if __name__ == '__main__':
    unittest.main(buffer=True)
