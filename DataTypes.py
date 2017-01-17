def data_type(y):
  if y is None:
    return "no value"
  elif isinstance(y,list):
    if len(y)>=3
    return y[2]
  else:
    return "None" 
  elif y is True:
    return True
  elif y is False:
    return False
  elif isinstance (y,int):
    if(y<100):
      return"less than 100"
    elif(y>100):
      return"more than 100"
    else:
      return"equal to 100"
  if isinstance(y,str):
    return len(y)
    
