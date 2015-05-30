from game import Direction
import numpy

class gameboard(object):
    
    def __init__(self, boardX, boardY):
        self.board = numpy.zeros(shape=(boardX, boardY))
        self.boardSizeX = boardX
        self.boardSizeY = boardY

    def move(self, direction):
        # Game.move(direction)
        raise 'Unimplemented method'

    def validMove(self, direction):
        vec = None
        if direction == Direction.LEFT: # 1
            vec = { 'x': -1, 'y': 0 }
        elif direction == Direction.RIGHT: # 2
            vec = { 'x': 1, 'y': 0 }
        elif direction == Direction.UP: # 3
            vec = { 'x': 0, 'y': -1 }
        elif direction == Direction.DOWN: # 4
            vec = { 'x': 0, 'y': 1 }
        else:
            return False

        # Check if Valid
        return True

    def sizeX(self):
        return self.boardSizeX

    def sizeY(self):
        return self.boardSizeY

    def getCell(self, x, y):
        return self.board[x,y]

    def setCell(self, x, y, value):
        #board.itemset([x,y], value)
        self.board[x,y] = value


if __name__ == '__main__':
    board = gameboard(5,2)
    print board.board

    print "Size X = ", board.sizeX() # 5 Rows
    print "Size Y = ", board.sizeY() # 2 Columns

    board.setCell(2,1,5)
    print board.board
    print "Cell [2,1] = ", board.getCell(2,1) # 5 in Row 2 Col 1 (Note: Zero based index)

    print board.validMove(1)                # True
    print board.validMove(Direction.LEFT)   # True
    print board.validMove(-1)               # False
    print board.validMove(5)                # False

    try:
        board.move(Direction.LEFT)
    except Exception, e:
        print e
    else:
        pass
    finally:
        pass