

```python
# Comeback Award(s)
from utils import *
SPIDS = ['511285','800096','511706','636669','511754','636713','511793','636805','253495','253168',
         '42005','62437','75334','96749','122860','133160','160688','188490','215206','243199','258525','290941'
        ,'312624','345508','383952','564376','860435','1008992','1076034','1148170','1277741','1390334',
         '1571941','1835449','2009916','2348283','2484028','2600428','2766462','2911451','3077136']

```


```python
# Extract out all the authors for each year
#

# year author dict
ya = {}
for spid in SPIDS:
    spf = make_sp_name(spid)
    authors = parse_out_authors(spf)
    year = parse_out_year(spf)
    ya[year] = authors
        
# author year dict
au = {}    
for year in ya:
    for author in ya[year]:
        if author in au:
            yl = au[author]
        else:
            yl = []
        yl.append(year)
        au[author] = yl
        
# Print out the authors where the span is greater than 20 years
        
for author in au:
    (ms,ys) = max_span(au[author])
    if ms > 17:
        print("http://dl.acm.org/{0}  with a span of {1} from/to: {2}".format(author, ms, ys))
        
```

    http://dl.acm.org/author_page.cfm?id=81100409020  with a span of 18 from/to: (1982, 2000)
    http://dl.acm.org/author_page.cfm?id=81100489485  with a span of 19 from/to: (1981, 2000)
    http://dl.acm.org/author_page.cfm?id=81100038060  with a span of 19 from/to: (1985, 2004)
    http://dl.acm.org/author_page.cfm?id=81100609693  with a span of 24 from/to: (1989, 2013)
    http://dl.acm.org/author_page.cfm?id=81100172373  with a span of 18 from/to: (1993, 2011)
    http://dl.acm.org/author_page.cfm?id=81100481185  with a span of 19 from/to: (1993, 2012)



```python
# Catherine Berrut 24 years (paper to poster)
# Michael Nelson 18 years (paper to paper)
```
