import os.path

import pytest
from src.decorators import log


def test_log_decorator_console(capsys):
    @log()
    def my_function(x, y):
        return x / y

    my_function(4, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"


def test_log_decorator_console_err(capsys):
    @log()
    def my_function(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        my_function(2, 0)
    captured_err = capsys.readouterr()
    assert "my_function error: division by zero. Inputs:(2, 0), {}\n" in captured_err.out


def test_log_decorator():
    @log("test_log.txt")
    def my_function(x, y):
        return x / y

    my_function(4, 2)
    with open("test_log.txt") as log_file:
        log_content = log_file.read()
        assert "my_function ok\n" in log_content


def test_log_decorator_err():
    @log("test_log.txt")
    def my_function(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        my_function(2, 0)
    with open("test_log.txt", "r") as log_file:
        log_content = log_file.read()
        assert "my_function error: division by zero. Inputs:(2, 0), {}\n" in log_content


def test_delete_test_log():

    os.remove("test_log.txt")
