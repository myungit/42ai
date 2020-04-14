data = (3, 30, 19, 9, 25)
'''
printdate = []
for i in data:
    if i < 10:
        printdate.append(str(i).rjust(2, '0'))
    else:
        printdate.append(str(i))

printdate[2] = printdate[2].rjust(4, '0')

print("{0}/{1}/{2} {3}:{4}".format
      (printdate[3], printdate[4], printdate[2], printdate[0], printdate[1]))
'''
print("{:0>2}/{:0>2}/{:0>4} {:0>2}:{:0>2}".format
      (data[3], data[4], data[2], data[0], data[1]))
