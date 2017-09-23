import requests
from bs4 import BeautifulSoup
import csv

#takes in the webpage
webpage= input('Enter in link to guitar tab followed by a space.\n')
webpage=webpage[:-1]

#uses beautiful soup to get page
page=requests.get(webpage)
soup=BeautifulSoup(page.content, "html.parser")
notes= soup.findAll("pre", {"class":"js-tab-content js-init-edit-form js-copy-content js-tab-controls-item"} )

#casts the bs4 object to string
note_string=str(notes)

#turns string into list
result=note_string.split(" ")

#gets rid of the span tags on either end
result = [x[6:-7] for x in result if x[0:6] == '<span>' and x[-7:]=='</span>']

#joins elements to form one string
result_string=" ".join(result)

#gets title
title=soup.find('h1',attrs={'itemprop':'name'})
title=title.get_text()
#makes sure inputs are correct
title_bool=input('Does title look correct?(Y/N):\n'+ title+'\n')
if(title_bool=='Y'):
    pass
else:
    title=input('Please enter in correct title\n')

note_bool=input('Do these notes look correct?(Y/N):\n'+ result_string+ '\n')
if(note_bool=='Y'):
    pass
else:
    result_string=input('Please enter in correct notes\n')

print("The following will be entered into the csv:")
print(title)
print(result_string)

#logs to csv file with data
new_row=[title, result_string]

with open('music_notes.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(new_row)

