# Appendix I: Strategies in keyword searching and normalizing

In reality, words do not carry equal significance – demonstrated by position of the word (e.g. word in an assessed standard vs in a supporting example). 

In this project, keyword counts are normalized by total words in those standards (called a comparable score).  State A may use 40,000 words to describe its K12 science standards, where state B uses 400,000 words.  While the documents may or may not include the same concepts, the machine counts the occurrence of each keyword.  The 400,000-word document may not include concepts not in the 40,000 word document, however the larger document may more thoroughly explain a concept with multiple examples.  By normalizing the machine’s count (dividing by total words in the standards), we improve the reported values for state-by-state comparison purposes. This is not a perfect solution, but a better one.

Word counts look for runs of letters, separated by a space. This generally works well, although tables can be problematic. Extensive footers throughout a document can skew the practical total word count. Finally, the identifiers used in standards (e.g. C.1.234f) can be counted as one or more words, depending on how the indicator string is written.

Documents archived include (in order of preference):
- Core, Content, or Performance tandards
- Frameworks
- Course or programs of study (CTE)
- Assessment blueprints (CTE)

Documents not included:
- Progressions
- Introductions (unless a part of an above document)
- “placemat” standards (unless no other standards documents were found)

Not all state standards are equally impactful – whether there is variable compliance by educators, or simply a state with a small population.  Are West Virginia’s standards as impactful as California’s?

CTE 'standardss' should probably not be compared to the four core acaemic standards.  The majority of documents used in CTE are course or program of study descriptions, while the core academic disciplines use content standards.  By and large, social studies standards vary more greatly (in content and form) from state to state than the other three academic areas.  

### Reading PDFs
Standards documents were either downloaded in a PDF (format) or converted to PDF.  There were cases where PDFs needed to be encoded without binary objects (like images), allowing for the PDF to be readable by the machine.  These PDFs are included in the file archive.  Most of these updated PDFs are not easy for humans to read, but are far more machine readable than the originals. The MacIntosh worflow for conversion: 1. Adobe Acrobat > File: Export to: Rich Text Format 2. TextEdit > Print : PDF : Save as PDF.


<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-VJ281EFGY0"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-VJ281EFGY0');
</script><!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-VJ281EFGY0"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-VJ281EFGY0');
</script>
