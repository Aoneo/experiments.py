##########  Search  ##########

def search(query, field):
    place = 'Null'
    for i in range(len(field)):
        if field[i] == query:
            place = i
            break
    return place

# print( search(10, [1,2,34,10,5,67,8,9,10,24,67,3,3]) )
