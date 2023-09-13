def create_an_empty_list():

    return []

def create_a_list():
    list= [12, 'Nic',4.5,8]
    return list

def add_element_to_end_of_list(list, element):
   list= [12, 'Nic',4.5]
   list.append(element)
   return list

def add_element_to_start_of_list(list, element):
    list= [12, 'Nic',4.5]
    list.insert(0,element)

    return list

def remove_element_from_end_of_list(list):
    list.pop()
    return list

def remove_element_from_start_of_list(list):
    del(list[0])
    return list

def retrieve_first_element_from_list(list):
    if list:
        return list[0]
    else:
        return None 

def retrieve_element_from_index(list, index):
    if 0 <= index < len(list):
        return list[index]
    else:
        return None

def retrieve_last_element_from_list(list):
    if list:
        return list[-1]
    else: 
        return None
