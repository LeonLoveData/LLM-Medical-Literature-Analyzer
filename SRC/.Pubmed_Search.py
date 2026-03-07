# =====================================================
# 2. PUBMED SEARCH
# =====================================================
def search_pubmed(query, max_results):
    handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
    record = Entrez.read(handle)
    handle.close()
    return record["IdList"]

def fetch_pubmed_abstract(pmid):
    handle = Entrez.efetch(db="pubmed", id=pmid, rettype="abstract", retmode="text")
    text = handle.read()
    handle.close()
    return text

def batch_fetch_pubmed(pmids, delay=0.4):
    texts = {}
    for pmid in pmids:
        try:
            texts[pmid] = fetch_pubmed_abstract(pmid)
        except:
            continue
        time.sleep(delay)
    return texts
