# =====================================================
# 1. DRUG CONFIG 
# =====================================================
DRUG_CONFIG = {
    "company": "AbbVie",
    "focus_area": "Gene therapy and RNA therapeutics",
    "drug_name": "RNA_Gene_Therapy_Portfolio",
    "disease": "Multiple indications",
    # 基因治疗兴趣点
    "gene_therapy_targets": [
        "retinal diseases",
        "wet age-related macular degeneration",
        "diabetic retinopathy",
        "inherited retinal dystrophy",
        "AAV gene therapy",
        "non-viral gene delivery",
        "CNS-targeted gene therapy"
    ],
    # RNA治疗兴趣点
    "rna_therapy_targets": [
        "antisense oligonucleotide",
        "siRNA",
        "mRNA therapeutics",
        "RNA editing (ADAR)",
        "LNP delivery",
        "GalNAc conjugates",
        "CNS RNA therapeutics"
    ],
    # PubMed 搜索关键词
    "pubmed_query": (
        "(AbbVie[Affiliation] OR AbbVie[Title/Abstract]) AND "
        "(gene therapy OR AAV OR viral vector OR non-viral vector OR "
        "RNA therapy OR antisense OR siRNA OR mRNA OR RNA editing)"
    ),
    # Patent 搜索关键词（USPTO/ Lens API）
    "patent_query": "AbbVie AND (gene therapy OR RNA OR AAV OR siRNA OR mRNA)",
    # 最大检索数量
    "max_pubmed_results": 50,
    "max_patent_results": 20,
    # LLM角色
    "expert_role": "AbbVie BD&L strategy analyst for gene and RNA therapeutics",
    # 关键评价指标
    "evaluation_metrics": {
        "gene_therapy": [
            "delivery platform maturity",
            "target tissue accessibility",
            "immune response risk",
            "commercial potential",
            "clinical stage distribution",
            "competitive landscape"
        ],
        "rna_therapy": [
            "delivery efficiency",
            "target specificity",
            "durability of effect",
            "safety profile",
            "CNS penetration",
            "platform scalability"
        ]
    }
}

OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)
