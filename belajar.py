def menu():
    print('''\033[32m
    CODING by->BeeCY713
    +++++++++++++++++++++++++++++++++++++++++
    mau-tembak-gebetan?--->                +
    1-tembak?                            +
    2-tidak                            +
    ++++++++++++++++++++++++++++++++++
    ''')
    pilih= int(input('\033[33m->'))
    if pilih is 1:
        print('iLOVE-YOU!!!!')
        menu()
    if pilih is 2:
        print('PECUNDANG!!!!')
        kluar()


def kluar():
    print('''\033[33m
    ++++++++++++++++++++++
    yakin-keluar?
    1. ya
    2 tdk
    ++++++++++++++++++++++
    ''')
    pi= int(input('\033[32m->'))
    if pi is 1:
       print('\033[32mbye-bye•_• \n PECUNDANG!!!!!')
       exit()
    if pi is 2:
       menu()




print('\033[33m='*50)
print('''\033[96mTOOLS-TEMBAK-GEBETAN
CODING-by-TEBEcy''')
print('''
+++++++++++++++++++++++++++++++++++
PILIH-BROW-->
1-lanjut
2-tidak
+++++++++++++++++++++++++++++++++++
''')
pil= int(input('\033[33m->'))
if pil is 1:
    menu()
if pil is 2:
    kluar()
