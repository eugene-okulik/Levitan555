text = (
    'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
    'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
)

words = text.split()

for word in words:
    if ',' in word:
        word = word.replace(',', 'ing,')
    if '.' in word:
        word = word.replace('.', 'ing.')
    elif ',' not in word:
        word = word + 'ing'

    print(word, end=' ')
