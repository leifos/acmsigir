

```python
from utils import *

SPIDS = ['511285','800096','511706','636669','511754','636713','511793','636805','253495','253168',
         '42005','62437','75334','96749','122860','133160','160688','188490','215206','243199','258525','290941'
        ,'312624','345508','383952','564376','860435','1008992','1076034','1148170','1277741','1390334',
         '1571941','1835449','2009916','2348283','2484028','2600428','2766462','2911451','3077136']

```


```python
# This scripts srapes the ACM DL and downloads all the proceedings, 
# and then from each proceedings it downloads all the published articles
# appearing in the proceeings (keynotes, full papers, short papers, demos, tutorial)

# Note that in the 1990 proceedings, it is labelled as being published in 1989.
# I manually changed the HTML for this one to have the correct year in it.

spfiles = []

# Only downloads papers that are not already/previously downloaded
for spid in SPIDS:
    sigir_url = "http://dl.acm.org/citation.cfm?id={0}&preflayout=flat".format(spid)
    sigir_head_file = make_sp_name(spid)
    spfiles.append(sigir_head_file)
    if not os.path.isfile(sigir_head_file): 
        print("Downloading " + sigir_head_file)
        download(sigir_url, sigir_head_file)
        time.sleep(1)
        
        
spc = []
count = 0
for spid in SPIDS:
    sigir_head_file = make_sp_name(spid)
    papers = parse_out_papers(sigir_head_file, spid)
    year = parse_out_year(sigir_head_file)
    # for each paper in the proceedings, download the paper
    
    for p in papers:
        pid = get_paper_id(p)
        paper_file = 'data/{0}.html'.format(pid)
        
        if not os.path.isfile(paper_file): 
            download(p, paper_file)
            time.sleep(2)    
    print("Downloaded: {0} papers from proceedings: {1} from year: {2} no.{3}".format(len(papers), spid, year, count))
    count += 1
```

    Downloaded: 19 papers from proceedings: 511285 from year: 1971 no.0
    Downloaded: 15 papers from proceedings: 800096 from year: 1978 no.1
    Downloaded: 14 papers from proceedings: 511706 from year: 1979 no.2
    Downloaded: 24 papers from proceedings: 636669 from year: 1980 no.3
    Downloaded: 21 papers from proceedings: 511754 from year: 1981 no.4
    Downloaded: 21 papers from proceedings: 636713 from year: 1982 no.5
    Downloaded: 28 papers from proceedings: 511793 from year: 1983 no.6
    Downloaded: 27 papers from proceedings: 636805 from year: 1984 no.7
    Downloaded: 33 papers from proceedings: 253495 from year: 1985 no.8
    Downloaded: 37 papers from proceedings: 253168 from year: 1986 no.9
    Downloaded: 33 papers from proceedings: 42005 from year: 1987 no.10
    Downloaded: 45 papers from proceedings: 62437 from year: 1988 no.11
    Downloaded: 28 papers from proceedings: 75334 from year: 1989 no.12
    Downloaded: 29 papers from proceedings: 96749 from year: 1990 no.13
    Downloaded: 35 papers from proceedings: 122860 from year: 1991 no.14
    Downloaded: 33 papers from proceedings: 133160 from year: 1992 no.15
    Downloaded: 44 papers from proceedings: 160688 from year: 1993 no.16
    Downloaded: 37 papers from proceedings: 188490 from year: 1994 no.17
    Downloaded: 46 papers from proceedings: 215206 from year: 1995 no.18
    Downloaded: 67 papers from proceedings: 243199 from year: 1996 no.19
    Downloaded: 40 papers from proceedings: 258525 from year: 1997 no.20
    Downloaded: 93 papers from proceedings: 290941 from year: 1998 no.21
    Downloaded: 82 papers from proceedings: 312624 from year: 1999 no.22
    Downloaded: 75 papers from proceedings: 345508 from year: 2000 no.23
    Downloaded: 87 papers from proceedings: 383952 from year: 2001 no.24
    Downloaded: 108 papers from proceedings: 564376 from year: 2002 no.25
    Downloaded: 107 papers from proceedings: 860435 from year: 2003 no.26
    Downloaded: 143 papers from proceedings: 1008992 from year: 2004 no.27
    Downloaded: 140 papers from proceedings: 1076034 from year: 2005 no.28
    Downloaded: 157 papers from proceedings: 1148170 from year: 2006 no.29
    Downloaded: 222 papers from proceedings: 1277741 from year: 2007 no.30
    Downloaded: 204 papers from proceedings: 1390334 from year: 2008 no.31
    Downloaded: 206 papers from proceedings: 1571941 from year: 2009 no.32
    Downloaded: 217 papers from proceedings: 1835449 from year: 2010 no.33
    Downloaded: 235 papers from proceedings: 2009916 from year: 2011 no.34
    Downloaded: 225 papers from proceedings: 2348283 from year: 2012 no.35
    Downloaded: 210 papers from proceedings: 2484028 from year: 2013 no.36
    Downloaded: 228 papers from proceedings: 2600428 from year: 2014 no.37
    Downloaded: 200 papers from proceedings: 2766462 from year: 2015 no.38
    Downloaded: 233 papers from proceedings: 2911451 from year: 2016 no.39
    Downloaded: 255 papers from proceedings: 3077136 from year: 2017 no.40



```python
# Process each proceedings and extract out the year, refs and cites for each paper.

counts = []
spc = []
for spid in SPIDS:
    sigir_head_file = make_sp_name(spid)
    papers = parse_out_papers(sigir_head_file, spid)
    # for each paper in the proceedings, download the paper
    for p in papers:
        pid = get_paper_id(p)
        paper_file = 'data/{0}.html'.format(pid)      
        [year, refs,cites] = count_references(paper_file)
        counts.append([pid, year, refs, cites])     
    spc.append(len(papers))
    

# Save the counts data to file
with open("data/counts.txt", "w") as f:
    for c in counts:
        f.write("{0} {1} {2} {3}\n".format(c[0], c[1], c[2], c[3] ))
        
```


```python

```
