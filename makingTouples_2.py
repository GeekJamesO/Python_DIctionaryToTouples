print "Assignment: Dictionary in, tuples out"
print "  Write a function that takes in a dictionary and returns a list of "
print "  tuples where the first tuple item is the key and the second is the value."

my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def DictToTouples(inDict):
    outList = []
    for key in inDict:
        outList.append( ( key , inDict[key] ) )
    return outList

print "Input Dictionary:   ", my_dict
output = DictToTouples(my_dict)
print "Output list Touples:", output
