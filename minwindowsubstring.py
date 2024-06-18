def MinWindowSubstring(strArr):
  N,K=strArr
  windowsize=len(K)
  while True:

    for i in range (0,(len(N)-windowsize)+1):

      windowstring=N[i:i+windowsize]
      # print(windowstring)
      isTrue=True
      for char in set(list(K)):
        if (char not in windowstring or windowstring.count(char)<K.count(char)):
          isTrue=False
          break
      if (isTrue):
        # print(windowstring)
        return windowstring
    windowsize=windowsize+1

# keep this function call here 
print(MinWindowSubstring(input()))