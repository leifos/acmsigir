
Calculate the author who is closest to all other authors in the largest connected co-authorship graph


```python
from utils import *
import networkx as nx
SPIDS = ['511285','800096','511706','636669','511754','636713','511793','636805','253495','253168',
         '42005','62437','75334','96749','122860','133160','160688','188490','215206','243199','258525','290941'
        ,'312624','345508','383952','564376','860435','1008992','1076034','1148170','1277741','1390334',
         '1571941','1835449','2009916','2348283','2484028','2600428','2766462','2911451','3077136']


def create_graph(spids, graph_filename):
    pc = 0
    x = []
    y = []
    counts = {}
    for spid in spids:
        sigir_head_file = make_sp_name(spid)
        papers = parse_out_papers(sigir_head_file, spid)
        # for each paper in the proceedings, download the paper
        for p in papers:
            pid = get_paper_id(p)
            paper_file = 'data/{0}.html'.format(pid)
            pc +=1 
            authors = extract_paper_authors(paper_file)
        
            # only add a node if there is at least two authors
            if (len(authors)>1):
                for a in authors:
                    for b in authors:
                        if a != b:
                            x.append(a)
                            y.append(b)
                
    with open(graph_filename, "w") as f:
        for i in range(0,len(x)):
            f.write("{0} {1}\n".format(x[i], y[i] ))
            
            

def create_graph(graph_filename):       
    G = nx.Graph()
    with open(graph_filename,'r') as f:
        line = f.readline()
        while line:
            (a,b) = line.split()
            G.add_edge(a,b)
            line = f.readline()
            
    return G

def find_centre(graph_filename):
    G = create_graph(graph_filename)
    short = nx.shortest_path_length(G)
    
    author = 0
    dist = 10000000000
    s = 0
    
    
    for key in short:
        a = short[key]
        sum = 0
        if len(a) > 80:
            for b in a:
                sum += a[b]
            m = float(sum)/float(len(a))
            if m < dist:
                author = key
                dist = m
                s = len(a)

    print("Author: http://dl.acm.org/author_page.cfm?id={0}".format(author))
    print("with a distance of: {0} in biggest connected cluser of size: {1} and graph of: {2}".format( dist, s, G.order()))   
    
    return (author, dist, s, G.order())
```


```python
out = {}
for i in range(20,41):
    print("SIGIR #: {0} http://dl.acm.org/citation.cfm?id={1}".format(i, SPIDS[i]))
    graph_filename = "data/graph-{0}.txt".format(i)
    tspids = SPIDS[:i]
    if not os.path.isfile(graph_filename): 
        create_graph(tspids, graph_filename)
    (author, dist, s, o) = find_centre(graph_filename)
    out[i] = (author, dist, s, o)
```

    SIGIR #: 20 http://dl.acm.org/citation.cfm?id=258525
    Author: http://dl.acm.org/author_page.cfm?id=81350588112
    with a distance of: 3.2831858407079646 in biggest connected cluser of size: 113 and graph of: 646
    SIGIR #: 21 http://dl.acm.org/citation.cfm?id=290941
    Author: http://dl.acm.org/author_page.cfm?id=81350588112
    with a distance of: 3.275 in biggest connected cluser of size: 120 and graph of: 694
    SIGIR #: 22 http://dl.acm.org/citation.cfm?id=312624
    Author: http://dl.acm.org/author_page.cfm?id=81350588112
    with a distance of: 3.198473282442748 in biggest connected cluser of size: 131 and graph of: 824
    SIGIR #: 23 http://dl.acm.org/citation.cfm?id=345508
    Author: http://dl.acm.org/author_page.cfm?id=81100350752
    with a distance of: 3.1301369863013697 in biggest connected cluser of size: 146 and graph of: 942
    SIGIR #: 24 http://dl.acm.org/citation.cfm?id=383952
    Author: http://dl.acm.org/author_page.cfm?id=81100350752
    with a distance of: 3.2701149425287355 in biggest connected cluser of size: 174 and graph of: 1055
    SIGIR #: 25 http://dl.acm.org/citation.cfm?id=564376
    Author: http://dl.acm.org/author_page.cfm?id=81100350752
    with a distance of: 3.390625 in biggest connected cluser of size: 192 and graph of: 1191
    SIGIR #: 26 http://dl.acm.org/citation.cfm?id=860435
    Author: http://dl.acm.org/author_page.cfm?id=81100350752
    with a distance of: 3.969111969111969 in biggest connected cluser of size: 259 and graph of: 1346
    SIGIR #: 27 http://dl.acm.org/citation.cfm?id=1008992
    Author: http://dl.acm.org/author_page.cfm?id=81363594457
    with a distance of: 4.661946902654868 in biggest connected cluser of size: 565 and graph of: 1509
    SIGIR #: 28 http://dl.acm.org/citation.cfm?id=1076034
    Author: http://dl.acm.org/author_page.cfm?id=81363594457
    with a distance of: 4.5028985507246375 in biggest connected cluser of size: 690 and graph of: 1680
    SIGIR #: 29 http://dl.acm.org/citation.cfm?id=1148170
    Author: http://dl.acm.org/author_page.cfm?id=81363594457
    with a distance of: 4.086142322097379 in biggest connected cluser of size: 801 and graph of: 1889
    SIGIR #: 30 http://dl.acm.org/citation.cfm?id=1277741
    Author: http://dl.acm.org/author_page.cfm?id=81363594457
    with a distance of: 4.176165803108808 in biggest connected cluser of size: 965 and graph of: 2079
    SIGIR #: 31 http://dl.acm.org/citation.cfm?id=1390334
    Author: http://dl.acm.org/author_page.cfm?id=81363594457
    with a distance of: 4.304498269896194 in biggest connected cluser of size: 1156 and graph of: 2378
    SIGIR #: 32 http://dl.acm.org/citation.cfm?id=1571941
    Author: http://dl.acm.org/author_page.cfm?id=81363594457
    with a distance of: 4.1098901098901095 in biggest connected cluser of size: 1365 and graph of: 2637
    SIGIR #: 33 http://dl.acm.org/citation.cfm?id=1835449
    Author: http://dl.acm.org/author_page.cfm?id=81363594457
    with a distance of: 4.110968569595895 in biggest connected cluser of size: 1559 and graph of: 2918
    SIGIR #: 34 http://dl.acm.org/citation.cfm?id=2009916
    Author: http://dl.acm.org/author_page.cfm?id=81100303767
    with a distance of: 4.086314593980693 in biggest connected cluser of size: 1761 and graph of: 3196
    SIGIR #: 35 http://dl.acm.org/citation.cfm?id=2348283
    Author: http://dl.acm.org/author_page.cfm?id=81363594457
    with a distance of: 4.238049713193116 in biggest connected cluser of size: 2092 and graph of: 3535
    SIGIR #: 36 http://dl.acm.org/citation.cfm?id=2484028
    Author: http://dl.acm.org/author_page.cfm?id=81100612930
    with a distance of: 4.225085910652921 in biggest connected cluser of size: 2328 and graph of: 3858
    SIGIR #: 37 http://dl.acm.org/citation.cfm?id=2600428
    Author: http://dl.acm.org/author_page.cfm?id=81100390699
    with a distance of: 4.0462816455696204 in biggest connected cluser of size: 2528 and graph of: 4135
    SIGIR #: 38 http://dl.acm.org/citation.cfm?id=2766462
    Author: http://dl.acm.org/author_page.cfm?id=81100617179
    with a distance of: 3.993197278911565 in biggest connected cluser of size: 2793 and graph of: 4472
    SIGIR #: 39 http://dl.acm.org/citation.cfm?id=2911451
    Author: http://dl.acm.org/author_page.cfm?id=81100390699
    with a distance of: 3.8258557660352275 in biggest connected cluser of size: 3009 and graph of: 4739
    SIGIR #: 40 http://dl.acm.org/citation.cfm?id=3077136
    Author: http://dl.acm.org/author_page.cfm?id=81100617179
    with a distance of: 3.75206106870229 in biggest connected cluser of size: 3275 and graph of: 5073



```python
print(out)
```

    {20: ('81350588112', 3.2831858407079646, 113, 646), 21: ('81350588112', 3.275, 120, 694), 22: ('81350588112', 3.198473282442748, 131, 824), 23: ('81100350752', 3.1301369863013697, 146, 942), 24: ('81100350752', 3.2701149425287355, 174, 1055), 25: ('81100350752', 3.390625, 192, 1191), 26: ('81100350752', 3.969111969111969, 259, 1346), 27: ('81363594457', 4.661946902654868, 565, 1509), 28: ('81363594457', 4.5028985507246375, 690, 1680), 29: ('81363594457', 4.086142322097379, 801, 1889), 30: ('81363594457', 4.176165803108808, 965, 2079), 31: ('81363594457', 4.304498269896194, 1156, 2378), 32: ('81363594457', 4.1098901098901095, 1365, 2637), 33: ('81363594457', 4.110968569595895, 1559, 2918), 34: ('81100303767', 4.086314593980693, 1761, 3196), 35: ('81363594457', 4.238049713193116, 2092, 3535), 36: ('81100612930', 4.225085910652921, 2328, 3858), 37: ('81100390699', 4.0462816455696204, 2528, 4135), 38: ('81100617179', 3.993197278911565, 2793, 4472), 39: ('81100390699', 3.8258557660352275, 3009, 4739), 40: ('81100617179', 3.75206106870229, 3275, 5073)}



```python

```
