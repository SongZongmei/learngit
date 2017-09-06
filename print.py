age = 20
name = 'Swaroop'

print('{0} was {1} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))


print('{0:.3f}'.format(1.0 / 3))
print('{0:_^11}'.format('helloworld'), end=' ')
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))

print('a', end='')
print('b', end='')
print()
print('What\'s your name?')
print('This i s the first line\nThis is the second line')
print(r'Newlines are indicated by \n This')

# P 39
i = 5
print(i)
i = i + 1
print(i)
s = '''This is a multi-line string.
This is the second line.'''
print(s)

k = 'This is a string. \
This continues the string.'
print(k)


length = 5
breadth = 2

area = length * breadth
print('Area is', area)
print('Perimeter is', 2 * (length + breadth))
