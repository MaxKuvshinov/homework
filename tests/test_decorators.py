from typing import Any

import pytest
from src.decorators import log


def test_log_console(capsys: Any) -> None:  # Тест при успешном вызове в консоль
    @log()
    def add(x: int, y: int) -> int:
        return x + y

    result = add(1, 2)

    captured = capsys.readouterr()

    assert result == 3
    assert captured.out == "add ok: 3\n"


def test_log_error_console(capsys: Any) -> None:  # Тест при вызове ошибки в консоль
    @log()
    def divide(x: int, y: int) -> float:
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
    captured = capsys.readouterr()

    assert "divide error: ZeroDivisionError. Inputs: (1, 0), {}\n" in captured.out


def test_log_file() -> None:  # Тест при успешном вызове функции в файл
    log_file = "mylog.txt"

    @log(filename=log_file)
    def add(x: int, y: int) -> int:
        return x + y

    result = add(1, 2)

    with open(log_file) as file:
        log_content = file.read()

    assert result == 3
    assert log_content == "add ok: 3\n"


def test_log_error_file() -> None:  # Тест при вызове ошибки в файл
    log_file = "mylog.txt"

    @log(filename=log_file)
    def divide(x: int, y: int) -> float:
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide(5, 0)

    with open(log_file) as file:
        log_content = file.read()

    assert "divide error: ZeroDivisionError. Inputs: (5, 0), {}\n" in log_content
