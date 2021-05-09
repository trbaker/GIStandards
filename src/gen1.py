
# search PDF for keywords
# https://www.alsde.edu/sec/sct/COS/2010%20Alabama%20Social%20Studies%20Course%20of%20Study.pdf

# import packages
import PyPDF2
import re

# open the pdf file
object = PyPDF2.PdfFileReader("/Users/tom5137/Documents/GitHub/GIStandards/samples/2010ALSS.pdf")

# get number of pages
NumPages = object.getNumPages()

# define keyterms
String = "GIS"

# extract text and do the search
for i in range(0, NumPages):
    PageObj = object.getPage(i)
    Text = PageObj.extractText()
    #print(Text)
    research = re.search(String, Text)
    if research != None:
        #print(research.span())
        start=research.span()[0]
        stop=research.span()[1]
        print(String.rstrip(), "on page: " + str(i), 'character: ', start)
        newstart = Text.find(' ', start-200)
        extracted=Text[newstart:stop+100]
        #try to get a clean start pos that doesn't split words.
        print('new: ', newstart)
        extracted=extracted.replace('\n','').replace('\r','')
        print('  ....' + extracted + '....', sep='')