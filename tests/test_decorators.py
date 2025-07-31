from src.decorators import log


def test_log_console(capsys) -> None:

    # Проверка вызова декоратора без параметра
    @log()
    def my_function(x, y):
        return x + y

    result = my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"


def test_log_file() -> None:
    filename = "data/log.txt"

    # Проверка вызова декоратора без параметра
    @log(filename)
    def my_test_function(x, y):
        return x + y

    with open(filename, mode="r") as file:
        data = file.read()

    assert "my_test_func ok" in data
