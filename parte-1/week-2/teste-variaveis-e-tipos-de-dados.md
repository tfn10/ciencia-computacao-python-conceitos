# Variáveis e tipos de dados

### 1. Qual o tipo de dado armazenado na variável x pelo comando abaixo?
~~~python
x = input ("Qual a idade? ")
~~~
- [ ] inteiro, pois considera apenas a idade completa do usuário
- [x] **a função input sempre devolve um string**
- [ ] float (número real), pois considera a idade fracionada do usuário
- [ ] booleano, pois o sinal de igualdade é operador relacional

### 2. Quais os valores finais das variáveis a e b, se o usuário digitar 1 e 2, respectivamente?
~~~python
a = int(input("Qual o valor de a? "))
b = int(input("Qual o valor de b? "))
a = b
b = a
print(a)
print(b)
~~~
- [ ] a e b serão 1
- [x] **a e b serão 2**
- [ ] a será 1 e b será 2
- [ ] a será 2 e b será 1

### 3. Quais os valores finais das variáveis a e b, se o usuário digitar 1 e 2, respectivamente?
~~~python
a = int(input("Qual o valor de a? "))
b = int(input("Qual o valor de b? "))
aux = a
a = b
b = aux
print(a)
print(b)
~~~
- [ ] a será 1 e b será 2
- [ ] a e b serão 2
- [x] **a será 2 e b será 1**
- [ ] a e b serão 1
