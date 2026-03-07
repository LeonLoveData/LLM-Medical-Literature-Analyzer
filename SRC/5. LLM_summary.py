llm_summary = ChatGroq(model="llama-3.1-8b-instant", temperature=0, groq_api_key=GROQ_API_KEY)

SUMMARY_TEMPLATE = """
You are a clinical trial and patent expert.

Using the structured JSON record below, generate a 3-4 sentence summary.
ALLOWED: you may infer and interpret.
MARK clearly as "LLM inferred summary".

Record:
{text}
"""
summary_prompt = PromptTemplate(input_variables=["text"], template=SUMMARY_TEMPLATE)

def generate_summary(record):
    prompt = summary_prompt.format(text=json.dumps(record, indent=2))
    res = llm_summary.invoke(prompt)
    return res.content
