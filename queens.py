import bpy
from  mathutils import Vector
from copy import copy


DISPLACEMENT = 15.4

DEFAULT_N = 8

N = 6
INCR = 2.25

interval = 10
current_scene = bpy.context.scene
#queens = [current_scene.objects["Queen.010"],
#            current_scene.objects["Queen.011"],
#            current_scene.objects["Queen.012"],
#            current_scene.objects["Queen.013"]]

queens = [  current_scene.objects["Queen.027"],
            current_scene.objects["Queen.028"],
            current_scene.objects["Queen.029"],
            current_scene.objects["Queen.030"],
            current_scene.objects["Queen.031"],
            current_scene.objects["Queen.032"]
]
            
start_pos = copy(current_scene.objects["Queen.027"].location)
current_frame = current_scene.frame_current

history = list([[]] * N)

def lastof(index):
    global history,N
    index = min(N-1,index)
#    print("got index ",index)
    if len(history[index])==0:
        return (0,0)
    ret = history[index][-1]
    history[index] = history[index][:-1]
    return ret

def move(index,i,j):
    global current_frame
    if queens.__len__()<index+1:
        return
#    print("Got index " ,index)
    queens[index].keyframe_insert(data_path="location", frame=current_frame)
    t_pos = copy(start_pos)
    t_pos.x += j*INCR
    t_pos.y += i*INCR
    queens[index].location=t_pos
    queens[index].keyframe_insert(data_path="location", frame=current_frame+interval)

    current_frame+=interval
    
#    print("current_frame ",current_frame)
    

# here we create a chessboard
# NxN matrix with all elements set to 0
board = [[0]*N for _ in range(N)]

def attack(i, j):
    #checking vertically and horizontally
    global board,N
    for k in range(0,N):
        if board[i][k]==1 or board[k][j]==1:
#            if (i,j)==(5,3):
#                print("attack is from {} or {}".format((i,k),(k,j)))
            return True
    #checking diagonally
    for k in range(0,N):
        for l in range(0,N):
            if (k+l==i+j) or (k-l==i-j):
                if board[k][l]==1:
#                    if (i,j)==(5,3):
#                        print("attack is from {} or {}".format((i,k),(k,j)))
                    return True
    return False

queen_index = 0

def N_queens(n):
    global queen_index,pij,history,board,N
    if n==0:
        return True
    for i in range(0,N):
        for j in range(0,N):
                history[queen_index].append((i,j))
                if (attack(i,j)==False and board[i][j]!=1):
    #                Create and animation code | calls
                    board[i][j] = 1
                    move(queen_index,i,j)
#                    print("queen {} set at {}".format(queen_index,(i,j)))
                    
                    t_queen_index = copy(queen_index)
                    queen_index+=1                                  
                    
                    if N_queens(n-1)==True:
                        return True    
                    
#                    print("setting {},{} to 0".format(i,j))
                    board[i][j] = 0

                    pij=lastof(t_queen_index)    
                    move(t_queen_index,pij[0],pij[1])
                    queen_index=t_queen_index
                    #why did 4,3 get set to 0
#                    because n_queens(n-1) returned false that means either the previous n wasn't 0 or couldn't find a suitable solution
                    # okay what to do now 
#                    need to be set to (5,3)
#                else:
##                    if ((i,j)==(N-1,N-1)):
#                    pij=lastof(queen_index)    
#                    move(queen_index,pij[0],pij[1])
#                    print("when okke else part gets executed, ",(i,j))
#                    print("In this special case what else we need to know : attack({},{})=={} ".format(i,j,"true" if attack(i,j)==True else "false"))
#                    print("board {} = {}".format((i,j),board[i][j]))

                    # move to previous position  

#    no need to move to lastof sinec already moved in if block above
#    print('returning false aadhyayittu at n=',n)
    pij=lastof(queen_index)    
    move(queen_index,0,0)
    return False
N_queens(N)
#[print(x) for x in history]
#[print(x) for x in board]





