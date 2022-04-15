# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
def alf_check(a:str,b:str) -> int:
    return f'{a} на месте {ord(a) - ord("a") + 1},{b} на месте {ord(b) - ord("a") +1}, между ними {(ord(b) - ord("a")) - (ord(a) - ord("a")) - 1}'

print(alf_check('a', 'c'))
print(alf_check('b', 'e'))
print(alf_check('v', 'z'))

