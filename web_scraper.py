import requests
from bs4 import BeautifulSoup


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
print(result_string)

