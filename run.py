import perplexity

# Criar cliente
client = perplexity.Client()

# Fazer uma pergunta
response = client.search("Explain quantum computing", mode="auto")

# Mostrar resposta
answer = response.get("answer")
if not answer:
    answer = (response.get("blocks") or [{}])[0].get("markdown_block", {}).get("answer", "")
print("Resposta:", answer or "No answer field found in response")
