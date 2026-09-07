import perplexity

# Criar cliente
client = perplexity.Client()

# Fazer uma pergunta
response = client.search("Explain quantum computing", mode="auto")

# Mostrar resposta
answer = response["blocks"][0]["markdown_block"]["answer"]
print("Resposta:", answer)
# print(answer)