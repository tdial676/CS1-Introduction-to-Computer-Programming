"""
Provided testing program for Final Part A Rubik's cube
(rubiks_rep.py) program.

Note that these are not pytest tests, and have a bit
more useful display/feedback for tests involving output
for the purposes of the Final Exam.
"""
import random
import string
import traceback as tb
from rubiks_rep import RubiksRep

NTESTS = 100


# Custom TestError for this test program.
class TestError(Exception):
    pass


# ----------------------------------------------------------------------
# Test framework.
# ----------------------------------------------------------------------

# Global variables.
ntests = 0
test_failures = 0
test_successes = 0


def reset_test_counts():
    """
    Reset the test counter variables to 0.
    """

    global ntests, test_failures, test_successes
    ntests = 0
    test_failures = 0
    test_successes = 0


def run_test(testfunc):
    """
    Run a test.  Catch and display any tracebacks.
    Update test statistics.

    Arguments:
      testfunc -- the test function

    Return value: none

    Side effects:
      The global variables 'ntests', 'test_failures', and 'test_successes'
      may be updated.
    """

    global ntests, test_failures, test_successes
    print('{} ... '.format(testfunc.__name__), end='')
    ntests += 1
    try:
        testfunc()
    except AssertionError as e:
        traceback_str = ''.join(tb.format_tb(e.__traceback__))
        print()
        print('-' * 70)
        print(traceback_str.strip())
        print('-' * 70)
        test_failures += 1
        print('test failed\n')
        return
    test_successes += 1
    print('passed')


def wrap_up():
    """Print overall test results."""
    print(f'Number of tests:  {ntests:4}')
    print(f'Tests passed:     {test_successes:4}')
    print(f'Tests failed:     {test_failures:4}')
    print()


def check_equal(expected, actual, err_msg):
    """
    Check if an expected value equals an actual value.
    If so, return True.
    If not, print an error message and return False.
    """
    if expected != actual:
        print(f'\nCHECK EQUALITY ERROR: {err_msg}')
        print(f'  Expected: {expected}')
        print(f'  Got: {actual}')
        return False
    return True


def check(expr):
    try:
        expr()
        return True
    except TestError as e:
        print(e)
        return False


# ----------------------------------------------------------------------
# Helper functions.
# ----------------------------------------------------------------------

def uniform_list_of_lists(lst, size):
    """
    Check that a list of lists contains a single value.
    """
    assert size > 0

    val = lst[0][0]
    for sublist in lst:
        for item in sublist:
            assert item == val
            # if item != val:
            #     msg = 'list {lst} has more than one color'
            #     raise TestError(msg)


def validate_cube_lite(cube, size):
    """
    Check if a cube representation is valid.
    NOTE: Doesn't check colors.
    NOTE: Doesn't check for parity errors.
    """

    # Check that the cube is a dictionary.
    assert type(cube) is dict
    # if type(cube) is not dict:
    #     print(f'cube: {cube}')
    #     raise TestError('cube is not a dictionary')

    # Check that there are exactly six keys: 'U', 'D', 'F', 'B', 'L' and 'R'.
    assert set(cube.keys()) == {'U', 'D', 'F', 'B', 'L', 'R'}
    #     print(f'cube: {cube}')
    #     raise TestError('cube does not have the correct keys: U D F B L R')

    # Check that all values are size*size lists of lists.
    for (key, val) in cube.items():
        assert type(val) is list
        # if type(val) is not list:
        #     print(f'key: {key}; value: {val}')
        #     raise TestError('cube value is not a list')
        assert len(val) == size 
        # if len(val) != size:
        #     print(f'key: {key}; value: {val}')
        #     msg = f'cube value does not have the right length: {size}'
        #     raise TestError(msg)
        for item in val:
              assert type(item) is list
        #     if type(item) is not list:
        #         print(f'key: {key}; value: {val}')
        #         raise TestError(f'cube value is not a list of lists')
              assert len(item) == size
        #     if len(item) != size:
        #         print(f'key: {key}; value: {val}')
        #         msg = f'value sublist does not have the right length: {size}'
        #         raise TestError(msg)

    # Check for aliasing.
    for val in cube.values():
        for i in range(size):
            for j in range(i + 1, size):
                # Assert that sublists are not aliases
                assert val[i] is not val[j]
                # if val[i] is val[j]:   # identity checking
                #     msg = f'val {val}: sublists {i} and {j} are aliases'
                #     return TestError(msg)


def validate_cube(cube, size):
    """
    Check if a cube representation is valid, raising a TestError
    with a descriptive error message if not.
    NOTE: Doesn't check for parity errors.
    """

    # Check that the cube is a dictionary.
    assert type(cube) is dict
    # if type(cube) is not dict:
    #     print(f'cube: {cube}')
    #     raise TestError('cube is not a dictionary')

    # Check that there are exactly six keys: 'U', 'D', 'F', 'B', 'L' and 'R'.
    assert set(cube.keys()) == {'U', 'D', 'F', 'B', 'L', 'R'}
    # if set(cube.keys()) != {'U', 'D', 'F', 'B', 'L', 'R'}:
    #     print(f'cube: {cube}')
    #     raise TestError('cube does not have the correct keys: U D F B L R')

    # Color counts.
    counts = {'r': 0, 'g': 0, 'b': 0, 'y': 0, 'o': 0, 'w': 0}

    # Check that all values are size*size lists of lists.
    for (key, val) in cube.items():
        assert type(val) is list
        # if type(val) is not list:
        #     print(f'key: {key}; value: {val}')
        #     raise TestError('cube value is not a list')
        assert len(val) == size
        # if len(val) != size:
        #     print(f'key: {key}; value: {val}')
        #     msg = f'cube value does not have the right length: {size}'
        #     raise TestError(msg)
        for item in val:
            assert type(item) is list
        #           if type(item) is not list:
        #               print(f'key: {key}; value: {val}')
        #               raise TestError(f'cube value is not a list of lists')
            assert len(item) == size
        #           if len(item) != size:
        #               print(f'key: {key}; value: {val}')
        #               msg = f'value sublist does not have the right length: {size}'
        #               raise TestError(msg)

            # Check that all values are one of six color characters: 'rgbyow'.
            for color in item:
                assert color in ['r', 'g', 'b', 'y', 'o', 'w']
                # if color not in ['r', 'g', 'b', 'y', 'o', 'w']:
                #     print(f'key: {key}; value: {val}; color: {color}')
                #     msg = f'color is not one of the acceptable colors: r g b y o w'
                #     raise TestError(msg)
                counts[color] += 1

    # Check that the sum of each color character is size*size.
    for color in counts:
        count = counts[color]
        expected = size * size
        assert count == expected
        # if count != expected:
        #     msg = 'Invalid count of color {}: expected {}, got {}'
        #     msg = msg.format(color, expected, count)
        #     raise TestError(msg)

    # Check for aliasing.
    for val in cube.values():
        for i in range(size):
            for j in range(i + 1, size):
                # Test that val[j] and val[j] are not aliases of each other
                assert val[i] is not val[j]
                # if val[i] is val[j]:   # identity checking
                #     msg = f'val {val}: sublists {i} and {j} are aliases'
                #     return TestError(msg)


# ----------------------------------------------------------------------
# Tests.
# ----------------------------------------------------------------------

def test_init():
    """
    Tests for correctness of Part A.1 using different sizes (not just
    2x2x2 or 3x3x3).
    """
    face_colors = {
        'U': 'w', 'D': 'y', 'F': 'r', 'B': 'o', 'L': 'g', 'R': 'b'
    }

    for size in [2, 3, 4, 5, 6, 7]:
        rep = RubiksRep(size)
        assert rep.size == size
        assert type(rep.face_contents) is dict
        assert set(rep.face_contents.keys()) == {'U', 'D', 'F', 'B', 'L', 'R'}
        contents = rep.face_contents

        assert check(lambda: validate_cube(contents, size))

        # Check that each face only has one color.
        for face in contents:
            vals = contents[face]
            assert check(lambda: uniform_list_of_lists(vals, size))

            # Check that it's the right color.
            ok_col = face_colors[face]
            assert check_equal(vals[0][0], ok_col,
                               f'face: {vals} should only have color {ok_col}')


def test_get_row():
    """
    Tests for correctness of Part A.2 using a 2x2x2 and 3x3x3
    cube representation.
    """
    # Check that getting a known row gets the right thing.
    rep = RubiksRep(3)
    rep.test_faces()  # Use fake contents.
    r1 = rep.get_row('U', 0)
    assert r1 == ['a', 'b', 'c']
    r2 = rep.get_row('D', 2)
    assert r2 == ['p', 'q', 'r']
    r3 = rep.get_row('F', 1)
    assert r3 == ['v', 'w', 'x']
    r4 = rep.get_row('B', 1)
    assert r4 == ['E', 'F', 'G']
    r5 = rep.get_row('L', 0)
    assert r5 == ['K', 'L', 'M']
    r6 = rep.get_row('R', 2)
    assert r6 == ['Z', '@', '#']
    # Check that changing the contents of a retrieved row doesn't affect
    # the original row.
    r1 = rep.get_row('U', 0)
    r1[0] = '0'
    assert rep.get_row('U', 0) == ['a', 'b', 'c']

    # Check that getting a known row gets the right thing.
    rep = RubiksRep(2)
    rep.test_faces()  # Use fake contents.
    r1 = rep.get_row('U', 0)
    assert r1 == ['a', 'b']
    r2 = rep.get_row('D', 1)
    assert r2 == ['g', 'h']
    r3 = rep.get_row('F', 1)
    assert r3 == ['k', 'l']
    r4 = rep.get_row('B', 1)
    assert r4 == ['o', 'p']
    r5 = rep.get_row('L', 0)
    assert r5 == ['q', 'r']
    r6 = rep.get_row('R', 1)
    assert r6 == ['w', 'x']
    # Check that changing the contents of a retrieved row doesn't affect
    # the original row.
    r1 = rep.get_row('U', 0)
    r1[0] = '0'
    assert rep.get_row('U', 0) == ['a', 'b']


def test_get_col():
    """
    Tests for correctness of Part A.3 using a 2x2x2 and 3x3x3
    cube representation.
    """
    # Check that getting a known column gets the right thing.
    # Check that changing the contents of a retrieved column doesn't affect
    # the original column.
    # Check that getting a known row gets the right thing.
    rep = RubiksRep(3)
    rep.test_faces()  # Use fake contents.
    r1 = rep.get_col('U', 0)
    assert r1 == ['a', 'd', 'g']
    r2 = rep.get_col('D', 2)
    assert r2 == ['l', 'o', 'r']
    r3 = rep.get_col('F', 1)
    assert r3 == ['t', 'w', 'z']
    r4 = rep.get_col('B', 1)
    assert r4 == ['C', 'F', 'I']
    r5 = rep.get_col('L', 0)
    assert r5 == ['K', 'N', 'Q']
    r6 = rep.get_col('R', 2)
    assert r6 == ['V', 'Y', '#']
    # Check that changing the contents of a retrieved column doesn't affect
    # the original column.
    r1 = rep.get_col('U', 0)
    r1[0] = '0'
    assert rep.get_col('U', 0) == ['a', 'd', 'g']

    # Check that getting a known row gets the right thing.
    rep = RubiksRep(2)
    rep.test_faces()  # Use fake contents.
    r1 = rep.get_col('U', 0)
    assert r1 == ['a', 'c']
    r2 = rep.get_col('D', 1)
    assert r2 == ['f', 'h']
    r3 = rep.get_col('F', 1)
    assert r3 == ['j', 'l']
    r4 = rep.get_col('B', 1)
    assert r4 == ['n', 'p']
    r5 = rep.get_col('L', 0)
    assert r5 == ['q', 's']
    r6 = rep.get_col('R', 1)
    assert r6 == ['v', 'x']
    # Check that changing the contents of a retrieved column doesn't affect
    # the original column.
    r1 = rep.get_col('U', 0)
    r1[0] = '0'
    assert rep.get_col('U', 0) == ['a', 'c']


def test_set_row():
    """
    Tests for correctness of Part A.3 using a 2x2x2 and
    3x3x3 cube representation. Randomization is used
    in testing random cube samples.
    """
    # Check that setting a row and then getting the same row
    # returns a copy of the same row, but not the exact same row.
    for _ in range(NTESTS):
        for size in [2, 3]:
            rep = RubiksRep(size)
            # Generate a random face.
            face = random.choice('UDFBLR')
            # Generate a random row index.
            row_index = random.randrange(size)

            # Generate a random row.
            row_values = random.sample(string.ascii_letters, size)
            rep.set_row(face, row_index, row_values)
            retrieved = rep.get_row(face, row_index)
            assert retrieved == row_values
            # Make sure row returned is distinct from the row set.
            assert retrieved is not row_values

            # Generate a random row again.
            row_values = random.sample(string.ascii_letters, size)
            rep.set_row(face, row_index, row_values)
            # Check for aliasing.
            row_values[0] = '@'  # a non-alphabetic character.
            retrieved = rep.get_row(face, row_index)
            assert retrieved[0] != '@'


def test_set_col():
    """
    Tests for correctness of Part A.3 using a 2x2x2 and
    3x3x3 cube representation. Randomization is used to test
    for different cube samples.
    """
    # Check that setting a column and then getting the same column
    # returns a copy of the same column, but not the exact same column.
    for _ in range(NTESTS):
        for size in [2, 3]:
            rep = RubiksRep(size)
            # Generate a random face.
            face = random.choice('UDFBLR')
            # Generate a random column index.
            col_index = random.randrange(size)

            # Generate a random column.
            col_values = random.sample(string.ascii_letters, size)
            rep.set_col(face, col_index, col_values)
            retrieved = rep.get_col(face, col_index)
            assert retrieved == col_values
            # Make sure column returned is distinct from the column set.
            assert retrieved is not col_values

            # Generate a random column again.
            col_values = random.sample(string.ascii_letters, size)
            rep.set_col(face, col_index, col_values)
            # Check for aliasing.
            col_values[0] = '@'  # a non-alphabetic character.
            retrieved = rep.get_col(face, col_index)
            assert retrieved[0] != '@'


def test_get_face():
    """
    Tests for correctness of Part A.4 using a 2x2x2 and
    3x3x3 cube representation.
    """
    # Check that face has the appropriate properties
    # (list, size*size).
    # Check that it is equivalent but not identical to the internal face.
    for size in [2, 3]:
        rep = RubiksRep(size)
        for face in 'UDFBLR':
            contents = rep.get_face(face)
            assert contents == rep.face_contents[face]
            assert contents is not rep.face_contents[face]
            assert type(contents) is list
            assert len(contents) == size
            for i in range(size):
                row = contents[i]
                assert type(row) is list
                assert len(row) == size


def test_rotate_face():
    """
    Test the rotate_face_cw() and rotate_face_ccw() methods
    from A.5.
    """

    #
    # Size = 2
    #

    rep = RubiksRep(2)
    rep.test_faces()
    face_F_0 = [['i', 'j'], ['k', 'l']]
    face_F_1 = [['k', 'i'], ['l', 'j']]
    face_F_2 = [['l', 'k'], ['j', 'i']]
    face_F_3 = [['j', 'l'], ['i', 'k']]

    face_F = rep.get_face('F')
    face_U_0 = rep.get_face('U')
    assert check_equal(face_F, face_F_0, 'invalid F face')
    assert check(lambda: validate_cube_lite(rep.face_contents, rep.size))

    rep.rotate_face_cw('F')
    face_F = rep.get_face('F')
    face_U = rep.get_face('U')
    assert check_equal(face_F, face_F_1, 'invalid F face')
    assert check_equal(face_U, face_U_0, 'U face should not have changed')
    assert check(lambda: validate_cube_lite(rep.face_contents, rep.size))

    rep.rotate_face_cw('F')
    face_F = rep.get_face('F')
    face_U = rep.get_face('U')
    assert check_equal(face_F, face_F_2, 'invalid F face')
    assert check_equal(face_U, face_U_0, 'U face should not have changed')
    assert check(lambda: validate_cube_lite(rep.face_contents, rep.size))

    rep.rotate_face_cw('F')
    face_F = rep.get_face('F')
    face_U = rep.get_face('U')
    assert check_equal(face_F, face_F_3, 'invalid F face')
    assert check_equal(face_U, face_U_0, 'U face should not have changed')
    assert check(lambda: validate_cube_lite(rep.face_contents, rep.size))

    rep.rotate_face_cw('F')
    face_F = rep.get_face('F')
    face_U = rep.get_face('U')
    assert check_equal(face_F, face_F_0, 'invalid F face')
    assert check_equal(face_U, face_U_0, 'U face should not have changed')
    assert check(lambda: validate_cube_lite(rep.face_contents, rep.size))

    rep.rotate_face_ccw('F')
    face_F = rep.get_face('F')
    face_U = rep.get_face('U')
    assert check_equal(face_F, face_F_3, 'invalid F face')
    assert check_equal(face_U, face_U_0, 'U face should not have changed')
    assert check(lambda: validate_cube_lite(rep.face_contents, rep.size))

    rep.rotate_face_ccw('F')
    rep.rotate_face_ccw('F')
    face_F = rep.get_face('F')
    face_U = rep.get_face('U')
    assert check_equal(face_F, face_F_1, 'invalid F face')
    assert check_equal(face_U, face_U_0, 'U face should not have changed')
    assert check(lambda: validate_cube_lite(rep.face_contents, rep.size))

    #
    # Size = 3
    #

    rep = RubiksRep(3)
    rep.test_faces()
    face_F_0 = [['s', 't', 'u'], ['v', 'w', 'x'], ['y', 'z', 'A']]
    face_F_1 = [['y', 'v', 's'], ['z', 'w', 't'], ['A', 'x', 'u']]
    face_F_2 = [['A', 'z', 'y'], ['x', 'w', 'v'], ['u', 't', 's']]
    face_F_3 = [['u', 'x', 'A'], ['t', 'w', 'z'], ['s', 'v', 'y']]

    face_F = rep.get_face('F')
    face_U_0 = rep.get_face('U')
    assert check_equal(face_F, face_F_0, 'invalid F face')
    assert check(lambda: validate_cube_lite(rep.face_contents, rep.size))

    rep.rotate_face_cw('F')
    face_F = rep.get_face('F')
    face_U = rep.get_face('U')
    assert check_equal(face_F, face_F_1, 'invalid F face')
    assert check_equal(face_U, face_U_0, 'U face should not have changed')
    assert check(lambda: validate_cube_lite(rep.face_contents, rep.size))

    rep.rotate_face_cw('F')
    face_F = rep.get_face('F')
    face_U = rep.get_face('U')
    assert check_equal(face_F, face_F_2, 'invalid F face')
    assert check_equal(face_U, face_U_0, 'U face should not have changed')
    assert check(lambda: validate_cube_lite(rep.face_contents, rep.size))

    rep.rotate_face_cw('F')
    face_F = rep.get_face('F')
    face_U = rep.get_face('U')
    assert check_equal(face_F, face_F_3, 'invalid F face')
    assert check_equal(face_U, face_U_0, 'U face should not have changed')
    assert check(lambda: validate_cube_lite(rep.face_contents, rep.size))

    rep.rotate_face_cw('F')
    face_F = rep.get_face('F')
    face_U = rep.get_face('U')
    assert check_equal(face_F, face_F_0, 'invalid F face')
    assert check_equal(face_U, face_U_0, 'U face should not have changed')
    assert check(lambda: validate_cube_lite(rep.face_contents, rep.size))

    rep.rotate_face_ccw('F')
    face_F = rep.get_face('F')
    face_U = rep.get_face('U')
    assert check_equal(face_F, face_F_3, 'invalid F face')
    assert check_equal(face_U, face_U_0, 'U face should not have changed')
    assert check(lambda: validate_cube_lite(rep.face_contents, rep.size))

    rep.rotate_face_ccw('F')
    rep.rotate_face_ccw('F')
    face_F = rep.get_face('F')
    face_U = rep.get_face('U')
    assert check_equal(face_F, face_F_1, 'invalid F face')
    assert check_equal(face_U, face_U_0, 'U face should not have changed')
    assert check(lambda: validate_cube_lite(rep.face_contents, rep.size))


def test_move_front():
    """
    Tests for correctness of Part A.6 using a 2x2x2 and
    3x3x3 cube representation.
    """
    #
    # Size = 2
    #

    rep = RubiksRep(2)
    rep.test_faces()
    face_F_r0 = [['i', 'j'], ['k', 'l']]
    face_U_r0 = [['a', 'b'], ['c', 'd']]
    face_D_r0 = [['e', 'f'], ['g', 'h']]
    face_L_r0 = [['q', 'r'], ['s', 't']]
    face_R_r0 = [['u', 'v'], ['w', 'x']]
    face_B_r0 = [['m', 'n'], ['o', 'p']]

    face_F_r1 = [['k', 'i'], ['l', 'j']]
    face_U_r1 = [['a', 'b'], ['t', 'r']]
    face_D_r1 = [['w', 'u'], ['g', 'h']]
    face_L_r1 = [['q', 'e'], ['s', 'f']]
    face_R_r1 = [['c', 'v'], ['d', 'x']]

    face_F_0 = rep.get_face('F')
    face_U_0 = rep.get_face('U')
    face_D_0 = rep.get_face('D')
    face_L_0 = rep.get_face('L')
    face_R_0 = rep.get_face('R')
    face_B_0 = rep.get_face('B')
    assert check_equal(face_F_r0, face_F_0, 'invalid F face')
    assert check_equal(face_U_r0, face_U_0, 'invalid U face')
    assert check_equal(face_D_r0, face_D_0, 'invalid D face')
    assert check_equal(face_L_r0, face_L_0, 'invalid L face')
    assert check_equal(face_R_r0, face_R_0, 'invalid R face')
    assert check_equal(face_B_r0, face_B_0, 'invalid B face')
    assert check(lambda: validate_cube_lite(rep.face_contents, rep.size))

    rep.move_front()
    face_F_1 = rep.get_face('F')
    face_U_1 = rep.get_face('U')
    face_D_1 = rep.get_face('D')
    face_L_1 = rep.get_face('L')
    face_R_1 = rep.get_face('R')
    face_B_1 = rep.get_face('B')
    assert check_equal(face_F_r1, face_F_1, 'invalid F face')
    assert check_equal(face_U_r1, face_U_1, 'invalid U face')
    assert check_equal(face_D_r1, face_D_1, 'invalid D face')
    assert check_equal(face_L_r1, face_L_1, 'invalid L face')
    assert check_equal(face_R_r1, face_R_1, 'invalid R face')
    assert check_equal(face_B_r0, face_B_1, 'invalid B face')
    assert check(lambda: validate_cube_lite(rep.face_contents, rep.size))

    #
    # Size = 3
    #

    rep = RubiksRep(3)
    rep.test_faces()
    face_F_r0 = [['s', 't', 'u'], ['v', 'w', 'x'], ['y', 'z', 'A']]
    face_U_r0 = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
    face_D_r0 = [['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r']]
    face_L_r0 = [['K', 'L', 'M'], ['N', 'O', 'P'], ['Q', 'R', 'S']]
    face_R_r0 = [['T', 'U', 'V'], ['W', 'X', 'Y'], ['Z', '@', '#']]
    face_B_r0 = [['B', 'C', 'D'], ['E', 'F', 'G'], ['H', 'I', 'J']]

    face_F_r1 = [['y', 'v', 's'], ['z', 'w', 't'], ['A', 'x', 'u']]
    face_U_r1 = [['a', 'b', 'c'], ['d', 'e', 'f'], ['S', 'P', 'M']]
    face_D_r1 = [['Z', 'W', 'T'], ['m', 'n', 'o'], ['p', 'q', 'r']]
    face_L_r1 = [['K', 'L', 'j'], ['N', 'O', 'k'], ['Q', 'R', 'l']]
    face_R_r1 = [['g', 'U', 'V'], ['h', 'X', 'Y'], ['i', '@', '#']]

    face_F_0 = rep.get_face('F')
    face_U_0 = rep.get_face('U')
    face_D_0 = rep.get_face('D')
    face_L_0 = rep.get_face('L')
    face_R_0 = rep.get_face('R')
    face_B_0 = rep.get_face('B')
    assert check_equal(face_F_r0, face_F_0, 'invalid F face')
    assert check_equal(face_U_r0, face_U_0, 'invalid U face')
    assert check_equal(face_D_r0, face_D_0, 'invalid D face')
    assert check_equal(face_L_r0, face_L_0, 'invalid L face')
    assert check_equal(face_R_r0, face_R_0, 'invalid R face')
    assert check_equal(face_B_r0, face_B_0, 'invalid B face')
    assert check(lambda: validate_cube_lite(rep.face_contents, rep.size))

    rep.move_front()
    face_F_1 = rep.get_face('F')
    face_U_1 = rep.get_face('U')
    face_D_1 = rep.get_face('D')
    face_L_1 = rep.get_face('L')
    face_R_1 = rep.get_face('R')
    face_B_1 = rep.get_face('B')
    assert check_equal(face_F_r1, face_F_1, 'invalid F face')
    assert check_equal(face_U_r1, face_U_1, 'invalid U face')
    assert check_equal(face_D_r1, face_D_1, 'invalid D face')
    assert check_equal(face_L_r1, face_L_1, 'invalid L face')
    assert check_equal(face_R_r1, face_R_1, 'invalid R face')
    assert check_equal(face_B_r0, face_B_1, 'invalid B face')
    assert check(lambda: validate_cube_lite(rep.face_contents, rep.size))


def test_rotate_cube_x():
    """
    Tests for correctness of Part A.7 using a 2x2x2 and
    3x3x3 cube representation.
    """
    #
    # Size = 2
    #

    rep = RubiksRep(2)
    rep.test_faces()
    face_U_r0 = [['a', 'b'], ['c', 'd']]
    face_D_r0 = [['e', 'f'], ['g', 'h']]
    face_F_r0 = [['i', 'j'], ['k', 'l']]
    face_B_r0 = [['m', 'n'], ['o', 'p']]
    face_L_r0 = [['q', 'r'], ['s', 't']]
    face_R_r0 = [['u', 'v'], ['w', 'x']]

    face_U_r1 = [['i', 'j'], ['k', 'l']]
    face_D_r1 = [['m', 'n'], ['o', 'p']]
    face_F_r1 = [['e', 'f'], ['g', 'h']]
    face_B_r1 = [['a', 'b'], ['c', 'd']]
    face_L_r1 = [['r', 't'], ['q', 's']]
    face_R_r1 = [['w', 'u'], ['x', 'v']]

    face_U_0 = rep.get_face('U')
    face_D_0 = rep.get_face('D')
    face_F_0 = rep.get_face('F')
    face_B_0 = rep.get_face('B')
    face_L_0 = rep.get_face('L')
    face_R_0 = rep.get_face('R')
    assert check_equal(face_U_r0, face_U_0, 'invalid U face')
    assert check_equal(face_D_r0, face_D_0, 'invalid D face')
    assert check_equal(face_F_r0, face_F_0, 'invalid F face')
    assert check_equal(face_B_r0, face_B_0, 'invalid B face')
    assert check_equal(face_L_r0, face_L_0, 'invalid L face')
    assert check_equal(face_R_r0, face_R_0, 'invalid R face')
    assert check(lambda: validate_cube_lite(rep.face_contents, rep.size))

    rep.rotate_cube_x()
    face_U_1 = rep.get_face('U')
    face_D_1 = rep.get_face('D')
    face_F_1 = rep.get_face('F')
    face_B_1 = rep.get_face('B')
    face_L_1 = rep.get_face('L')
    face_R_1 = rep.get_face('R')
    assert check_equal(face_U_r1, face_U_1, 'invalid U face')
    assert check_equal(face_D_r1, face_D_1, 'invalid D face')
    assert check_equal(face_F_r1, face_F_1, 'invalid F face')
    assert check_equal(face_B_r1, face_B_1, 'invalid B face')
    assert check_equal(face_L_r1, face_L_1, 'invalid L face')
    assert check_equal(face_R_r1, face_R_1, 'invalid R face')
    assert check(lambda: validate_cube_lite(rep.face_contents, rep.size))

    #
    # Size = 3
    #

    rep = RubiksRep(3)
    rep.test_faces()
    face_U_r0 = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
    face_D_r0 = [['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r']]
    face_F_r0 = [['s', 't', 'u'], ['v', 'w', 'x'], ['y', 'z', 'A']]
    face_B_r0 = [['B', 'C', 'D'], ['E', 'F', 'G'], ['H', 'I', 'J']]
    face_L_r0 = [['K', 'L', 'M'], ['N', 'O', 'P'], ['Q', 'R', 'S']]
    face_R_r0 = [['T', 'U', 'V'], ['W', 'X', 'Y'], ['Z', '@', '#']]

    face_U_r1 = [['s', 't', 'u'], ['v', 'w', 'x'], ['y', 'z', 'A']]
    face_D_r1 = [['B', 'C', 'D'], ['E', 'F', 'G'], ['H', 'I', 'J']]
    face_F_r1 = [['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r']]
    face_B_r1 = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
    face_L_r1 = [['M', 'P', 'S'], ['L', 'O', 'R'], ['K', 'N', 'Q']]
    face_R_r1 = [['Z', 'W', 'T'], ['@', 'X', 'U'], ['#', 'Y', 'V']]

    face_U_0 = rep.get_face('U')
    face_D_0 = rep.get_face('D')
    face_F_0 = rep.get_face('F')
    face_B_0 = rep.get_face('B')
    face_L_0 = rep.get_face('L')
    face_R_0 = rep.get_face('R')
    assert check_equal(face_U_r0, face_U_0, 'invalid U face')
    assert check_equal(face_D_r0, face_D_0, 'invalid D face')
    assert check_equal(face_F_r0, face_F_0, 'invalid F face')
    assert check_equal(face_B_r0, face_B_0, 'invalid B face')
    assert check_equal(face_L_r0, face_L_0, 'invalid L face')
    assert check_equal(face_R_r0, face_R_0, 'invalid R face')
    assert check(lambda: validate_cube_lite(rep.face_contents, rep.size))

    rep.rotate_cube_x()
    face_U_1 = rep.get_face('U')
    face_D_1 = rep.get_face('D')
    face_F_1 = rep.get_face('F')
    face_B_1 = rep.get_face('B')
    face_L_1 = rep.get_face('L')
    face_R_1 = rep.get_face('R')
    assert check_equal(face_U_r1, face_U_1, 'invalid U face')
    assert check_equal(face_D_r1, face_D_1, 'invalid D face')
    assert check_equal(face_F_r1, face_F_1, 'invalid F face')
    assert check_equal(face_B_r1, face_B_1, 'invalid B face')
    assert check_equal(face_L_r1, face_L_1, 'invalid L face')
    assert check_equal(face_R_r1, face_R_1, 'invalid R face')
    assert check(lambda: validate_cube_lite(rep.face_contents, rep.size))


def test_rotate_cube_y():
    """
    Tests for correctness of Part A.8 using a 2x2x2 and
    3x3x3 cube representation.
    """
    #
    # Size = 2
    #

    rep = RubiksRep(2)
    rep.test_faces()
    face_U_r0 = [['a', 'b'], ['c', 'd']]
    face_D_r0 = [['e', 'f'], ['g', 'h']]
    face_F_r0 = [['i', 'j'], ['k', 'l']]
    face_B_r0 = [['m', 'n'], ['o', 'p']]
    face_L_r0 = [['q', 'r'], ['s', 't']]
    face_R_r0 = [['u', 'v'], ['w', 'x']]

    face_U_r1 = [['c', 'a'], ['d', 'b']]
    face_D_r1 = [['f', 'h'], ['e', 'g']]
    face_F_r1 = [['u', 'v'], ['w', 'x']]
    face_B_r1 = [['t', 's'], ['r', 'q']]
    face_L_r1 = [['i', 'j'], ['k', 'l']]
    face_R_r1 = [['p', 'o'], ['n', 'm']]

    face_U_0 = rep.get_face('U')
    face_D_0 = rep.get_face('D')
    face_F_0 = rep.get_face('F')
    face_B_0 = rep.get_face('B')
    face_L_0 = rep.get_face('L')
    face_R_0 = rep.get_face('R')
    assert check_equal(face_U_r0, face_U_0, 'invalid U face')
    assert check_equal(face_D_r0, face_D_0, 'invalid D face')
    assert check_equal(face_F_r0, face_F_0, 'invalid F face')
    assert check_equal(face_B_r0, face_B_0, 'invalid B face')
    assert check_equal(face_L_r0, face_L_0, 'invalid L face')
    assert check_equal(face_R_r0, face_R_0, 'invalid R face')
    assert check(lambda: validate_cube_lite(rep.face_contents, rep.size))

    rep.rotate_cube_y()
    face_U_1 = rep.get_face('U')
    face_D_1 = rep.get_face('D')
    face_F_1 = rep.get_face('F')
    face_B_1 = rep.get_face('B')
    face_L_1 = rep.get_face('L')
    face_R_1 = rep.get_face('R')
    assert check_equal(face_U_r1, face_U_1, 'invalid U face')
    assert check_equal(face_D_r1, face_D_1, 'invalid D face')
    assert check_equal(face_F_r1, face_F_1, 'invalid F face')
    assert check_equal(face_B_r1, face_B_1, 'invalid B face')
    assert check_equal(face_L_r1, face_L_1, 'invalid L face')
    assert check_equal(face_R_r1, face_R_1, 'invalid R face')
    assert check(lambda: validate_cube_lite(rep.face_contents, rep.size))

    #
    # Size = 3
    #

    rep = RubiksRep(3)
    rep.test_faces()
    face_U_r0 = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
    face_D_r0 = [['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r']]
    face_F_r0 = [['s', 't', 'u'], ['v', 'w', 'x'], ['y', 'z', 'A']]
    face_B_r0 = [['B', 'C', 'D'], ['E', 'F', 'G'], ['H', 'I', 'J']]
    face_L_r0 = [['K', 'L', 'M'], ['N', 'O', 'P'], ['Q', 'R', 'S']]
    face_R_r0 = [['T', 'U', 'V'], ['W', 'X', 'Y'], ['Z', '@', '#']]

    face_U_r1 = [['g', 'd', 'a'], ['h', 'e', 'b'], ['i', 'f', 'c']]
    face_D_r1 = [['l', 'o', 'r'], ['k', 'n', 'q'], ['j', 'm', 'p']]
    face_F_r1 = [['T', 'U', 'V'], ['W', 'X', 'Y'], ['Z', '@', '#']]
    face_B_r1 = [['S', 'R', 'Q'], ['P', 'O', 'N'], ['M', 'L', 'K']]
    face_L_r1 = [['s', 't', 'u'], ['v', 'w', 'x'], ['y', 'z', 'A']]
    face_R_r1 = [['J', 'I', 'H'], ['G', 'F', 'E'], ['D', 'C', 'B']]

    face_U_0 = rep.get_face('U')
    face_D_0 = rep.get_face('D')
    face_F_0 = rep.get_face('F')
    face_B_0 = rep.get_face('B')
    face_L_0 = rep.get_face('L')
    face_R_0 = rep.get_face('R')
    assert check_equal(face_U_r0, face_U_0, 'invalid U face')
    assert check_equal(face_D_r0, face_D_0, 'invalid D face')
    assert check_equal(face_F_r0, face_F_0, 'invalid F face')
    assert check_equal(face_B_r0, face_B_0, 'invalid B face')
    assert check_equal(face_L_r0, face_L_0, 'invalid L face')
    assert check_equal(face_R_r0, face_R_0, 'invalid R face')
    assert check(lambda: validate_cube_lite(rep.face_contents, rep.size))

    rep.rotate_cube_y()
    face_U_1 = rep.get_face('U')
    face_D_1 = rep.get_face('D')
    face_F_1 = rep.get_face('F')
    face_B_1 = rep.get_face('B')
    face_L_1 = rep.get_face('L')
    face_R_1 = rep.get_face('R')
    assert check_equal(face_U_r1, face_U_1, 'invalid U face')
    assert check_equal(face_D_r1, face_D_1, 'invalid D face')
    assert check_equal(face_F_r1, face_F_1, 'invalid F face')
    assert check_equal(face_B_r1, face_B_1, 'invalid B face')
    assert check_equal(face_L_r1, face_L_1, 'invalid L face')
    assert check_equal(face_R_r1, face_R_1, 'invalid R face')
    assert check(lambda: validate_cube_lite(rep.face_contents, rep.size))


def test_rotate_cube_z():
    """
    Tests for correctness of Part A.9 using a 2x2x2 and
    3x3x3 cube representation.
    """
    #
    # Size = 2
    #

    rep = RubiksRep(2)
    rep.test_faces()
    face_U_r0 = [['a', 'b'], ['c', 'd']]
    face_D_r0 = [['e', 'f'], ['g', 'h']]
    face_F_r0 = [['i', 'j'], ['k', 'l']]
    face_B_r0 = [['m', 'n'], ['o', 'p']]
    face_L_r0 = [['q', 'r'], ['s', 't']]
    face_R_r0 = [['u', 'v'], ['w', 'x']]

    face_U_r1 = [['s', 'q'], ['t', 'r']]
    face_D_r1 = [['w', 'u'], ['x', 'v']]
    face_F_r1 = [['k', 'i'], ['l', 'j']]
    face_B_r1 = [['n', 'p'], ['m', 'o']]
    face_L_r1 = [['g', 'e'], ['h', 'f']]
    face_R_r1 = [['c', 'a'], ['d', 'b']]

    face_U_0 = rep.get_face('U')
    face_D_0 = rep.get_face('D')
    face_F_0 = rep.get_face('F')
    face_B_0 = rep.get_face('B')
    face_L_0 = rep.get_face('L')
    face_R_0 = rep.get_face('R')
    assert check_equal(face_U_r0, face_U_0, 'invalid U face')
    assert check_equal(face_D_r0, face_D_0, 'invalid D face')
    assert check_equal(face_F_r0, face_F_0, 'invalid F face')
    assert check_equal(face_B_r0, face_B_0, 'invalid B face')
    assert check_equal(face_L_r0, face_L_0, 'invalid L face')
    assert check_equal(face_R_r0, face_R_0, 'invalid R face')
    assert check(lambda: validate_cube_lite(rep.face_contents, rep.size))

    rep.rotate_cube_z()
    face_U_1 = rep.get_face('U')
    face_D_1 = rep.get_face('D')
    face_F_1 = rep.get_face('F')
    face_B_1 = rep.get_face('B')
    face_L_1 = rep.get_face('L')
    face_R_1 = rep.get_face('R')
    assert check_equal(face_U_r1, face_U_1, 'invalid U face')
    assert check_equal(face_D_r1, face_D_1, 'invalid D face')
    assert check_equal(face_F_r1, face_F_1, 'invalid F face')
    assert check_equal(face_B_r1, face_B_1, 'invalid B face')
    assert check_equal(face_L_r1, face_L_1, 'invalid L face')
    assert check_equal(face_R_r1, face_R_1, 'invalid R face')
    assert check(lambda: validate_cube_lite(rep.face_contents, rep.size))

    #
    # Size = 3
    #

    rep = RubiksRep(3)
    rep.test_faces()
    face_U_r0 = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
    face_D_r0 = [['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r']]
    face_F_r0 = [['s', 't', 'u'], ['v', 'w', 'x'], ['y', 'z', 'A']]
    face_B_r0 = [['B', 'C', 'D'], ['E', 'F', 'G'], ['H', 'I', 'J']]
    face_L_r0 = [['K', 'L', 'M'], ['N', 'O', 'P'], ['Q', 'R', 'S']]
    face_R_r0 = [['T', 'U', 'V'], ['W', 'X', 'Y'], ['Z', '@', '#']]

    face_U_r1 = [['Q', 'N', 'K'], ['R', 'O', 'L'], ['S', 'P', 'M']]
    face_D_r1 = [['Z', 'W', 'T'], ['@', 'X', 'U'], ['#', 'Y', 'V']]
    face_F_r1 = [['y', 'v', 's'], ['z', 'w', 't'], ['A', 'x', 'u']]
    face_B_r1 = [['D', 'G', 'J'], ['C', 'F', 'I'], ['B', 'E', 'H']]
    face_L_r1 = [['p', 'm', 'j'], ['q', 'n', 'k'], ['r', 'o', 'l']]
    face_R_r1 = [['g', 'd', 'a'], ['h', 'e', 'b'], ['i', 'f', 'c']]

    face_U_0 = rep.get_face('U')
    face_D_0 = rep.get_face('D')
    face_F_0 = rep.get_face('F')
    face_B_0 = rep.get_face('B')
    face_L_0 = rep.get_face('L')
    face_R_0 = rep.get_face('R')
    assert check_equal(face_U_r0, face_U_0, 'invalid U face')
    assert check_equal(face_D_r0, face_D_0, 'invalid D face')
    assert check_equal(face_F_r0, face_F_0, 'invalid F face')
    assert check_equal(face_B_r0, face_B_0, 'invalid B face')
    assert check_equal(face_L_r0, face_L_0, 'invalid L face')
    assert check_equal(face_R_r0, face_R_0, 'invalid R face')
    assert check(lambda: validate_cube_lite(rep.face_contents, rep.size))

    rep.rotate_cube_z()
    face_U_1 = rep.get_face('U')
    face_D_1 = rep.get_face('D')
    face_F_1 = rep.get_face('F')
    face_B_1 = rep.get_face('B')
    face_L_1 = rep.get_face('L')
    face_R_1 = rep.get_face('R')
    assert check_equal(face_U_r1, face_U_1, 'invalid U face')
    assert check_equal(face_D_r1, face_D_1, 'invalid D face')
    assert check_equal(face_F_r1, face_F_1, 'invalid F face')
    assert check_equal(face_B_r1, face_B_1, 'invalid B face')
    assert check_equal(face_L_r1, face_L_1, 'invalid L face')
    assert check_equal(face_R_r1, face_R_1, 'invalid R face')
    assert check(lambda: validate_cube_lite(rep.face_contents, rep.size))


# ----------------------------------------------------------------------
# Entry point.
# ----------------------------------------------------------------------

if __name__ == '__main__':
    reset_test_counts()

    tests = [
      test_init,
      test_get_row,
      test_get_col,
      test_set_row,
      test_set_col,
      test_get_face,
      test_rotate_face,
      test_move_front,
      test_rotate_cube_x,
      test_rotate_cube_y,
      test_rotate_cube_z,
    ]

    print()
    for test in tests:
        run_test(test)
    print()
    wrap_up()
