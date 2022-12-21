def show_all_contacts ():
    show = []
    with open ('boook.csv', 'r') as file:
        while True:
            text = file.readline ()
            show.append (text)
            if not text:
                break
    show.pop()
    if len(show) == 0:
        print ('no results found')
    else:
        for i in show:
            contact = i.split(';')
            for_zip = ['Name:', 'Surname:', 'Telephone number:', 'Job title:']
            view = list(zip (for_zip, contact))
            view = [list(i) for i in view]
            result = ''
            for i in range (len(view)):
                for g in view[i]:
                    result = result + ' ' + g
                if i != len(view) - 1:
                    result = result + ";"
            print (result)
    return show

def search_contact ():
    print ('please enter name, surname, telephone number, job title or part of them to start searching: ')
    search = input ()
    search = search.casefold()
    show = []
    with open ('boook.csv', 'r') as file:
        while True:
            text = file.readline ()
            temp = text.casefold()
            if not text:
                break
            if temp.find (search) != -1:
                show.append (text)
            else: continue
    return show

def view_search_res (show):
    if len(show) == 0:
        answer ='no results found'
    else:
        count = 1
        for i in show:
            contact = i.split(';')
            for_zip = ['Name:', 'Surname:', 'Telephone number:', 'Job title:']
            view = list(zip (for_zip, contact))
            view = [list(i) for i in view]
            result = ''
            for i in range (len(view)):
                for g in view[i]:
                    result = result + ' ' + g
                if i != len(view) - 1:
                    result = result + ";"
            print (f'{count}: {result}')
            count += 1
        answer = 'search completed'
    print(answer)
    return show

def delete_employee():
    show = search_contact()
    view_search_res (show)
    if len(show) < 1:
        print ('')
        return (show)
    elif len (show) > 1:
        print ('')
        print ('choose employee to delete')
        choice = int(input('enter the number from the list: '))
        to_delete = show [choice -1]
    elif len (show) == 1:
        to_delete = show [0]
    with open ('book.txt', 'r') as file1, open ('boook.csv', 'r') as file2:
        file_content1 = file1.readlines()
        file_content2 = file2.readlines()
        print (f'deleting {to_delete}')
        file_content2.pop (file_content2.index(to_delete))
        to_delete = to_delete.replace (';', ' ')
        file_content1.pop (file_content1.index(to_delete))
    with open ('boook.csv', 'w') as file2, open ('book.txt', 'w') as file1:
        file2.writelines(file_content2)
        file1.writelines(file_content1)
        print ('employee successfully removed from the list')

                





        