"""Tests for assignment 3, section A."""


from lab3a import *


def test_list_reverse():
    assert list_reverse([21, 33, 42, 67, 99]) == [99, 67, 42, 33, 21]
    assert list_reverse([]) == []
    assert list_reverse([1]) == [1]


def test_list_reverse2():
    assert list_reverse2([21, 33, 42, 67, 99]) == [99, 67, 42, 33, 21]
    assert list_reverse2([]) == []
    assert list_reverse2([1]) == [1]


def test_file_info():
    assert file_info('rooter.txt') == (238, 2371, 15381) 
    assert file_info('hamlet.txt') == (7996, 32006, 197341)


def test_file_info2():
    assert file_info2('rooter.txt') == \
        {'line_count': 238, 'word_count': 2371, 'character_count': 15381}
    assert file_info2('hamlet.txt') == \
        {'line_count': 7996, 'word_count': 32006, 'character_count': 197341}


def test_longest_line():
    ll1 = ('\tIntroduces a user to the program and prompts them for two numbers,\n')
    ll2 = '    /Enter KING CLAUDIUS, QUEEN GERTRUDE, ROSENCRANTZ, and GUILDENSTERN/ \n' 
    ll3 = 'Along these same lines, to accomplish this mission, we concentrate our efforts on showing that the famous ubiquitous algorithm for the exploration of robots by Sato et al. runs in H((n log n)) time [22]. In the end, we conclude.\n'
    assert longest_line('math_fns.py') == (68, ll1)
    assert longest_line('hamlet.txt') == (74, ll2)
    assert longest_line('rooter.txt') == (229, ll3)


def test_count_fns():
    '''
    Note: This test function will create 2 tempoary files to test against some
    edge cases.
    '''
    assert count_fns('math_fns.py') == 3
    assert count_fns('test_lab3a.py') == 8
    assert count_fns('rooter.txt') == 0
    print('Creating empty text file to test count_fns...')
    with open('empty.txt', 'w') as f:
        f.write('\n')
    assert count_fns('empty.txt') == 0
    print('Creating single-line py file with \'def\' no trailing space...') 
    with open('silly_defs_no_trailing_space.py', 'w') as f:
        f.write('defdef\n')
    assert count_fns('silly_defs_no_trailing_space.py') == 0
    

def test_tabs_to_spaces(capsys):
    '''
    Note: This test function will create tempoary files to test against some
    edge cases.
    '''
    output_template = 'Lines with tabs: {}\nTabs replaced: {}\n'
    tabs_to_spaces('math_fns.py', 2)
    captured = capsys.readouterr()
    lines_changed = 29
    tab_count = 31
    assert captured.out == output_template.format(lines_changed, tab_count)
    math_fn_wc = file_info('math_fns.py')
    spaced2_wc = file_info('spaced_math_fns.py')
    # Line count should be unchanged
    assert math_fn_wc[0] == spaced2_wc[0]
    # Word count should be unchanged 
    assert math_fn_wc[1] == spaced2_wc[1]
    # Spaced file should have 2 * tab_count (orig count + orig tabs)
    assert math_fn_wc[2] + tab_count == spaced2_wc[2]
    tabs_to_spaces('math_fns.py', 4)
    captured = capsys.readouterr()
    assert captured.out == output_template.format(29, 31)
    spaced4_wc = file_info('spaced_math_fns.py')
    # Line count should be unchanged
    assert math_fn_wc[0] == spaced4_wc[0]
    # Word count should be unchanged 
    assert math_fn_wc[1] == spaced4_wc[1]
    # Spaced file should have 4 * tab_count (orig count + orig tabs * 3)
    assert math_fn_wc[2] + tab_count * 3 == spaced4_wc[2]
    with open('tab1_test.txt', 'w') as f:
        f.write('\t\n')
    f.close()
    tabs_to_spaces('tab1_test.txt', 20)
    captured = capsys.readouterr()
    lines_changed = 1
    tab_count = 1
    assert captured.out == output_template.format(1, 1)
    spaced20_wc = file_info('spaced_tab1_test.txt')
    assert spaced20_wc[0] == 1
    assert spaced20_wc[1] == 0
    # 21 = 20 \t + 1 \n
    assert spaced20_wc[2] == 21
    # Removes all tabs (0 spaces), has some inner and trailing \t
    with open('tab0_test.txt', 'w') as f:
        f.write('\tLorem ipsum:\tA good boi...\nLanguage:\tWoof.\t\n')
    f.close()
    tabs_to_spaces('tab0_test.txt', 0)
    captured = capsys.readouterr()
    lines_changed = 2
    tab_count = 4
    assert captured.out == output_template.format(lines_changed, tab_count)
    test_wc = file_info('spaced_tab0_test.txt')
    assert test_wc[0] == 2
    assert test_wc[1] == 5 
    assert test_wc[2] == 41


def test_binary_to_decimal():
    assert binary_to_decimal([0]) == 0
    assert binary_to_decimal([1]) == 1
    assert binary_to_decimal([0, 0]) == 0
    assert binary_to_decimal([0, 1]) == 1
    assert binary_to_decimal([1, 0]) == 2
    assert binary_to_decimal([1, 1]) == 3
    assert binary_to_decimal([0, 1, 1]) == 3
    assert binary_to_decimal([0, 0, 1, 1]) == 3
    assert binary_to_decimal([0, 0, 0]) == 0
    assert binary_to_decimal([0, 0, 1]) == 1
    assert binary_to_decimal([0, 1, 0]) == 2
    assert binary_to_decimal([0, 1, 1]) == 3
    assert binary_to_decimal([1, 0, 0]) == 4
    assert binary_to_decimal([1, 0, 1]) == 5
    assert binary_to_decimal([1, 1, 0]) == 6
    assert binary_to_decimal([1, 1, 1]) == 7
    assert binary_to_decimal([0, 1, 1, 1]) == 7
    assert binary_to_decimal([0, 0, 1, 1, 1]) == 7
    assert binary_to_decimal([0, 0, 0, 1, 1, 1]) == 7
    assert binary_to_decimal([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 1024
