import sys, os
import chess
import math
import random
import scipy, numpy, pandas, sklearn
import sqlite3
from stuckfishsupport import * 

class Stuckfish(object):
    def __init__(self, perspective="b"):
        self.connection = sqlite3.connect("alphaghetto.db")
        self.fen = ""
        self.perspective = perspective
        self.moves_list = []
        self.engine = AlphaGhetto()
        #self.piece_values = {'K': 10000, 'k': 10000, 'Q': 90, 'q': 90, 'R': 50, 'r': 50, 'B': 35, 'b': 35, 'N': 33, 'n': 33, 'P': 10, 'p': 10}

    def set_moves_list(self, moves):
        self.moves_list = moves

    def pick_random(self):
        if len(self.moves_list) > 0:
            return random.choice(self.moves_list)


    def ingest_fen(self, fen):
        self.fen = fen

    def get_position(self):
        return self.fen[:(findnth(self.fen, " ", 1) - 2)]

    '''
    def calculate_material(self):
        material_score = 0
        if self.perspective == "b":
            for piece in self.get_position():
                if piece in ['q', 'r', 'b', 'n', 'p']:
                    material_score = material_score + self.piece_values.get(piece)
        elif self.perspective == "w":
            for piece in self.get_position():
                if piece in ['Q', 'R', 'B', 'N', 'P']:
                    material_score = material_score + self.piece_values.get(piece)

                ''''''
                if piece.isnumeric() or piece == "/":
                    continue
                else:
                    material_score = material_score + self.piece_values.get(piece)
                ''''''
        return material_score
    '''

    def factors(self):
        print("nah son")

    def calculate_move_score(self, move):
        move_score = 0
        #move_score = move_score + calculate_material()


    def make_move(self):
        print("yolo")