#--Credentials-----------------------------------------------------------------------------

## Author: Rahul V Sumbly
## Date: 27/11/2020
## Copyright: Copyright 2020, Snacks Collection Problem
## Credits: Rahul V Sumbly
## License: ~None~
## Version: {mayor}.{minor}.{rel}
## Maintainer: Rahul V Sumbly
## Email: rahulrtg7703@gmail.com
## Status: COMPLETED

#-------------------------------------------------------------------------------------------

import numpy as np
import math
#  "0" represents an open cell,
#  "2" represents a blocked cell and
#  "1" represents snacks in the maze

from collections import deque

#SOME BOARDS TO TEST THE CODE WITH
"""
board =[[0,0,0,0,0],
        [0,0,0,1,0],
        [0,2,2,2,2],
        [0,0,0,1,0],
        [0,0,0,0,0]]
"""

"""
board =[[0, 0, 0, 1, 0, 2, 2],
        [2, 2, 2, 0, 0, 2, 2],
        [2, 2, 2, 0, 1, 2, 2],
        [0, 1, 0, 0, 0, 1, 0],
        [2, 2, 0, 1, 0, 0, 0],
        [2, 2, 0, 0, 1, 2, 2],
        [1, 0, 0, 1, 0, 2, 2]]
"""

#"""
board =[
 [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
 [2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
 [2, 2, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0],
 [0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0],
 [0, 0, 0, 1, 2, 2, 2, 2, 0, 0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0],
 [0, 0, 0, 0, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
 [0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]]
#"""

# M x N matrix
#-Y
M = len(board)
#-X
N = len(board[0])

final_x = [0]
final_y = [0]
final_path = [[0,0]]
reached = []

#-GET COORDINATES OF SNACKS AND WALLS
def coordinates(tar):
    n = tar
    x=-1
    y=-1
    co_lst = []
    for i in board:
        y=y+1
        for j in i:
            x=x+1
            if j == n:
                co = [x,y]
                co_lst.append(co)
                #print("Coordinates:",x,",",y)
                #print(board[y][x])
        x = -1
    #print("-------------------")
    return co_lst

print("--------------------------------------")
#-GET COOORDINATES OF SNACKS AND WALLS
snacks = coordinates(1)
snacks_lst = coordinates(1)
walls = coordinates(2)

print("--------------------------------------")
print(snacks)
print("--------------------------------------")
print(walls)
print("--------------------------------------")

"""
#-SORT COORDINATES SO THAT TWO CONSECUTIVE COORDINATES IN THE LIST ARE NEAREST
def euclidian_distance(a, b):
    return np.linalg.norm(a - b)

coords = np.array(snacks)

coords = sorted(coords, key=lambda point: euclidian_distance(point, coords[0]))
print(np.matrix(coords)) # matrix is only for formatting for readability purposes
"""

# check if specified row and column are valid matrix index
def isValid(i, j):
    global M,N
    return (0 <= i < M) and (0 <= j < N)

# check if current cell is an open area and its distance from "1" is not yet calculated
def isSafe(i, j, mat, result):
    return mat[i][j] == 0 and result[i][j] == -1
 
# Replace all "0" in the matrix with their shortest distance from the nearest "1"
def updateDistance(mat, result):
 
    # initialize an empty queue
    q = deque()
 
    # find all "1" location and add them to the queue
    for i in range(M):
        for j in range(N):
            # if current cell represents a mine
            if mat[i][j] == 1:
                q.append((i, j, 0))

                # update "1" distance as "0"
                result[i][j] = 0
 
            # else initialize distance as -1
            else:
                result[i][j] = -1
 
    # lists to get indices of 4 adjacent cells of a given cell
    R = [0, -1, 0, 1]
    C = [-1, 0, 1, 0]
 
    # do for each in the queue
    while q:
        # dequeue the front cell
        x, y, distance = q.popleft()
 
        # update the 4 adjacent cells of the front node in the queue
        for i in range(4):
            # enqueue the adjacent cell if it is valid, unvisited and has a path through it
            if isValid(x + R[i], y + C[i]) and isSafe(x + R[i], y + C[i], mat, result):
                result[x + R[i]][y + C[i]] = distance + 1
                q.append((x + R[i], y + C[i], distance + 1))
    return result

path_board = []

#-START TO SETTING THE DISTANCE OF NEAREST "1"
def distancegraph(new_board):
    global path_board,N,M
    res = [[0 for x in range(N)] for y in range(M)]
    path_board = updateDistance(new_board, res)

#-RESET BOARD AND REDIFINE DISTANCES AFTER EACH "1" IS FOUND
def setboard():
    global path_board,snacks,walls,N,M

    new_board = [[0 for x in range(N)] for y in range(M)]
    for i in snacks_lst:
        xx = i[0]
        yy = i[1]
        new_board[yy][xx] = 1
    for i in walls:
        xx = i[0]
        yy = i[1]
        new_board[yy][xx] = 2

    #CALLING THE FUNCTION
    distancegraph(new_board)

    for i in walls:
        xx = i[0]
        yy = i[1]
        path_board[yy][xx] = 99

setboard()

"""
for i in path_board:
    print(i)
print("-------------------")
"""

#-TO CHECK IF A CELL IS VISITED OR NOT
#col row
visited = [[False for i in range(M)] for j in range(N)]
# Mark the source cell as visited 
visited[0][0] = True

#RESET VISITING MATRIX AFTER REACHING "1"
def visiting(x,y):
    global visited,M,N
    #col row
    visited = [[False for i in range(M)] for j in range(N)]
    # Mark the source cell as visited 
    visited[y][x] = True

#CHECK IF NEIGHBOURING CELL IS VALID
def isvalid(x,y):
    global M,N,path_board
    if x>=0 and y>=0 and x<N and y<M and path_board[y][x] != 99:
        return True
    else:
        return False


def path(x,y):
    global final_x,final_y,final_path

    final_x.append(x)
    final_y.append(y)
    final_path.append([x,y])

def remainingsnacks(x,y):
    global snacks_lst
    print(snacks_lst)
    index = snacks_lst.index([x,y])
    snacks_lst.pop(index)

while len(snacks)>0:
    x = final_x[-1]
    y = final_y[-1]
    choice = []
    choice_val = []
    skip = 0

    #          L  R  U  D UL UR DL DR
    rowNum = [-1, 0, 0, 1,-1, 1,-1, 1]
    colNum = [ 0,-1, 1, 0, 1, 1,-1,-1]

    for i in range(8):
        row = x + rowNum[i]
        col = y + colNum[i]
        #print(row,col)
        #print("--------------")

        if (isvalid(row,col) and not visited[col][row]):
            if path_board[col][row] == 0:
                reached.append([row,col])
                #print('Done')
                skip = 1
                snacks.pop(0)
                remainingsnacks(row,col)
                path(row,col)
                visiting(row,col)
                if len(snacks)>0:
                    setboard()

            else:
                choice.append([row,col])
                #print(row,col)
                #print("--------------")

    if skip == 0:
        for i in choice:
            ch_x = i[0]
            ch_y = i[1]
            choice_val.append(path_board[ch_y][ch_x])

        #print(choice_val)
        try:
            min_pos = choice_val.index(min(choice_val))
            #print(min_pos)
            pos = choice[min_pos]
            #print(pos)
            pos_x = pos[0]
            pos_y = pos[1]
            #print(pos_x,pos_y)
            path(pos_x,pos_y)
            visited[pos_y][pos_x] = True
        except:
            break


print("-----------")
print(final_x)
print(final_y)


print("-----------")
print(reached)


"""
#-CELLS-PATH-SHOWN-ON-GRAPH
print("-----------")
for i in visited:
    print(i)
"""
"""
resulting_board = [[0 for i in range(M)] for j in range(N)]

for i in range(len(final_x)):
    xxx = final_x[i]
    yyy = final_y[i]
    resulting_board[yyy][xxx] = 1

print("-----------")
for i in resulting_board:
    print(i)
"""
