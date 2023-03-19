def split_string(s):
    result = []
    current_word = ''
    d = input('slpit symbol > ')
    for char in s:
        if char != d:
            current_word += char
        else:
            result.append(current_word)
            current_word = ''

    result.append(current_word)

    return result

print(split_string('разделить-строку-без-split'))
#---------------------------------------------------------



def strip_string(s):
    d= input('strip symbol > ')
    string = s.replace(" ", "")
    result = s.split(d)
    return result

print(strip_string('разделить-строку-без-strip'))
#---------------------------------------------------------



def count_l(w):
    w = w.lower()
    l_count = {}
    for l in w:
        if l in l_count:
            l_count[l] += 1
        else:
            l_count[l] = 1
    for l, count in l_count.items():
        print(f"{l.upper()}-{count}")

w = input('Vvedite predlojenie > ')
count_l(w)
