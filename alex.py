# board=[]
# tie_var=0
# game_over=False
# def setting_up():
#     for i in range(3):
#         row=[" "]*3
#         board.append(row)

# def printing():
#     for row in board:
#         print(" | ".join(row))
#         print("-"*10)
# def check_row():
#     for i in range(3):
#         if board[i][0] == board[i][1] == board[i][2] !=" ":
#             print(f"You won - {turn}")
#             return True
#     return False

           
# def check_col():
#     for i in range(3):
#         if board[0][i] == board[1][i] == board[2][i] !=" ":
#             print(f"You won - {turn}")
#             return True
#     return False

# def check_diag():
#     if board[0][0] == board[1][1] == board[2][2] !=" ":
#         print(f"You won - {turn}")
#         return True
#     elif board[0][2] == board[1][1] == board[2][0] !=" ":
#         print(f"You won - {turn}")
#         return True
#     return False

# def check_tie():
#     global tie_var
#     for row in board:
#         if " " not in row:
#             tie_var +=1
#         if tie_var == 3:
#             print("its a tie")
#             return True
#     return False

# setting_up()
# turn="X"

# while True:
#     printing()
#     choice_row=int(input("What row do you want to choose: "))
#     choice_col=int(input("What column do you want to choose: "))

#     board[choice_row][choice_col]=turn

#     if check_row() or check_col() or check_diag() or check_tie():
#         printing()
#         break


#     turn="X" if turn == "O" else "O"   


# import pgzrun
# WIDTH=500
# HEIGHT=500
# turn_count=1
# turn="X"
# squares= [
#     Rect((0,0), (150, 150)), 
#     Rect((0,175), (150, 150)), 
#     Rect((0,350), (150, 150)), 
#     Rect((175,0), (150, 150)), 
#     Rect((175,175), (150, 150)), 
#     Rect((175,350), (150, 150)), 
#     Rect((350,0), (150, 150)), 
#     Rect((350,175), (150, 150)), 
#     Rect((350,350), (150, 150))
# ]
# clicked_squares=[[], []]
# Click=False

# def draw():
#     screen.fill("black")
#     for i in squares:
#         screen.draw.filled_rect(i, "white")
#         if i in clicked_squares[0]:
#             screen.draw.text("X", center=i.center, fontsize=80, color="black")
#         elif i in clicked_squares[1]:
#             screen.draw.text("O", center=i.center, fontsize=80, color="black")

# def update():
#     pass
  


# def on_mouse_down(pos):
#     global turn_count, turn
#     for i in squares:
#         if i not in clicked_squares[0] and i not in clicked_squares[1]:
#             if i.collidepoint(pos):
#                 if turn == "X":
#                     clicked_squares[0].append(i)
#                 else:
#                     clicked_squares[1].append(i)
                
#                 turn = "O" if turn =="X" else "X"
#         check_row()

# def check_row():
#     # for a in range(3):
#         # for i in range(3):
#         if squares[0] in clicked_squares[0]  and squares[1]  in clicked_squares[0] and squares[2] in clicked_squares[0]:
#             print("You win")
        if squares[2] in clicked_squares[3]  and squares[1]  in clicked_squares[0] and squares[2] in clicked_squares[0]:
#             print("You win")


# ##### Not sure how to check


# pgzrun.go()


import pgzrun

board = []

for i in range(3):
    row = []
    for j in range(3):
        cell = Rect((j*160, i*160), (150,150))
        row.append(cell)
    
    board.append(row)

def draw():
    for cell in board:
        screen.draw.filled_rect(cell, color="white")
    
    


pgzrun.go()






























