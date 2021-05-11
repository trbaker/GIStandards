# search PDF for keywords

# import packages
import PyPDF2
import re
import requests
import pymysql

#geospatial keywords
string1 = "GIS"
counter=0
string2 = 'Geographic Information System'
string3 = 'geospatial'
# ########## tier 2 words ##########
string4=" spatial"  #space added before spatial to remove 'geospatial' and similar
string5="geographic analysis"

# database
# set database params
connection = pymysql.connect(host="localhost",
                             user="pymysql",
                             password="Geospatial2040",
                             db='GIStandards',
                             cursorclass=pymysql.cursors.DictCursor)

# get pdf
url = 'https://www.alsde.edu/sec/sct/COS/2010%20Alabama%20Social%20Studies%20Course%20of%20Study.pdf'
response = requests.get(url)
with open('/Users/tom5137/Documents/GitHub/GIStandards/samples/sample.pdf', 'wb') as f:
    f.write(response.content)

# open the pdf file
object = PyPDF2.PdfFileReader('/Users/tom5137/Documents/GitHub/GIStandards/samples/sample.pdf')
# get number of pages
NumPages = object.getNumPages()

# extract text and do the search
for i in range(0, NumPages):
    pageObj = object.getPage(i)
    text = pageObj.extractText()
    stlist=[string1, string2, string3, string4, string5]
    for j in stlist:
        research = re.search(j, text)
        if research != None:
            counter=counter+1
            #print('occurrence #', counter)
            #print(research.span())
            start=research.span()[0]
            stop=research.span()[1]
            print("*",j.rstrip(), "* on page: " + str(i), 'char start: ', start)
            newstart = text.find(' ', start-200)
            extracted=text[newstart:stop+100]
            #try to get a clean start pos that doesn't split words.
            #print('new start: ', newstart)
            extracted=extracted.replace('\n','').replace('\r','')
            print('  ....' + extracted + '....', sep='')
            print('')
            # write database insert
            with connection.cursor() as cursor:
                sql = "insert into GIstandards.findings (keyword) values ('" + str(j) + "');"
                cursor.execute(sql)
                connection.commit()
print('There were ', counter, 'occurrences of all terms.')
counter=0
connection.close()