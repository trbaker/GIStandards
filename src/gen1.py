# search PDF for keywords

# import packages
import PyPDF2
import re
#variables
# define keyterms
string1 = "GIS"
string1_counter=0

# open the pdf file
object = PyPDF2.PdfFileReader("/Users/tom5137/Documents/GitHub/GIStandards/samples/2010ALSS.pdf")
# get number of pages
NumPages = object.getNumPages()


# extract text and do the search
for i in range(0, NumPages):
    pageObj = object.getPage(i)
    text = pageObj.extractText()
    #print(text)
    research = re.search(string1, text)
    if research != None:
        string1_counter=string1_counter+1
        print('occurrence #', string1_counter)
        #print(research.span())
        start=research.span()[0]
        stop=research.span()[1]
        print(string1.rstrip(), "on page: " + str(i), 'char start: ', start)
        newstart = text.find(' ', start-200)
        extracted=text[newstart:stop+100]
        #try to get a clean start pos that doesn't split words.
        #print('new start: ', newstart)
        extracted=extracted.replace('\n','').replace('\r','')
        print('  ....' + extracted + '....', sep='')
        print('')

print('There were ', string1_counter, 'occurrences of', string1.rstrip())