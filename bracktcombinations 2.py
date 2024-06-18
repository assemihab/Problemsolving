# import itertools
# numofcombinations=0
def getcombsrec(newlist, oldlist):
    if not oldlist and not newlist:
        return 1
    
    count = 0
    
    if 1 in oldlist:
        new_oldlist = oldlist.copy()
        new_newlist = newlist.copy()
        new_oldlist.remove(1)
        new_newlist.append(1)
        print("1", new_oldlist, new_newlist)
        count += getcombsrec(new_newlist, new_oldlist)
    
    if 2 in oldlist and newlist:
        new_oldlist = oldlist.copy()
        new_newlist = newlist.copy()
        new_oldlist.remove(2)
        new_newlist.remove(1)
        print("2", new_newlist, new_oldlist)
        count += getcombsrec(new_newlist, new_oldlist)
    
    return count


    
def BracketCombinations(num):
  listofbracks=[]
  for i in range (num):
    listofbracks.append(1)
    listofbracks.append(2)
  newlist=[]
  # numofcombinations=0
  print('test')
  # global numofcombinations
  # numofcombinations=0
  numofcombinations=getcombsrec(newlist,listofbracks)
  print(numofcombinations)

  return numofcombinations

# keep this function call here 
print(BracketCombinations(int(input())))