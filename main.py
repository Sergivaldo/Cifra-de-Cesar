def modo():
    while True:
        modo_escolhido = input("Você deseja criptografar ou decriptografar ?")
        if modo_escolhido == "c" or modo_escolhido == "d" or modo_escolhido == "criptografar" or modo_escolhido == "decriptografar":
            return modo_escolhido
        else:
            print("Insira uma entrada válida")
        
        
def chave():
        alfabeto = "abcdefghijklmnopqrstuvwxyz"
        alfabeto = list(alfabeto)
        TAM_MAX_CHAVE = 26
        chave= ""    
        while True:   
            valor_chave = int(input("Informe o valor da chave: "))
            if valor_chave < 1 or valor_chave > TAM_MAX_CHAVE:
                print("Informe um valor de 1-26")
            else:
                lista_chave = alfabeto.copy()
                for i in range(1,valor_chave+1):
                    lista_chave.insert(0,lista_chave[-1])
                    lista_chave.pop()
                for letra in lista_chave:
                    chave += letra
            
                return chave 


def mensagem_traduzida(modo,mensagem,chave):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
                
    alfabeto = list(alfabeto)
    mensagem_traduzida = ""
    if modo == "c" or modo == "criptografar":
        for letra in mensagem:
            for j in range(len(chave)):
                if letra == chave[j]:
                    mensagem_traduzida += alfabeto[j]
                    break
                elif letra == chave[j].upper():
                    mensagem_traduzida += alfabeto[j].upper()
                    break
                elif letra != chave[j] and j == len(chave) - 1:
                    mensagem_traduzida += letra
            
    elif modo == "d" or modo == "decriptografar":
        for letra in mensagem:
            for j in range(len(alfabeto)):
                if letra == alfabeto[j]:
                    mensagem_traduzida += chave[j]
                    break
                elif letra == alfabeto[j].upper():
                    mensagem_traduzida += chave[j].upper()
                    break
                elif letra != alfabeto[j] and j == len(alfabeto) - 1:
                    mensagem_traduzida += letra
        
    return mensagem_traduzida
            

def main():
    escolha_modo = modo()
    mensagem = input("Entre com a mensagem: \n\n")
    escolha_chave = chave()
    print(f"\n\nMENSAGEM: \n\n {mensagem_traduzida(escolha_modo,mensagem,escolha_chave)}")

main()

