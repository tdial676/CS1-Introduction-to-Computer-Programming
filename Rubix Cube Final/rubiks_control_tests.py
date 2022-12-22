"""
Provided testing program for Final Part C Rubik's cube
(rubiks_control.py) program.

Note that these are not pytest tests, and have a bit
more useful display/feedback for tests involving output
for the purposes of the Final Exam.

To run:
$ python3 rubiks_control_tests.py
"""
import copy
import traceback as tb
from rubiks_control import RubiksControl, InvalidCommand
from rubiks_cube import RubiksCube

NTESTS = 100

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


# ----------------------------------------------------------------------
# Tests.
# ----------------------------------------------------------------------

def test_exec_add_command():
    """
    Tests for correctness of Part C.1 using a 2x2x2 and
    3x3x3 cube representation.
    """
    for size in [2, 3]:
        control = RubiksControl(size)
        cmds = copy.deepcopy(control.user_commands)
        # 1 argument
        control.exec_add_command('foobar', ['baz'])
        cmds2 = control.user_commands
        assert len(cmds2) == len(cmds) + 1
        assert cmds2['foobar'] == 'baz'

    for size in [2, 3]:
        control = RubiksControl(size)
        cmds = copy.deepcopy(control.user_commands)
        # 3 arguments
        control.exec_add_command('xyzzy', ['foo', 'bar', 'baz'])
        cmds2 = control.user_commands
        assert len(cmds2) == len(cmds) + 1
        assert cmds2['xyzzy'] == 'foo bar baz'


def test_exec_command():
    """
    Tests for correctness of Part C.2 using a 2x2x2 and
    3x3x3 cube representation.
    """
    for size in [2, 3]:
        control = RubiksControl(size)
        cube = RubiksCube(size)

        # Use test data, as usual.
        control.cube.rep.test_faces()
        cube.rep.test_faces()

        control.exec_command('f')
        cube.move_face('F', '+')
        # Faces should be updated appropriately for F+ mvoe
        assert control.cube.rep.face_contents == cube.rep.face_contents

        control.exec_command("u'")
        cube.move_face('U', '-')
        # Faces should be updated appropriately for U- mvoe
        assert control.cube.rep.face_contents == cube.rep.face_contents

        control.exec_command('fur')  # == f u r u' r' f'
        cube.move_face('F', '+')
        cube.move_face('U', '+')
        cube.move_face('R', '+')
        cube.move_face('U', '-')
        cube.move_face('R', '-')
        cube.move_face('F', '-')
        assert control.cube.rep.face_contents == cube.rep.face_contents

        # Check that bogus moves raise an InvalidCommand exception.
        try:
            control.exec_command('foobarbazbam')
            print('TEST ERROR: an InvalidCommand exception should have been raised')
            assert False
        except InvalidCommand:
            pass
        except:
            print('TEST ERROR: an InvalidCommand exception should have been raised ', end='')
            print('       but a different exception was raised instead.')
            assert False


# ----------------------------------------------------------------------
# Entry point.
# ----------------------------------------------------------------------

if __name__ == '__main__':
    reset_test_counts()

    tests = [
      test_exec_add_command,
      test_exec_command,
    ]

    print()
    for test in tests:
        run_test(test)
    print()
    wrap_up()
