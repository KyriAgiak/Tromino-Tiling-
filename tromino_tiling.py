import sys
#import argparse

#Functions in use:
def define_quadrants(board, n, mid):
    quadrant1 = [row[mid:n] for row in board[0:mid]]
    quadrant2 = [row[0:mid] for row in board[0:mid]] 
    quadrant3 = [row[0:mid] for row in board[mid:n]]      
    quadrant4 = [row[mid:n] for row in board[mid:n]] 
    return quadrant1, quadrant2, quadrant3, quadrant4
      
def center_placer(square, mid, orientation):
     if orientation == 'bottom_right':
        square[mid-1][mid] = 'G'
        square[mid][mid] = 'G'
        square[mid][mid-1] = 'G'
     else:
        square = set_orientation(square, orientation, mid)
     return square 
      
def another_brick_in_the_board(board, T1, T2, T3, T4, mid, a):
  #board = [[' ' for _ in range(a)] for _ in range(a)]
  #center_placer(board, mid)        
  for i in range(mid):
      for j in range(mid, a):
        board[i][j] = T1[i][abs(j-mid)]

  for i in range(mid):
      for j in range(0, mid):
        board[i][j] = T2[i][j]

  for i in range(mid, a):
      for j in range(mid):
        board[i][j] = T3[abs(i-mid)][j]

  for i in range(mid, a):
      for j in range(mid, a):
        board[i][j] = T4[abs(i-mid)][abs(j-mid)]
  board
  return board

def set_orientation(square, orientation, mid):
  for i in range(len(square)):
    square = list(square)
  match orientation:
  
      case 'bottom_left':
        
        square[mid-1][mid-1] = 'G'  
        square[mid][mid] = 'G'    
        square[mid][mid-1] = 'G'      
    

      case 'bottom_right':
        
        square[mid-1][mid] = 'G'
        square[mid][mid] = 'G'
        square[mid][mid-1] = 'G'
       
        
      case 'top_right':
        
        square[mid-1][mid-1] = 'G'  
        square[mid-1][mid] = 'G'         
        square[mid][mid] = 'G'
        
      case 'top_left':
        
        square[mid-1][mid] = 'G'    
        square[mid-1][mid-1] = 'G'      
        square[mid][mid-1] = 'G'        
  return square          


def find_quadrants(board, a, mid):
   T1, T2, T3, T4 = define_quadrants(board, a, mid)
   if len(T1) == 4 :
     for i in range(1,5):
        lst.append('T' + str(i))
     return lst
   else:
     for i in range(1,5):
       find_quadrants('T' + str(i), len('T'+ str(i)), len('T' + str(i))//2)
       

def set_quadrands(lst):
    for i in range(len(lst)):
      lst[i] = list(lst[i])
      if i%4 == 0:
        lst[i] = set_orientation(lst[i], 'top_right', len(lst[i])//2)
      elif (i-1) %4==0:
        lst[i] = set_orientation(lst[i], 'top_left', len(lst[i])//2)
      elif (i-2) %4 == 0:
        lst[i] = set_orientation(lst[i], 'bottom_left', len(lst[i])//2)
      else:
        lst[i] = set_orientation(lst[i], 'bottom_right', len(lst[i])//2)
    return lst

def write_to_file(board):
    with open('output.txt', 'w') as f:
        for row in board:
            f.write(' '.join(row) + '\n')
 
            
def empty_spaces(square):
    n = len(square)
    color_sequence = ['B', 'B', 'R', 'R', 'R', 'B', 'B', 'B', 'R', 'R', 'R']
    index = 0
    blue_counter = 0
    red_counter = 0
    top, bottom, left, right = 0, n - 1, 0, n - 1
    
    # Fill the empty spaces in circular pattern
    while top <= bottom and left <= right:
        # Fill top row
        for i in range(left, right + 1):
            if square[top][i] == ' ':
               square[top][i] = color_sequence[index]
               if color_sequence[index] == 'B':
                      blue_counter+=1
               elif color_sequence[index] =='R':
                      red_counter+=1
            index = (index + 1) % len(color_sequence)
        top += 1
        
        
        # Fill right column
        for i in range(top, bottom + 1):
            if square[i][right] == ' ':
                square[i][right] = color_sequence[index]
                if color_sequence[index] == 'B':
                      blue_counter+=1
                elif color_sequence[index] =='R':
                      red_counter+=1
            index = (index + 1) % len(color_sequence)
        right -= 1
        
        # Fill bottom row
        for i in range(right, left - 1, -1):
            if square[bottom][i] == ' ':
                square[bottom][i] = color_sequence[index]
                if color_sequence[index] == 'B':
                      blue_counter+=1
                elif color_sequence[index] =='R':
                      red_counter+=1
            index = (index + 1) % len(color_sequence)
        bottom -= 1
        
        # Fill left column
        for i in range(bottom, top - 1, -1):
            if square[i][left] == ' ':
                square[i][left] = color_sequence[index]
                if color_sequence[index] == 'B':
                      blue_counter+=1
                elif color_sequence[index] =='R':
                      red_counter+=1
            index = (index + 1) % len(color_sequence)
        left += 1
    # Fill the last hole
    if blue_counter == 6:
        last_color = 'R'
    else:
        last_color = 'B'
    for i in range(n):
        for j in range(n):
            if square[i][j] == ' ':
               square[i][j] = last_color
    return square 
             
      
# Receiving argument
n = int(sys.argv[1])
a = 2**n 
lst = []
# Generating an empty square a x a table
board = [[' ' for _ in range(a)] for _ in range(a)]
match n:
    case 1:
        board =  [['G', 'X'],
                  ['G', 'G']]
        
        
    case 2:
        mid = 2
        board = center_placer(board, mid, 'bottom_right')
        board[mid-1][mid-1] = 'X'
        empty_spaces(board)
        
    case _:
        # find the middle and put a green tromino there
        mid = 2 ** (n - 1)
        board = center_placer(board, mid, 'bottom_right')
        board[mid-1][mid-1] = 'X'
        b = a/2
        lst = find_quadrants(board, a, mid)
        lst = set_quadrands(lst)
        for i in range(len(lst)):
             lst[i] = empty_spaces(lst[i])
             board = another_brick_in_the_board(lst[i], len(lst[i]), a)
write_to_file(board)  