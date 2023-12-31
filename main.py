import pygame
from searching_algorithms import binary_search, exponential_search, linear_search, ternary_search
from visualize import DrawSettings, draw

def main():

	run = True
	clock = pygame.time.Clock()

	n = 150

	lst = [i for i in range(n)]
	draw_setting = DrawSettings(1000, 600, lst)
	searching = False

	searching_algorithm = binary_search
	algo_name = "Binary Search"
	searching_algorithm_generator = None

	while run:
		clock.tick(1)

		if searching:
			try:
				next(searching_algorithm_generator)
			except StopIteration:
				searching = False
		else:
			draw(draw_setting, algo_name)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			      
			if event.type != pygame.KEYDOWN:
				continue

			if event.key == pygame.K_r:
				searching = False
			elif event.key == pygame.K_SPACE and searching == False:
				searching = True
				searching_algorithm_generator = searching_algorithm(draw_setting, draw_setting.TARGET)
			elif event.key == pygame.K_b and not searching:
				searching_algorithm = binary_search
				algo_name = "Binary Search"
			elif event.key == pygame.K_l and not searching:
				searching_algorithm = linear_search
				algo_name = "Linear Search"
			elif event.key == pygame.K_t and not searching:
				searching_algorithm = ternary_search
				algo_name = "Ternary Search"
			elif event.key == pygame.K_e and not searching:
				searching_algorithm = exponential_search
				algo_name = "Exponential Search"
			elif event.key == pygame.K_BACKSPACE: 
				draw_setting.user_input = draw_setting.user_input[:-1] 
			elif event.key == pygame.K_RETURN:
				draw_setting.TARGET = int(draw_setting.user_input)
			else:
				draw_setting.user_input += event.unicode
		
	pygame.quit()

if __name__ == "__main__":
	main()