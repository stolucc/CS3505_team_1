# Team 1
import unittest
import pygame
from Team_1_client import Ludo
from Team_1_board import Board
from Team_1_piece import Piece
import threading


class TestClient(unittest.TestCase):
    def setUp(self):
        self.ludo = Ludo()
        
    def test__initial_values(self):
        self.assertEqual(self.ludo.my_player, None)
        self.assertEqual(self.ludo.genie_owner, None)
        self.assertIsInstance(self.ludo.board, Board)
        self.assertIsInstance(self.ludo.all_pieces[0], Piece)
        self.assertEqual(self.ludo.colour_check, 0)
        self.assertEqual(self.ludo.time_limited, 15)
        self.assertTrue(self.ludo.p.empty())

    def test_show_start_screen(self):
        self.assertIsNone(self.ludo.connection.my_player)
        screen_thread = threading.Thread(target=self.ludo.show_start_screen)
        screen_thread.start()
        self.ludo.connection.my_player = 1
        self.assertIsNotNone(self.ludo.connection.my_player)
        while screen_thread.is_alive():
            pass
        screen_thread.join()
        pygame.quit()


if __name__ == '__main__':
    unittest.main()
