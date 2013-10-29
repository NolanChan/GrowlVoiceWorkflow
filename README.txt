GrowlVoiceWorkflow
==================

V 0.1

Hi everyone,

I've created a GrowlVoice Alfred Workflow. It honestly doesn't save you that much time, 
since opening GrowlVoice takes about half a second with a shortcut,
but things are always more fun to do in Alfred!

So down to business:

There are two keyword calls in the workflow at the moment:

1) UpdateContacts [no arguements]

So before you use this keyword, there are a few steps you have to follow. The main idea of this script is to pull the first 1000 phone numbers
you have on your google account, and store them on your hard drive as a text file. 

***
Disclaimer:
You will also need to input your username and password into the python file for this to work. 
I know this sounds a little shady, and I promise that my code doesn't do anything weird (since I'm basically
using Google's Gdata skeleton with a slight change to pull phone numbers) but I'm including this here as a warning.
***

So the steps to preform before calling this workflow is:

  1) Get into the GrowlVoice Alfred Workflow folder: Right Click on the GrowlVoice section in Alfred Preferences and choose show in finder
  2) Open up UpdateContacts.py in your favorite code editor; The TextEdit application should be fine
  3) Put your email and password in-between the quotes: 
  
  email = ""
  password = ""
  
  4) Save the file
  5) Run in the alfred box: UpdateContacts
  6) If you are connected to the internet and you put in your email and password correctly, you should receive a notification that everything has worked
  7) You're good to go!
  
2) gv [name of person]

This keyword, followed by the name of the person you want to text, should bring down options of people you can choose to text. 
When you choose a person to text, the growlvoice window should open up, and the person's number should be in the addresse' box.

YOU MUST PRESS TAB BEFORE YOU START TYPING A MESSAGE IN GROWLVOICE, OR ELSE IT'LL JUST CLEAR THE NUMBER.
You'll know what I mean when you start typing. :)


