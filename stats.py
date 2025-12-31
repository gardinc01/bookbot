def sort_on(char_list):
    return char_list["num"]

def sorting(found_l):
    char_list = []

    for chara in found_l:
        count = found_l[chara]
        item = {"char": chara, "num": count}
        char_list.append(item)

    char_list.sort(key=sort_on, reverse=True)
    return char_list



def characters(file_contents):
    found_l = {}
    for word in file_contents.lower():
        if word not in found_l:
            found_l[word] =1
        else:
            found_l[word] += 1

    #sorting(found_l)
    return found_l
   
    
def get_num_words(file_contents):
    text = file_contents.split()
    num_words = len(text)
    return num_words
    #characters(file_contents)

