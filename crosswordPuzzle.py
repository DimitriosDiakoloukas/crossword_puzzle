import math
import os
import random
import re
import sys

def fill_word(grid, word, start_row, start_col, direction):
    word_length = len(word)
    for i in range(word_length):
        if direction == 'HORIZONTAL':
            grid[start_row][start_col + i] = word[i]
        else:
            grid[start_row + i][start_col] = word[i]

def clear_word(grid, word, start_row, start_col, direction):
    word_length = len(word)
    for i in range(word_length):
        if direction == 'HORIZONTAL':
            grid[start_row][start_col + i] = '-'
        else:
            grid[start_row + i][start_col] = '-'

def is_word_fit(grid, word, start_row, start_col, direction):
    word_length = len(word)
    grid_size = len(grid)

    if direction == 'HORIZONTAL':
        if start_col + word_length > grid_size:
            return False
        for i in range(word_length):
            cell = grid[start_row][start_col + i]
            if cell != '-' and cell != word[i]:
                return False
    else:
        if start_row + word_length > grid_size:
            return False
        for i in range(word_length):
            cell = grid[start_row + i][start_col]
            if cell != '-' and cell != word[i]:
                return False

    return True

def crosswordPuzzle(grid, words):
    grid = [list(row) for row in grid]
    word_list = words.split(';')
    word_count = len(word_list)

    def solve(grid, word_index):
        if word_index == word_count:
            return grid

        word = word_list[word_index]
        grid_size = len(grid)

        for row in range(grid_size):
            for col in range(grid_size):
                if grid[row][col] == '-' or grid[row][col] == word[0]:
                    if is_word_fit(grid, word, row, col, 'HORIZONTAL'):
                        fill_word(grid, word, row, col, 'HORIZONTAL')
                        result = solve(grid, word_index + 1)
                        if result:
                            return result
                        clear_word(grid, word, row, col, 'HORIZONTAL')

                    if is_word_fit(grid, word, row, col, 'VERTICAL'):
                        fill_word(grid, word, row, col, 'VERTICAL')
                        result = solve(grid, word_index + 1)
                        if result:
                            return result
                        clear_word(grid, word, row, col, 'VERTICAL')

        return None

    result = solve(grid, 0)
    return [''.join(row) for row in result]

             
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    crossword = []

    for _ in range(10):
        crossword_item = input()
        crossword.append(crossword_item)

    words = input()

    result = crosswordPuzzle(crossword, words)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
