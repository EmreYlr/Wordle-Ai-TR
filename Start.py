from Search import *
import random
import Tutorial
wrong = []
wrong_index = []
cbwi = []  # Correct_But_Wrong_Index
cbwi_index = []
correct = []
correct_index = []
first_key = int(input(" Henüz herhangi bir kelime tahmin etmediyseniz, güzel bir ilk kelime için 1'e basın!\n Kendi "
                      "tahmininizi yazmak istiyorsanız 0'a basın!\n >>>"))
while 1:
    if first_key == 1:
        key = "ABIDE"  # First Key
        break
    elif first_key == 0:
        key = input(">")
        break
    else:
        print("Wrong Key")
        first_key = int(input(">>>"))

print("\n" * 10)
turn = 0
while turn < 6:
    i = 0
    print(key)
    prediction = input(">")
    if prediction.upper() == "GGGGG":
        print("Win")
        exit(0)
    while 1:
        if i == 5:
            break
        if prediction[i].upper() == "G":
            correct.append(key[i])
            correct_index.append(i)

        elif prediction[i].upper() == "Y":
            cbwi.append(key[i])
            cbwi_index.append(i)

        elif prediction[i].upper() == "B":
            wrong.append(key[i])
            wrong_index.append(i)
        else:
            print("Wrong Key")
            print(key)
            prediction = input(">")
            continue
        i += 1

    wrong_list_common = []
    for k in range(len(wrong)):
        wrong_list = wrong_search(wrong[k], wrong_index[k])
        if len(wrong_list_common):
            wrong_list_common = list(set(wrong_list_common).intersection(wrong_list))
        else:
            wrong_list_common = wrong_list

    correct_list_common = []
    for k in range(len(correct)):
        correct_list = correct_search(correct[k], correct_index[k])
        if len(correct_list_common):
            correct_list_common = list(set(correct_list_common).intersection(correct_list))
        else:
            correct_list_common = correct_list

    cbwi_list_common = []
    for k in range(len(cbwi)):
        cbwi_list = CBWI_search(cbwi[k], cbwi_index[k])
        if len(cbwi_list_common):
            cbwi_list_common = list(set(cbwi_list_common).intersection(cbwi_list))
        else:
            cbwi_list_common = cbwi_list
    common = []
    if not len(wrong_list_common):
        common = list(set(correct_list_common).intersection(cbwi_list_common))
    if not len(correct_list_common):
        common = list(set(cbwi_list_common).intersection(cbwi_list_common))
    if not len(cbwi_list_common):
        common = list(set(correct_list_common).intersection(wrong_list_common))
    if len(wrong_list_common) and len(cbwi_list_common) and len(correct_list_common):
        common = list(set(correct_list_common).intersection(wrong_list_common))
        common = list(set(common).intersection(cbwi_list_common))

    key = random.choice(common).upper()
    turn += 1
