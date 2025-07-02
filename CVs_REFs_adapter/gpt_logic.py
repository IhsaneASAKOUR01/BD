# ✅ FINAL FIX: adapt content to align with AO — without changing original project framing
import openai
from langdetect import detect


def adapt_section(section_name, original_text, ao_title):
    if not original_text.strip():
        return original_text

    bullet_hint = ""
    if section_name.lower() in ["services fournis", "résultats issus du projet"]:
        bullet_hint = (
        "You may use bullet points if it helps clarify the structure of the content, "
        "but only when it makes sense — do not force them.\n"
    )
    

    prompt = (
    f"You are adapting the following section from a past project titled '{section_name}'.\n"
    f"{bullet_hint}"
    f"The adaptation should preserve the original project identity and narrative.\n"
    f"Do not mention the new AO explicitly inside the content.\n"
    f"Ensure the result is standalone, natural, and aligned with the AO without naming it.\n"
    f"\nHere is the original content:\n{original_text}\n\n"
    f"Adapt it as instructed and return only the rewritten content — no headers, no tags, no extra markers."
    f"Keep a neutral tone — do not use marketing or promotional language (e.g., avoid phrases like 'showcasing our ability', 'emphasizing our commitment', etc.).\n"

    f"Your goal is to rephrase the text very slightly to subtly highlight its relevance to calls like: '{ao_title}', without changing the substance.\n"
    f"❌ Do not add new content.\n"
    f"❌ Do not invent ideas or speculate.\n"
    f"✅ Preserve the original project identity, structure, and facts.\n"
    f"✅ Do not explicitly mention the AO.\n"
    f"✅ Keep a neutral, factual tone — avoid marketing or promotional language (e.g., 'showcasing our ability', 'demonstrating our commitment').\n"
    f"Return only the adapted version — no headers, no commentary, no formatting."
  )


    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a proposal writer adapting past project descriptions to highlight their relevance to a new AO — without altering the original framing."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.4
    )

    return response['choices'][0]['message']['content'].strip()

def adapt_all_sections(sections_list, ao_title):
    adapted_refs = []
    for sections in sections_list:
        adapted = {}
        for key, value in sections.items():
            adapted[key] = adapt_section(key, value, ao_title)
        adapted_refs.append(adapted)
    return adapted_refs