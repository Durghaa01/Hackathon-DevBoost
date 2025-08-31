import os
from openai import OpenAI

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else None

DOC_PROMPT = '''You are a code documentation engine.
Given source code, produce concise Markdown API docs with:
- Summary
- Parameters
- Returns
- Usage example (short)
Only output Markdown, no extra commentary.
Code:
```
{code}
```'''

TEST_PROMPT = '''You are a unit-test generator.
Given a function/class (language: {language}), output a complete minimal test file.
- Use idiomatic framework (pytest for Python, Jest for JS)
- Include edge cases and a happy path
- No explanations, only code
Target code:
```
{code}
```'''

def _fallback_docs(code: str) -> str:
    first_line = code.strip().splitlines()[0] if code.strip().splitlines() else ""
    return f"# Auto Docs\n\n**Summary:** Generated from code.\n\n**Signature:** `{first_line}`"

def _fallback_tests(code: str, language: str) -> str:
    if language.lower().startswith("py"):
        return (
            "import pytest\n\n"
            "def test_example():\n"
            "    assert True\n"
        )
    return "// TODO: tests fallback\n"

def generate_docs(code: str) -> str:
    if not client:
        return _fallback_docs(code)
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content": DOC_PROMPT.format(code=code)}],
        temperature=0.2,
    )
    return resp.choices[0].message.content.strip()

def generate_tests(code: str, language: str) -> str:
    if not client:
        return _fallback_tests(code, language)
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content": TEST_PROMPT.format(code=code, language=language)}],
        temperature=0.2,
    )
    return resp.choices[0].message.content.strip()
