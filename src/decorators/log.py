"""
Модуль с декоратором log для логирования вызова функций.
"""

from typing import Callable, Optional, Any, Tuple, Dict
import functools


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования результата работы функции.

    Args:
        filename (Optional[str]): Имя файла для записи логов.
            Если None — вывод в консоль.

    Returns:
        Callable: Обёрнутая функция.
    """

    def decorator(func: Callable) -> Callable:

        @functools.wraps(func)
        def wrapper(*args: Tuple[Any, ...], **kwargs: Dict[str, Any]) -> Any:
            try:
                result = func(*args, **kwargs)

                message = f"{func.__name__} ok"

                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(message + "\n")
                else:
                    print(message)

                return result

            except Exception as error:
                message = (
                    f"{func.__name__} error: {error}. "
                    f"Inputs: {args}, {kwargs}"
                )

                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(message + "\n")
                else:
                    print(message)

                raise

        return wrapper

    return decorator
