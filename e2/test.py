import count_chars
import mock
from count_chars import countChars


def test_stdout_with_input(capsys):
    test_input = 'Hello Python'
    test_input_len = len(test_input)
    test_output = '{} has {} characters.\n'.format(test_input, test_input_len)
    with mock.patch.object(count_chars, 'input', lambda x: test_input):
        countChars()
    out, _ = capsys.readouterr()
    assert test_output == out
