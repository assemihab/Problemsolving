def BracketCombinations(num):

  if num <= 1:
    return 1
  
  res = 0
  for i in range(num):
    one=BracketCombinations(i)
    two=BracketCombinations(num-i-1)
    print(one,two)
    res+=  one* two

  # code goes here
  return res

# keep this function call here 
print(BracketCombinations(int(input())))