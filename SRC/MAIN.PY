def main():
    print("Searching PubMed...")
    pmids = search_pubmed(DRUG_CONFIG["pubmed_query"], DRUG_CONFIG["max_pubmed_results"])
    print(f"Found {len(pmids)} PubMed IDs")
    pubmed_texts = batch_fetch_pubmed(pmids)

    print("Extracting structured records...")
    records = []
    # PubMed records
    for pmid, text in pubmed_texts.items():
        r = extract_record(text, pmid)
        if validate_record(r):
            records.append(r)

    if not records:
        print("No valid records extracted.")
        return

    df = pd.json_normalize(records)
    df.to_csv(f"{OUTPUT_DIR}/{DRUG_CONFIG['drug_name']}_records.csv", index=False)

    print("Generating summaries...")
    summaries = [generate_summary(r) for r in records]

    print("Generating competitive analysis...")
    analysis = generate_competitive_analysis(summaries)

    word_path = export_word(records, summaries, analysis)
    print("\nBD-ready report generated:", word_path)

if __name__ == "__main__":
    main()
