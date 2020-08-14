#   Kinds of errors: syntax errors and exceptions

##  Syntax Errors   ##

    #   Um erro de sintaxe, muitas vezes é um erro na escrita do código. Comum ocorrer isso quando se esquece
    #   de colocar uma determinada vírgula, argumento, fechar parenteses, fechar chaves etc. 
    #   É a inobservância a sintaxe esperada pelo programa.

    #   Ex: while True print('Hello World!')

    #   No exemplo mencionado, falta-se o ':' após o True, indicando o começo do laço. 

##  Exceptions      ##

    #   Exceptions são erros detectados durante a execução do código. A verificação ocorre após a confirmação de
    #   que não há nenhum erro na expressão ou statement (sintaxe).

    #   >>> 200 * (1/0)
    #   Traceback (most recent call last):
    #     File "<stdin>", line 1, in <module>
    #   ZeroDivisionError: division by zero

    #   Existem diversas formas de exceptions: ZeroDivisionError, NameError, TypeError
