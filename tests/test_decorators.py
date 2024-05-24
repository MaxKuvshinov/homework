import pytest

from src.decorators import log


def test_log_console(capsys):  # Тест при успешном вызове в консоль
    @log()
    def add(x, y):
        return x + y

    result = add(1, 2)

    captured = capsys.readouterr()

    assert result == 3
    assert captured.out == "add ok: 3\n"


def test_log_error_console(capsys):  # Тест при вызове ошибки в консоль
    @log()
    def divide(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
    captured = capsys.readouterr()

    assert "divide error: ZeroDivisionError. Inputs: (1, 0), {}\n" in captured.out


# Тестируем логирование успешного вызова функции в файл
def test_log_file():
    log_file = "mylog.txt"

    @log(filename=log_file)
    def add(x, y):
        return x + y

    result = add(1, 2)

    with open(log_file) as file:
        log_content = file.read()

    assert result == 3
    assert log_content == "add ok: 3\n"


def test_log_error_file():
    log_file = "mylog.txt"

    @log(filename=log_file)
    def divide(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide(5, 0)

    with open(log_file) as file:
        log_content = file.read()

    assert "divide error: ZeroDivisionError. Inputs: (5, 0), {}\n" in log_content


