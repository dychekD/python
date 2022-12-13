def get_data ():
    print ('Please enter contact details to create a new contact.'
        ' If you want to left some field blank, please enter "-" or "no info" ')
    name = input('please enter name: ')
    surname = input('please enter surname: ')
    telephone = input('please enter telephone number: ')
    comment = input('please enter comment: ')
    contact = [name, surname, telephone, comment]
    return contact

def log_contact (contact):
    with open ('book.txt', 'a') as file1:
        file1.writelines('\n'+' '.join(contact))
    with open ('boook.csv', 'a') as file2:
        file2.writelines('\n'+';'.join(contact))


