import functools
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор для логирования вызовов функций и ее результатов"""

    def decorator(func: Callable) -> Callable:
        """Декоратор, оборачивающий функцию `func` для логирования вызовов и результатов."""

        @functools.wraps(func)
        def wrapper(*args: tuple, **kwargs: dict) -> Any:
            """Обернутая функция, логирующая вызовы и результаты оригинальной функции."""
            try:
                result = func(*args, **kwargs)
                # Вызов оригинальной функции
                log_message = f"{func.__name__} ok: {result}\n"
                # Сообщение о результате вызова функции
                if filename:
                    with open(filename, "a") as file:
                        file.write(log_message)
                else:
                    print(log_message, end="")
                return result

            except Exception as e:
                log_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n"
                # Сообщение об ошибке
                if filename:
                    with open(filename, "a") as file:
                        file.write(log_message)
                else:
                    print(log_message, end="")
                raise

        return wrapper

    return decorator
