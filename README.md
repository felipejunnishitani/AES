# AES - Introdução à Criptografia

## Grupo

* Anne Mari Suenaga Sakai – RA: 822304  
* Felipe Jun Nishitani – RA: 822353 
* Lucas Pereira Goes – RA: 822938 

---

## Descrição do projeto

Este projeto consiste em uma implementação do zero em Python do algoritmo de criptografia AES (Advanced Encryption Standard), especificamente para chaves de 128 bits. O objetivo é demonstrar o funcionamento interno do algoritmo, incluindo a expansão de chave e todas as transformações de rodada (SubBytes, ShiftRows, MixColumns e AddRoundKey).

A implementação utiliza a biblioteca NumPy para facilitar a manipulação das matrizes de estado, que são fundamentais para o funcionamento do AES.


## Como Executar
1. **Certifique-se de que você tem o Python e o NumPy instalados.**
    * Para instalar a biblioteca NumPy, utilize o pip:
        ```sh
        pip install numpy
        ```
2. **Salve o código do projeto em um arquivo, por exemplo, AES.py.**
3. **Execute o script através do terminal:**
    ```sh
    python AES.py
    ```
4. **Siga as instruções:** O programa solicitará a mensagem a ser criptografada e a chave.

# Importante:

* **A mensagem pode ter no máximo 16 caracteres (ou 16 bytes em UTF-8).**
* **A chave deve ter exatamente 16 caracteres.**


# Entrada do Usuário:
* **Mensagem**: Uma string em texto plano.
* **Chave**: Uma string de 16 caracteres.

# Saída do programa
* **Texto codificado** em formato hexadecimal.
* **Texto decodificado** em formato de string.


## Estrutura do Código
* **main():** Controla a interface com o usuário, captura as entradas e exibe os resultados.
* **criptografar():** Realiza o processo de cifragem.
* **descriptografar():** Realiza o processo de decifragem.
* **expandir_chave():** Gera as chaves de cada rodada.
* **mix_colunas():** Função genérica que aceita qualquer matrix multiplicativa constante 4x4 bytes, que realiza a transformação de embaralhamento de colunas tanto para a criptografia quanto para a descriptografia.
* **gmul():** Função auxiliar para a multiplicação no corpo finito GF(2^8), necessária para o MixColumns.
* **Constantes:** S_BOX, INV_S_BOX, RCON, MIX_COL_MATRIX, INV_MIX_COL_MATRIX armazenam as tabelas e matrizes fixas usadas pelo algoritmo.
