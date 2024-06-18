def TreeConstructor(strArr):
  dictt={}
  for i in strArr:
    try:
      dictt[i[3]]=dictt[i[3]]+1
    except:
      dictt[i[3]]=1
  
  for keys,values in dictt.items():
    # print(keys,values)
    if values >2:
      return 'false'
    
  # code goes here
  return 'true'

# keep this function call here 
print(TreeConstructor(input()))