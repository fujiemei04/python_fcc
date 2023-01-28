class Category:
  ledger = list()
  ledger2 = dict()
  sum = 0
  operations = 0
  withdraws = 0 
  def __init__(self,category):
    self.category = category
    self.ledger=list()
    self.ledger2=dict()

  def __str__(self):
    string = "*************"+self.category+"*************\n"
    for key,val in self.ledger2.items():
      keylen = 0
      if (len(key) >23):
        keylen = 23
        for j in range(23):
          string=string+key[j]
      else: 
        string = string+key
        keylen = len(key)
      number = str(format(val, '.2f'))
      spaces = 30-len(number)-keylen
      for j in range(spaces):string = string+" "
      string=string+number+"\n"
    string= string+"Total: "+str(self.sum)
    return string
    

  def check_funds(self,amount):
    if self.sum < amount: return False
    return True
    
  def deposit(self,amount,description=""):
    self.ledger.append({"amount": amount, "description": description})
    self.ledger2[description]=amount
    self.sum += amount
  
  def withdraw(self,amount,description=""):
    if not self.check_funds(amount): return False
    self.ledger.append({"amount": -amount, "description": description})
    self.sum = self.sum-amount
    self.ledger2[description]=-amount
    self.operations+=1
    self.withdraws+=1
    return True

  def get_balance(self):
    return self.sum

  def transfer(self,amount,Category):
    if not self.check_funds(amount): return False
    string = "Transfer to "+Category.category
    self.withdraw(amount,string)
    string1 = "Transfer from "+self.category
    Category.deposit(amount,string1)
    self.operations+=1
    return True
  
  

def create_spend_chart(categories):
  totalop = 0
  string=""
  names=list()
  for i in categories:
    print(i.operations)
    totalop+= i.operations
    names.append(i.category)
  perc = list()
  maxlen=0
  for i in categories:
    print(i.withdraws/totalop)
    perc.append(int((i.withdraws/totalop)*100))
    if (len(i.category)>maxlen):       
      maxlen=len(i.category)
  vertlen=12+maxlen
  print(perc)
  for i in range(10,-1,-1):
    if i<=9 and i >= 1:string+=" "
    if i == 0:string += "  "
    string=string+str(i*10)+"| "
    if perc[0] >= i*10: string+="o  "
    else:string+="   "
    if perc[1] >= i*10: string+="o  "
    else:string+="   "
    if perc[2] >= i*10: string+="o  "
    else:string+="   "
    string+="\n"
  string+="    "
  for i in range(len(names)*3+1):
    string+="_"
  string+="\"
  return string
    