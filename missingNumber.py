def missingNumber(a, b):
  a = set(a)
  b = set(b)
  if a < b:
    c = list(b-a)
  elif a > b:
  	c = list(a - b)
  else:
  	return 0
  
  for items in c:
  	return items
print missingNumber((1,2,3,4,5), (1,2,3,4))
