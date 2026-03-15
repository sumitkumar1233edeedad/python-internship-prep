word = ['naman', 'tat', 'hello', 'livil', 'pumup']

result = []
name = ''
for words in word:
    for w in words:
        name = w+name
    result.append(True if name == words else False)
    name = ''

print(result)
 