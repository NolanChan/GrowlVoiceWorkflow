import DictToFile
import FuzzyDict
import sys


class XMLTemplateCreator:

    def __init__(self):
        self.xmlTemplate = """
      <items>
          <item uid="%(uid)s" arg="%(arg)s" valid="%(valid)s" autocomplete="%(autocomplete)s">
              <title>%(title)s</title>
              <subtitle>%(subtitle)s</subtitle>
              <icon>%(icon)s</icon>
           </item>
      </items>
      """

    def createXMLfromVerse(self, passageNumber, passage):
        data = {'uid': passageNumber, 'arg': passageNumber, 'valid': 'YES', 'autocomplete':
                passageNumber, 'title': passageNumber, 'subtitle': passage, 'icon': "icon.png"}
        return self.xmlTemplate % data

    def createXMLfromPhoneNumber(self, name, phone_type, phone_number):
    	title = str(name) + ": " + str(phone_type)
    	arg = "growlvoice:" + phone_number + "?text"
        data = {
            'uid': phone_number, 'arg': arg, 'valid': 'YES',
            'autocomplete': name, 'title': title, 'subtitle': phone_number, 'icon': "icon.png"}
        return self.xmlTemplate % data


# retrive the command line arguements and concat them into the name
arguements = sys.argv
name = sys.argv[1]

w = DictToFile.Writer()
contactsFuzzyDictionary = w.reading('ContactNumbers.txt')

# check if it returns no key, then return a 'none' xml
if str(contactsFuzzyDictionary[name][0:5]) == "Sorry":
	print XMLTemplateCreator().createXMLfromVerse("None", "None")

	
# test
x = XMLTemplateCreator()
XMLString = ""
names_and_phone_numbers = contactsFuzzyDictionary[name]
for name_and_phone_number in names_and_phone_numbers:
    name = name_and_phone_number[0]
    for phone_type_and_number in name_and_phone_number[1]:
        t = phone_type_and_number[0]
        n = phone_type_and_number[1]
        XMLString = XMLString + x.createXMLfromPhoneNumber(name, t, n)

print "<items> \n" + XMLString + " \n </items>"




# w = DictToFile.Writer()
# data = w.reading('ContactNumbers.txt')
# print data['Bryan']
