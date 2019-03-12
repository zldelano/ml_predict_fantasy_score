import argparse
import difflib
import math
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

COLS_PPG = ["Rk", "Player", "Pos", "Age", "Tm", "G", "GS", "MP", "FG", "FGA",
            "FG%", "3P", "3PA", "3P%", "2P", "2PA", "2P%", "eFG%", "FT", "FTA",
            "FT%", "ORB", "DRB", "TRB", "AST", "STL", "BLK", "TOV", "PF", "PS/G"]