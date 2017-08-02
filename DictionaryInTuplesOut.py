# Assignment: Dictionary in, tuples out
# Write a function that takes in a dictionary and returns a list of tuples where
#the first tuple item is the key and the second is the value. Here's an example:
# # function input
# my_dict = {
#   "Speros": "(555) 555-5555",
#   "Michael": "(999) 999-9999",
#   "Jay": "(777) 777-7777"
# }

# #function output
# [("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]


def DictionaryToTouple(inDictionary):
    outTouple = []
    for key in inDictionary:
        outTouple.append( (key, inDictionary[key]) )
    return outTouple

my_Dictionary = { "Speros": "(555) 555-5555", "Michael": "(999) 999-9999", "Jay": "(777) 777-7777" }
print "Function DictionaryToTouple"
print "Inputs: {0}".format(my_Dictionary)
ArrayOfTouples = DictionaryToTouple(my_Dictionary)
print "Outputs: {0}".format(ArrayOfTouples)
