Primeiramente, é preciso retirar do arquivo de entrada .csv o(s) atributo(s) classe, caso exista(m).
Para então executar o programa, deve-se executar pelo terminal o comando:

    python3 src/runme.py < arquivo_entrada > arquivo_saida flag

onde:
    arquivo_entrada é o arquivo .csv,
    arquivo_saida é o nome do arquivo txt onde se encontrará um vetor que indica em qual cluster cada um dos elementos foi colocado,
    flag é o número K de clusters desejados.

Exemplo do arquivo_saida de uma base com sete elementos e três clusters:
    0, 0, 1, 2, 1, 0, 2

O "0" indica que o primeiro, segundo e sexto elementos foram colocados no primeiro cluster.
O "1" indica que o terceiro e quinto elementos foram colocados no segundo cluster.
O "2" indica que o quarto e sétimo elementos foram colocados no terceiro cluster.

Exemplo do comando no terminal: 

    python3 src/runme.py < example.csv > out.txt 3


