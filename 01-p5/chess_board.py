class ChessBoard:
    def __init__(self, white, black):
        '''
        Initializes table attributes, expected input
        :param white (string): Ke1,Qd1,Ra1
        :param black (string): Ke9,Qd8,Ra8
        :return: Returns True if everything is fine, raises Exception if error
        '''
        # corresponding to a b c d e f g h
        self.black_input = []
        self.white_input = []
        self.board =      {
            'a':['','','','','','','',''],
            'b':['','','','','','','',''],
            'c':['','','','','','','',''],
            'd':['','','','','','','',''],
            'e':['','','','','','','',''],
            'f':['','','','','','','',''],
            'g':['','','','','','','',''],
            'h':['','','','','','','','']
        }

        self.validPieces = ('K','Q','R','B','N')
        try:
            self.interpret_input(white, 'w')
            self.interpret_input(black, 'b')
        except Exception as e:
            raise e

    def get_piece_row(self, piece=''):
        if int(piece[-1]) < 1 or int(piece[-1]) > 8:
            raise Exception('Not a valid row', piece[-1])
        return int(piece[-1])-1

    def get_piece_column(self, piece=''):
        if piece[-2] not in self.board.keys():
            raise Exception('Not a valid column', piece[-2])
        return piece[-2]

    def get_piece_type(self, piece=''):
        if len(piece) == 2:
            return 'P'
        else:
            if piece[0].upper() not in self.validPieces:
                raise Exception('Not valid piece type', piece[0])
            return piece[0].upper()

    def interpret_input(self, input='', color='w'):
        linput = input.split(',')
        for piece in linput:
            if len(piece) > 3 or len(piece)<2:
                raise Exception('Not valid piece', piece)
            # position
            try:
                ptype = self.get_piece_type(piece)
                column = self.get_piece_column(piece)
                row = self.get_piece_row(piece)
                if color == 'w':
                    ptype = ptype.upper()
                if color == 'b':
                    ptype = ptype.lower()
                self.board[column][row] = ptype
            except Exception as e:
                raise e

        if color == 'w':
            self.white_input = input
        elif color == 'b':
            self.black_input = input

    def show(self):
        '''
        Draws the table on the screen
        :return: None
        '''
        c = 0
        for row in reversed(range(0,8)):
            print('+---'*8 + '+')
            # for every row it checks whether the corresponding column has a piece on it
            for column in self.board.keys():
                squarechar = ':'
                if c % 2 != 0:
                    squarechar = '.'
                piecechar = squarechar
                if self.board[column][row] != '':
                    piecechar = self.board[column][row]
                print('|' + squarechar + piecechar + squarechar , end='')
                c = c + 1
            print('|')
        print('+---' * 8 + '+')
    def __repr__(self):
        return 'Inputs:\nBlack ' + str(self.black_input) + \
                '\nWhite ' + str(self.white_input) + \
                '\nBoard:' + str(self.board)