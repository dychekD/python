def search_contact ():
    print ('please enter name, surname, telephone number, comment or part of them to start searching: ')
    search = input ()
    search = search.casefold()
    show = []
    with open ('book.txt', 'r') as file:
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
        for i in show:
            contact = i.split()
            for_zip = ['Name:', 'Surname:', 'Telephone number:', 'Comment:']
            view = list(zip (for_zip, contact))
            view = [list(i) for i in view]
            result = ''
            for i in range (len(view)):
                for g in view[i]:
                    result = result + ' ' + g
                if i != len(view) - 1:
                    result = result + ";"
            print (result)
        answer = 'search completed'
    print(answer)
    return show

        