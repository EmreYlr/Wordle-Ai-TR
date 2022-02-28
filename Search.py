def correct_search(correct, correct_index):
    f = open("word.txt", "r")
    count = 0
    file = f.readlines()
    list_correct = []
    while 1:
        if correct == file[count][correct_index].upper():
            list_correct.append(file[count])
            if count == 4974:
                return list_correct
            count += 1
        else:
            if count == 4974:
                return list_correct
            count += 1


def wrong_search(wrong, wrong_index):
    f = open("word.txt", "r")
    count = 0
    file = f.readlines()
    list_wrong = []
    while 1:
        if wrong != file[count][wrong_index].upper():
            list_wrong.append(file[count])
            if count == 4974:
                return list_wrong
            count += 1
        else:
            if count == 4974:
                return list_wrong
            count += 1


def CBWI_search(cbwi, cbwi_index):
    f = open("word.txt", "r")
    count = 0
    file = f.readlines()
    list_cbwi = []
    while 1:
        if cbwi != file[count][cbwi_index].upper() and cbwi in file[count].upper():
            list_cbwi.append(file[count])
            if count == 4974:
                return list_cbwi
            count += 1
        else:
            if count == 4974:
                return list_cbwi
            count += 1
