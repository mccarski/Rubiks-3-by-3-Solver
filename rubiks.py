import random
import collections
import signal


class RubiksError(Exception):
    pass


class Rubiks:
    def __init__(self):
        self.reset_inputs()

    @staticmethod
    def makesolvedside(colour):
        side = [[colour for j in range(3)]for i in range(3)]
        return side

    def reset_inputs(self):
        self.total_moves = 0
        self.solving = False
        self.list_of_moves = []
        self.solved_moves = []

        self.front = self.makesolvedside('w')
        self.top = self.makesolvedside('r')
        self.back = self.makesolvedside('y')
        self.bottom = self.makesolvedside('o')
        self.left = self.makesolvedside('b')
        self.right = self.makesolvedside('g')

        self.front_center = self.front[1][1]
        self.top_center = self.top[1][1]
        self.back_center = self.back[1][1]
        self.bottom_center = self.bottom[1][1]
        self.left_center = self.left[1][1]
        self.right_center = self.right[1][1]

    def inputs_init(self):
        self.f = tuple(tuple(i) for i in self.front)
        self.t = tuple(tuple(i) for i in self.top)
        self.b = tuple(tuple(i) for i in self.back)
        self.bo = tuple(tuple(i) for i in self.bottom)
        self.l = tuple(tuple(i) for i in self.left)
        self.r = tuple(tuple(i) for i in self.right)
        return

    def r_90(self):
        self.inputs_init()
        for i in range(3):

            self.top[i][2] = self.f[i][2]
            self.back[i][2] = self.t[i][2]
            self.bottom[i][2] = self.b[i][2]
            self.front[i][2] = self.bo[i][2]

            self.right[0][2 - i] = self.r[i][0]
            self.right[2][2 - i] = self.r[i][2]

        self.right[1][0] = self.r[2][1]
        self.right[1][2] = self.r[0][1]

    def r_prime_90(self):
        self.inputs_init()
        for i in range(3):

            self.bottom[i][2] = self.f[i][2]
            self.front[i][2] = self.t[i][2]
            self.top[i][2] = self.b[i][2]
            self.back[i][2] = self.bo[i][2]

            self.right[2][i] = self.r[i][0]
            self.right[0][i] = self.r[i][2]

        self.right[1][2] = self.r[2][1]
        self.right[1][0] = self.r[0][1]

    def l_90(self):
        self.inputs_init()
        for i in range(3):
            self.bottom[i][0] = self.f[i][0]
            self.front[i][0] = self.t[i][0]
            self.top[i][0] = self.b[i][0]
            self.back[i][0] = self.bo[i][0]

            self.left[0][2 - i] = self.l[i][0]
            self.left[2][2 - i] = self.l[i][2]

        self.left[1][0] = self.l[2][1]
        self.left[1][2] = self.l[0][1]

    def l_prime_90(self):
        self.inputs_init()
        for i in range(3):
            self.top[i][0] = self.f[i][0]
            self.back[i][0] = self.t[i][0]
            self.bottom[i][0] = self.b[i][0]
            self.front[i][0] = self.bo[i][0]

            self.left[2][i] = self.l[i][0]
            self.left[0][i] = self.l[i][2]

        self.left[1][2] = self.l[2][1]
        self.left[1][0] = self.l[0][1]

    def f_90(self):
        self.inputs_init()
        for i in range(3):
            self.top[2][2 - i] = self.l[i][2]
            self.right[i][0] = self.t[2][i]
            self.bottom[0][2 - i] = self.r[i][0]
            self.left[i][2] = self.bo[0][i]

            self.front[0][2 - i] = self.f[i][0]
            self.front[2][2 - i] = self.f[i][2]

        self.front[1][0] = self.f[2][1]
        self.front[1][2] = self.f[0][1]

    def f_prime_90(self):
        self.inputs_init()
        for i in range(3):
            self.bottom[0][i] = self.l[i][2]
            self.left[2 - i][2] = self.t[2][i]
            self.top[2][i] = self.r[i][0]
            self.right[2 - i][0] = self.bo[0][i]

            self.front[2][i] = self.f[i][0]
            self.front[0][i] = self.f[i][2]

        self.front[1][2] = self.f[2][1]
        self.front[1][0] = self.f[0][1]

    def b_90(self):
        self.inputs_init()
        for i in range(3):
            self.bottom[2][i] = self.l[i][0]
            self.left[2 - i][0] = self.t[0][i]
            self.top[0][i] = self.r[i][2]
            self.right[2 - i][2] = self.bo[2][i]

            self.back[0][2 - i] = self.b[i][0]
            self.back[2][2 - i] = self.b[i][2]

        self.back[1][0] = self.b[2][1]
        self.back[1][2] = self.b[0][1]

    def b_prime_90(self):
        self.inputs_init()
        for i in range(3):
            self.top[0][2 - i] = self.l[i][0]
            self.right[i][2] = self.t[0][i]
            self.bottom[2][2 - i] = self.r[i][2]
            self.left[i][0] = self.bo[2][i]

            self.back[2][i] = self.b[i][0]
            self.back[0][i] = self.b[i][2]

        self.back[1][2] = self.b[2][1]
        self.back[1][0] = self.b[0][1]

    def t_90(self):
        self.inputs_init()
        for i in range(3):
            self.left[0][i] = self.f[0][i]
            self.back[2][2-i] = self.l[0][i]
            self.front[0][i] = self.r[0][i]
            self.right[0][2 - i] = self.b[2][i]

            self.top[0][2 - i] = self.t[i][0]
            self.top[2][2 - i] = self.t[i][2]

        self.top[1][0] = self.t[2][1]
        self.top[1][2] = self.t[0][1]

    def t_prime_90(self):
        self.inputs_init()
        for i in range(3):
            self.right[0][i] = self.f[0][i]
            self.front[0][i] = self.l[0][i]
            self.back[2][2 - i] = self.r[0][i]
            self.left[0][2-i] = self.b[2][i]

            self.top[2][i] = self.t[i][0]
            self.top[0][i] = self.t[i][2]

        self.top[1][2] = self.t[2][1]
        self.top[1][0] = self.t[0][1]

    def bo_90(self):
        self.inputs_init()
        for i in range(3):
            self.right[2][i] = self.f[2][i]
            self.front[2][i] = self.l[2][i]
            self.back[0][2 - i] = self.r[2][i]
            self.left[2][2 - i] = self.b[0][i]

            self.bottom[0][2 - i] = self.bo[i][0]
            self.bottom[2][2 - i] = self.bo[i][2]

        self.bottom[1][0] = self.bo[2][1]
        self.bottom[1][2] = self.bo[0][1]

    def bo_prime_90(self):
        self.inputs_init()
        for i in range(3):
            self.left[2][i] = self.f[2][i]
            self.back[0][2 - i] = self.l[2][i]
            self.front[2][i] = self.r[2][i]
            self.right[2][2 - i] = self.b[0][i]

            self.bottom[2][i] = self.bo[i][0]
            self.bottom[0][i] = self.bo[i][2]

        self.bottom[1][2] = self.bo[2][1]
        self.bottom[1][0] = self.bo[0][1]

    def scramble(self):
        D = dict(r=self.rr, rp=self.rrp, l=self.ll, lp=self.llp, f=self.ff, fp=self.ffp, b=self.bb,
                 bp=self.bbp, t=self.tt, tp=self.ttp, bo=self.bbo, bop=self.bbop)
        keys = tuple(D.keys())

        for i in range(15):
            b = random.randint(0, len(D)-1)
            D[keys[b]]()

    def colour_changer(self, clicked_row, clicked_column, colour, face):
        faces = {'f': self.front, 't': self.top, 'b': self.back,
                 'bo': self.bottom, 'l': self.left, 'r': self.right}
        faces[face][clicked_row][clicked_column] = colour

    def check_all_faces_if_theoritically_possible(self):
        a = []
        for i in range(3):
            for j in range(3):
                a.extend([self.front[i][j], self.top[i][j], self.back[i]
                          [j], self.bottom[i][j], self.left[i][j], self.right[i][j]])

        counter = collections.Counter(a)
        counter = counter.values()

        if len(set(counter)) <= 1 and len(counter) == 6:
            possible = True
        else:
            possible = False
        return possible

    def check_all_faces_if_theoritically_possible_two(self):
        rubiks_theoritical = Rubiks()

        rubiks_theoritical.front = self.front[:]
        rubiks_theoritical.top = self.top[:]
        rubiks_theoritical.back = self.back[:]
        rubiks_theoritical.bottom = self.bottom[:]
        rubiks_theoritical.left = self.left[:]
        rubiks_theoritical.right = self.right[:]
        possible = True

        def attempt():
            rubiks_theoritical.solve_cross_bottom_back()
            rubiks_theoritical.solve_cross_bottom_right()
            rubiks_theoritical.solve_cross_bottom_left()
            rubiks_theoritical.solve_cross_bottom_front()
            rubiks_theoritical.orient_cross_bottom()
            rubiks_theoritical.solve_corner_bottom_front_right()
            rubiks_theoritical.solve_corner_bottom_front_left()
            rubiks_theoritical.solve_corner_bottom_back_right()
            rubiks_theoritical.solve_corner_bottom_back_left()
            rubiks_theoritical.orient_corners_bottom_front_right()
            rubiks_theoritical.orient_corners_bottom_front_left()
            rubiks_theoritical.orient_corners_bottom_back_right()
            rubiks_theoritical.orient_corners_bottom_back_left()
            rubiks_theoritical.solve_edge_front_right()
            rubiks_theoritical.solve_edge_front_left()
            rubiks_theoritical.solve_edge_back_left()
            rubiks_theoritical.solve_edge_back_right()
            rubiks_theoritical.orient_middle_edge()
            rubiks_theoritical.solve_top_edge()
            rubiks_theoritical.orient_top_edge()
            rubiks_theoritical.solve_corner_top()
            rubiks_theoritical.orient_corner_top_solve()
            possible = True

        try:
            attempt()
        except:
            possible = False

        return possible

    def corresponding_sides(self, side, location):

        D_f = {('f', (1, 0)): ('l', (1, 2)), ('f', (2, 1)): ('bo', (0, 1)),
               ('f', (1, 2)): ('r', (1, 0)), ('f', (0, 1)): ('t', (2, 1))}
        D_r = {('r', (1, 0)): ('f', (1, 2)), ('r', (2, 1)): ('bo', (1, 2)),
               ('r', (1, 2)): ('b', (1, 2)), ('r', (0, 1)): ('t', (1, 2))}
        D_l = {('l', (1, 0)): ('b', (1, 0)), ('l', (2, 1)): ('bo', (1, 0)),
               ('l', (1, 2)): ('f', (1, 0)), ('l', (0, 1)): ('t', (1, 0))}
        D_bo = {('bo', (1, 0)): ('l', (2, 1)), ('bo', (2, 1)): ('b', (0, 1)),
                ('bo', (1, 2)): ('r', (2, 1)), ('bo', (0, 1)): ('f', (2, 1))}
        D_t = {('t', (1, 0)): ('l', (0, 1)), ('t', (2, 1)): ('f', (0, 1)),
               ('t', (1, 2)): ('r', (0, 1)), ('t', (0, 1)): ('b', (2, 1))}
        D_b = {('b', (1, 0)): ('l', (1, 0)), ('b', (2, 1)): ('t', (0, 1)),
               ('b', (1, 2)): ('r', (1, 2)), ('b', (0, 1)): ('bo', (2, 1))}
        D = {}

        for i in [D_f, D_r, D_l, D_bo, D_t, D_b]:
            D.update(i)
        tuple_corresponding = D[(side, location)]

        return tuple_corresponding

    def position_bottom_cross(self):
        faces = {'f': self.front, 't': self.top, 'b': self.back,
                 'bo': self.bottom, 'l': self.left, 'r': self.right}
        position = [(1, 0), (0, 1), (1, 2), (2, 1)]

        for face in faces:
            for pos in position:
                i, j = pos
                face2, pos2 = self.corresponding_sides(face, pos)

                if faces[face][i][j] == self.bottom_center and faces[face2][pos2[0]][pos2[1]] == self.right_center:
                    BoR = face, pos
                if faces[face][i][j] == self.bottom_center and faces[face2][pos2[0]][pos2[1]] == self.left_center:
                    BoL = face, pos
                if faces[face][i][j] == self.bottom_center and faces[face2][pos2[0]][pos2[1]] == self.front_center:
                    BoF = face, pos
                if faces[face][i][j] == self.bottom_center and faces[face2][pos2[0]][pos2[1]] == self.back_center:
                    BoB = face, pos
        return BoR, BoB, BoL, BoF

    def solve_cross_bottom_right(self):
        self.solving = True
        self.solved_moves.append('\nBottom-Right edge\n')
        BoR, BoB, BoL, BoF = self.position_bottom_cross()
        if BoR == ('f', (1, 0)) or BoR == self.corresponding_sides('f', (1, 0)):
            self.ff()
            self.ff()
            self.rrp()
            self.ffp()
            self.ffp()
            BoR, BoB, BoL, BoF = self.position_bottom_cross()

        if BoR == ('f', (2, 1)) or BoR == self.corresponding_sides('f', (2, 1)):
            self.ffp()
            self.rrp()
            BoR, BoB, BoL, BoF = self.position_bottom_cross()

        if BoR == ('f', (1, 2)) or BoR == self.corresponding_sides('f', (1, 2)):
            self.rrp()
            BoR, BoB, BoL, BoF = self.position_bottom_cross()

        if BoR == ('f', (0, 1)) or BoR == self.corresponding_sides('f', (0, 1)):
            self.ff()
            self.rrp()
            self.ffp()
            BoR, BoB, BoL, BoF = self.position_bottom_cross()

        if BoR == ('b', (1, 0)) or BoR == self.corresponding_sides('b', (1, 0)):
            self.bb()
            self.bb()
            self.rr()
            self.bb()
            self.bb()
            BoR, BoB, BoL, BoF = self.position_bottom_cross()

        if BoR == ('b', (2, 1)) or BoR == self.corresponding_sides('b', (2, 1)):
            self.bbp()
            self.rr()
            self.bb()
            BoR, BoB, BoL, BoF = self.position_bottom_cross()

        if BoR == ('b', (1, 2)) or BoR == self.corresponding_sides('b', (1, 2)):
            self.rr()
            BoR, BoB, BoL, BoF = self.position_bottom_cross()

        if BoR == ('b', (0, 1)) or BoR == self.corresponding_sides('b', (0, 1)):
            self.bb()
            self.rr()
            BoR, BoB, BoL, BoF = self.position_bottom_cross()

        if BoR == ('t', (1, 0)) or BoR == self.corresponding_sides('t', (1, 0)):
            self.tt()
            self.tt()
            self.rr()
            self.rr()
            BoR, BoB, BoL, BoF = self.position_bottom_cross()

        if BoR == ('t', (1, 2)) or BoR == self.corresponding_sides('t', (1, 2)):
            self.rr()
            self.rr()
            BoR, BoB, BoL, BoF = self.position_bottom_cross()

        if BoR == ('bo', (1, 0)) or BoR == self.corresponding_sides('bo', (1, 0)):
            self.ll()
            self.ll()
            self.tt()
            self.tt()
            self.rr()
            self.rr()
            BoR, BoB, BoL, BoF = self.position_bottom_cross()

        if BoR == ('bo', (1, 2)) or BoR == self.corresponding_sides('bo', (1, 2)):
            BoR, BoB, BoL, BoF = self.position_bottom_cross()
            pass

        self.solving = False

    def solve_cross_bottom_back(self):
        self.solving = True
        self.solved_moves.append('\nBottom-Back edge\n')
        BoR, BoB, BoL, BoF = self.position_bottom_cross()
        if BoB == ('f', (1, 0)) or BoB == self.corresponding_sides('f', (1, 0)):
            self.llp()
            self.tt()
            self.bb()
            self.bb()
            self.ll()
            BoR, BoB, BoL, BoF = self.position_bottom_cross()

        if BoB == ('f', (2, 1)) or BoB == self.corresponding_sides('f', (2, 1)):
            self.ff()
            self.ff()
            self.tt()
            self.tt()
            self.bb()
            self.bb()
            BoR, BoB, BoL, BoF = self.position_bottom_cross()

        if BoB == ('f', (1, 2)) or BoB == self.corresponding_sides('f', (1, 2)):
            self.ffp()
            self.tt()
            self.tt()
            self.bb()
            self.bb()
            self.ff()
            BoR, BoB, BoL, BoF = self.position_bottom_cross()

        if BoB == ('f', (0, 1)) or BoB == self.corresponding_sides('f', (0, 1)):
            self.tt()
            self.tt()
            self.bb()
            self.bb()
            BoR, BoB, BoL, BoF = self.position_bottom_cross()

        if BoB == ('b', (1, 0)) or BoB == self.corresponding_sides('b', (1, 0)):
            self.bb()
            BoR, BoB, BoL, BoF = self.position_bottom_cross()

        if BoB == ('b', (2, 1)) or BoB == self.corresponding_sides('b', (2, 1)):
            self.bb()
            self.bb()
            BoR, BoB, BoL, BoF = self.position_bottom_cross()

        if BoB == ('b', (1, 2)) or BoB == self.corresponding_sides('b', (1, 2)):
            self.bbp()
            BoR, BoB, BoL, BoF = self.position_bottom_cross()

        if BoB == ('t', (1, 0)) or BoB == self.corresponding_sides('t', (1, 0)):
            self.tt()
            self.bb()
            self.bb()
            BoR, BoB, BoL, BoF = self.position_bottom_cross()

        if BoB == ('t', (1, 2)) or BoB == self.corresponding_sides('t', (1, 2)):
            self.ttp()
            self.bb()
            self.bb()
            BoR, BoB, BoL, BoF = self.position_bottom_cross()

        if BoB == ('bo', (1, 0)) or BoB == self.corresponding_sides('bo', (1, 0)):
            self.ll()
            self.bb()
            BoR, BoB, BoL, BoF = self.position_bottom_cross()

        if BoB == ('bo', (1, 2)) or BoB == self.corresponding_sides('bo', (1, 2)):
            self.rrp()
            self.bbp()

        if BoB == ('b', (0, 1)) or BoB == self.corresponding_sides('b', (0, 1)):
            BoR, BoB, BoL, BoF = self.position_bottom_cross()
            pass
        self.solving = False

    def solve_cross_bottom_left(self):
        self.solving = True
        self.solved_moves.append('\nBottom-Left edge\n')

        BoR, BoB, BoL, BoF = self.position_bottom_cross()
        if BoL == ('f', (1, 0)) or BoL == self.corresponding_sides('f', (1, 0)):
            self.ll()
            BoR, BoB, BoL, BoF = self.position_bottom_cross()

        if BoL == ('f', (2, 1)) or BoL == self.corresponding_sides('f', (2, 1)):
            self.ff()
            self.ll()
            BoR, BoB, BoL, BoF = self.position_bottom_cross()

        if BoL == ('f', (1, 2)) or BoL == self.corresponding_sides('f', (1, 2)):
            self.ff()
            self.ff()
            self.ll()
            BoR, BoB, BoL, BoF = self.position_bottom_cross()

        if BoL == ('f', (0, 1)) or BoL == self.corresponding_sides('f', (0, 1)):
            self.ffp()
            self.ll()
            self.ff()
            BoR, BoB, BoL, BoF = self.position_bottom_cross()

        if BoL == ('b', (1, 0)) or BoL == self.corresponding_sides('b', (1, 0)):
            self.llp()
            BoR, BoB, BoL, BoF = self.position_bottom_cross()

        if BoL == ('b', (2, 1)) or BoL == self.corresponding_sides('b', (2, 1)):
            self.ttp()
            self.ll()
            self.ll()
            BoR, BoB, BoL, BoF = self.position_bottom_cross()

        if BoL == ('b', (1, 2)) or BoL == self.corresponding_sides('b', (1, 2)):
            self.bb()
            self.bb()
            self.llp()
            self.bb()
            self.bb()
            BoR, BoB, BoL, BoF = self.position_bottom_cross()

        if BoL == ('b', (0, 1)) or BoL == self.corresponding_sides('b', (0, 1)):
            self.bbp()
            self.llp()
            BoR, BoB, BoL, BoF = self.position_bottom_cross()

        if BoL == ('t', (1, 0)) or BoL == self.corresponding_sides('t', (1, 0)):
            self.ll()
            self.ll()
            BoR, BoB, BoL, BoF = self.position_bottom_cross()

        if BoL == ('t', (1, 2)) or BoL == self.corresponding_sides('t', (1, 2)):
            self.tt()
            self.tt()
            self.ll()
            self.ll()
            BoR, BoB, BoL, BoF = self.position_bottom_cross()

        if BoL == ('bo', (1, 2)) or BoL == self.corresponding_sides('bo', (1, 2)):
            self.rr()
            self.rr()
            self.tt()
            self.tt()
            self.ll()
            self.ll()
            BoR, BoB, BoL, BoF = self.position_bottom_cross()

        if BoL == ('bo', (1, 0)) or BoL == self.corresponding_sides('bo', (1, 0)):
            BoR, BoB, BoL, BoF = self.position_bottom_cross()
            pass
        self.solving = False

    def solve_cross_bottom_front(self):
        self.solving = True
        self.solved_moves.append('\nBottom-Front edge\n')

        BoR, BoB, BoL, BoF = self.position_bottom_cross()
        if BoF == ('f', (1, 0)) or BoF == self.corresponding_sides('f', (1, 0)):
            self.ffp()
            BoR, BoB, BoL, BoF = self.position_bottom_cross()

        if BoF == ('f', (1, 2)) or BoF == self.corresponding_sides('f', (1, 2)):
            self.rrp()
            BoR, BoB, BoL, BoF = self.position_bottom_cross()

        if BoF == ('f', (0, 1)) or BoF == self.corresponding_sides('f', (0, 1)):
            self.ff()
            self.ff()
            BoR, BoB, BoL, BoF = self.position_bottom_cross()

        if BoF == ('b', (1, 0)) or BoF == self.corresponding_sides('b', (1, 0)):
            self.ll()
            self.ttp()
            self.ff()
            self.ff()
            self.llp()
            BoR, BoB, BoL, BoF = self.position_bottom_cross()

        if BoF == ('b', (2, 1)) or BoF == self.corresponding_sides('b', (2, 1)):
            self.tt()
            self.tt()
            self.ff()
            self.ff()
            BoR, BoB, BoL, BoF = self.position_bottom_cross()

        if BoF == ('b', (1, 2)) or BoF == self.corresponding_sides('b', (1, 2)):
            self.rrp()
            self.tt()
            self.ff()
            self.ff()
            self.rr()
            BoR, BoB, BoL, BoF = self.position_bottom_cross()

        if BoF == ('b', (0, 1)) or BoF == self.corresponding_sides('b', (0, 1)):
            self.bb()
            self.bb()
            self.tt()
            self.tt()
            self.ff()
            self.ff()
            BoR, BoB, BoL, BoF = self.position_bottom_cross()

        if BoF == ('t', (1, 0)) or BoF == self.corresponding_sides('t', (1, 0)):
            self.ttp()
            self.ff()
            self.ff()
            BoR, BoB, BoL, BoF = self.position_bottom_cross()

        if BoF == ('t', (1, 2)) or BoF == self.corresponding_sides('t', (1, 2)):
            self.tt()
            self.ff()
            self.ff()
            BoR, BoB, BoL, BoF = self.position_bottom_cross()

        if BoF == ('bo', (1, 0)) or BoF == self.corresponding_sides('bo', (1, 0)):
            self.ll()
            self.ll()
            self.ttp()
            self.ff()
            self.ff()
            BoR, BoB, BoL, BoF = self.position_bottom_cross()

        if BoF == ('bo', (1, 2)) or BoF == self.corresponding_sides('bo', (1, 2)):
            self.rr()
            self.ff()
            BoR, BoB, BoL, BoF = self.position_bottom_cross()

        if BoF == ('f', (2, 1)) or BoF == self.corresponding_sides('f', (2, 1)):
            BoR, BoB, BoL, BoF = self.position_bottom_cross()
            pass
        self.solving = False

    def debug_cross_bottom_sides(self):

        if (self.bottom[1][0] == self.bottom_center or self.left[2][1] == self.bottom_center) and \
                (self.bottom[1][0] == self.left_center or self.left[2][1] == self.left_center):
            print('true_bottom_left')
        if (self.bottom[2][1] == self.bottom_center or self.back[0][1] == self.bottom_center) and \
                (self.bottom[2][1] == self.back_center or self.back[0][1] == self.back_center):
            print('true_bottom_back')
        if (self.bottom[1][2] == self.bottom_center or self.right[2][1] == self.bottom_center) and \
                (self.bottom[1][2] == self.right_center or self.right[2][1] == self.right_center):
            print('true_bottom_right')
        if (self.bottom[0][1] == self.bottom_center or self.front[2][1] == self.bottom_center) and \
                (self.bottom[0][1] == self.front_center or self.front[2][1] == self.front_center):
            print('true_bottom_right')

    def cross_bottom_check_flip(self):
        if (self.bottom[1][0] == self.bottom_center and self.left[2][1] == self.left_center):
            Bo_Left = True
        else:
            Bo_Left = False

        if (self.bottom[2][1] == self.bottom_center and self.back[0][1] == self.back_center):
            Bo_Back = True
        else:
            Bo_Back = False

        if (self.bottom[1][2] == self.bottom_center and self.right[2][1] == self.right_center):
            Bo_Right = True
        else:
            Bo_Right = False

        if (self.bottom[0][1] == self.bottom_center and self.front[2][1] == self.front_center):
            Bo_Front = True
        else:
            Bo_Front = False
        return Bo_Left, Bo_Back, Bo_Right, Bo_Front

    def orient_cross_bottom(self):
        self.solving = True
        Bo_Left, Bo_Back, Bo_Right, Bo_Front = self.cross_bottom_check_flip()
        if Bo_Left == False:
            self.llp()
            self.ff()
            self.tt()
            self.ffp()
            self.ll()
            self.ll()

        if Bo_Back == False:
            self.bbp()
            self.ll()
            self.tt()
            self.llp()
            self.bb()
            self.bb()

        if Bo_Right == False:
            self.rr()
            self.ffp()
            self.ttp()
            self.ff()
            self.rr()
            self.rr()

        if Bo_Front == False:
            self.ff()
            self.llp()
            self.ttp()
            self.ll()
            self.ff()
            self.ff()
        self.solving = False

    def corresponding_corners(self, side, loc):
        D_f = {('f', (0, 0)): (('t', (2, 0)), ('l', (0, 2))),
               ('f', (0, 2)): (('t', (2, 2)), ('r', (0, 0))),
               ('f', (2, 2)): (('bo', (0, 2)), ('r', (2, 0))),
               ('f', (2, 0)): (('bo', (0, 0)), ('l', (2, 2)))}
        D_b = {('b', (0, 0)): (('bo', (2, 0)), ('l', (2, 0))),
               ('b', (0, 2)): (('bo', (2, 2)), ('r', (2, 2))),
               ('b', (2, 2)): (('t', (0, 2)), ('r', (0, 2))),
               ('b', (2, 0)): (('t', (0, 0)), ('l', (0, 0)))}
        D_t = {('t', (0, 0)): (('b', (2, 0)), ('l', (0, 0))),
               ('t', (0, 2)): (('b', (2, 2)), ('r', (0, 2))),
               ('t', (2, 2)): (('f', (0, 2)), ('r', (0, 0))),
               ('t', (2, 0)): (('f', (0, 0)), ('l', (0, 2)))}

        D = {}
        for i in [D_f, D_b, D_t]:
            D.update(i)

        tuples_corresponding = D[(side, loc)]

        return tuples_corresponding

    def position_bottom_corner(self):
        faces = {'f': self.front, 't': self.top, 'b': self.back,
                 'bo': self.bottom, 'l': self.left, 'r': self.right}
        faces_spec = {'f': self.front, 'b': self.back}
        positions = [(0, 0), (0, 2), (2, 2), (2, 0)]

        for face in faces_spec:
            for pos in positions:
                i, j = pos
                (face2, pos2), (face3, pos3) = self.corresponding_corners(face, pos)

                x = faces[face][i][j]
                y = faces[face2][pos2[0]][pos2[1]]
                z = faces[face3][pos3[0]][pos3[1]]

                if ((x == self.bottom_center or x == self.front_center or x == self.right_center)
                        and (y == self.bottom_center or y == self.front_center or y == self.right_center)
                        and (z == self.bottom_center or z == self.front_center or z == self.right_center)):
                    Bo_f_r_corner = (face, pos)

                if ((x == self.bottom_center or x == self.front_center or x == self.left_center)
                        and (y == self.bottom_center or y == self.front_center or y == self.left_center)
                        and (z == self.bottom_center or z == self.front_center or z == self.left_center)):
                    Bo_f_l_corner = (face, pos)

                if ((x == self.bottom_center or x == self.back_center or x == self.right_center)
                        and (y == self.bottom_center or y == self.back_center or y == self.right_center)
                        and (z == self.bottom_center or z == self.back_center or z == self.right_center)):
                    Bo_b_r_corner = (face, pos)

                if ((x == self.bottom_center or x == self.back_center or x == self.left_center)
                        and (y == self.bottom_center or y == self.back_center or y == self.left_center)
                        and (z == self.bottom_center or z == self.back_center or z == self.left_center)):
                    Bo_b_l_corner = (face, pos)

        return Bo_f_r_corner, Bo_f_l_corner, Bo_b_r_corner, Bo_b_l_corner

    def solve_corner_bottom_front_right(self):
        self.solving = True
        self.solved_moves.append('\nBottom-Front-Right corner\n')
        Bo_f_r_corner, Bo_f_l_corner, Bo_b_r_corner, Bo_b_l_corner = self.position_bottom_corner()
        if Bo_f_r_corner == ('f', (0, 0)):
            self.ttp()
            self.rr()
            self.tt()
            self.rrp()
            Bo_f_r_corner, Bo_f_l_corner, Bo_b_r_corner, Bo_b_l_corner = self.position_bottom_corner()

        if Bo_f_r_corner == ('f', (0, 2)):
            self.rr()
            self.tt()
            self.rrp()
            Bo_f_r_corner, Bo_f_l_corner, Bo_b_r_corner, Bo_b_l_corner = self.position_bottom_corner()

        if Bo_f_r_corner == ('f', (2, 2)):
            Bo_f_r_corner, Bo_f_l_corner, Bo_b_r_corner, Bo_b_l_corner = self.position_bottom_corner()
            pass

        if Bo_f_r_corner == ('f', (2, 0)):
            self.llp()
            self.ttp()
            self.ll()
            self.rr()
            self.tt()
            self.rrp()
            Bo_f_r_corner, Bo_f_l_corner, Bo_b_r_corner, Bo_b_l_corner = self.position_bottom_corner()

        if Bo_f_r_corner == ('b', (0, 0)):
            self.ll()
            self.tt()
            self.tt()
            self.llp()
            self.rr()
            self.tt()
            self.rrp()
            Bo_f_r_corner, Bo_f_l_corner, Bo_b_r_corner, Bo_b_l_corner = self.position_bottom_corner()

        if Bo_f_r_corner == ('b', (0, 2)):
            self.rrp()
            self.tt()
            self.rr()
            self.tt()
            self.rr()
            self.tt()
            self.rrp()
            Bo_f_r_corner, Bo_f_l_corner, Bo_b_r_corner, Bo_b_l_corner = self.position_bottom_corner()

        if Bo_f_r_corner == ('b', (2, 2)):
            self.tt()
            self.rr()
            self.tt()
            self.rrp()
            Bo_f_r_corner, Bo_f_l_corner, Bo_b_r_corner, Bo_b_l_corner = self.position_bottom_corner()

        if Bo_f_r_corner == ('b', (2, 0)):
            self.tt()
            self.tt()
            self.rr()
            self.tt()
            self.rrp()
            Bo_f_r_corner, Bo_f_l_corner, Bo_b_r_corner, Bo_b_l_corner = self.position_bottom_corner()

        self.solving = False

    def orient_corners_bottom_front_right(self):
        self.solving = True
        Bo_f_r_corner, Bo_f_l_corner, Bo_b_r_corner, Bo_b_l_corner = self.position_bottom_corner()
        tot1 = Bo_f_r_corner
        tot2, tot3 = self.corresponding_corners(*tot1)
        is_solved = self.matching(tot1, tot2, tot3)
        counter = 0
        while is_solved == False:
            self.rr()
            self.tt()
            self.rrp()
            self.ttp()
            self.rr()
            self.tt()
            self.rrp()
            is_solved = self.matching(tot1, tot2, tot3)

            counter += 1
            if counter == 10:
                raise RubiksError()

        self.solving = False

    def solve_corner_bottom_front_left(self):
        self.solving = True
        self.solved_moves.append('\nBottom-Front-Left corner\n')
        Bo_f_r_corner, Bo_f_l_corner, Bo_b_r_corner, Bo_b_l_corner = self.position_bottom_corner()
        if Bo_f_l_corner == ('f', (0, 0)):
            self.llp()
            self.ttp()
            self.ll()
            Bo_f_r_corner, Bo_f_l_corner, Bo_b_r_corner, Bo_b_l_corner = self.position_bottom_corner()

        if Bo_f_l_corner == ('f', (0, 2)):
            self.tt()
            self.llp()
            self.ttp()
            self.ll()
            Bo_f_r_corner, Bo_f_l_corner, Bo_b_r_corner, Bo_b_l_corner = self.position_bottom_corner()

        if Bo_f_l_corner == ('f', (2, 2)):
            Bo_f_r_corner, Bo_f_l_corner, Bo_b_r_corner, Bo_b_l_corner = self.position_bottom_corner()
            self.rr()
            self.tt()
            self.rrp()
            self.llp()
            self.ttp()
            self.ll()

        if Bo_f_l_corner == ('f', (2, 0)):
            Bo_f_r_corner, Bo_f_l_corner, Bo_b_r_corner, Bo_b_l_corner = self.position_bottom_corner()
            pass

        if Bo_f_l_corner == ('b', (0, 0)):
            self.ll()
            self.tt()
            self.tt()
            self.llp()
            self.tt()
            self.llp()
            self.ttp()
            self.ll()
            Bo_f_r_corner, Bo_f_l_corner, Bo_b_r_corner, Bo_b_l_corner = self.position_bottom_corner()

        if Bo_f_l_corner == ('b', (0, 2)):
            self.rrp()
            self.tt()
            self.tt()
            self.rr()
            self.llp()
            self.ttp()
            self.ll()
            Bo_f_r_corner, Bo_f_l_corner, Bo_b_r_corner, Bo_b_l_corner = self.position_bottom_corner()

        if Bo_f_l_corner == ('b', (2, 2)):
            self.tt()
            self.tt()
            self.llp()
            self.ttp()
            self.ll()
            Bo_f_r_corner, Bo_f_l_corner, Bo_b_r_corner, Bo_b_l_corner = self.position_bottom_corner()

        if Bo_f_l_corner == ('b', (2, 0)):
            self.ttp()
            self.llp()
            self.ttp()
            self.ll()
            Bo_f_r_corner, Bo_f_l_corner, Bo_b_r_corner, Bo_b_l_corner = self.position_bottom_corner()

        self.solving = False

    def orient_corners_bottom_front_left(self):
        self.solving = True
        Bo_f_r_corner, Bo_f_l_corner, Bo_b_r_corner, Bo_b_l_corner = self.position_bottom_corner()
        tot1 = Bo_f_l_corner
        tot2, tot3 = self.corresponding_corners(*tot1)
        is_solved = self.matching(tot1, tot2, tot3)
        counter = 0
        while is_solved == False:
            self.llp()
            self.ttp()
            self.ll()
            self.tt()
            self.llp()
            self.ttp()
            self.ll()
            is_solved = self.matching(tot1, tot2, tot3)

            counter += 1
            if counter == 10:
                raise RubiksError()
        self.solving = False

    def solve_corner_bottom_back_right(self):
        self.solving = True
        self.solved_moves.append('\nBottom-Back-Right corner\n')
        Bo_f_r_corner, Bo_f_l_corner, Bo_b_r_corner, Bo_b_l_corner = self.position_bottom_corner()
        if Bo_b_r_corner == ('f', (0, 0)):
            self.tt()
            self.tt()
            self.rrp()
            self.ttp()
            self.rr()
            Bo_f_r_corner, Bo_f_l_corner, Bo_b_r_corner, Bo_b_l_corner = self.position_bottom_corner()

        if Bo_b_r_corner == ('f', (0, 2)):
            self.ttp()
            self.rrp()
            self.ttp()
            self.rr()
            Bo_f_r_corner, Bo_f_l_corner, Bo_b_r_corner, Bo_b_l_corner = self.position_bottom_corner()

        if Bo_b_r_corner == ('f', (2, 2)):
            Bo_f_r_corner, Bo_f_l_corner, Bo_b_r_corner, Bo_b_l_corner = self.position_bottom_corner()
            self.rr()
            self.ttp()
            self.rrp()
            self.ttp()
            self.bb()
            self.tt()
            self.bbp()

        if Bo_b_r_corner == ('f', (2, 0)):
            Bo_f_r_corner, Bo_f_l_corner, Bo_b_r_corner, Bo_b_l_corner = self.position_bottom_corner()
            self.llp()
            self.tt()
            self.ll()
            self.tt()
            self.bbp()
            self.ttp()
            self.bb()

        if Bo_b_r_corner == ('b', (0, 0)):
            self.ll()
            self.ttp()
            self.llp()
            self.rrp()
            self.tt()
            self.rr()
            Bo_f_r_corner, Bo_f_l_corner, Bo_b_r_corner, Bo_b_l_corner = self.position_bottom_corner()

        if Bo_b_r_corner == ('b', (0, 2)):
            Bo_f_r_corner, Bo_f_l_corner, Bo_b_r_corner, Bo_b_l_corner = self.position_bottom_corner()
            pass

        if Bo_b_r_corner == ('b', (2, 2)):
            self.rrp()
            self.ttp()
            self.rr()
            Bo_f_r_corner, Bo_f_l_corner, Bo_b_r_corner, Bo_b_l_corner = self.position_bottom_corner()

        if Bo_b_r_corner == ('b', (2, 0)):
            self.tt()
            self.rrp()
            self.ttp()
            self.rr()
            Bo_f_r_corner, Bo_f_l_corner, Bo_b_r_corner, Bo_b_l_corner = self.position_bottom_corner()

        self.solving = False

    def orient_corners_bottom_back_right(self):
        self.solving = True
        Bo_f_r_corner, Bo_f_l_corner, Bo_b_r_corner, Bo_b_l_corner = self.position_bottom_corner()
        tot1 = Bo_b_r_corner
        tot2, tot3 = self.corresponding_corners(*tot1)
        is_solved = self.matching(tot1, tot2, tot3)
        counter = 0
        while is_solved == False:
            self.rrp()
            self.ttp()
            self.rr()
            self.tt()
            self.rrp()
            self.ttp()
            self.rr()
            is_solved = self.matching(tot1, tot2, tot3)

            counter += 1
            if counter == 10:
                raise RubiksError()

        self.solving = False

    def solve_corner_bottom_back_left(self):
        self.solving = True
        self.solved_moves.append('\nBottom-Back-Left corner\n')
        Bo_f_r_corner, Bo_f_l_corner, Bo_b_r_corner, Bo_b_l_corner = self.position_bottom_corner()
        if Bo_b_l_corner == ('f', (0, 0)):
            self.tt()
            self.ll()
            self.tt()
            self.llp()
            Bo_f_r_corner, Bo_f_l_corner, Bo_b_r_corner, Bo_b_l_corner = self.position_bottom_corner()

        if Bo_b_l_corner == ('f', (0, 2)):
            self.tt()
            self.tt()
            self.ll()
            self.tt()
            self.llp()
            Bo_f_r_corner, Bo_f_l_corner, Bo_b_r_corner, Bo_b_l_corner = self.position_bottom_corner()

        if Bo_b_l_corner == ('f', (2, 2)):
            self.rr()
            self.ttp()
            self.rrp()
            self.tt()
            self.bbp()
            self.ttp()
            self.bb()
            Bo_f_r_corner, Bo_f_l_corner, Bo_b_r_corner, Bo_b_l_corner = self.position_bottom_corner()

        if Bo_b_l_corner == ('f', (2, 0)):
            self.llp()
            self.tt()
            self.ll()
            self.bbp()
            self.tt()
            self.bb()
            Bo_f_r_corner, Bo_f_l_corner, Bo_b_r_corner, Bo_b_l_corner = self.position_bottom_corner()

        if Bo_b_l_corner == ('b', (0, 0)):
            Bo_f_r_corner, Bo_f_l_corner, Bo_b_r_corner, Bo_b_l_corner = self.position_bottom_corner()
            pass

        if Bo_b_l_corner == ('b', (0, 2)):
            self.rrp()
            self.ttp()
            self.rr()
            self.bbp()
            self.ttp()
            self.bb()
            Bo_f_r_corner, Bo_f_l_corner, Bo_b_r_corner, Bo_b_l_corner = self.position_bottom_corner()

        if Bo_b_l_corner == ('b', (2, 2)):
            self.ll()
            self.ttp()
            self.llp()
            Bo_f_r_corner, Bo_f_l_corner, Bo_b_r_corner, Bo_b_l_corner = self.position_bottom_corner()

        if Bo_b_l_corner == ('b', (2, 0)):
            self.ll()
            self.tt()
            self.llp()
            Bo_f_r_corner, Bo_f_l_corner, Bo_b_r_corner, Bo_b_l_corner = self.position_bottom_corner()

        self.solving = False

    def orient_corners_bottom_back_left(self):
        self.solving = True
        Bo_f_r_corner, Bo_f_l_corner, Bo_b_r_corner, Bo_b_l_corner = self.position_bottom_corner()
        tot1 = Bo_b_l_corner
        tot2, tot3 = self.corresponding_corners(*tot1)
        is_solved = self.matching(tot1, tot2, tot3)
        counter = 0
        while is_solved == False:
            self.ll()
            self.tt()
            self.llp()
            self.ttp()
            self.ll()
            self.tt()
            self.llp()
            is_solved = self.matching(tot1, tot2, tot3)

            counter += 1
            if counter == 10:
                raise RubiksError()
        self.solving = False

    def matching(self, tot1, tot2, tot3):
        faces = {'f': self.front, 't': self.top, 'b': self.back,
                 'bo': self.bottom, 'l': self.left, 'r': self.right}
        face1, pos1 = tot1
        face2, pos2 = tot2
        face3, pos3 = tot3

        if faces[face1][pos1[0]][pos1[1]] == faces[face1][1][1] and \
                faces[face2][pos2[0]][pos2[1]] == faces[face2][1][1] and \
                faces[face3][pos3[0]][pos3[1]] == faces[face3][1][1]:
            a = True
        else:
            a = False
        return a

    def position_middle_edges(self):
        faces = {'f': self.front, 't': self.top, 'b': self.back,
                 'bo': self.bottom, 'l': self.left, 'r': self.right}
        position = [(1, 0), (0, 1), (1, 2), (2, 1)]

        for face in faces:
            for pos in position:
                i, j = pos
                face2, pos2 = self.corresponding_sides(face, pos)

                if faces[face][i][j] == self.front_center and faces[face2][pos2[0]][pos2[1]] == self.right_center:
                    FR = face, pos
                if faces[face][i][j] == self.front_center and faces[face2][pos2[0]][pos2[1]] == self.left_center:
                    FL = face, pos
                if faces[face][i][j] == self.back_center and faces[face2][pos2[0]][pos2[1]] == self.right_center:
                    BR = face, pos
                if faces[face][i][j] == self.back_center and faces[face2][pos2[0]][pos2[1]] == self.left_center:
                    BL = face, pos
        return FR, FL, BR, BL

    def solve_edge_front_right(self):
        self.solving = True
        self.solved_moves.append('\nFront-Right edge\n')
        FR, FL, BR, BL = self.position_middle_edges()

        if FR == ('f', (1, 0)) or FR == self.corresponding_sides('f', (1, 0)):
            self.llp()
            self.tt()
            self.ll()
            self.tt()
            self.ff()
            self.ttp()
            self.ffp()

            self.ffp()
            self.tt()
            self.ff()
            self.tt()
            self.rr()
            self.ttp()
            self.rrp()
            FR, FL, BR, BL = self.position_middle_edges()

        if FR == ('f', (0, 1)) or FR == self.corresponding_sides('f', (0, 1)):
            self.tt()
            self.rr()
            self.ttp()
            self.rrp()
            self.ttp()
            self.ffp()
            self.tt()
            self.ff()
            FR, FL, BR, BL = self.position_middle_edges()

        if FR == ('f', (1, 2)) or FR == self.corresponding_sides('f', (1, 2)):
            FR, FL, BR, BL = self.position_middle_edges()
            pass

        if FR == ('t', (1, 0)) or FR == self.corresponding_sides('t', (1, 0)):
            self.rr()
            self.ttp()
            self.rrp()
            self.ttp()
            self.ffp()
            self.tt()
            self.ff()
            FR, FL, BR, BL = self.position_middle_edges()

        if FR == ('t', (1, 2)) or FR == self.corresponding_sides('t', (1, 2)):
            self.tt()
            self.tt()
            self.rr()
            self.ttp()
            self.rrp()
            self.ttp()
            self.ffp()
            self.tt()
            self.ff()
            FR, FL, BR, BL = self.position_middle_edges()

        if FR == ('b', (1, 0)) or FR == self.corresponding_sides('b', (1, 0)):
            self.ll()
            self.ttp()
            self.llp()
            self.ttp()
            self.bbp()
            self.tt()
            self.bb()

            self.tt()
            self.rr()
            self.ttp()
            self.rrp()
            self.ttp()
            self.ffp()
            self.tt()
            self.ff()
            FR, FL, BR, BL = self.position_middle_edges()

        if FR == ('b', (1, 2)) or FR == self.corresponding_sides('b', (1, 2)):
            self.rrp()
            self.tt()
            self.rr()
            self.tt()
            self.bb()
            self.ttp()
            self.bbp()

            self.tt()
            self.rr()
            self.ttp()
            self.rrp()
            self.ttp()
            self.ffp()
            self.tt()
            self.ff()
            FR, FL, BR, BL = self.position_middle_edges()

        if FR == ('b', (2, 1)) or FR == self.corresponding_sides('b', (2, 1)):
            self.ttp()
            self.rr()
            self.ttp()
            self.rrp()
            self.ttp()
            self.ffp()
            self.tt()
            self.ff()
            FR, FL, BR, BL = self.position_middle_edges()
        self.solving = False

    def solve_edge_front_left(self):
        self.solving = True
        self.solved_moves.append('\nFront-Left edge\n')
        FR, FL, BR, BL = self.position_middle_edges()

        if FL == ('f', (1, 0)) or FL == self.corresponding_sides('f', (1, 0)):
            FR, FL, BR, BL = self.position_middle_edges()
            pass

        if FL == ('f', (0, 1)) or FL == self.corresponding_sides('f', (0, 1)):
            self.ttp()
            self.llp()
            self.tt()
            self.ll()
            self.tt()
            self.ff()
            self.ttp()
            self.ffp()
            FR, FL, BR, BL = self.position_middle_edges()

        if FL == ('f', (1, 2)) or FL == self.corresponding_sides('f', (1, 2)):
            self.rr()
            self.ttp()
            self.rrp()
            self.ttp()
            self.ffp()
            self.tt()
            self.ff()

            self.ff()
            self.ttp()
            self.ffp()
            self.ttp()
            self.llp()
            self.tt()
            self.ll()
            FR, FL, BR, BL = self.position_middle_edges()

        if FL == ('t', (1, 0)) or FL == self.corresponding_sides('t', (1, 0)):
            self.ttp()
            self.ttp()
            self.llp()
            self.tt()
            self.ll()
            self.tt()
            self.ff()
            self.ttp()
            self.ffp()
            FR, FL, BR, BL = self.position_middle_edges()

        if FL == ('t', (1, 2)) or FL == self.corresponding_sides('t', (1, 2)):
            self.llp()
            self.tt()
            self.ll()
            self.tt()
            self.ff()
            self.ttp()
            self.ffp()
            FR, FL, BR, BL = self.position_middle_edges()

        if FL == ('b', (1, 0)) or FL == self.corresponding_sides('b', (1, 0)):
            self.bbp()
            self.tt()
            self.bb()
            self.tt()
            self.ll()
            self.ttp()
            self.llp()

            self.llp()
            self.tt()
            self.ll()
            self.tt()
            self.ff()
            self.ttp()
            self.ffp()
            FR, FL, BR, BL = self.position_middle_edges()

        if FL == ('b', (1, 2)) or FL == self.corresponding_sides('b', (1, 2)):
            self.bb()
            self.tt()
            self.bbp()
            self.ttp()
            self.rrp()
            self.ttp()
            self.rr()

            self.ttp()
            self.ttp()
            self.llp()
            self.tt()
            self.ll()
            self.tt()
            self.ff()
            self.ttp()
            self.ffp()
            FR, FL, BR, BL = self.position_middle_edges()

        if FL == ('b', (2, 1)) or FL == self.corresponding_sides('b', (2, 1)):
            self.tt()
            self.llp()
            self.tt()
            self.ll()
            self.tt()
            self.ff()
            self.ttp()
            self.ffp()
            FR, FL, BR, BL = self.position_middle_edges()
        self.solving = False

    def solve_edge_back_left(self):
        self.solving = True
        self.solved_moves.append('\nBack-Left edge\n')
        FR, FL, BR, BL = self.position_middle_edges()

        if BL == ('f', (1, 0)) or BL == self.corresponding_sides('f', (1, 0)):
            self.llp()
            self.tt()
            self.ll()
            self.tt()
            self.ff()
            self.ttp()
            self.ffp()

            self.tt()
            self.ll()
            self.ttp()
            self.llp()
            self.ttp()
            self.bbp()
            self.tt()
            self.bb()
            FR, FL, BR, BL = self.position_middle_edges()

        if BL == ('f', (0, 1)) or BL == self.corresponding_sides('f', (0, 1)):
            self.bbp()
            self.tt()
            self.bb()
            self.tt()
            self.ll()
            self.ttp()
            self.llp()
            FR, FL, BR, BL = self.position_middle_edges()

        if BL == ('f', (1, 2)) or BL == self.corresponding_sides('f', (1, 2)):
            self.rr()
            self.ttp()
            self.rrp()
            self.ttp()
            self.ffp()
            self.tt()
            self.ff()

            self.tt()
            self.ll()
            self.ttp()
            self.llp()
            self.ttp()
            selb.bbp()
            self.tt()
            self.bb()
            FR, FL, BR, BL = self.position_middle_edges()

        if BL == ('t', (1, 0)) or BL == self.corresponding_sides('t', (1, 0)):
            self.ttp()
            self.bbp()
            self.tt()
            self.bb()
            self.tt()
            self.ll()
            self.ttp()
            self.llp()
            FR, FL, BR, BL = self.position_middle_edges()

        if BL == ('t', (1, 2)) or BL == self.corresponding_sides('t', (1, 2)):
            self.tt()
            self.bbp()
            self.tt()
            self.bb()
            self.tt()
            self.ll()
            self.ttp()
            self.llp()
            FR, FL, BR, BL = self.position_middle_edges()

        if BL == ('b', (1, 0)) or BL == self.corresponding_sides('b', (1, 0)):
            pass
            FR, FL, BR, BL = self.position_middle_edges()

        if BL == ('b', (1, 2)) or BL == self.corresponding_sides('b', (1, 2)):
            self.rrp()
            self.tt()
            self.rr()
            self.tt()
            self.bb()
            self.ttp()
            self.bbp()

            self.bbp()
            self.tt()
            self.bb()
            self.tt()
            self.ll()
            self.ttp()
            self.llp()
            FR, FL, BR, BL = self.position_middle_edges()

        if BL == ('b', (2, 1)) or BL == self.corresponding_sides('b', (2, 1)):
            self.ttp()
            self.ttp()
            self.bbp()
            self.tt()
            self.bb()
            self.tt()
            self.ll()
            self.ttp()
            self.llp()
            FR, FL, BR, BL = self.position_middle_edges()
        self.solving = False

    def solve_edge_back_right(self):
        self.solving = True
        self.solved_moves.append('\nBack-Right edge\n')
        FR, FL, BR, BL = self.position_middle_edges()

        if BR == ('f', (1, 0)) or BR == self.corresponding_sides('f', (1, 0)):
            self.llp()
            self.tt()
            self.ll()
            self.tt()
            self.ff()
            self.ttp()
            self.ffp()

            self.ttp()
            self.rrp()
            self.tt()
            self.rr()
            self.tt()
            self.bb()
            self.ttp()
            self.bbp()
            FR, FL, BR, BL = self.position_middle_edges()

        if BR == ('f', (0, 1)) or BR == self.corresponding_sides('f', (0, 1)):
            self.bb()
            self.ttp()
            self.bbp()
            self.ttp()
            self.rrp()
            self.tt()
            self.rr()
            FR, FL, BR, BL = self.position_middle_edges()

        if BR == ('f', (1, 2)) or BR == self.corresponding_sides('f', (1, 2)):
            self.rr()
            self.ttp()
            self.rrp()
            self.ttp()
            self.ffp()
            self.tt()
            self.ff()

            self.ttp()
            self.rrp()
            self.tt()
            self.rr()
            self.tt()
            self.bb()
            self.ttp()
            self.bbp()
            FR, FL, BR, BL = self.position_middle_edges()

        if BR == ('t', (1, 0)) or BR == self.corresponding_sides('t', (1, 0)):
            self.rrp()
            self.tt()
            self.rr()
            self.tt()
            self.bb()
            self.ttp()
            self.bbp()
            FR, FL, BR, BL = self.position_middle_edges()

        if BR == ('t', (1, 2)) or BR == self.corresponding_sides('t', (1, 2)):
            self.tt()
            self.bb()
            self.ttp()
            self.bbp()
            self.ttp()
            self.rrp()
            self.tt()
            self.rr()
            FR, FL, BR, BL = self.position_middle_edges()

        if BR == ('b', (1, 0)) or BR == self.corresponding_sides('b', (1, 0)):
            self.ll()
            self.ttp()
            self.llp()
            self.ttp()
            self.bbp()
            self.tt()
            self.bb()

            self.bb()
            self.ttp()
            self.bbp()
            self.ttp()
            self.rrp()
            self.tt()
            self.rr()
            FR, FL, BR, BL = self.position_middle_edges()

        if BR == ('b', (1, 2)) or BR == self.corresponding_sides('b', (1, 2)):
            pass
            FR, FL, BR, BL = self.position_middle_edges()

        if BR == ('b', (2, 1)) or BR == self.corresponding_sides('b', (2, 1)):
            self.ttp()
            self.rrp()
            self.tt()
            self.rr()
            self.tt()
            self.bb()
            self.ttp()
            self.bbp()
            FR, FL, BR, BL = self.position_middle_edges()

        self.solving = False

    def middle_edge_check_flip(self):
        if (self.front[1][0] == self.front_center and self.left[1][2] == self.left_center):
            Fr_Left = True
        else:
            Fr_Left = False

        if (self.front[1][2] == self.front_center and self.right[1][0] == self.right_center):
            Fr_Right = True
        else:
            Fr_Right = False

        if (self.back[1][0] == self.back_center and self.left[1][0] == self.left_center):
            Ba_Left = True
        else:
            Ba_Left = False

        if (self.back[1][2] == self.back_center and self.right[1][2] == self.right_center):
            Ba_Right = True
        else:
            Ba_Right = False
        return Fr_Left, Fr_Right, Ba_Left, Ba_Right

    def orient_middle_edge(self):
        self.solving = True
        Fr_Left, Fr_Right, Ba_Left, Ba_Right = self.middle_edge_check_flip()
        if Fr_Left == False:
            self.llp()
            self.tt()
            self.ll()
            self.tt()
            self.ff()
            self.ttp()
            self.ffp()

            self.tt()
            self.llp()
            self.tt()
            self.ll()
            self.tt()
            self.ff()
            self.ttp()
            self.ffp()

        Fr_Left, Fr_Right, Ba_Left, Ba_Right = self.middle_edge_check_flip()
        if Fr_Right == False:
            self.rr()
            self.ttp()
            self.rrp()
            self.ttp()
            self.ffp()
            self.tt()
            self.ff()

            self.ttp()
            self.rr()
            self.ttp()
            self.rrp()
            self.ttp()
            self.ffp()
            self.tt()
            self.ff()

        Fr_Left, Fr_Right, Ba_Left, Ba_Right = self.middle_edge_check_flip()
        if Ba_Left == False:
            self.ll()
            self.ttp()
            self.llp()
            self.ttp()
            self.bbp()
            self.tt()
            self.bb()

            self.ttp()
            self.ll()
            self.ttp()
            self.llp()
            self.ttp()
            self.bbp()
            self.tt()
            self.bb()

        Fr_Left, Fr_Right, Ba_Left, Ba_Right = self.middle_edge_check_flip()
        if Ba_Right == False:
            self.rrp()
            self.tt()
            self.rr()
            self.tt()
            self.bb()
            self.ttp()
            self.bbp()

            self.tt()
            self.rrp()
            self.tt()
            self.rr()
            self.tt()
            self.bb()
            self.ttp()
            self.bbp()

    def top_edge_check(self):
        top_edges = [self.top[1][0], self.top[0][1], self.top[1][2], self.top[2][1]]
        counter_top = 0
        for i in top_edges:
            if i == self.top_center:
                counter_top += 1

        return counter_top

    def solve_top_edge(self):
        is_solved = False
        counter = 0
        while is_solved == False:

            if self.top_edge_check() == 0:
                self.ff()
                self.rr()
                self.tt()
                self.rrp()
                self.ttp()
                self.ffp()

            elif self.top_edge_check() == 2 and (self.top[1][0], self.top[0][1]) == (self.top_center, self.top_center):
                self.ff()
                self.rr()
                self.tt()
                self.rrp()
                self.ttp()
                self.ffp()

            elif self.top_edge_check() == 2 and (self.top[0][1], self.top[1][2]) == (self.top_center, self.top_center):
                self.ttp()
                self.ff()
                self.rr()
                self.tt()
                self.rrp()
                self.ttp()
                self.ffp()

            elif self.top_edge_check() == 2 and (self.top[1][2], self.top[2][1]) == (self.top_center, self.top_center):
                self.ttp()
                self.ttp()
                self.ff()
                self.rr()
                self.tt()
                self.rrp()
                self.ttp()
                self.ffp()

            elif self.top_edge_check() == 2 and (self.top[2][1], self.top[1][0]) == (self.top_center, self.top_center):
                self.tt()
                self.ff()
                self.rr()
                self.tt()
                self.rrp()
                self.ttp()
                self.ffp()

            elif self.top_edge_check() == 2 and (self.top[1][0], self.top[1][2]) == (self.top_center, self.top_center):
                self.ff()
                self.rr()
                self.tt()
                self.rrp()
                self.ttp()
                self.ffp()

            elif self.top_edge_check() == 2 and (self.top[0][1], self.top[2][1]) == (self.top_center, self.top_center):
                self.tt()
                self.ff()
                self.rr()
                self.tt()
                self.rrp()
                self.ttp()
                self.ffp()

            elif self.top_edge_check() == 4:
                is_solved = True

            counter += 1
            if counter == 10:
                raise RubiksError()

    def position_top_edge(self):
        position = [(1, 0), (0, 1), (1, 2), (2, 1)]
        T_R, T_L, T_F, T_B = False, False, False, False
        if self.top[1][2] == self.top_center and self.right[0][1] == self.right_center:
            T_R = True
        if self.top[1][0] == self.top_center and self.left[0][1] == self.left_center:
            T_L = True
        if self.top[2][1] == self.top_center and self.front[0][1] == self.front_center:
            T_F = True
        if self.top[0][1] == self.top_center and self.back[2][1] == self.back_center:
            T_B = True
        return T_R, T_L, T_F, T_B

    def tester(self):
        pass

    def orient_top_edge(self):
        def count():
            pos = self.position_top_edge()
            c = 0
            for i in pos:
                if i == True:
                    c += 1
            return c

        is_solved = False
        counter = 0
        while is_solved == False:
            if count() == 0:
                self.tt()

            elif count() == 1:
                self.tt()

            elif count() == 2 and self.position_top_edge() == (False, True, True, False):
                self.tt()
                self.tt()
                self.rr()
                self.tt()
                self.rrp()
                self.tt()
                self.rr()
                self.tt()
                self.tt()
                self.rrp()
                self.ttp()

            elif count() == 2 and self.position_top_edge() == (False, True, False, True):
                self.tt()
                self.rr()
                self.tt()
                self.rrp()
                self.tt()
                self.rr()
                self.tt()
                self.tt()
                self.rrp()
                self.tt()

            elif count() == 2 and self.position_top_edge() == (True, False, False, True):
                self.rr()
                self.tt()
                self.rrp()
                self.tt()
                self.rr()
                self.tt()
                self.tt()
                self.rrp()
                self.tt()

            elif count() == 2 and self.position_top_edge() == (True, False, True, False):
                self.ttp()
                self.rr()
                self.tt()
                self.rrp()
                self.tt()
                self.rr()
                self.tt()
                self.tt()
                self.rrp()
                self.tt()
                self.tt()

            elif count() == 2 and self.position_top_edge() == (True, True, False, False):
                self.rr()
                self.tt()
                self.rrp()
                self.tt()
                self.rr()
                self.tt()
                self.tt()
                self.rrp()

            elif count() == 2 and self.position_top_edge() == (False, False, True, True):
                self.rr()
                self.tt()
                self.rrp()
                self.tt()
                self.rr()
                self.tt()
                self.tt()
                self.rrp()

            elif count() == 4:
                is_solved = True

            counter += 1
            if counter == 10:
                raise RubiksError()

    def position_top_corner(self):
        faces = {'f': self.front, 't': self.top, 'b': self.back,
                 'bo': self.bottom, 'l': self.left, 'r': self.right}
        faces_spec = {'t': self.top}
        positions = [(0, 0), (0, 2), (2, 2), (2, 0)]
        T_f_r_corner, T_f_l_corner, T_b_r_corner, T_b_l_corner = False, False, False, False

        for face in faces_spec:
            for pos in positions:
                i, j = pos
                (face2, pos2), (face3, pos3) = self.corresponding_corners(face, pos)

                x = faces[face][i][j]
                y = faces[face2][pos2[0]][pos2[1]]
                z = faces[face3][pos3[0]][pos3[1]]

                if ((x == self.top_center or x == self.front_center or x == self.right_center)
                        and (y == self.top_center or y == self.front_center or y == self.right_center)
                        and (z == self.top_center or z == self.front_center or z == self.right_center) and pos == (2, 2)):
                    T_f_r_corner = True

                if ((x == self.top_center or x == self.front_center or x == self.left_center)
                        and (y == self.top_center or y == self.front_center or y == self.left_center)
                        and (z == self.top_center or z == self.front_center or z == self.left_center) and pos == (2, 0)):
                    T_f_l_corner = True

                if ((x == self.top_center or x == self.back_center or x == self.right_center)
                        and (y == self.top_center or y == self.back_center or y == self.right_center)
                        and (z == self.top_center or z == self.back_center or z == self.right_center) and pos == (0, 2)):
                    T_b_r_corner = True

                if ((x == self.top_center or x == self.back_center or x == self.left_center)
                        and (y == self.top_center or y == self.back_center or y == self.left_center)
                        and (z == self.top_center or z == self.back_center or z == self.left_center) and pos == (0, 0)):
                    T_b_l_corner = True

        return T_f_r_corner, T_f_l_corner, T_b_r_corner, T_b_l_corner

    def solve_corner_top(self):
        self.solving = True
        T_f_r_corner, T_f_l_corner, T_b_r_corner, T_b_l_corner = self.position_top_corner()
        solved = False
        first = True

        if (T_f_r_corner, T_f_l_corner, T_b_r_corner, T_b_l_corner) == (False, False, False, False) and first == True:

            def rotate():
                self.tt()
                self.rr()
                self.ttp()
                self.llp()
                self.tt()
                self.rrp()
                self.ttp()
                self.ll()

            counter = 0
            while first == True:
                rotate()
                T_f_r_corner, T_f_l_corner, T_b_r_corner, T_b_l_corner = self.position_top_corner()
                if (T_f_r_corner, T_f_l_corner, T_b_r_corner, T_b_l_corner) != (False, False, False, False):
                    first = False
                    counter += 1
                    if counter == 10:
                        raise RubiksError()

        if (T_f_r_corner, T_f_l_corner, T_b_r_corner, T_b_l_corner) == (True, False, False, False):

            def rotate():
                self.tt()
                self.rr()
                self.ttp()
                self.llp()
                self.tt()
                self.rrp()
                self.ttp()
                self.ll()

            counter2 = 0
            while solved == False:
                rotate()
                T_f_r_corner, T_f_l_corner, T_b_r_corner, T_b_l_corner = self.position_top_corner()
                if (T_f_r_corner, T_f_l_corner, T_b_r_corner, T_b_l_corner) == (True, True, True, True):
                    solved = True
                    counter2 += 1
                    if counter2 == 10:
                        raise RubiksError()

        if (T_f_r_corner, T_f_l_corner, T_b_r_corner, T_b_l_corner) == (False, True, False, False):

            def rotate():
                self.ttp()
                self.llp()
                self.tt()
                self.rr()
                self.ttp()
                self.ll()
                self.tt()
                self.rrp()

            counter3 = 0
            while solved == False:
                rotate()
                T_f_r_corner, T_f_l_corner, T_b_r_corner, T_b_l_corner = self.position_top_corner()
                if (T_f_r_corner, T_f_l_corner, T_b_r_corner, T_b_l_corner) == (True, True, True, True):
                    solved = True
                    counter3 += 1
                    if counter3 == 10:
                        raise RubiksError()

        if (T_f_r_corner, T_f_l_corner, T_b_r_corner, T_b_l_corner) == (False, False, True, False):

            def rotate():
                self.tt()
                self.bb()
                self.ttp()
                self.ffp()
                self.tt()
                self.bbp()
                self.ttp()
                self.ff()

            counter4 = 0
            while solved == False:
                rotate()
                T_f_r_corner, T_f_l_corner, T_b_r_corner, T_b_l_corner = self.position_top_corner()
                if (T_f_r_corner, T_f_l_corner, T_b_r_corner, T_b_l_corner) == (True, True, True, True):
                    solved = True
                    counter4 += 1
                    if counter4 == 10:
                        raise RubiksError()

        if (T_f_r_corner, T_f_l_corner, T_b_r_corner, T_b_l_corner) == (False, False, False, True):

            def rotate():
                self.ttp()
                self.bbp()
                self.tt()
                self.ff()
                self.ttp()
                self.bb()
                self.tt()
                self.ffp()

            counter5 = 0
            while solved == False:
                rotate()
                T_f_r_corner, T_f_l_corner, T_b_r_corner, T_b_l_corner = self.position_top_corner()
                if (T_f_r_corner, T_f_l_corner, T_b_r_corner, T_b_l_corner) == (True, True, True, True):
                    solved = True
                    counter5 += 1
                    if counter5 == 10:
                        raise RubiksError()

    def orient_corner_top(self):
        faces_spec = {'t': self.top}
        positions = [(0, 0), (0, 2), (2, 2), (2, 0)]
        T_b_r_corner, T_b_l_corner, T_f_r_corner, T_f_l_corner = False, False, False, False

        for face in faces_spec:
            for pos in positions:

                if ((pos == (0, 0) and self.top[0][0] == self.top_center and self.back[2][0] == self.back_center and self.left[0][0] == self.left_center)):
                    T_b_r_corner = True

                if ((pos == (0, 2) and self.top[0][2] == self.top_center and self.back[2][2] == self.back_center and self.right[0][2] == self.right_center)):
                    T_b_l_corner = True

                if ((pos == (2, 2) and self.top[2][2] == self.top_center and self.front[0][2] == self.front_center and self.right[0][0] == self.right_center)):
                    T_f_r_corner = True

                if ((pos == (2, 0) and self.top[2][0] == self.top_center and self.front[0][0] == self.front_center and self.left[0][2] == self.left_center)):
                    T_f_l_corner = True

        return T_b_r_corner, T_b_l_corner, T_f_r_corner, T_f_l_corner

    def check_orient_corner(self):
        check = False
        if ((self.top[2][2] == self.top_center and self.front[0][2] == self.front[0][1] and self.right[0][0] == self.right[0][1])):
            check = True
        return check

    def orient_corner_top_solve(self):
        T_b_r_corner, T_b_l_corner, T_f_r_corner, T_f_l_corner = self.orient_corner_top()
        if (T_b_r_corner, T_b_l_corner, T_f_r_corner, T_f_l_corner) == (True, True, True, True):
            solved = True
        else:
            solved = False

        counter = 0
        while solved == False:

            if (self.orient_corner_top()) == (False, False, False, False):

                def rotate():
                    self.rrp()
                    self.bbop()
                    self.rr()
                    self.bbo()
                while self.check_orient_corner() == False:
                    rotate()
                self.ttp()
                while self.check_orient_corner() == False:
                    rotate()
                self.ttp()
                while self.check_orient_corner() == False:
                    rotate()
                self.ttp()
                while self.check_orient_corner() == False:
                    rotate()
                self.ttp()
                solved = True

            if (self.orient_corner_top()) == (False, False, False, True):

                def rotate():
                    self.rrp()
                    self.bbop()
                    self.rr()
                    self.bbo()
                while self.check_orient_corner() == False:
                    rotate()
                self.ttp()
                self.ttp()
                while self.check_orient_corner() == False:
                    rotate()
                self.ttp()
                while self.check_orient_corner() == False:
                    rotate()
                self.ttp()
                solved = True

            if (self.orient_corner_top()) == (False, False, True, False):

                def rotate():
                    self.rrp()
                    self.bbop()
                    self.rr()
                    self.bbo()
                self.ttp()
                while self.check_orient_corner() == False:
                    rotate()
                self.ttp()
                while self.check_orient_corner() == False:
                    rotate()
                self.ttp()
                while self.check_orient_corner() == False:
                    rotate()
                self.ttp()
                solved = True

            if (self.orient_corner_top()) == (False, True, False, False):

                def rotate():
                    self.rrp()
                    self.bbop()
                    self.rr()
                    self.bbo()
                while self.check_orient_corner() == False:
                    rotate()
                self.ttp()
                while self.check_orient_corner() == False:
                    rotate()
                self.ttp()
                while self.check_orient_corner() == False:
                    rotate()
                self.ttp()
                self.ttp()
                solved = True

            if (self.orient_corner_top()) == (True, False, False, False):

                def rotate():
                    self.rrp()
                    self.bbop()
                    self.rr()
                    self.bbo()
                while self.check_orient_corner() == False:
                    rotate()
                self.ttp()
                while self.check_orient_corner() == False:
                    rotate()
                self.ttp()
                self.ttp()
                while self.check_orient_corner() == False:
                    rotate()
                self.ttp()
                solved = True

            if (self.orient_corner_top()) == (True, True, False, False):

                def rotate():
                    self.rrp()
                    self.bbop()
                    self.rr()
                    self.bbo()
                while self.check_orient_corner() == False:
                    rotate()
                self.ttp()
                while self.check_orient_corner() == False:
                    rotate()
                self.ttp()
                self.ttp()
                self.ttp()
                solved = True

            if (self.orient_corner_top()) == (True, False, True, False):

                def rotate():
                    self.rrp()
                    self.bbop()
                    self.rr()
                    self.bbo()
                self.ttp()
                while self.check_orient_corner() == False:
                    rotate()
                self.ttp()
                self.ttp()
                while self.check_orient_corner() == False:
                    rotate()
                self.ttp()
                solved = True

            if (self.orient_corner_top()) == (True, False, False, True):

                def rotate():
                    self.rrp()
                    self.bbop()
                    self.rr()
                    self.bbo()

                while self.check_orient_corner() == False:
                    rotate()
                self.ttp()
                self.ttp()
                self.ttp()

                while self.check_orient_corner() == False:
                    rotate()
                self.ttp()
                solved = True

            if (self.orient_corner_top()) == (False, True, False, True):

                def rotate():
                    self.rrp()
                    self.bbop()
                    self.rr()
                    self.bbo()
                while self.check_orient_corner() == False:
                    rotate()
                self.ttp()
                self.ttp()
                while self.check_orient_corner() == False:
                    rotate()
                self.ttp()
                self.ttp()
                solved = True

            if (self.orient_corner_top()) == (False, True, True, False):

                def rotate():
                    self.rrp()
                    self.bbop()
                    self.rr()
                    self.bbo()
                self.ttp()
                while self.check_orient_corner() == False:
                    rotate()
                self.ttp()
                while self.check_orient_corner() == False:
                    rotate()
                self.ttp()
                self.ttp()
                solved = True

            if (self.orient_corner_top()) == (False, False, True, True):

                def rotate():
                    self.rrp()
                    self.bbop()
                    self.rr()
                    self.bbo()
                self.ttp()
                self.ttp()
                while self.check_orient_corner() == False:
                    rotate()
                self.ttp()
                while self.check_orient_corner() == False:
                    rotate()
                self.ttp()
                solved = True

            counter += 1
            if counter == 10:
                raise RubiksError()

    def ff(self):
        self.f_90()
        self.list_of_moves.append('F')
        self.total_moves += 1
        if self.solving:
            self.solved_moves.append('F')

    def ffp(self):
        self.f_prime_90()
        self.list_of_moves.append('F\'')
        self.total_moves += 1
        if self.solving:
            self.solved_moves.append('F\'')

    def tt(self):
        self.t_90()
        self.list_of_moves.append('U')
        self.total_moves += 1
        if self.solving:
            self.solved_moves.append('U')

    def ttp(self):
        self.t_prime_90()
        self.list_of_moves.append('U\'')
        self.total_moves += 1
        if self.solving:
            self.solved_moves.append('U\'')

    def bb(self):
        self.b_90()
        self.list_of_moves.append('B')
        self.total_moves += 1
        if self.solving:
            self.solved_moves.append('B')

    def bbp(self):
        self.b_prime_90()
        self.list_of_moves.append('B\'')
        self.total_moves += 1
        if self.solving:
            self.solved_moves.append('B\'')

    def bbo(self):
        self.bo_90()
        self.list_of_moves.append('D')
        self.total_moves += 1
        if self.solving:
            self.solved_moves.append('D')

    def bbop(self):
        self.bo_prime_90()
        self.list_of_moves.append('D\'')
        self.total_moves += 1
        if self.solving:
            self.solved_moves.append('D\'')

    def ll(self):
        self.l_90()
        self.list_of_moves.append('L')
        self.total_moves += 1
        if self.solving:
            self.solved_moves.append('L')

    def llp(self):
        self.l_prime_90()
        self.list_of_moves.append('L\'')
        self.total_moves += 1
        if self.solving:
            self.solved_moves.append('L\'')

    def rr(self):
        self.r_90()
        self.list_of_moves.append('R')
        self.total_moves += 1
        if self.solving:
            self.solved_moves.append('R')

    def rrp(self):
        self.r_prime_90()
        self.list_of_moves.append('R\'')
        self.total_moves += 1
        if self.solving:
            self.solved_moves.append('R\'')
