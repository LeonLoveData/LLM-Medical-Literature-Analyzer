from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from src.config import GROQ_API_KEY

llm_comp = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    groq_api_key=GROQ_API_KEY
)

COMP_TEMPLATE = """
You are a competitive intelligence expert.

Based on the following trial and patent summaries, generate a competitive landscape:
- Key competitors and MoA
- Efficacy & safety comparisons
- Clinical and patent positioning
- Strategic threat level (High/Medium/Low)
MARK clearly as "LLM inferred analysis".

Summaries:
{summaries}
"""

comp_prompt = PromptTemplate(
    input_variables=["summaries"],
    template=COMP_TEMPLATE
)


def generate_competitive_analysis(summaries):
    """Generate competitive intelligence analysis."""
    prompt = comp_prompt.format(summaries="\n\n".join(summaries))
    res = llm_comp.invoke(prompt)
    return res.content
