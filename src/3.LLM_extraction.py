import json
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from src.config import GROQ_API_KEY

# LLM client
llm_extract = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    groq_api_key=GROQ_API_KEY
)

STRICT_TEMPLATE = """
You are a clinical trial or patent data extraction system.

STRICT RULES:
- Extract ONLY information explicitly written in the text.
- DO NOT infer for structured fields.
- If not explicitly stated, return null.
- Include exact source sentence.

TEXT:
{text}

Return STRICT JSON only:

{{
 "source_id": "{source_id}",
 "sample_size": {{"value": "...", "source_text": "..." }},
 "study_design": {{"value": "...", "source_text": "..." }},
 "phase": {{"value": "...", "source_text": "..." }},
 "primary_endpoint": {{"value": "...", "source_text": "..." }},
 "efficacy_results": {{"value": "...", "source_text": "..." }},
 "safety_results": {{"value": "...", "source_text": "..." }}
}}
"""

extract_prompt = PromptTemplate(
    input_variables=["text", "source_id"],
    template=STRICT_TEMPLATE
)


def extract_record(text, source_id):
    """Run strict LLM extraction with JSON parsing."""
    prompt = extract_prompt.format(text=text, source_id=source_id)
    res = llm_extract.invoke(prompt)

    try:
        parsed = json.loads(res.content)
        parsed["source_id"] = source_id
        return parsed
    except:
        return {
            "source_id": source_id,
            "error": "JSON_PARSE_FAILED",
            "raw_output": res.content
        }
