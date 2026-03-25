# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1
        l1 = [digitstr[0], digitstr[1], digitstr[2]]
        l2 = [digitstr[3], digitstr[4], digitstr[5]]
        l3 = [digitstr[6], digitstr[7], digitstr[8]]
        self.tiles = [l1, l2, l3]
        
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                if self.tiles[r][c]=='0':
                    self.blank_r = r
                    self.blank_c = c

    def __repr__(self):
        """ returns a string representation of a Board object. 
        """
        s = ''
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                if self.tiles[r][c]=='0':
                    s += '_ '
                else:
                    s += self.tiles[r][c] + ' '
            s += '\n'
        return s
    
    def move_blank(self, direction):
        """ takes as input a string direction that specifies the direction 
            in which the blank should move, and attempts to modify the contents 
            of the called Board object accordingly. 
        """
        if direction == 'up':
            if (self.blank_r - 1) < 0:
                return False
            else:
                self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r - 1][self.blank_c]
                self.tiles[self.blank_r - 1][self.blank_c] = '0'
                self.blank_r -= 1
                return True 
                        
        elif direction == 'down':
            if (self.blank_r + 1) > 2:
                return False
            else:
                self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r + 1][self.blank_c]
                self.tiles[self.blank_r + 1][self.blank_c] = '0'
                self.blank_r += 1
                return True
                        
        elif direction == 'left': 
            if (self.blank_c - 1) < 0:
                return False
            else:
                self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r][self.blank_c - 1]
                self.tiles[self.blank_r][self.blank_c - 1] = '0'
                self.blank_c -= 1
                return True
                        
        elif direction == 'right': 
            if (self.blank_c + 1) > 2:
                return False
            else:
                self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r][self.blank_c + 1]
                self.tiles[self.blank_r][self.blank_c + 1] = '0'
                self.blank_c += 1
                return True
                        
        else: 
            return False 
   
    def digit_string(self):
        """ creates and returns a string of digits that corresponds to the 
            current contents of the called Board object’s tiles attribute.
        """
        s = ''
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                s += self.tiles[r][c]
        return s
                    
    def copy(self):
        """ returns a newly-constructed Board object that is a deep copy of 
            the called object. 
        """
        b2 = self.digit_string()[:]
        return Board(b2)
    
    def num_misplaced(self):
        """ counts and returns the number of tiles in the called Board object 
            that are not where they should be in the goal state. 
        """
        count = 0 
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                if self.tiles[r][c] != GOAL_TILES[r][c] and self.tiles[r][c]!= '0':
                    count += 1 
        return count 
    
    def goal_indexes(self, tile):
        """ Finds misplaced tile on the goal board
        """
        row = 0
        col = 0
        
        for r in range(3):
            for c in range(3):
                if GOAL_TILES[r][c] == tile:
                    row = r
                    col = c
        return [row, col]
    
    def rc_misplaced(self):
        """ counts and returns the number of misplaced rows and cols
        """
        count = 0 
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] != GOAL_TILES[r][c]:
                    # call helper function and store in a variable (named coords or something else)
                    coords = self.goal_indexes(self.tiles[r][c])
                    if r != coords[0]:
                        count += 1
                    if c != coords[1]:
                        count += 1 
        return count 
    
    def __eq__(self, other):
        """ comapres the content of two Board objects and returns True if they 
            are the same and False if otherwise. 
        """
        if self.tiles == other.tiles:
            return True 
        else:
            return False 
        
                
                    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
