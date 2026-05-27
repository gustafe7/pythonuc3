import os

palavra_secreta = "python"
letras_acertadas = ["_", "_", "_", "_", "_", "_"] # Uma para cada letra de 'python'
tentativas = 6

while tentativas > 0 and "_" in letras_acertadas:
    os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela
    
    print("=== JOGO DA FORCA SIMPLES ===")
    print("DICA: Programação.\n")
    print(f"Palavra: {' '.join(letras_acertadas)}")
    print(f"Tentativas restantes: {tentativas}")
    
    chute = input("\nDigite uma letra: ").lower()

   
    if chute in palavra_secreta:
        
        if chute == "p": letras_acertadas[0] = "p"
        if chute == "y": letras_acertadas[1] = "y"
        if chute == "t": letras_acertadas[2] = "t"
        if chute == "h": letras_acertadas[3] = "h"
        if chute == "o": letras_acertadas[4] = "o"
        if chute == "n": letras_acertadas[5] = "n"
    else:
        tentativas -= 1

# 3. Final do jogo
os.system('cls' if os.name == 'nt' else 'clear')
if "_" not in letras_acertadas:
    print("Você ganhou! A palavra era PYTHON.")
else:
    print("Você perdeu!")