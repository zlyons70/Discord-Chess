import chess
import chess.svg
import aspose.words as aw

def display_board(board):
    file_name = chess.svg.board(board=board)
    doc = aw.Document()
    builder = aw.DocumentBuilder(doc)
    shape = builder.insert_image(file_name)
    return shape
def initialize_board():
    board = chess.Board()
    display_board(board)
    return board

def make_move(board, move):
    board.push_san(move)
    
def game_over(board):
    return board.outcome()