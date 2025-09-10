import numpy as np

def criptografar(texto, chave):
    # Inicialização
    texto_bytes = texto.encode('utf-8') # transformação da string em bytes
    texto_bytes = texto_bytes.ljust(16, b'\x00') # preenche com byte zero

    estado = np.zeros((4,4), dtype=np.uint8) # inicialização matriz 4x4 de bytes

    k = 0
    for i in range(4):
        for j in range(4):
            estado[j, i] = texto_bytes[k] # preenche matriz por coluna
            k += 1


    # Rodada inicial -> operação xor

    # Rodadas intermediárias
        # Substituição dos bytes

        # Deslocamento das linhas

        # Mix de colunas
        
        # Adicionar roundkey

    # Rodada final

def descriptografar(texto, chave):
    pass


def main():
    texto = input("Insira a mensagem:")
    chave = input("Insira a chave:")

    print("Mensagem criptografada:")
    criptografar(texto, chave)

    print("Mensagem descriptografada:")
    descriptografar(texto, chave)


    

if __name__ == "__main__":
    main()