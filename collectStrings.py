def collectStrings(obj, arr = []):
  for x in obj:
    if isinstance(obj[x], str):
      arr.append(obj[x])
    elif isinstance(obj[x], dict):
      collectStrings(obj[x], arr)
  return arr 


obj = {
    'stuff': "foo",
    'data': {
        'val': {
            'thing': {
                'info': "bar",
                'moreInfo': {
                    'evenMoreInfo': {
                        'weMadeIt': "baz"
                    }
                }
            }
        }
    }
}

print(collectStrings(obj))