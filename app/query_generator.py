# query_generator.py
import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

def gerar_sql(pergunta_usuario):
    prompt = f"Converta isso para uma query SQL: {pergunta_usuario}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response['choices'][0]['message']['content']



##pip install openai transformers torch spacy
