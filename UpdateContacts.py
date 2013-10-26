import sys
import getopt
import getpass
import atom
import gdata.contacts.data
import gdata.contacts.client
import DictToFile
import FuzzyDict

def WriteAllContactsWithNumbers():

    allContacts = FuzzyDict.FuzzyDict()
    query = gdata.contacts.client.ContactsQuery()
    query.max_results = 1000
    feed = gd_client.GetContacts(q=query)
    if not feed.entry:
      print '\nNo contacts in feed.\n'
      return 0
    for i, entry in enumerate(feed.entry):
      if not entry.phone_number: continue
      if not entry.name is None:
        family_name = entry.name.family_name is None and " " or entry.name.family_name.text
        full_name = entry.name.full_name is None and " " or entry.name.full_name.text
        given_name = entry.name.given_name is None and " " or entry.name.given_name.text
      numbers = []
      if entry.phone_number:
        for phone_number_obj in entry.phone_number:
          number = phone_number_obj.text
          relation = phone_number_obj.rel[33:]
          digits = ''.join(n for n in number if n.isdigit())
          numbers.append((relation, digits))  

      allContacts[full_name] = (full_name, numbers)
    w = DictToFile.Writer()
    w.writing('ContactNumbers.txt', allContacts)
    return allContacts


email = ""
password = ""
not_authenticated = False

try:
	gd_client = gdata.contacts.client.ContactsClient(source='GoogleInc-ContactsPythonSample-1')
	gd_client.ClientLogin(email, password, gd_client.source)
except Exception, e:
	not_authenticated = True

if not_authenticated:
	print "Contacts Update Failed"
else:
	notification = WriteAllContactsWithNumbers()
	if notification: print "Contacts Updated Successfully"
	else: print "Contacts Update Failed"


