#Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.

def count_vowels(phrase):
    vowels = "aeiouy"
    return sum([1 for letter in phrase if letter in vowels])

poem = input("Введите стих: ").split()
vowels_count = count_vowels(poem[0])

for phrase in poem[1:]:
    if count_vowels(phrase) != vowels_count:
        print("Пам парам")
        break
else:
    print("Вывод: " + "Парам пам-пам")