def export_word(records, summaries, analysis):
    doc = Document()
    doc.add_heading(f"{DRUG_CONFIG['drug_name']} – Clinical Trial & Patent Analysis", 0)
    doc.add_paragraph(
        f"Indication: {DRUG_CONFIG['disease']}\n"
        f"Data Source: PubMed + Lens Patents\n"
        f"Structured Fields: extracted with source sentences\n"
        f"Summary & Analysis: LLM inferred (marked)\n"
        f"Purpose: BD / Strategy / Due Diligence"
    )
    doc.add_heading("Structured Evidence", level=1)
    for r in records:
        doc.add_paragraph(f"Source ID: {r['source_id']}")
        for f in REQUIRED_FIELDS:
            v = r.get(f)
            if v:
                doc.add_paragraph(f"{f.upper()}:\n  Value: {v.get('value')}\n  Source: {v.get('source_text')}")
    doc.add_heading("LLM Inferred Summary", level=1)
    for s in summaries:
        doc.add_paragraph(s)
    doc.add_heading("LLM Inferred Competitive Analysis", level=1)
    doc.add_paragraph(analysis)
    path = f"{OUTPUT_DIR}/{DRUG_CONFIG['drug_name']}_BD_READY_REPORT.docx"
    doc.save(path)
    return path
