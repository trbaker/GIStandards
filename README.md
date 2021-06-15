# Geospatial keywords in US K12 curriculum standards
#### A machine analysis of geospatial language in US K-12 state curriculum standards

#### Abstract
This website contains the results of a machine analysis of US curriculum standards.  All state core standards (English, math, science, and social studies) and Career and Technical Education (CTE) program descriptions were collected.  A custom python-based program read each standard in search of a keyword (spatial, geospatial, GIS, geographic information system, and geographic analysis).  Counts were summed and normalized based on total words in the collection of documents for that state and subject area. Analysis of data is forthcoming. See project status below for more information.

#### Academic citation:
[Baker,T.R.](https://orcid.org/0000-0002-5005-9663) (2021). *Geospatial keywords in US K12 curriculum standards*. http://trbaker.github.io/GIStandards

#### Chapters
- Overview and findings
- [Alabama](AL.html)
- [Alaska](AK.html)
- [Arizona](AZ.html)
- [Arkansas](AR.html)
- [California](CA.html)
- [Connecticut](CT.html)
- [DC](DC.html)
- [Delaware](DE.html)
- [Florida](FL.html)
- [Georgia](GA.html)
- [Hawaii](HI.html)
- [Illinois](IL.html)
- [Indiana](ID.html)
- [Iowa](IA.html)
- [Kansas](KS.html)
- [Kentucky](KY.html)
- [Louisiana](LA.html)
- [Maine](ME.html)
- [Maryland](MD.html)
- [Michigan](MI.html)
- [Minnesota](MN.html)
- [Mississippi](MS.html)
- [Missouri](MO.html)
- [Montana](MT.html)
- [Nebraska](NE.html)
- [New Jersey](NJ.html)
- [New Mexico](NM.html)
- [North Carolina](NC.html)
- [North Dakota](ND.html)
- [Nevada](NV.html)

#### Appendices
- [Appendix I: Strategies in keyword searching in standards documents](appendix_search.md)
- [Appendix II: Keyword listing and brief discussion](appendix_keywords.md)

----------------------
#### Project status and feedback
As of June 1, 2021, the standards are being collected and the analysis script is being finalized.  A phase 1 release is targeted for mid  June 2021. If you find errors or have concerns about any part of this work, please email: trbaker@gmail.com

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


