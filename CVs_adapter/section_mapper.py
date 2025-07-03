import openai


def semantic_map_sections(resume_sections, template_text):
    """
    Uses GPT to understand and map sections semantically.
    template_text: the full raw text of the template
    resume_sections: list of strings, each resume section
    """
    resume_blocks = "\n\n".join([f"[{i}] {s[:500]}" for i, s in enumerate(resume_sections)])  # truncate for length

    prompt = f"""
You are a document understanding assistant. The user gives you:

1. A resume split into sections (with indices)
2. A resume template in raw text

Your task is to match sections from the resume to the appropriate part of the template, based on meaning and content (not just the title). Return a JSON object that maps template section descriptions to resume section indices.

### RESUME SECTIONS:
{resume_blocks}

### TEMPLATE:
{template_text}

Return only the JSON. Example:
{{
  "Education": 1,
  "Work Experience": 0,
  "Skills": 2
}}
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return eval(response.choices[0].message['content'])

def gpt_fill_template_as_text(template_text, resume_text):
    prompt = f"""
You are a document assistant. You will fill a resume template using real resume information.

Return the full filled-in resume as plain text, replacing any placeholders or gaps.

### TEMPLATE:
{template_text}

### RESUME INFO:
{resume_text}
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response.choices[0].message["content"]

def gpt_fill_as_dict(template_text, resume_text):
    prompt = f"""
    You are a CV filling assistant.

    You are given:
    1. A CV template with labels and instructions (text within curly braces {{}}).
    2. A resume as raw text.

    Your task:
    - Return a Python dictionary with keys exactly as they appear in the template (including all instructions in curly braces {{}}), except always ignore the "Certification" section.
    - Each key’s value should clearly and concisely contain the relevant resume information to fill that section.
    - For tables, provide lists of lists (headers included in first list).

    ### TEMPLATE:
    {template_text}

    ### RESUME:
    {resume_text}

    Return only valid Python dictionary. No additional text.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    return eval(response.choices[0].message["content"])
