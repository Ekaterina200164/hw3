array = ["1","2"]
f = open('text2.txt', 'w')
def write_array(array, f):
    array = map(lambda x: x + '\n', array)
    f.writelines(array)
    f.close()
pass
write_array(array, f)
