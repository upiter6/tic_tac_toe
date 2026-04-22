from inspect import getsource, isfunction, ismethod
from gameparts import Board

game = Board()

print('='*20, 'Способ 1', '='*20)
print(type(game)) # выводим тип game с помощью метода type 
# Делаем проверку
print(type(game) == Board)
print(type(game) is Board)
print(type(game) == str)

print(isinstance(game, Board))
print(isinstance(game, str))

print('='*20, 'Способ 2', '='*20)
print(game.__class__)

print('='*20, 'Способ 3', '='*20)
print('__str__' in dir(game)) # тут проверяем есть ли метод __str__ в game
print(dir(game)) # а тут он нам выводит все методы и атрибуты которые есть у game

print('='*20, 'Способ 4', '='*20)
print(hasattr(game, '__str__'))

print('='*20, 'Способ 5', '='*20)
print(game.__class__.__dict__) 

print('='*20, 'Способ 6', '='*20)
print(getsource(Board)) # Показывает все что написано в Board 

print('='*20, 'Способ 7', '='*20)
print(isfunction(game.display))
print(ismethod(game.display))
