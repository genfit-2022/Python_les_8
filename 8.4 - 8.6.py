#   4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
#   который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
#   В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
#   уникальные для каждого типа оргтехники.

#   5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и
#   передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
#   а также других данных, можно использовать любую подходящую структуру (например, словарь).

#   6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
#   для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
#
#           Подсказка:      постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на
#                           уроках по ООП.

class Orgteh:

    def __init__(self, name, cena, kol, numb_lists, *args):
        self.name = name
        self.cena = cena
        self.kol = kol
        self.numb = numb_lists
        self.my_sf = []
        self.my_s = []
        self.my_un = {'Модель устройства': self.name, 'Цена за ед': self.cena, 'Количество': self.kol}

    def __str__(self):
        return f'{self.name} цена, руб. {self.cena} количество, компл. {self.kol}'

    def reception(self):

        try:
            un = input(f'Введите наименование ')
            un_c = int(input(f'Введите цену за ед, рублей - '))
            un_k = int(input(f'Введите количество, комплект - '))
            uni = {'Модель устройства': un, 'Цена за ед, рублей': un_c, 'Количество, комплектов': un_k}
            self.my_un.update(uni)
            self.my_s.append(self.my_un)
            print(f'Текущий список: \n {self.my_s}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_sf.append(self.my_s)
            print(f'Весь склад -\n {self.my_sf}')
            return f'Выход'
        else:
            return Orgteh.reception(self)
class Printer(Orgteh):
    def my_print(self):
        return f'to print smth {self.numb} times'

class Scanner(Orgteh):
    def my_scan(self):
        return f'to scan smth {self.numb} times'

class Copier(Orgteh):
    def my_copier(self):
        return f'to copier smth  {self.numb} times'


unit_1 = Printer('Conon', 900, 4, 10)
unit_2 = Scanner('HP', 990, 5, 10)
unit_3 = Copier('Xerox', 2400, 6, 15)

print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())

print(unit_1.my_print())
print(unit_2.my_scan())
print(unit_3.my_copier())