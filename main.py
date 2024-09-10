# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

    # module3_4.py
  #"Произвольное число параметров"
  #Объявляем функцию single_root_words с параметрами root_word и *other_words.
def single_root_words(root_word, *other_words):
    same_words = []  #Создаёь внутри функции пустой список same_words
    root_word_lower = root_word.lower()
    for i in other_words:
        other_words_lower = i.lower()
        if root_word_lower in other_words_lower or other_words_lower in root_word_lower:
            same_words.append(i)
    return same_words

result1 = single_root_words('холод', 'холод', 'похолодало','холодильник','зимний','холодок')
result2 = single_root_words('стол', 'столовый', 'столешница', 'столик','столярный')
print(result1)
print(result2)