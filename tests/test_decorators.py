from src.decorators import log


def test_log(capsys):

    # Проверка вызова декоратора без параметра
    @log()
    def my_function(x, y):
        return x + y

    result = my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"
