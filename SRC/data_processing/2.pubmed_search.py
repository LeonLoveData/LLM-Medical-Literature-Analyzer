import time
from Bio import Entrez
from src.config import NCBI_EMAIL, NCBI_API_KEY

# Configure Entrez
Entrez.email = NCBI_EMAIL
Entrez.api_key = NCBI_API_KEY


def search_pubmed(query, max_results):
    """Search PubMed and return list of PMIDs."""
    handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
    record = Entrez.read(handle)
    handle.close()
    return record["IdList"]


def fetch_pubmed_abstract(pmid):
    """Fetch a single PubMed abstract."""
    handle = Entrez.efetch(db="pubmed", id=pmid, rettype="abstract", retmode="text")
    text = handle.read()
    handle.close()
    return text


def batch_fetch_pubmed(pmids, delay=0.4):
    """Fetch multiple PubMed abstracts with delay."""
    texts = {}
    for pmid in pmids:
        try:
            texts[pmid] = fetch_pubmed_abstract(pmid)
        except:
            continue
        time.sleep(delay)
    return texts
