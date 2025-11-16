from src.decorators.log import log
import pytest


# Тест успешного выполнения функции + лог в файл

def test_log_success(tmp_path):
    log_file = tmp_path / "log.txt"

    @log(filename=str(log_file))
    def add(a, b):
        return a + b

    # Функция должна вернуть корректный результат
    assert add(1, 2) == 3

    # Проверяем запись в файл
    content = log_file.read_text(encoding="utf-8")
    assert "add ok" in content



# Тест ошибки + лог в файл
def test_log_error(tmp_path):
    log_file = tmp_path / "log.txt"

    @log(filename=str(log_file))
    def div(a, b):
        return a / b

    # Функция должна поднять исключение
    with pytest.raises(ZeroDivisionError):
        div(1, 0)

    # Проверяем, что ошибка записалась
    content = log_file.read_text(encoding="utf-8")

    assert "div error:" in content
    assert "(1, 0)" in content  # входные аргументы


# Тест вывода в консоль, если filename=None

def test_log_console(capsys):
    @log()
    def hi():
        return "hello"

    hi()

    # Читаем вывод в консоль
    captured = capsys.readouterr()

    assert "hi ok" in captured.out
