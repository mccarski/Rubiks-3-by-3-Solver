import tkinter
from tkinter import messagebox, Frame, Text, Scrollbar, Button, Canvas, Tk, Menu, Label, Widget
import controller

num_rows = 3
num_cols = 3
square_dim = 64
colour_map = {'r': 'red', 'w': 'white', 'o': 'orange',
              'y': 'yellow', 'g': 'green', 'b': 'blue'}


class View():

    def __init__(self, parent, controller):
        self.parent = parent
        self.controller = controller
        self.draw_rubiks_init()
        self.draw_canvas_faces_init()
        self.input_order = [False, False, False, False, False]
        self.count = 0

    def draw_rubiks_init(self):
        self.create_top_menu_init()
        self.create_canvas_init()
        self.create_turn_bar_init()
        self.create_moves_text_frame_init()
        self.create_solved_text_frame_init()
        self.create_label_moves_init()
        self.create_colour_selecter_init()

    def create_colour_selecter_init(self):
        self.frame6 = Frame(self.parent)
        self.frame6.grid(row=3, column=0, sticky='NESW')

        self.ButtonV = Button(self.frame6,  text='White',
                              command=self.change_colour_white, height=2)
        self.ButtonV.grid(row=0, column=0, sticky='NESW')
        self.ButtonW = Button(self.frame6,  text='Red',
                              command=self.change_colour_red, height=2)
        self.ButtonW.grid(row=0, column=1, sticky='NESW')
        self.ButtonX = Button(self.frame6,  text='Yellow',
                              command=self.change_colour_yellow, height=2)
        self.ButtonX.grid(row=0, column=2, sticky='NESW')
        self.ButtonY = Button(self.frame6,  text='Orange',
                              command=self.change_colour_orange, height=2)
        self.ButtonY.grid(row=1, column=0, sticky='NESW')
        self.ButtonZ = Button(self.frame6,  text='Blue',
                              command=self.change_colour_blue, height=2)
        self.ButtonZ.grid(row=1, column=1, sticky='NESW')
        self.ButtonZ = Button(self.frame6,  text='Green',
                              command=self.change_colour_green, height=2)
        self.ButtonZ.grid(row=1, column=2, sticky='NESW')
        self.ButtonZ = Button(self.frame6,  text='Check if Possible',
                              command=self.check_all_faces_if_theoritically_possible, height=2)
        self.ButtonZ.grid(row=2, column=0, sticky='NESW')

    def check_all_faces_if_theoritically_possible(self):
        possible = self.controller.check_all_faces_if_theoritically_possible()
        if possible is True:
            messagebox.showinfo("", "Is possible configuration.")
        else:
            messagebox.showinfo(
                "", "Is not possible configuration.\nMay crash if attempting to solve")
        return possible

    def create_top_menu_init(self):
        self.menu_bar = Menu(self.parent)
        self.create_file_menu()
        self.create_about_menu()

    def create_file_menu(self):
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(
            label='Reset Cube', command=self.reset_upd)
        self.file_menu.add_command(
            label='Help', command=self.help)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        self.parent.config(menu=self.menu_bar)

    def create_about_menu(self):
        self.about_menu = Menu(self.menu_bar, tearoff=0)
        self.about_menu.add_command(
            label='About', command=self.on_about_menu_selected)
        self.menu_bar.add_cascade(label="About", menu=self.about_menu)
        self.parent.config(menu=self.menu_bar)

    def on_about_menu_selected(self):
        messagebox.showinfo("", "McCarthy \nRubik\'s Cube Solver")

    def create_canvas_init(self):
        self.l_face_canvas = self.create_individual_canvas(2, 1)
        self.f_face_canvas = self.create_individual_canvas(2, 2)
        self.r_face_canvas = self.create_individual_canvas(2, 3)
        self.b_face_canvas = self.create_individual_canvas(0, 2)
        self.t_face_canvas = self.create_individual_canvas(1, 2)
        self.bo_face_canvas = self.create_individual_canvas(3, 2)

    def create_individual_canvas(self, r, c):

        canvas_width = num_cols*square_dim
        canvas_height = num_rows*square_dim
        self.canvas = Canvas(self.parent, width=canvas_width,
                             height=canvas_height)
        self.canvas.grid(row=r, column=c, sticky='NESW')
        return self.canvas

    def create_turn_bar_init(self):
        self.frame = Frame(self.parent)
        self.frame.grid(row=0, column=0, sticky='NESW')

        self.ButtonB = Button(self.frame, text="Front", command=self.front, height=2)
        self.ButtonB.grid(row=0, column=0,  sticky='NSEW')
        self.ButtonC = Button(self.frame, text="Front Prime", command=self.frontprime, height=2)
        self.ButtonC.grid(row=0, column=1,  sticky='NSEW')
        self.ButtonD = Button(self.frame, text="Up", command=self.top, height=2)
        self.ButtonD.grid(row=1, column=0, sticky='NSEW')
        self.ButtonE = Button(self.frame, text="Up Prime", command=self.topprime, height=2)
        self.ButtonE.grid(row=1, column=1,  sticky='NSEW')
        self.ButtonF = Button(self.frame, text="Back", command=self.back,  height=2)
        self.ButtonF.grid(row=2, column=0,  sticky='NSEW')
        self.ButtonG = Button(self.frame, text="Back Prime", command=self.backprime, height=2)
        self.ButtonG.grid(row=2, column=1,  sticky='NSEW')

        self.ButtonH = Button(self.frame, text="Down", command=self.bottom,  height=2)
        self.ButtonH.grid(row=0, column=2,  sticky='NSEW')
        self.ButtonI = Button(self.frame, text="Down Prime", command=self.bottomprime,  height=2)
        self.ButtonI.grid(row=0, column=3,  sticky='NSEW')
        self.ButtonJ = Button(self.frame, text="Left", command=self.left,  height=2)
        self.ButtonJ.grid(row=1, column=2,  sticky='NSEW')
        self.ButtonK = Button(self.frame, text="Left Prime", command=self.leftprime, height=2)
        self.ButtonK.grid(row=1, column=3,  sticky='NSEW')
        self.ButtonL = Button(self.frame, text="Right", command=self.right,  height=2)
        self.ButtonL.grid(row=2, column=2,  sticky='NSEW')
        self.ButtonM = Button(self.frame, text="Right Prime", command=self.rightprime, height=2)
        self.ButtonM.grid(row=2, column=3,  sticky='NSEW')

        self.frame3 = Frame(self.parent)
        self.frame3.grid(row=3, column=3, sticky='NESW')

        self.ButtonN = Button(self.frame3, text="Reset", command=self.reset_upd, height=2, width=15)
        self.ButtonN.grid(row=0, column=0, sticky='NSEW')
        self.ButtonO = Button(self.frame3, text="Scramble",
                              command=self.scramble, height=2, width=15)
        self.ButtonO.grid(row=1, column=0, sticky='NSEW')
        self.ButtonP = Button(self.frame3, text="1. Down Edges",
                              command=self.solve_cross_bottom, height=2, width=15)
        self.ButtonP.grid(row=2, column=0, sticky='NSEW')
        self.ButtonQ = Button(self.frame3, text="2. Down Corners",
                              command=self.solve_corner_bottom, height=2, width=15)
        self.ButtonQ.grid(row=3, column=0, sticky='NSEW')
        self.ButtonR = Button(self.frame3, text="3. Middle Edges",
                              command=self.solve_edges_middle_control, height=2, width=15)
        self.ButtonR.grid(row=0, column=1, sticky='NSEW')
        self.ButtonT = Button(self.frame3, text="4. Up Edges",
                              command=self.solve_edges_top_control, height=2, width=15)
        self.ButtonT.grid(row=1, column=1, sticky='NSEW')
        self.ButtonU = Button(self.frame3, text="5. Up Corners",
                              command=self.solve_corners_top_control, height=2, width=15)
        self.ButtonU.grid(row=2, column=1, sticky='NSEW')
        self.ButtonV = Button(self.frame3, text="6. Up Corners Final",
                              command=self.solve_final_control, height=2, width=15)
        self.ButtonV.grid(row=3, column=1, sticky='NSEW')

    def create_moves_text_frame_init(self):
        self.frame4 = Frame(self.parent)
        self.frame4.grid(row=0, column=1, rowspan=2, columnspan=1, sticky='NW')

        self.my_text = Text(self.frame4, width=21, bg='lightgrey', wrap=tkinter.WORD)
        self.my_text.pack(side=tkinter.LEFT, fill=tkinter.X, padx=2)

        self.X = tkinter.StringVar()
        self.create_bottom_text_frame_upd()

        self.scrollbar = Scrollbar(self.frame4, orient=tkinter.VERTICAL, command=self.my_text.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.my_text.configure(yscrollcommand=self.scrollbar.set)

    def create_bottom_text_frame_upd(self):
        self.X.set('Prints outputs')
        self.my_text.delete(1.0, tkinter.END)
        self.my_text.insert(tkinter.END,  self.X.get())
        self.X.set('')

    def create_solved_text_frame_init(self):
        self.frame5 = Frame(self.parent)
        self.frame5.grid(row=0, column=3, rowspan=2, columnspan=1,  sticky='NW')

        self.my_text1 = Text(self.frame5, bg='lightgrey', width=60, wrap=tkinter.WORD)
        self.my_text1.pack(side=tkinter.LEFT, fill=tkinter.X, padx=2)

        self.Y = tkinter.StringVar()
        self.create_top_text_frame_upd()

        self.scrollbar1 = Scrollbar(self.frame5, orient=tkinter.VERTICAL,
                                    command=self.my_text1.yview)
        self.scrollbar1.pack(side="right", fill="y")
        self.my_text1.configure(yscrollcommand=self.scrollbar1.set)

    def create_top_text_frame_upd(self):
        self.Y.set('Prints only solution outputs')
        self.my_text1.delete(1.0, tkinter.END)
        self.my_text1.insert(tkinter.END,  self.Y.get())
        self.Y.set('')

    def draw_canvas_faces_init(self):
        self.controller.get_postions()
        self.draw_canvas_face(self.f_face_canvas, self.controller.f)
        self.draw_canvas_face(self.t_face_canvas, self.controller.t)
        self.draw_canvas_face(self.b_face_canvas, self.controller.b)
        self.draw_canvas_face(self.bo_face_canvas, self.controller.bo)
        self.draw_canvas_face(self.l_face_canvas, self.controller.l)
        self.draw_canvas_face(self.r_face_canvas, self.controller.r)

        self.f_face_canvas.bind("<Button-1>", self.on_square_clicked)
        self.t_face_canvas.bind("<Button-1>", self.on_square_clicked)
        self.b_face_canvas.bind("<Button-1>", self.on_square_clicked)
        self.bo_face_canvas.bind("<Button-1>", self.on_square_clicked)
        self.l_face_canvas.bind("<Button-1>", self.on_square_clicked)
        self.r_face_canvas.bind("<Button-1>", self.on_square_clicked)

    def create_label_moves_init(self):
        self.var = tkinter.StringVar()
        self.var.set('Number of moves: {}'.format(self.controller.get_total_moves()))
        self.label = Label(self.parent, textvariable=self.var)
        self.label.grid(row=3, column=1, sticky='NE')

    #####################################

    def reset_upd(self):
        self.input_order = [False, False, False, False, False]
        self.controller.__init__()
        self.draw_canvas_all_face_upd()
        self.document_clear()
        self.create_bottom_text_frame_upd()
        self.create_top_text_frame_upd()
        self.create_label_upd()

    def help(self):
        messagebox.showinfo(
            "", "Can setup unsolved position using colour buttons. \nClicking buttons 1. 2. 3. etc sequentially will solve cube. \nCube centers have to match shown layout (front=white, left=blue, right=green, top=red, back=yellow, bottom=orange). \nIf not switch colours when inputting unsolved position.")

    def draw_canvas_all_face_upd(self):
        self.controller.get_postions()
        self.b_face_canvas.delete(tkinter.ALL)
        self.t_face_canvas.delete(tkinter.ALL)
        self.f_face_canvas.delete(tkinter.ALL)
        self.bo_face_canvas.delete(tkinter.ALL)
        self.l_face_canvas.delete(tkinter.ALL)
        self.r_face_canvas.delete(tkinter.ALL)

        self.draw_canvas_face(self.t_face_canvas, self.controller.t)
        self.draw_canvas_face(self.b_face_canvas, self.controller.b)
        self.draw_canvas_face(self.f_face_canvas, self.controller.f)
        self.draw_canvas_face(self.bo_face_canvas, self.controller.bo)
        self.draw_canvas_face(self.l_face_canvas, self.controller.l)
        self.draw_canvas_face(self.r_face_canvas, self.controller.r)

        self.f_face_canvas.bind("<Button-1>", self.on_square_clicked)
        self.t_face_canvas.bind("<Button-1>", self.on_square_clicked)
        self.b_face_canvas.bind("<Button-1>", self.on_square_clicked)
        self.bo_face_canvas.bind("<Button-1>", self.on_square_clicked)
        self.l_face_canvas.bind("<Button-1>", self.on_square_clicked)
        self.r_face_canvas.bind("<Button-1>", self.on_square_clicked)

    def document_clear(self):
        # file = open('textcontext.txt', 'w').close()
        # self.my_text.delete(1.0, tkinter.END)
        pass

    def create_label_upd(self):
        self.var.set('Number of moves: {}'.format(self.controller.get_total_moves()))

    def scramble(self):
        self.input_order = [False, False, False, False, False]
        self.controller.scramble_controller()
        self.draw_canvas_all_face_upd()
        self.list_of_moves_upd()
        self.create_bottom_frame_upd()
        self.create_label_upd()

    def on_square_clicked(self, event):
        clicked_row, clicked_column = self.get_clicked_row_column(event)
        a = str(event.widget)
        colour = self.get_colour_selected()
        print("Clicked on", clicked_row, clicked_column)
        if '.!canvas' == a and colour != None:
            face = 'l'
            self.controller.colour_changer(clicked_row, clicked_column, colour, face)
            self.draw_canvas_all_face_upd()

        if '.!canvas2' == a and colour != None:
            face = 'f'
            self.controller.colour_changer(clicked_row, clicked_column, colour, face)
            self.draw_canvas_all_face_upd()

        if '.!canvas3' == a and colour != None:
            face = 'r'
            self.controller.colour_changer(clicked_row, clicked_column, colour, face)
            self.draw_canvas_all_face_upd()

        if '.!canvas4' == a and colour != None:
            face = 'b'
            self.controller.colour_changer(clicked_row, clicked_column, colour, face)
            self.draw_canvas_all_face_upd()

        if '.!canvas5' == a and colour != None:
            face = 't'
            self.controller.colour_changer(clicked_row, clicked_column, colour, face)
            self.draw_canvas_all_face_upd()

        if '.!canvas6' == a and colour != None:
            face = 'bo'
            self.controller.colour_changer(clicked_row, clicked_column, colour, face)
            self.draw_canvas_all_face_upd()

    def draw_canvas_face(self, canvas_face, positions):
        for row in range(num_rows):
            for col in range(num_cols):
                colour = self.get_colour(positions, row, col)

                x1, y1 = self.get_x_y_coord(row, col)
                x2, y2 = x1+square_dim, y1+square_dim
                canvas_face.create_rectangle(
                    x1, y1, x2, y2,  fill=colour)

    def draw_canvas_face_back(self, canvas_face, positions):
        row_col_convertor = {(0, 0): (2, 2), (0, 1): (2, 1), (0, 2): (2, 0),
                             (1, 0): (1, 2), (1, 1): (1, 1), (1, 2): (1, 0),
                             (2, 0): (0, 2), (2, 1): (0, 1), (2, 2): (0, 0)}

        for row in range(num_rows):
            for col in range(num_cols):
                colour = self.get_colour(positions, row, col)
                row_upd, col_upd = row_col_convertor[row, col]
                x1, y1 = self.get_x_y_coord(row_upd, col_upd)
                x2, y2 = x1+square_dim, y1+square_dim
                canvas_face.create_rectangle(
                    x1, y1, x2, y2,  fill=colour)

    def get_clicked_row_column(self, event):
        clicked_column = event.x // square_dim
        clicked_row = event.y // square_dim
        return (clicked_row, clicked_column)

    def get_colour(self, positions, row, col):
        colour = positions[row][col]
        colour = colour_map[colour]
        return colour

    def get_x_y_coord(self, row, col):
        x = (col*square_dim)
        y = (row*square_dim)

        return(x, y)

    def list_of_moves_upd(self):
        # file = open('textcontext.txt', 'w')
        # moves = self.controller.get_info_moves()
        # text = ''
        # text = ',   '.join(moves)
        # file.write(text)
        # file.close()
        pass

        moves = self.controller.get_info_moves()
        self.text = ''
        self.text = ',  '.join(moves)

    def create_bottom_frame_upd(self):
        self.X.set(self.text)
        self.my_text.delete(1.0, tkinter.END)
        self.my_text.insert(tkinter.END,  self.X.get())
        self.X.set('')

    def create_top_frame_upd(self):
        solved = self.controller.get_solved_moves()
        self.Y.set(' '.join(solved))
        self.my_text1.delete(1.0, tkinter.END)
        self.my_text1.insert(tkinter.END,  self.Y.get())
        self.Y.set('')

    def change_colour_white(self):
        self.colour = 'w'

    def change_colour_red(self):
        self.colour = 'r'

    def change_colour_yellow(self):
        self.colour = 'y'

    def change_colour_orange(self):
        self.colour = 'o'

    def change_colour_blue(self):
        self.colour = 'b'

    def change_colour_green(self):
        self.colour = 'g'

    def get_colour_selected(self):
        try:
            self.colour
        except:
            self.colour = None
        return self.colour
        #####################################

    def solve_cross_bottom(self):
        if self.input_order != [False, False, False, False, False]:
            messagebox.showinfo("", "Solving functions should be used in order 1. 2. 3. etc.")
            return
        self.input_order[0] = True
        self.controller.solve_cross_bottom_control()
        self.update_moves_gui()

    def solve_corner_bottom(self):
        if self.input_order != [True, False, False, False, False]:
            messagebox.showinfo("", "Solving functions should be used in order 1. 2. 3. etc.")
            return
        self.input_order[1] = True
        self.controller.solve_corners_bottom_control()
        self.update_moves_gui()

    def solve_edges_middle_control(self):
        if self.input_order != [True, True, False, False, False]:
            messagebox.showinfo("", "Solving functions should be used in order 1. 2. 3. etc.")
            return
        self.input_order[2] = True
        self.controller.solve_edges_middle_control()
        self.update_moves_gui()

    def solve_edges_top_control(self):
        if self.input_order != [True, True, True, False, False]:
            messagebox.showinfo("", "Solving functions should be used in order 1. 2. 3. etc.")
            return
        self.input_order[3] = True
        self.controller.solve_edges_top_control()
        self.update_moves_gui()

    def solve_corners_top_control(self):
        if self.input_order != [True, True, True, True, False]:
            messagebox.showinfo("", "Solving functions should be used in order 1. 2. 3. etc.")
            return
        self.input_order[4] = True
        self.controller.solve_corners_top_control()
        self.update_moves_gui()

    def solve_final_control(self):
        if self.input_order != [True, True, True, True, True]:
            messagebox.showinfo("", "Solving functions should be used in order 1. 2. 3. etc.")
            return
        self.controller.solve_final_control()
        self.update_moves_gui()

    #####################################

    def front(self):
        self.controller.ff()
        self.update_moves_gui()

    def frontprime(self):
        self.controller.ffp()
        self.update_moves_gui()

    def top(self):
        self.controller.tt()
        self.update_moves_gui()

    def topprime(self):
        self.controller.ttp()
        self.update_moves_gui()

    def back(self):
        self.controller.bb()
        self.update_moves_gui()

    def backprime(self):
        self.controller.bbp()
        self.update_moves_gui()

    def bottom(self):
        self.controller.bbo()
        self.update_moves_gui()

    def bottomprime(self):
        self.controller.bbop()
        self.update_moves_gui()

    def left(self):
        self.controller.ll()
        self.update_moves_gui()

    def leftprime(self):
        self.controller.llp()
        self.update_moves_gui()

    def right(self):
        self.controller.rr()
        self.update_moves_gui()

    def rightprime(self):
        self.controller.rrp()
        self.update_moves_gui()

    def update_moves_gui(self):
        self.draw_canvas_all_face_upd()
        self.list_of_moves_upd()
        self.create_bottom_frame_upd()
        self.create_top_frame_upd()
        self.create_label_upd()


def main(controller):
    root = Tk()
    root.title("Rubik\'s Cube 3x3")
    View(root, controller)
    root.mainloop()


def init_new_game():
    game_controller = controller.Controller()
    main(game_controller)


if __name__ == "__main__":
    init_new_game()
