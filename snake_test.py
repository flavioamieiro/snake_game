import unittest
from snake_game import Snake, Game, GameOver

class TestSnake(unittest.TestCase):

    def test_snake_initial_position(self):
        snake = Snake()
        self.assertEqual(snake.positions, [[5, 3], [5, 4], [5, 5]])

    def test_snake_can_be_initialized_with_position(self):
        positions = [[5, 3], [6, 3], [6, 4]]
        snake = Snake(positions)
        self.assertEqual(snake.positions, positions)

    def test_move_snake_down_from_initial_position(self):
        snake = Snake()
        snake.move('down')
        self.assertEqual(snake.positions, [[5, 4], [5, 5], [5, 6]])

    def test_move_horizontal_snake_down(self):
        snake = Snake([[4, 3], [5, 3], [6, 3]])
        snake.move('down')
        self.assertEqual(snake.positions, [[5, 3], [6, 3], [6, 4]])

    def test_move_snake_left_from_initial_position(self):
        snake = Snake()
        snake.move('left')
        self.assertEqual(snake.positions, [[5, 4], [5, 5], [4, 5]])

    def test_move_snake_right_from_initial_position(self):
        snake = Snake()
        snake.move('right')
        self.assertEqual(snake.positions, [[5, 4], [5, 5], [6, 5]])

    def test_cant_move_right_if_going_left(self):
        positions = [[6, 3], [5, 3], [4, 3]]
        snake = Snake(initial_positions=positions, direction='left')
        snake.move('right')
        self.assertEqual(snake.positions, positions) # nothing happened


class TestGame(unittest.TestCase):
    def test_end_game_if_the_snake_hits_a_wall(self):
        game = Game()
        game.snake.positions = [[5, 7], [5, 8], [5, 9]]
        with self.assertRaises(GameOver):
            game.play()

    def test_no_invalid_positions(self):
        game = Game()
        self.assertFalse(game.invalid_position)

    def test_invalid_position_with_negative_index(self):
        game = Game()
        game.snake.positions[0] = [-1, 2]
        self.assertTrue(game.invalid_position)

    def test_invalid_position_with_y_outside_map_through_the_bottom(self):
        game = Game()
        game.snake.positions[0] = [10, 2]
        self.assertTrue(game.invalid_position)

    def test_invalid_position_with_y_outside_map_through_the_top(self):
        game = Game()
        game.snake.positions[0] = [-1, 2]
        self.assertTrue(game.invalid_position)

    def test_invalid_position_with_x_outside_map_through_the_right(self):
        game = Game()
        game.snake.positions[0] = [5, 10]
        self.assertTrue(game.invalid_position)

    def test_invalid_position_with_x_outside_map_through_the_left(self):
        game = Game()
        game.snake.positions[0] = [5, -1]
        self.assertTrue(game.invalid_position)


if __name__ == '__main__':
    unittest.main(buffer=True)
