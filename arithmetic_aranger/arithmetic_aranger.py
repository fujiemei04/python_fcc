def arithmetic_arranger(problems,default = False):
  blocks = list()
  arranged_problems = ""
  error =0
  if len(problems) > 5:
    arranged_problems="Error: Too many problems."
    return arranged_problems
  for i in problems:
    blocks.append(i.split())
  error = 0
  for i in blocks:
    operations = i
    if operations[1] != '+' and operations[1] != '-':
      arranged_problems = "Error: Operator must be '+' or '-'."
      error = 1
      break
    elif len(operations[0]) > 4 or len(operations[2]) > 4:
      arranged_problems ="Error: Numbers cannot be more than four digits."
      error = 1
      break  
    elif not operations[0].isdigit() or not operations[2].isdigit():
      arranged_problems = "Error: Numbers must only contain digits."
      error = 1
      break
  if (error == 1):
    return arranged_problems

  count = 0
  step = 0
  space = "    "
  for x in range(3):  
    if (count == 1):
      arranged_problems= arranged_problems+"\n"
    count = 1 
    step+=1
    if (step ==3):
      count = 0
    if (step == 1):
      max = 0
      end = 1
      for i in blocks:
        if len(i[0]) > len(i[2]):
          for k in range(2):
            arranged_problems = arranged_problems+" "
          arranged_problems = arranged_problems+i[0]
          if (end != len(blocks)):
            arranged_problems=arranged_problems+space
        else:
          max = 2+len(i[2])-len(i[0])
          for j in range(max):
            arranged_problems = arranged_problems+" "
          arranged_problems = arranged_problems+i[0] 
          if (end != len(blocks)):
            arranged_problems=arranged_problems+space
        end+=1
    if (step == 2):
      end = 1
      for i in blocks:
        arranged_problems=arranged_problems+i[1]
        if len(i[0]) > len(i[2]):
          for k in range(1+len(i[0])-len(i[2])):
            arranged_problems = arranged_problems+" "
          arranged_problems = arranged_problems+i[2]
          if (end != len(blocks)):
            arranged_problems=arranged_problems+space
        else:
          arranged_problems = arranged_problems+" "
          arranged_problems = arranged_problems+i[2]
          if (end != len(blocks)):
            arranged_problems=arranged_problems+space
        end+=1  
    if (step == 3):
      end=1
      for i in blocks:
        max = 0
        if len(i[0]) > len(i[2]):
          max = len(i[0])
        else:
          max = len(i[2])
        for j in range(max+2):
          arranged_problems=arranged_problems+"-"
        if (end != len(blocks)):
          arranged_problems=arranged_problems+space
        end+=1 
  if default == True:
    arranged_problems = arranged_problems+"\n"
    end = 1
    for i in blocks:
      result = ""
      if (i[1] == "+"):
        result = str(int(i[0])+int(i[2]))
      else:
        result = str(int(i[0])-int(i[2]))
      max=0
      if len(i[0]) > len(i[2]):
        max = len(i[0])+2
      else:
        max = len(i[2])+2
      for x in range(max-len(result)):
        arranged_problems= arranged_problems+" "
      arranged_problems= arranged_problems+result
      if (end != len(blocks)):
        arranged_problems=arranged_problems+space
      end+=1 
  return arranged_problems