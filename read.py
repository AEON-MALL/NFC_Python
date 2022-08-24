import nfc

def reader():
    clf = nfc.ContactlessFrontend('usb')
    print("タッチしてください")

    tag = clf.connect(rdwr={'on-connect': lambda tag:False})

    card_info = tag.dump()

    print(card_info)

    student_number = card_info[4][61:68]

    print(student_number)
    return student_number