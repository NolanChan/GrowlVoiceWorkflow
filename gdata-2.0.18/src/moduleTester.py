import DictToFile

w = DictToFile.Writer()

data = w.reading('ContactNumbers.txt')

print "\n\n\n"

print data["Lishen Lu"]