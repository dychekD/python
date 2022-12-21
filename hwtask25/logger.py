def get_data ():
    print ("Please enter employee's contact details to add them to the employee list."
        ' If you want to left some field blank, please enter "-" or "no info" ')
    name = input('please enter name: ')
    surname = input('please enter surname: ')
    telephone = input('please enter telephone number: ')
    job = input('please enter job title: ')
    contact = [name, surname, telephone, job]
    return contact

def log_contact (contact):
    with open ('book.txt', 'a') as file1:
        file1.writelines(' '.join(contact)+'\n')
    with open ('boook.csv', 'a') as file2:
        file2.writelines(';'.join(contact)+'\n')


