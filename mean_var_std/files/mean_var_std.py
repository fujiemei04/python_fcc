import numpy as np

def calculate(list_input):

  if (len(list_input)) < 9:
    raise ValueError("List must contain nine numbers.")
  array = np.array(list_input)
  array = np.reshape(array,(3,3))
  calculations = dict()
  calculations["mean"] = list()
  calculations["variance"] = list()
  calculations["standard deviation"] = list()
  calculations["max"] = list()
  calculations["min"] = list()
  calculations["sum"] = list()
  for key in calculations:
    if key == "mean":
        for i in range(2):
            l = list(array.mean(axis=i))
            calculations[key].append(l)
        calculations[key].append(array.mean())
    elif key == "variance":
        for i in range(2):
            l = list(array.var(axis=i))
            calculations[key].append(l)
        calculations[key].append(array.var())
    elif key == "standard deviation":
        for i in range(2):
            l = list(array.std(axis=i))
            calculations[key].append(l)
        calculations[key].append(array.std())
    elif key == "max":
        for i in range(2):
            l = list(array.max(axis=i))
            calculations[key].append(l)
        calculations[key].append(array.max())  
    elif key == "min":
        for i in range(2):
            l = list(array.min(axis=i))
            calculations[key].append(l)
        calculations[key].append(array.min())
    elif key == "sum":
        for i in range(2):
            l = list(array.sum(axis=i))
            calculations[key].append(l)
        calculations[key].append(array.sum())
  

  return calculations