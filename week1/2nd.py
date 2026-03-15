word = 'hello how are you brother. I am ur friends'
result = 0
vowels = ['a', 'e', 'i', 'o', 'u']
for i in word.lower():
    if i in vowels:
        result += 1
print(result)