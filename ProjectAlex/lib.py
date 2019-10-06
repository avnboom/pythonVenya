# чтение массива из файла 
def read_array_from_file(filename):
    data = []
    f = open(filename, "r")
    for line in f:
        data += line.split(' ')
    f.close()    
    return data

# запись массива в файл
def write_array_to_file(filename, array):
    f = open(filename, "w")
    new_str = ' '.join([str(n) for n in array])
    f.write(new_str)
    f.close() 