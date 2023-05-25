
# Analisador Léxico e Sintático em Python

Olá, pessoal! Nós somos Maurício e a Bárbara, dois estudantes de Ciência da Computação que adoram programar e aprender coisas novas. Neste projeto, nós criamos um analisador léxico e sintático em Python para reconhecer expressões de três endereços. Essas expressões são usadas em compiladores para gerar código intermediário entre a linguagem de alto nível e a linguagem de máquina.

## Como funciona o nosso projeto?

O nosso projeto usa a biblioteca `ply`, que é uma implementação do Lex e do Yacc em Python. O Lex é uma ferramenta que gera analisadores léxicos, que são responsáveis por dividir o código-fonte em tokens. O Yacc é uma ferramenta que gera analisadores sintáticos, que são responsáveis por verificar se o código-fonte segue as regras da gramática da linguagem.

Nós definimos os tokens e as expressões regulares para reconhecê-los usando o Lex. Os tokens são os elementos básicos da linguagem, como identificadores, números, operadores e delimitadores. As expressões regulares são padrões que descrevem como os tokens são formados.

Nós também definimos a gramática e as regras para analisar as expressões usando o Yacc. A gramática é um conjunto de produções que especificam como as expressões são construídas a partir dos tokens. As regras são funções que executam alguma ação quando uma produção é reconhecida.

O nosso analisador léxico e sintático recebe uma entrada de dados do usuário e verifica se ela é uma expressão de três endereços válida. Uma expressão de três endereços é uma atribuição de uma variável a uma operação entre dois termos. Um termo pode ser uma variável ou um número. Por exemplo:

```python
x = y + z;
a = b * 2;
c = 3 / d;
Se a entrada for válida, o nosso analisador léxico e sintático mostra na tela uma tabela de símbolos com os lexemas e os tokens encontrados na entrada. Um lexema é a sequência de caracteres que forma um token. Por exemplo:

Tabela de Símbolos
lexema	token
x	IDENTIFICADOR
=	ATRIBUICAO
y	IDENTIFICADOR
+	OPERADOR_+
z	IDENTIFICADOR
;	DELIMITADOR
Se a entrada não for válida, o nosso analisador léxico e sintático mostra na tela uma mensagem de erro indicando qual foi o problema encontrado na entrada. Por exemplo:

Erro: expressão de três endereços inválida: x = y z;
Erro sintático: z na posição 6
O nosso projeto também permite que o usuário digite várias entradas em sequência, até que ele digite “sair” para encerrar o programa.

Como executar o nosso projeto?
Para executar o nosso projeto, você precisa ter o Python 3 instalado no seu computador. Você também precisa instalar a biblioteca ply usando o comando:

pip install ply
Depois disso, você pode baixar o nosso código-fonte neste repositório e executá-lo usando o comando:

python analisador.py
Isso vai abrir um prompt onde você pode digitar as suas entradas de dados e ver os resultados na tela.

O que nós aprendemos com este projeto?
Nós aprendemos muito com este projeto, como:

Como usar a biblioteca ply para criar analisadores léxicos e sintáticos em Python.
Como definir tokens e expressões regulares usando o Lex.
Como definir gramáticas e regras usando o Yacc.
Como reconhecer expressões de três endereços usando um analisador léxico e sintático.
Como mostrar tabelas de símbolos e mensagens de erro na tela.
Como usar o markdown para formatar textos.
Nós esperamos que você tenha gostado do nosso projeto e que ele possa te ajudar a entender melhor como funcionam os compiladores. Se você tiver alguma dúvida, sugestão ou feedback, por favor, entre em contato conosco. Nós adoraríamos ouvir a sua opinião!

Obrigado pela sua atenção e até a próxima!
