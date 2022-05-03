#   2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу
#   на данных, вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать
#   эту ситуацию и не завершиться с ошибкой.

class Null:
    def __init__(self, div, den):
        self.div = div
        self.den = den
    @staticmethod
    def div_null(div, den):
        try:
            return (div / den)
        except:
            return (f'Делить на ноль в области действительных чисел нельзя!')

div = Null(10, 100)
print(Null.div_null(10, 0))
print(Null.div_null(10, 0.1))
print(div.div_null(100, 0))