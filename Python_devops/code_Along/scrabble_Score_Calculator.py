"""
Scrabble Calculator

Letters                      |   Value

A, E, I, O, U, L, N, R, S, T |   1
D, G                         |   2
B, C, M, P                   |   3
F, H, V, W, Y                |   4
K                            |   5
J, X                         |   8
Q, Z,                        |   10
"""

one_point_letters = ["a", "e", "i", "o", "u", "l", "n", "r", "s", "t"]
two_point_letters = ["d", "g"]
three_point_letters = ["b", "c", "m", "p"]
four_point_letters = ["f", "h", "v", "w", "y"]
five_point_letters = ["k"]
eight_point_letters = ["j", "x"]
ten_point_letters = ["q", "z"]

def scrabble_calc(word):
    word_score = 0

    for char in word:
        if char in one_point_letters:
            word_score += 1
        elif char in two_point_letters:
            word_score += 2