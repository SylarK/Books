#   Saving structured data with json

#   When you want to save more complex data types like nested lists and dictionaries, parsing and
#   serializing by hand becomes complicated. We use JSON (Javascript Object Notation)

import json

#json.dumps([1, 'Serial', 'Tiger', 2020])

# some JSON
x = '{ "name":"Harry", "last name":"Potter", "age":"23"}'

#parse x:
y = json.loads(x)

#print(y)
print(y['name'], y['last name'])

archive = open('json_test.txt')


with open('json_test.txt', 'w') as f:
    json.dump(x, f)
with open('json_test.txt', 'r') as f:
    data = json.load(f)
    print(data)

with open('json_test.txt', 'w') as f:
    f.write(json.dumps(data))

with open('json_test.txt', 'r') as f:
    data = json.loads(f.read())
    print(data)
