from visualize import draw_list

def binary_search(draw_setting, target) -> int:
    lst = draw_setting.lst
    l, r = 0, len(lst) - 1
    while l <= r:
        m = (l + r) // 2 
        draw_list(draw_setting, {lst[l]: draw_setting.RED, lst[r]: draw_setting.RED, target: draw_setting.YELLOW, lst[m]: draw_setting.GREEN}, True)
        yield True
        if lst[m] > target:
            r = m - 1
        elif lst[m] < target:
            l = m + 1
        else:
            return m
    return -1

def ternary_search(draw_setting, target):
    lst = draw_setting.lst
    l, r = 0, len(lst) - 1
    while r >= l:
        mid1 = l + (r-l) // 3
        mid2 = r - (r-l) // 3
        draw_list(draw_setting, {lst[l]: draw_setting.RED, lst[r]: draw_setting.RED, target: draw_setting.YELLOW, lst[mid1]: draw_setting.GREEN, lst[mid2]: draw_setting.GREEN}, True)
        yield True
        if target == lst[mid1]:
            return mid1
        if target == lst[mid2]:
            return mid2
        if target < lst[mid1]:
            r = mid1 - 1
        elif target > lst[mid2]:
            l = mid2 + 1
        else:
            l = mid1 + 1
            r = mid2 - 1
    return -1

def exponential_search(draw_setting, target):
	lst = draw_setting.lst
	if lst[0] == target:
		return 0

	n = len(lst)
	i = 1
	while i < n and lst[i] <= target:
		draw_list(draw_setting, {lst[i]: draw_setting.RED, target: draw_setting.YELLOW}, True)
		yield True
		i *= 2

	low = i // 2
	high = min(i, n - 1)

	while low <= high:
		mid = (low + high) // 2
		draw_list(draw_setting, {lst[low]: draw_setting.RED, lst[high]: draw_setting.RED, target: draw_setting.YELLOW, lst[mid]: draw_setting.GREEN}, True)
		yield True
		if lst[mid] == target:
			return mid
		elif lst[mid] < target:
			low = mid + 1
		else:
			high = mid - 1

	return -1
    
def linear_search(draw_setting, target): 
    lst = draw_setting.lst
    for i in range(len(lst)): 
        draw_list(draw_setting, {lst[i]: draw_setting.RED, target: draw_setting.YELLOW}, True)
        yield True
        if (lst[i] == target): 
            return i 
    return -1