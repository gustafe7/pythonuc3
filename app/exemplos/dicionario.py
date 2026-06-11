pessoa = {
    "nome": "Ana",
    "cpf": "123.456.789-01",
    "telefone": 21992856985
}
print(pessoa)
print(pessoa["cpf"])
pessoa["nome"] = "Luiz"
print(pessoa["nome"])
print(pessoa)

for chave, valor in pessoa.items():
    print(f"seu {chave} é {valor}")

pessoa.update({"nome": "Gustavo","cpf": "258.369.147-01", "telefone": 21992368745})
print(pessoa)