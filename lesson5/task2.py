#2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open("file_t2.txt", "r") as file:
    lines = file.readlines()
    for number_str, words_l in enumerate(lines,1):
        print(f"В строке {number_str}  всего {len(words_l.split())} слова")
    print(f"В нашем файле всего {len(lines)} строк")
