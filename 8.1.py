#   1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
#   «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен
#   извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
#   должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной
#   структуры на реальных данных.

class Data:
    def __init__(sel, day_month_year):
        sel.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        date = []
        for i in day_month_year.split():
            if i != '-': date.append(i)
        return int(date[0]), int(date[1]), int(date[2])

    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 0:
                    return f'Данные даты введены верно!'
                else:
                    return f'Год задан неверно!'
            else:
                return f'Месяц в недопустимом диапазоне!'
        else:
            return f'Дата в недопустимом диапазоне!'

    def __str__(sel):
        return f'Текущая дата {Data.extract(sel.day_month_year)}'


today = Data('1 - 01 - 2020')
print(today)
print(Data.valid(11, 11, 2020))
print(Data.valid(11, 11, 2022))
print(today.valid(21, 13, 2006))
print(Data.extract('12 - 12 - 2012'))
print(today.extract('11 - 11 - 2011'))
print(Data.valid(1, 11, 2011))