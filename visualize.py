import pygame
pygame.init()

class DrawSettings:
	BLACK = 0, 0, 0
	WHITE = 255, 255, 255
	GREEN = 0, 255, 0
	RED = 255, 0, 0
	BLUE = 0, 0, 255
	YELLOW = 255, 255, 0
	BACKGROUND_COLOR = BLACK
	DEFAULT_BLOCKS = [
		(54, 40, 128),
		(43, 28, 120)
	]
 
	SMALL_FONT = pygame.font.SysFont('arial', 25)
	FONT = pygame.font.SysFont('arial', 30)
	LARGE_FONT = pygame.font.SysFont('arial', 40)
 
	SIDE_PAD = 100
	TOP_PAD = 230
	BOT_PAD = 160

	input_rect = pygame.Rect(470, 240, 50, 32) 
	user_input = ''
	TARGET = -100
	POINT_HEIGHT = 550
 
	def __init__(self, width, height, lst):
		self.width = width
		self.height = height

		self.screen = pygame.display.set_mode((width, height))
		pygame.display.set_caption("Searching Algorithms Visualizer")
		self.set_list(lst)

	def set_list(self, lst):
		self.lst = lst

		self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
		self.block_height = (self.height - self.TOP_PAD)
		self.start_x = self.SIDE_PAD // 2


def draw(draw_setting, algo_name):
	draw_setting.screen.fill(draw_setting.BACKGROUND_COLOR)

	title = draw_setting.LARGE_FONT.render(f"Active: {algo_name}", 1, draw_setting.GREEN)
	draw_setting.screen.blit(title, (draw_setting.width/2 - title.get_width()/2 , 10))

	options = draw_setting.FONT.render("B: Binary Search, L: Linear Search, T: Ternary Search, E: Exponential Search", 1, draw_setting.WHITE)
	draw_setting.screen.blit(options, (draw_setting.width/2 - options.get_width()/2 , 60))
 
	controls = draw_setting.FONT.render("SPACE: Begin Search, R: Reset", 1, draw_setting.WHITE)
	draw_setting.screen.blit(controls, (draw_setting.width/2 - controls.get_width()/2 , 100))
	
	index = draw_setting.SMALL_FONT.render("RED: Left & right, GREEN: Midpoint(s), YELLOW: Target", 1, draw_setting.WHITE)
	draw_setting.screen.blit(index, (draw_setting.width/2 - index.get_width()/2 , 150))
 
	tgt = draw_setting.SMALL_FONT.render("%d" % draw_setting.TARGET, 1, draw_setting.YELLOW)
	draw_setting.screen.blit(tgt, (draw_setting.start_x + (draw_setting.TARGET-1) * draw_setting.block_width , draw_setting.POINT_HEIGHT))
 
	max = draw_setting.SMALL_FONT.render("150", 1, draw_setting.WHITE)
	draw_setting.screen.blit(max, (draw_setting.start_x + 147 * draw_setting.block_width , draw_setting.POINT_HEIGHT))
 
	min = draw_setting.SMALL_FONT.render("0", 1, draw_setting.WHITE)
	draw_setting.screen.blit(min, (draw_setting.start_x - 3, draw_setting.POINT_HEIGHT))
 
	enter = draw_setting.SMALL_FONT.render("Enter target value:", 1, draw_setting.WHITE)
	draw_setting.screen.blit(enter, (draw_setting.width/2 - enter.get_width()/2, 200))

	draw_list(draw_setting)
	text_surface = draw_setting.SMALL_FONT.render(draw_setting.user_input, True, (255, 255, 255))
	draw_setting.screen.blit(text_surface, (draw_setting.input_rect.x+5, draw_setting.input_rect.y+3))
	pygame.display.update()
	

def draw_list(draw_setting, color_positions={}, clear_bg=False):
	lst = draw_setting.lst

	if clear_bg:
		clear_rect = (draw_setting.SIDE_PAD//2, draw_setting.TOP_PAD, 
						draw_setting.width - draw_setting.SIDE_PAD, draw_setting.height - draw_setting.TOP_PAD - draw_setting.BOT_PAD)
	
		pygame.draw.rect(draw_setting.screen, draw_setting.BACKGROUND_COLOR, clear_rect)
		
	for i in range(len(lst)):
		x = draw_setting.start_x + i * draw_setting.block_width
		y = 300
  
		color = draw_setting.DEFAULT_BLOCKS[i % 2]

		if i in color_positions:
			color = color_positions[i] 

		pygame.draw.rect(draw_setting.screen, color, (x, y, draw_setting.block_width, draw_setting.height - 350), border_radius=10)
		pygame.draw.rect(draw_setting.screen, (96, 154, 179), draw_setting.input_rect) 
	if clear_bg:
		pygame.display.update()
  