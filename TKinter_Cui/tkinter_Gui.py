import tkinter as tk
import tkinter.messagebox

window = tk.Tk()
window.title('微信好友分析器')
window.geometry('800x600')


# 这里是窗口的内容
# l = tk.Label(window,
#     text='Hello TK!',    # 标签的文字
#     bg='blue',     # 背景颜色
#     font=('Arial', 12),     # 字体和字体大小
#     width=15, height=2  # 标签长宽
#     )
# l.pack()    # 固定窗口位置

#Label & Buttom基本使用方法
#
# var = tk.StringVar()    # 文字变量储存器
# l = tk.Label(window,
#     textvariable=var,   # 使用 textvariable 替换 text, 因为这个可以变化
#     bg='green', font=('Arial', 12), width=15, height=2)
# l.pack()
#
# on_hit = False  # 默认初始状态为 False
# def hit_me():
#     global on_hit
#     if on_hit == False:     # 从 False 状态变成 True 状态
#         on_hit = True
#         var.set('you hit me')   # 设置标签的文字为 'you hit me'
#     else:       # 从 True 状态变成 False 状态
#         on_hit = False
#         var.set('') # 设置 文字为空
#
# b = tk.Button(window,
#     text='hit me',      # 显示在按钮上的文字
#     width=15, height=2,
#     command=hit_me)     # 点击按钮式执行的命令
# b.pack()    # 按钮位置

#Entry & Text基本使用方法
#
# def insert_point():
#     var = e.get()
#     t.insert('insert',var)
#
# def insert_end():
#     var = e.get()
#     t.insert('end',var)
#
# b1 = tk.Button(window,text="insert point",width=15,height=2,command=insert_point)
# b1.pack()
#
# b2 = tk.Button(window,text="insert end",command=insert_end)
# b2.pack()
# e = tk.Entry(window,show='*')
# e.pack()
# t = tk.Text(window,height=2)
# t.pack()

#Listbox 基本使用方法
# var2 = tk.StringVar()
# var2.set((11,22,33,44)) #为变量设置值
#
# #创建Listbox
#
# lb = tk.Listbox(window, listvariable=var2)  #将var2的值赋给Listbox

#创建一个list并将值循环添加到Listbox控件中
# list_items = [1,2,3,4]
# for item in list_items:
#     lb.insert('end', item)  #从最后一个位置开始加入值
# lb.insert(1, 'first')       #在第一个位置加入'first'字符
# lb.insert(2, 'second')      #在第二个位置加入'second'字符
# lb.delete(2)                #删除第二个位置的字符
# lb.pack()
#
# var1 = tk.StringVar()    #创建变量
# l =tk.Label(window,bg='yellow',width=4,textvariable=var1)
# l.pack()
# def print_selection():
#     value = lb.get(lb.curselection())   #获取当前选中的文本
#     var1.set(value)     #为label设置值
# def print_selection():
#     value = lb.get(lb.curselection())   #获取当前选中的文本
#     var1.set(value)     #为label设置值
# b1 = tk.Button(window, text='print selection', width=15,
#               height=2, command=print_selection)
# b1.pack()

#RadioButton基本使用方法
# var = tk.StringVar()
# l = tk.Label(window, bg='yellow', width=20, text='empty')
# l.pack()
# def print_selection():
#     l.config(text='you have selected ' + var.get())
#
# r1 = tk.Radiobutton(window, text='Option A',
#                     variable=var, value='A',
#                     command=print_selection)
# r2 = tk.Radiobutton(window, text='Option B',
#                     variable=var, value='B',
#                     command=print_selection)
# r1.pack()
# r2.pack()

#Scale尺度 基本使用方法
# l = tk.Label(window, bg='yellow', width=20, text='empty')
# l.pack()
# def print_selection(v):
#     l.config(text='you have selected ' + v)
# s = tk.Scale(window, label = 'try me',from_=5,to=11,orient = tk.HORIZONTAL,
#              length= 200,showvalue= True,tickinter = 3,resolution= 0.01,command= print_selection)
# s.pack()

#CheckButton 基本使用方法 所有的都可以被勾选
# def print_selection():
#     if (var1.get() == 1) & (var2.get() == 0):   #如果选中第一个选项，未选中第二个选项
#         l.config(text='I love only Python ')
#     elif (var1.get() == 0) & (var2.get() == 1): #如果选中第二个选项，未选中第一个选项
#         l.config(text='I love only C++')
#     elif (var1.get() == 0) & (var2.get() == 0):  #如果两个选项都未选中
#         l.config(text='I do not love either')
#     else:
#         l.config(text='I love both')
# var1 = tk.IntVar()
# var2 = tk.IntVar()
# c1 = tk.Checkbutton(window, text = 'Python',variable = var1,onvalue = 1,offvalue = 0,
#                     command = print_selection)
# c2 = tk.Checkbutton(window, text = 'C++',variable = var2,onvalue = 1,offvalue = 0,
#                     command = print_selection)
# c1.pack()
# c2.pack()

#Canvas 画布 基本使用方法
# canvas = tk.Canvas(window, bg='blue', height=100, width=200)
# image_file = tk.PhotoImage(file='ins.gif')
# image = canvas.create_image(10, 10, anchor='nw', image=image_file)
# x0, y0, x1, y1= 50, 50, 80, 80
# line = canvas.create_line(x0, y0, x1, y1)
# oval = canvas.create_oval(x0, y0, x1, y1, fill='red')
# arc = canvas.create_arc(x0+30, y0+30, x1+30, y1+30, start=0, extent=180)
# rect = canvas.create_rectangle(100, 30, 100+20, 30+20)
# canvas.pack()
#
# def moveit():
#     canvas.move(rect, 0, 2)
#
# b = tk.Button(window, text='move', command=moveit).pack()


#Menubar 基本使用方法
# l = tk.Label(window, text='', bg='yellow')
# l.pack()
# counter = 0
# def do_job():
#     global counter
#     l.config(text='do '+ str(counter))
#     counter+=1
#
# menubar = tk.Menu(window)
# filemenu = tk.Menu(menubar, tearoff=0)
# menubar.add_cascade(label='File', menu=filemenu)
# filemenu.add_command(label='New', command=do_job)
# filemenu.add_command(label='Open', command=do_job)
# filemenu.add_command(label='Save', command=do_job)
# filemenu.add_separator()
# filemenu.add_command(label='Exit', command=window.quit)
#
# editmenu = tk.Menu(menubar, tearoff=0)
# menubar.add_cascade(label='Edit', menu=editmenu)
# editmenu.add_command(label='Cut', command=do_job)
# editmenu.add_command(label='Copy', command=do_job)
# editmenu.add_command(label='Paste', command=do_job)
#
# submenu = tk.Menu(filemenu)
# filemenu.add_cascade(label='Import', menu=submenu, underline=0)
# submenu.add_command(label="Submenu1", command=do_job)
#
# window.config(menu=menubar) #

#Frame 框架应用
# tk.Label(window,text = 'on the window').pack()
# frm = tk.Frame(window).pack()
# frm_I = tk.Frame(frm,)
# frm_r = tk.Frame(frm,)
# frm_I.pack(side = 'left')
# frm_r.pack(side = 'right')
# tk.Label(frm_I,text='on the frm_I1').pack()
# tk.Label(frm_I,text='on the frm_I2').pack()
# tk.Label(frm_r, text='on the frm_r1').pack()  ##这个`label`长在`frm_r`上，显示为`on the frm_r1`

#messagebox 弹窗基本应用
# def hit_me():
#    tk.messagebox.showinfo(title='Hi', message='hahahaha')
# tk.messagebox.showinfo(title='',message='')#提示信息对话窗
# tk.messagebox.showwarning()#提出警告对话窗
# tk.messagebox.showerror()#提出错误对话窗
# tk.messagebox.askquestion()#询问选择对话窗
# print(tk.messagebox.askquestion())  # 返回yes和no
# print(tk.messagebox.askokcancel())  # 返回true和false
# print(tk.messagebox.askyesno())  # 返回true和false
# print(tk.messagebox.askretrycancel())  # 返回true和false
#
# tk.Button(window, text='hit me', command=hit_me).pack()

# pack()  grid() place()  放置使用
# canvas = tk.Canvas(window, height=150, width=500)
# canvas.grid(row=1, column=1)
# image_file = tk.PhotoImage(file='./welcome.gif')
# image = canvas.create_image(0, 0, anchor='nw', image=image_file)
#
# tk.Label(window, text='1').pack(side='top')
# tk.Label(window, text='1').pack(side='bottom')
# tk.Label(window, text='1').pack(side='left')
# tk.Label(window, text='1').pack(side='right')

# for i in range(4):
#     for j in range(3):
#         tk.Label(window, text=1).grid(row=i, column=j, padx=10, pady=10)

# tk.Label(window, text=1).place(x=20, y=10, anchor='nw')



window.mainloop()