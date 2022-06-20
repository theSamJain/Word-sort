import os

# use type = 'n' to append words in a new file, otherwise use type = 's'
 
def word_sort(path, word_length, type = 's', new_path = None):

    if (type != 's'):
        if(new_path == None):
            raise(NameError("\nWith new file comes a new path!\n"))
    words_I_need = []

    with open(path,'r') as file:    
        for line in file:      
            for word in line.split():
                if (len(word) == word_length+3): 
                    # +3 because words are in quotes followed by a comma
                    words_I_need.append(word + "\n")

    # same file
    if(type == 's'):
        open(path, 'r').truncate()
        with open(path, 'w') as oldfile:
            for new_words in words_I_need:
                oldfile.write(new_words)
    # new file
    else:
        with open(new_path, 'w') as newfile:
            for new_words in words_I_need:
                newfile.write(new_words)

# implementation
if __name__ == "__main__":
    path = r'C:\Users\jains\Desktop\words.txt'
    word_length = 7
    new_path = r'C:\Users\jains\Desktop\words_{:}.txt'.format(str(word_length))
    word_sort(path, word_length, type = 'n', new_path = new_path)