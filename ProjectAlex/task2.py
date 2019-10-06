#filename - не используется
def read_from_file(filename):
    f = open(".file.txt", 'r')
    text = f.read()
    f.close()
    return text

#filename - не используется
def write_to_file(filename, text):
    f = open(".file.txt", 'w') # скорее всего вместо 'w', надо 'w+'
    text = f.read() # не понятно зачем
    print(text)
    f.write(text)
    f.close()

#должна принимать текст, а возвращать количество слов в нем
def word_count(text):
    lines = 0
    words = 0
    letters = 0
    for line in а:
        lines += 1
        letters += len(line)

#должна принимать текст, а возвращать количество буквы 'а' и 'о' в нем
def liter_count(text):
    
    return count


text = read_from_file(".\data.txt")

w_count = word_count(text)
l_count = letter_count(text)

write_to_file(".\data1.txt", "words: " + str(w_count))
write_to_file(".\data1.txt", "letters: " + str(l_count))