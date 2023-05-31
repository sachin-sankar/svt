
def parseCarNumber(numberString):
  i = numberString.strip().upper()
  return " ".join([i[0:2],i[2:4],i[4:][:-4],i[-4:]])

def validateCarNumber(numberString):
  number = parseCarNumber(numberString).split()
  if number[0].isalpha() and number[1].isdigit() and number[2].isalpha() and number[3].isdigit():
    return True
  else:
    return False