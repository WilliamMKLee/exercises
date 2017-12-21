import hello
import mock
from hello import sayHello, stdSayHello

#from pytest import monkeypatch


def test_say_hello_with_input():
    # Override the Python built-in input method
    hello.input = lambda x: 'Python'
    output = hello.sayHello()
    assert 'Hello Python, nice to meet you!' == output


def test_say_hello_without_input():
    # Override the Python built-in input method
    hello.input = lambda x: ''
    output = hello.sayHello()
    assert 'Hello World' == output


def test_say_hello_with_input_with_mock():
    with mock.patch.object(hello, 'input', lambda x: 'Python'):
        output = sayHello()
    assert 'Hello Python, nice to meet you!' == output


def test_say_hello_without_input_with_mock():
    with mock.patch.object(hello, 'input', lambda x: ''):
        output = sayHello()
    assert 'Hello World' == output


def test_stdout_with_input(capsys):
    with mock.patch.object(hello, 'input', lambda x: 'Python'):
        stdSayHello()
    out, _ = capsys.readouterr()
    assert 'Hello Python, nice to meet you!\n' == out


def test_stdout_without_input(capsys):
    with mock.patch.object(hello, 'input', lambda x: ''):
        stdSayHello()
    out, _ = capsys.readouterr()
    assert 'Hello World\n' == out