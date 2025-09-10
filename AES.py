def criptografar(texto, chave):
    pass

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