
filename = "4x4.txt"
txtfile = open(filename, 'r')

output = txtfile.readlines()


for x in output:
    outpt = ''
    lst = x.strip().split()
    flist = []
    for i in lst:
        outpt += i
        # print(outpt, 'Output')
        returned = int(outpt)
        flist.append(returned)

    print(returned)

print(flist)

# def fromfile(s):
#     txtfile = open(filename, 'r')


#     txtfile.close()
