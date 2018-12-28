# 3. Сформировать из введенного числа обратное
# по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.


def reverce(to_revert, reverted):
    if to_revert < 10:
        return reverted
    return reverce(to_revert // 10, reverted * 10+to_revert % 10)


number = int(input('введите натуральное число: '))
print(reverce(number))
