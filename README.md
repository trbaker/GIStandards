# Geospatial keywords in US K12 curriculum standards
#### A machine analysis of geospatial language in US K-12 state standards
#### Project URL: http://trbaker.github.io/GIStandards

#### Academic citation:
[Baker,T.R.](https://orcid.org/0000-0002-5005-9663) (2021). *Geospatial keywords in 2021 US K12 curriculum standards*. http://trbaker.github.io/GIStandards

#### Abstract
This paper and website contain the results of a machine analysis.  All state core standards (English, math, science, and social studies) and CTEprogram descriptions were collected (here).  A custom python-based program read each standard in search of a keyword list.  Counts were summed and normalized based on total words in the collection of docuemens for that state and subject area.

#### Project status and feedback
As of May 27, 2021, standards are being collected and the analysis script is being finalized.  A phase 1 release is targeted for early June 2021. If you find errors or have concerns about any part of this work, please email: trbaker@gmail.com

#### Chapters
- Overview and findings
- [Alabama](AL.md)
- [Arizona](AZ.md)
- [Arkansas] (AR.md)
- ....

#### Appendices
- [Appendix I: Strategies in keyword searching in standards documents](appendix_search.md)

----------------------
#### Timelines and milesontes

Project Updates:
- Databases and Python engine are ready
- A state-by-state collection of standards is being built. Retreiving on-the-fly proved too problematic.

 Phase 1:
- Gather standards documents
- Use Python to read each of five core U.S. K-12 state curriculum standards documents.
- Log number of occurences from keyword list.
- Log total number of words.
- Log standard with structured id tag, by state, standard, and date.
- Public HTML files by state for report out.
- Publish overview report.

Phase 2:
- Log over time to understand spatial, temporal patterns.
- Account for concept blocks - places where keywords are used multiple times to address a single concept/standard.


