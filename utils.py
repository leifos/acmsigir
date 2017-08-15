import time
import re
import os.path
from requests import get  # to make GET request

# These are all the ids to SIGIR proceeings 1971 - 2017
SPIDS = ['511285','800096','511706','636669','511754','636713','511793','636805','253495','253168',
         '42005','62437','75334','96749','122860','133160','160688','188490','215206','243199','258525','290941'
        ,'312624','345508','383952','564376','860435','1008992','1076034','1148170','1277741','1390334',
         '1571941','1835449','2009916','2348283','2484028','2600428','2766462','2911451','3077136']


def download(url, file_name):
    # open in binary mode
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
    with open(file_name, "wb") as f:
        # get request
        response = get(url,headers=headers)
        # write to file
        f.write(response.content)
        
def make_sp_name(spid):
    return "data/sigir-{0}.html".format(spid)

def get_paper_id(paper_url):
    i = paper_url.find('=')
    j = paper_url.find('&',i)
    pid = paper_url[i+1:j]
    return pid

def extract_url(line):
    i = line.find('citation.cfm')
    j = line.find('"',i+1)
    url = line[i:j]
    return url


def remove_non_article_links(line, spid):
    r = ['flat','tabs','prox']
    r.append(spid)
    
    for w in r:
        if line.find(w)>0:
            line = ""
    
    return line

def strip_cfs(line):
    i = line.find("&CFID")
    sline = line[0:i+1]
    return sline
    

def parse_out_papers(file_name,spid):
    papers = []
    with open(file_name, "r") as f:
        line = f.readline()
        while line:
            if "citation" in line:
                line = remove_non_article_links(line,spid)
                line = strip_cfs(line)
                url = extract_url(line)              
                if url:
                    papers.append('http://dl.acm.org/{0}{1}'.format(url,'&preflayout=flat'))
            line = f.readline()
            
    return papers


def extract_author_id(line):
    i = line.find('author_page.cfm')
    j = line.find('"',i+1)
    aid = line[i:j]
    return aid

def parse_out_authors(file_name):
    authors = []
    with open(file_name, "r") as f:
        line = f.readline()
        while line:
            if "author_page" in line:
                line = strip_cfs(line)
                aid = extract_author_id(line)
                if aid:
                    authors.append(aid)
            line = f.readline()
            
    return authors


def parse_out_year(file_name):
    year = 0
    reyear = re.compile(r'\d\d\d\d Proceeding')
    with open(file_name, "r") as f:
        line = f.readline()
        while line:
            if " Proceeding" in line:
                d = reyear.search(line)
                if d:
                    year = int(d.group()[0:4])
                    break
            line = f.readline()
    return year



def max_span(year_list):
    #finds the max span between years
    max_span = 0
    years = (0,0)
    
    if len(year_list) == 1:
        return max_span, years
    
    prev_year = year_list[0]
    for curr_year in year_list[1:]:
        curr_span = curr_year-prev_year
        if curr_span > max_span:
            max_span = curr_span
            years = (prev_year,curr_year)
        prev_year = curr_year
    
    return max_span, years




def count_references(file_name):
    references = 0
    citations = 0
    year = 0
    
    redate = re.compile(r'\d\d\d\d Article')
    
    do_count = 0 # flag
    
    with open(file_name, "r") as f:
        line = f.readline()
        while line:
            if "REFERENCES" in line:
                do_count = 1
            if ("CITED BY" in line): 
                do_count = 2
            if ("INDEX TERMS" in line):
                do_count = 0
            
            if do_count == 1:
                if '"abstract"' in line:
                    references += 1 
            if do_count == 2:
                a = '"abstract"'
                if a in line:
                    i = line.find(a)
                    j = line.find(' ',i)
                    c = line[i+len(a)+1:j+1]
                                        
                    citations = c.strip()
                    do_count = 0
                    
            if " Article" in line:
                d = redate.search(line)
                if d:
                    year = d.group()[0:4]
                
            line = f.readline()

    if references > 0:
        references = references -1
    return [year, references, citations]



def extract_paper_authors(file_name):
    """ extracts out the authors for a given paper.
    returns a list of the co-authors
    """
    authors = []
    apc = 'author_page.cfm'
    l = len(apc)
    
    do_count = 0
    with open(file_name, "r") as f:
        line = f.readline()
        while line:
            if "Published in:" in line:
                break
                
            if "Publication of" in line:
                break
                
            if "author_page" in line:
                i = line.find(apc)
                j = line.find('&',i+1)
                aid = line[i+l+4:j]
                #print(aid)
                if aid:
                    authors.append(aid)
                
            line = f.readline()
    return authors



def compute_closest(mref, mcite, threshold):
    
    counts = []

    with open("counts.txt",'r') as f:
        line = f.readline()
        while line:
            (spid, year, refs, cites) = line.split()
            cites = int( cites.replace(',','') )
            refs = int(refs)
            score = ((refs-mref)*(refs-mref)) + ((cites-mcite)*(cites-mcite))
            counts.append([spid, int(year), refs, cites, score])
            if score < threshold:
                print("paper id: {0} year: {1} refs: {2} cites: {3} score: {4}".format( spid, year, refs, cites, score))
                print("http://dl.acm.org/citation.cfm?id={0}".format(spid))
            line = f.readline()
