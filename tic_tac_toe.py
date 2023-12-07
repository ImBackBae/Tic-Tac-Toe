import pygame
def display_game_over(player):
	font = pygame.font.SysFont("sitka", 100)
	win = font.render("Player " + str(player) + " won!", True, WHITE)
	win_rect = win.get_rect(center=(WIDTH//2, HEIGHT//2))

	draw = font.render("Draw!", True, WHITE)
	draw_rect = draw.get_rect(center=(WIDTH//2, HEIGHT//2))
	
	if player == 0:
		pygame.draw.rect(screen, BLACK, draw_rect)
		screen.blit(draw, draw_rect)
	else:
		pygame.draw.rect(screen, BLACK, win_rect)
		screen.blit(win, win_rect)

def check_win(board):
	for i in range(0,3):
		if board[i][0] == board[i][1] == board[i][2] != 0:
			return board[i][0]
		elif board[0][i] == board[1][i] == board[2][i] != 0:
			return board[0][i]
			
	if board[0][0] == board[1][1] == board[2][2] != 0:
		return board[0][0]
	elif board[0][2] == board[1][1] == board[2][0] != 0:
		return board[0][2]

	elif 0 not in board[0] and 0 not in board[1] and 0 not in board[2]:
		return 0
	return -1

def update_board(pos, turn, board):
	if turn and board[pos[0]][pos[1]] == 0:
		board[pos[0]][pos[1]] = 1
		turn = not turn
	elif not turn and board[pos[0]][pos[1]] == 0:
		board[pos[0]][pos[1]] = 2
		turn = not turn
	return board, turn

def check_pos():
	mouse_x, mouse_y = pygame.mouse.get_pos()
	for i in range(3):
		for j in range(3):
			if mouse_x >= i*200 and mouse_x <= i*200 + 200 and mouse_y >= j *200 and mouse_y <= j*200 + 200:
				return (i, j)

def create_block(x, y, board):
	font = pygame.font.SysFont('sitka', 200)
	draw_x = font.render("X", True, RED)
	draw_o = font.render("O", True, BLUE)

	rect = (x*200, y*200, 200, 200)
	pygame.draw.rect(screen, BLACK, rect, 1)
	if board[x][y] == 1:
		screen.blit(draw_x, (x*200+50, y*200+40))
	elif board[x][y] == 2:
		screen.blit(draw_o, (x*200+50, y*200+40))

def main():
	pygame.init()
	global screen, WHITE, BLACK, RED, BLUE, board, WIDTH, HEIGHT
	WIDTH = 600
	HEIGHT = 600
	
	WHITE = (255,255,255)
	BLACK = (0,0,0)
	RED = (255,0,0)
	BLUE = (0,0,255)

	turn = True
	board = [[0,0,0],
			 [0,0,0],
			 [0,0,0]]

	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	running = True
	while running:
		screen.fill(WHITE)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.MOUSEBUTTONUP and check_win(board) == -1:
				pos = check_pos()
				board, turn = update_board(pos, turn, board)
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_r:
					board = [[0,0,0],
							 [0,0,0],
							 [0,0,0]]
		for i in range(3):
			for j in range(3):
				create_block(i, j, board)

		winning_player = check_win(board)
		if winning_player == 1 or winning_player == 2 or winning_player == 0:
			display_game_over(winning_player)
		pygame.display.flip()

main()