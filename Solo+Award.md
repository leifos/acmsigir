

```python
from utils import *

SPIDS = ['511285','800096','511706','636669','511754','636713','511793','636805','253495','253168',
         '42005','62437','75334','96749','122860','133160','160688','188490','215206','243199','258525','290941'
        ,'312624','345508','383952','564376','860435','1008992','1076034','1148170','1277741','1390334',
         '1571941','1835449','2009916','2348283','2484028','2600428','2766462','2911451','3077136']

```


```python
pc = 0
x = []
y = []

solo_counts = {}
solo_papers = {}
for spid in SPIDS:
    sigir_head_file = make_sp_name(spid)
    papers = parse_out_papers(sigir_head_file, spid)
    # for each paper in the proceedings, download the paper
    for p in papers:
        pid = get_paper_id(p)
        paper_file = 'data/{0}.html'.format(pid)
        pc += 1 
        authors = extract_paper_authors(paper_file)
        
        l = len(authors)
        
        if len(authors)==1:
            a = authors[0]
            if a in solo_counts:
                solo_counts[a] += 1
            else:
                solo_counts[a] = 1

            if a in solo_papers:
                solo_papers[a].append(pid)
            else:
                solo_papers[a] = [pid]
                            
for a in solo_counts:
    if solo_counts[a] > 6:
        print("http://dl.acm.org/author_page.cfm?id={0} with {1} publications".format(a, solo_counts[a]))
        for p in solo_papers[a]:
            print("http://dl.acm.org/citation.cfm?id={0}".format(p))
```

    http://dl.acm.org/author_page.cfm?id=81328489030 with 8 publications
    http://dl.acm.org/citation.cfm?id=636819
    http://dl.acm.org/citation.cfm?id=253522
    http://dl.acm.org/citation.cfm?id=253226
    http://dl.acm.org/citation.cfm?id=75338
    http://dl.acm.org/citation.cfm?id=122879
    http://dl.acm.org/citation.cfm?id=243266
    http://dl.acm.org/citation.cfm?id=258531
    http://dl.acm.org/citation.cfm?id=564461
    http://dl.acm.org/author_page.cfm?id=81339534035 with 9 publications
    http://dl.acm.org/citation.cfm?id=253524
    http://dl.acm.org/citation.cfm?id=253203
    http://dl.acm.org/citation.cfm?id=160715
    http://dl.acm.org/citation.cfm?id=188508
    http://dl.acm.org/citation.cfm?id=291017
    http://dl.acm.org/citation.cfm?id=383963
    http://dl.acm.org/citation.cfm?id=1009121
    http://dl.acm.org/citation.cfm?id=1572138
    http://dl.acm.org/citation.cfm?id=2609524
    http://dl.acm.org/author_page.cfm?id=81100362356 with 7 publications
    http://dl.acm.org/citation.cfm?id=253221
    http://dl.acm.org/citation.cfm?id=75343
    http://dl.acm.org/citation.cfm?id=133202
    http://dl.acm.org/citation.cfm?id=160754
    http://dl.acm.org/citation.cfm?id=238480
    http://dl.acm.org/citation.cfm?id=215372
    http://dl.acm.org/citation.cfm?id=243325
    http://dl.acm.org/author_page.cfm?id=81100193167 with 8 publications
    http://dl.acm.org/citation.cfm?id=860529
    http://dl.acm.org/citation.cfm?id=1148261
    http://dl.acm.org/citation.cfm?id=1148322
    http://dl.acm.org/citation.cfm?id=1277756
    http://dl.acm.org/citation.cfm?id=1390454
    http://dl.acm.org/citation.cfm?id=2348517
    http://dl.acm.org/citation.cfm?id=2911492
    http://dl.acm.org/citation.cfm?id=2914684



```python

```
