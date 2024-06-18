import itertools
def BracketCombinations(num):
  listofbracks=[1,2]

  # for i in range (num*2):
  #   print (listofbracks[i%2])
  combinations = list(itertools.product(listofbracks, repeat=num*2))
  # print(combinations)
  numofcombinations=0
  for i in  combinations:

    stack=[]
    try:
      for j in i:
        if j==1:
          stack.append(j)
        else:
          stack.pop()
    except:
      continue
    if not stack:
      numofcombinations=numofcombinations+1
    

  return numofcombinations

# keep this function call here 
print(BracketCombinations(input()))