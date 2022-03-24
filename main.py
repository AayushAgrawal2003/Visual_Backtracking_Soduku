import math
import pygame
import time
import sys
WIDTH = 729
END  = 729
BOX_SIZE = 81
background_color = (251,247,245)
original_grid_element_color = (52, 31, 151)
buffer = 5
original_grid_element_color = (52, 31, 151)
T = 0.05 #Set Time Here, For better understanding run on higher time

def main(base):
    pygame.init()
    win = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("Click Anywhere To Start")

    win.fill(background_color)
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    pygame.display.update()
    for i in range(0, 10):
        if (i % 3 == 0):
            pygame.draw.line(win, (0, 0, 0), (BOX_SIZE * i, 0), (BOX_SIZE * i, END), 4)
            pygame.draw.line(win, (0, 0, 0), (0, BOX_SIZE * i), (END,BOX_SIZE * i), 4)

        pygame.draw.line(win, (0, 0, 0), (BOX_SIZE * i, 0), (BOX_SIZE * i, END), 1)
        pygame.draw.line(win, (0, 0, 0), (0, BOX_SIZE * i), (END,  BOX_SIZE * i), 1)
    pygame.display.update()
    time.sleep(2)

    for i in range(0, len(base[0])):
        for j in range(0, len(base[0])):
            if base[i][j] != ".":
                s = pygame.Surface((BOX_SIZE - 4, BOX_SIZE - 4))
                s.set_alpha(230)
                s.fill((24, 252, 95))
                win.blit(s, (j * BOX_SIZE +3, i * BOX_SIZE+3,))
                value = myfont.render(str(base[i][j]), True, (255, 77, 95))
                win.blit(value, (j* BOX_SIZE + 35, i  * BOX_SIZE+ 20))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                solve(win, board)
            if event.type == pygame.QUIT:
                pygame.quit()
                return




def isvalid(board, x, y, n):
    for i in board[y]:
        if str(i) == str(n):
            return False

    for j in range(len(board)):
        if str(board[j][x]) == str(n):
            return False

    m = math.ceil((x + 1) / 3) - 1
    l = math.ceil((y + 1) / 3) - 1

    for i in range(m * 3, ((m + 1) * 3)):
        for j in range(l * 3, ((l + 1) * 3)):
            if str(board[j][i]) == str(n):
                return False
    return True

def solve(win,board):
    f = pygame.font.SysFont('Comic Sans MS', 35)
    for y in range(len(board)):
        for x in range(len(board)):
            if board[y][x] == ".":
                for t in range(1, 10):
                    if isvalid(board, x, y, t):
                        t = str(t)
                        board[y][x] = t
                        pygame.draw.rect(win, (24, 234, 95),(x * BOX_SIZE + 3, y * BOX_SIZE + 3, BOX_SIZE - 4, BOX_SIZE - 4))
                        v = f.render(t, True, original_grid_element_color)
                        win.blit(v, (x * BOX_SIZE + 35, y * BOX_SIZE+ 20))
                        pygame.display.update()
                        time.sleep(T)
                        if solve(win,board):
                            return True
                        else:
                            time.sleep(T+0.03)
                            pygame.draw.rect(win, (255,255,255),(x * BOX_SIZE + 3, y * BOX_SIZE +3, BOX_SIZE - 4, BOX_SIZE - 4))
                            v = f.render(t, True, original_grid_element_color)
                            win.blit(v, (x * BOX_SIZE + 35, y * BOX_SIZE+ 20))
                            s = pygame.Surface((BOX_SIZE - 4, BOX_SIZE - 4))
                            s.set_alpha(150)
                            s.fill((233, 77, 60))
                            win.blit(s, (x * BOX_SIZE + 3, y * BOX_SIZE + 3, ))
                            board[y][x] = "."
                            pygame.display.update()
                return False
    return True
def validator(board):
    t = len(board)
    for i in range(t):
        list = []
        for j in board[i]:
            if j != '.':     
                if j in list:
                    return False
                else:
                    list.append(j)  
    for i in range(t):
        list = []
        for j in range(t):
            if board[j][i] != '.':     
                if board[j][i] in list:
                    return False
                else:
                    list.append(board[j][i])
        
        
    def check(i,j):
        list =[]
        for t in range(3):
            for m in range(3):
                if board[i+t][j+m] != '.':
                    
                    if board[i+t][j+m] in list:
                        list.append(board[i+t][j+m])
                        print(list)
                        return False
                    else:
                        list.append(board[i+t][j+m])
        return True
                        
        
    for i in range(3):
        for j in range(3):
            if not check(i*3,j*3):
                return False
            else:
                pass 
                
    return True 

if __name__ == "__main__":
    board = eval(input())
    if validator(board):
        main(board)
    else:
        print("In valid Sudoku")
        