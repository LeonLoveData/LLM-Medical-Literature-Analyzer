import os
from dotenv import load_dotenv

# =====================================================
# Load environment variables
# =====================================================
load_dotenv()

# NCBI / GROQ / LENS API keys
NCBI_EMAIL = os.getenv("NCBI_EMAIL")
NCBI_API_KEY = os.getenv("NCBI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
LENS_API_KEY = os.getenv("LENS_API_KEY")

if not NCBI_EMAIL or not GROQ_API_KEY:
    raise ValueError("NCBI_EMAIL or GROQ_API_KEY not set")

# =====================================================
# Drug configuration
# =====================================================
DRUG_CONFIG = {
    "company": "abc_pharma",
    "focus_area": "Gene therapy and RNA therapeutics",
    "drug_name": "RNA_Gene_Therapy_Portfolio",
    "disease": "Multiple indications",
    "gene_therapy_targets": [
        "retinal diseases",
        "wet age-related macular degeneration",
        "diabetic retinopathy",
        "inherited retinal dystrophy",
        "AAV gene therapy",
        "non-viral gene delivery",
        "CNS-targeted gene therapy"
    ],
    "rna_therapy_targets": [
        "antisense oligonucleotide",
        "siRNA",
        "mRNA therapeutics",
        "RNA editing (ADAR)",
        "LNP delivery",
        "GalNAc conjugates",
        "CNS RNA therapeutics"
    ],
    "pubmed_query": (
        "(abc_pharma[Affiliation] OR abc_pharma[Title/Abstract]) AND "
        "(gene therapy OR AAV OR viral vector OR non-viral vector OR "
        "RNA therapy OR antisense OR siRNA OR mRNA OR RNA editing)"
    ),
    "patent_query": "abc_pharma AND (gene therapy OR RNA OR AAV OR siRNA OR mRNA)",
    "max_pubmed_results": 50,
    "max_patent_results": 20,
    "expert_role": "abc_pharma BD&L strategy analyst for gene and RNA therapeutics",
}

# Output directory
OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)
