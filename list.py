# 1. простой список
names = ['Sergey', 'oleg', 'andrey']
print(names[0].title())
print(names[1].title())
# индекс -1 позволяет обратиться к последнему элементу списка
print(names[-1].title())

# 2. использование шаблона для вывода сообщения
message = f'My friend is {names[0]}'
print(message)
message = f'My friend is {names[-2].title()}'
print(message)
message = f'My friend is {names[2].upper()}'
print(message)

bicycles = ['honDa', 'suZuki', 'yAmaha']
message = f"I would like to bye a {bicycles[0].capitalize()}"
print(message)
message = f"I would like to bye a {bicycles[1].capitalize()}"
print(message)
message = f"I would like to bye a {bicycles[2].capitalize()}"
print(message)
