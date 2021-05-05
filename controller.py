import rubiks


class Controller():

    def __init__(self):
        self.rubiks = rubiks.Rubiks()
        self.rubiks.reset_inputs()

    def get_postions(self):
        self.f = self.rubiks.front
        self.t = self.rubiks.top
        self.b = self.rubiks.back
        self.bo = self.rubiks.bottom
        self.l = self.rubiks.left
        self.r = self.rubiks.right

    def scramble_controller(self):
        self.rubiks.scramble()

    def get_info_moves(self):
        return self.rubiks.list_of_moves

    def get_total_moves(self):
        return self.rubiks.total_moves

    def get_solved_moves(self):
        return self.rubiks.solved_moves

    def colour_changer(self, clicked_row, clicked_column, colour, face):

        self.rubiks.colour_changer(clicked_row=clicked_row,
                                   clicked_column=clicked_column, colour=colour, face=face)

    def check_all_faces_if_theoritically_possible(self):
        possible = self.rubiks.check_all_faces_if_theoritically_possible_two()
        return possible

    def tester(self):
        self.rubiks.tester()

    def solve_cross_bottom_control(self):
        self.rubiks.solved_moves.append('\n\nSOLVE DOWN EDGES ########\n\n')
        self.rubiks.solve_cross_bottom_back()
        self.rubiks.solve_cross_bottom_right()
        self.rubiks.solve_cross_bottom_left()
        self.rubiks.solve_cross_bottom_front()

        self.rubiks.solved_moves.append('\n\nORIENT DOWN EDGES ########\n\n')
        self.rubiks.orient_cross_bottom()

    def solve_corners_bottom_control(self):

        self.rubiks.solved_moves.append('\n\nSOLVE DOWN CORNERS ########\n\n')
        self.rubiks.solve_corner_bottom_front_right()
        self.rubiks.solve_corner_bottom_front_left()
        self.rubiks.solve_corner_bottom_back_right()
        self.rubiks.solve_corner_bottom_back_left()

        self.rubiks.solved_moves.append('\n\nORIENT DOWN CORNERS ########\n\n')
        self.rubiks.orient_corners_bottom_front_right()
        self.rubiks.orient_corners_bottom_front_left()
        self.rubiks.orient_corners_bottom_back_right()
        self.rubiks.orient_corners_bottom_back_left()

    def solve_edges_middle_control(self):
        self.rubiks.solved_moves.append('\n\nSOLVE MIDDLE EDGES ########\n\n')
        self.rubiks.solve_edge_front_right()
        self.rubiks.solve_edge_front_left()
        self.rubiks.solve_edge_back_left()
        self.rubiks.solve_edge_back_right()

        self.rubiks.solved_moves.append('\n\nORIENT MIDDLE EDGES ########\n\n')
        self.rubiks.orient_middle_edge()

    def solve_edges_top_control(self):
        self.rubiks.solved_moves.append('\n\nSOLVE UP EDGES ########\n\n')
        self.rubiks.solve_top_edge()

        self.rubiks.solved_moves.append('\n\nORIENT TOP EDGES ########\n\n')
        self.rubiks.orient_top_edge()

    def solve_corners_top_control(self):
        self.rubiks.solved_moves.append('\n\nSOLVE UP CORNERS ########\n\n')
        self.rubiks.solve_corner_top()

    def solve_final_control(self):
        self.rubiks.solved_moves.append('\n\nORIENT UP CORNERS ########\n\n')
        self.rubiks.orient_corner_top_solve()

        ######################################

    def ff(self):
        self.rubiks.ff()

    def ffp(self):
        self.rubiks.ffp()

    def tt(self):
        self.rubiks.tt()

    def ttp(self):
        self.rubiks.ttp()

    def ff(self):
        self.rubiks.ff()

    def bb(self):
        self.rubiks.bb()

    def bbp(self):
        self.rubiks.bbp()

    def bbo(self):
        self.rubiks.bbo()

    def bbop(self):
        self.rubiks.bbop()

    def ll(self):
        self.rubiks.ll()

    def llp(self):
        self.rubiks.llp()

    def rr(self):
        self.rubiks.rr()

    def rrp(self):
        self.rubiks.rrp()
