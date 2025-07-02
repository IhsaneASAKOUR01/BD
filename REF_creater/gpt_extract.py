import openai
import time
import json
from openai import RateLimitError

openai.api_key = "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"

def extract_field(report_text, fields):
    def split_text(text, max_tokens=3000):
        paragraphs = text.split("\n")
        chunks, current_chunk = [], []
        current_length = 0

        for para in paragraphs:
            length = len(para.split())
            if current_length + length > max_tokens:
                chunks.append("\n".join(current_chunk))
                current_chunk = [para]
                current_length = length
            else:
                current_chunk.append(para)
                current_length += length

        if current_chunk:
            chunks.append("\n".join(current_chunk))

        return chunks

    def build_prompt(text_chunk, fields):
        prompt = (
            "Tu es un expert analyste. Lis attentivement le rapport suivant et remplis les champs demandés.\n"
            "Chaque réponse doit être détaillée, bien rédigée et autonome.\n"
            "Les champs 'Services fournis' et 'Résultats issus du projet' doivent commencer par une phrase d’introduction complète (une ou deux lignes), puis continuer avec des puces '•' bien développées. Ne renvoie jamais de listes ou de tableaux JSON."
            "Donne beaucoup de contenu utile, précis, en français, même par inférence.\n\n"
            "Champs :\n"
        )

        for field in fields:
            prompt += f"- {field}\n"

        prompt += (
            "\nRéponds sous forme d’un objet JSON, avec chaque valeur de champ en tant que texte structuré.\n\n"
            f"Rapport :\n{text_chunk}"
        )
        return prompt

    chunks = split_text(report_text)
    final_data = {field: "" for field in fields}

    for chunk in chunks:
        prompt = build_prompt(chunk, fields)
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.4
            )
            content = response["choices"][0]["message"]["content"].strip()
            chunk_data = json.loads(content)
            for field in fields:
                if not final_data[field] and chunk_data.get(field):
                    final_data[field] = chunk_data[field]
        except Exception as e:
            print(f"Error: {e}\nPrompt:\n{prompt[:1000]}...")
        time.sleep(2)

    return final_data


def force_field_completion(fields):
    # Fallback if GPT missed key fields, you can map defaults or guesses
    if not fields["Catégorie de service"]:
        fields["Catégorie de service"] = "Études de marché"
    if not fields["Services fournis"]:
        fields["Services fournis"] = "Analyse de marché, entretiens avec les acteurs clés, recommandations"
    if not fields["Résultats issus du projet"]:
        fields["Résultats issus du projet"] = "Identification d’opportunités de financement vert et recommandations stratégiques"
    return fields
