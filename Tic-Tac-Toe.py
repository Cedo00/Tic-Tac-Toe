import tkinter
import tkinter.messagebox

# 输入顺序标志
order_flag = 1  # 1表示X输入，0表示O输入
# 输入次序标志
number_flag = 0
# X的输入
X_set = set()
# O的输入
O_set = set()

# 按钮触发事件
def submit():
	global order_flag
	global number_flag

	# 获得输入框内容
	in_char = entry.get()
	print("in_char = ", in_char)

	# 循环输入
	if 0 <= int(in_char) and int(in_char) <= 9:
		if order_flag == 1:  # 输入到X集合中
			if in_char not in X_set and in_char not in O_set:
				# X集合操作
				X_set.add(in_char)
				draw_X(in_char)
				# 其他操作
				order_flag = 0
				text.insert(1.0,'O-turn')
				number_flag += 1
		else:  # 输入到O集合中
			if in_char not in X_set and in_char not in O_set:
				# O集合操作
				O_set.add(in_char)
				draw_O(in_char)
				# 其他操作
				order_flag = 1
				text.insert(1.0,'X-turn')
				number_flag += 1

	# 判断是否胜利
	if is_win(X_set):
		tkinter.messagebox.showinfo("Tic-Tac-Toe", "X win !!!")
		# print("X win !!")
		root.destroy()
		return
	if is_win(O_set):
		tkinter.messagebox.showinfo("Tic-Tac-Toe", "O win !!!")
		# print("O win !!")
		root.destroy()
		return

	# 判断棋盘是否已满
	# print("number = ", number_flag)
	if number_flag >= 9:
		tkinter.messagebox.showwarning("Tic-Tac-Toe", "The chess board is full!")
		# print("full")
		root.destroy()
		return


# 判断胜利
def is_win(chess_set):
	if '1' in chess_set and '2' in chess_set and '3' in chess_set:
		return True
	elif '4' in chess_set and '5' in chess_set and '6' in chess_set:
		return True
	elif '7' in chess_set and '8' in chess_set and '9' in chess_set:
		return True
	elif '1' in chess_set and '4' in chess_set and '7' in chess_set:
		return True
	elif '2' in chess_set and '5' in chess_set and '8' in chess_set:
		return True
	elif '3' in chess_set and '6' in chess_set and '9' in chess_set:
		return True
	elif '1' in chess_set and '5' in chess_set and '9' in chess_set:
		return True
	elif '3' in chess_set and '5' in chess_set and '7' in chess_set:
		return True
	else:
		return False


# 画圆
def draw_O(in_char):
	xy = find_xy(in_char)
	# print("xy = ", xy)
	canvas.create_arc(xy[0]+10, xy[1]+10, xy[0]+90, xy[1]+90, extent=359)


# 画叉
def draw_X(in_char):
	xy = find_xy(in_char)
	# print("xy = ", xy)
	canvas.create_line(xy[0]+10, xy[1]+10, xy[0]+90, xy[1]+90)
	canvas.create_line(xy[0]+90, xy[1]+10, xy[0]+10, xy[1]+90)


# 寻找坐标
def find_xy(in_char):
	if in_char == '1':
		return (0, 0)
	elif in_char == '2':
		return (100, 0)
	elif in_char == '3':
		return (200, 0)
	elif in_char == '4':
		return (0, 100)
	elif in_char == '5':
		return (100, 100)
	elif in_char == '6':
		return (200, 100)
	elif in_char == '7':
		return (0, 200)
	elif in_char == '8':
		return (100, 200)
	elif in_char == '9':
		return (200, 200)


# 设置根窗口
root = tkinter.Tk()
root.title("Tic-Tac-Toe")
# 固定窗口大小
root.maxsize(300, 350)
root.minsize(300, 350)

# 创建画布
canvas = tkinter.Canvas(root, width=300, height=300)
# 两条竖线
canvas.create_line(100, 0, 100, 300)
canvas.create_line(200, 0, 200, 300)
# 两条横线
canvas.create_line(0, 100, 300, 100)
canvas.create_line(0, 200, 300, 200)
canvas.pack()

# 设置文本框
text = tkinter.Text(root, width=10, height=1)
text.place(anchor='sw', x=0, y=350)
text.insert(1.0,'X-turn')

# 设置输入框
entry = tkinter.Entry(root, width=10)
entry.place(anchor='s', x=100, y=350)

# 设置按钮
button = tkinter.Button(root, text="submit", command=submit)
button['width'] = 10
button['height'] = 1
# 按钮位置
button.place(anchor='se', x=300, y=350)

root.mainloop()

