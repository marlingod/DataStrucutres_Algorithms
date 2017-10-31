def bubleSort(myList):
  for iterpass in range(len(myList) -1, 0, -1):
    for i in range(iterpass):
      if myList[i]>myList[i+1]:
        myList[i], myList[i+1] = myList[i+1],myList[i]
