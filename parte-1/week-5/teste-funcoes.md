# Funções

### 1. Qual será o resultado apresentado pelo programa abaixo?
~~~python
multiplica (a, b):
    return a * b

print(multiplica(4,5))
~~~
- [ ] multiplica(4,5)
- [x] **Dará um erro de sintaxe**
- [ ] 4 * 5 = 20
- [ ] 20

### 2. O que o código abaixo irá imprimir?
~~~python
def troca(x, y):
    aux = x
    x = y
    y = aux

x = 10
y = 20
troca (x,y)
print("x =", x,"e y =",y)
~~~
- [x] **x = 10 e y = 20**
- [ ] x = 20 e y = 10  
- [ ] Todas as opções estão erradas
- [ ] x = 20 e y = 20
- [ ] x = 10 e y = 10

### 3. Assinale qual (ou quais) das opções abaixo apresenta a função que retorna a soma dos comprimentos de 3 palavras ou frases:

<input type="checkbox" disabled />

~~~python
def total_Caracteres (x, y, z):
    return sum(len(x)+len(y)+len(z))
~~~

<input type="checkbox" disabled />

~~~python
def total_Caracteres (x, y, z):
    return len(x,y,z)
~~~

<input type="checkbox" disabled />

~~~python
def total_Caracteres (x, y, z):
    return sum(len(x,y,z))
~~~

<input type="checkbox" disabled checked />

~~~python
def total_Caracteres (x, y, z):
    return len(x)+len(y)+len(z)
~~~~

### 4. O quê a função abaixo devolve? O que é math?
~~~python
import math

def suspense(x):
    return math.sqrt(x)
~~~
- [ ] Todas as opções estão erradas.
- [x] **Devolve a raiz quadrada de x. "math" é um módulo**
- [ ] Devolve a raiz quadrada de x. "math" é uma função  
- [ ] Devolve o quadrado de x. "math" é um módulo 
- [ ] Devolve o quadrado de x. "math" é uma função

### 5. Se você tivesse que resolver o seguinte exercício:
### "Desenvolva uma função que devolva um número lido, maior que zero", qual(is) das opções abaixo resolveria(m) seu problema?

<input type="checkbox" disabled>

~~~python
leitura():
    x = -1
    while x > 0:
        x = int(input("Digite um valor: "))
    return x
~~~

<input type="checkbox" disabled checked>

~~~python
def leitura():
    x = -1
    while x <= 0:
        x = int(input("Digite um valor: "))
    return x
~~~

<input type="checkbox" disabled>

~~~python
leitura():
    x = -1
    while x <= 0:
        x = int(input("Digite um valor: "))
    return x
~~~

<input type="checkbox" disabled>

~~~python
def leitura():
    x = -1
    while x > 0:
        x = int(input("Digite um valor: "))
    return x
~~~

<input type="checkbox" disabled checked>

~~~python
def leitura():
    x = int(input("Digite um valor: "))
    while x <= 0:
        x = int(input("Digite um valor: "))
    return x
~~~

### 6. Assinale as afirmações CORRETAS:

- [x] **Parâmetros de uma função são valores que ela recebe para trabalhar**
- [x] **Em código bem feito, o nome da função deve representar a tarefa que ela irá executar**
- [x] **A função pode ou não devolver valor**
- [x] **return é usado para a função devolver um determinado valor para quem a chamou**
- [x] **A função pode receber ou não parâmetros**
