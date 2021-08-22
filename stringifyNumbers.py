obj = {
    "num": 1,
    "test": [],
    "data": {
        "val": 4,
        "info": {
            "isRight": True,
            "random": 66
        }
    }
}

def stringifyNumbers(obj, newDict = {}):
  for key in obj:
    if isinstance(obj[key], (int, float) ):
    # if True:
      print("Numero!")
      newDict[key] = str(obj[key])
    elif isinstance(obj[key], dict) == True:
      newDict[key] = stringifyNumbers(obj[key])
    else:
      newDict[key] = obj[key]
  return newDict

result = stringifyNumbers(obj)
print(result)
print(type(result["num"]))


