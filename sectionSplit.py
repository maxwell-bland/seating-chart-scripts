import sys
with open(sys.argv[1]) as xls:
  current = xls.readline().rstrip()
  while current != "":
    print current
    current = xls.readline().rstrip()
  print current
  print xls.readline()[:-1]
  currentStu = xls.readline().rstrip()
  count = 1
  while currentStu:
    if count % 2 == 0:
      print '\t'.join([sys.argv[2]] + currentStu.split()[1:])
    else:
      print currentStu
    count += 1
    count %= 2
    currentStu = xls.readline().rstrip()
