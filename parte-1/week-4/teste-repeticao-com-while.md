# Repetição com while

### 1. O que será impresso pelo trecho abaixo?
~~~python
x = 1
while (x < 4):
    x = x + 1
print ("x vale", x)
~~~
- [ ] x vale 2
- [ ] x vale 0
- [ ] x vale 3
- [ ] x vale 1
- [x] **x vale 4**

### 2. O que será impresso pelo trecho de código abaixo?
### Observação: na impressão um número ficará abaixo do outro e não ao lado.
~~~python
i = 0
while (i < 5):
  print (i) 
  i = i + 1
~~~
- [ ] 0 1 2 3 4 5
- [ ] 1 2 3 4 5   
- [x] **0 1 2 3 4**
- [ ] 2 3 4 5

### 3. O que será impresso pelo código abaixo? 
### Observação: na impressão um número ficará abaixo do outro e não ao lado.  
~~~python
i = 2
while i % 3 != 0:
    print(i)
    i += 2
~~~
- [ ] 2 3
- [ ] 2 4 6 8 10 …
- [ ] error.
- [x] **2 4**

### 4. Analise cuidadosamente o código abaixo e assinale a(s) alternativa(s) correta(s):
~~~python
count = 0
while (count < 10):
     # Ponto A
     print ("Olá...", count)
     count =  count + 1
     # Ponto B
# Ponto C
~~~
- [ ] count < 10 é sempre false no ponto B.
- [ ] count < 10 é sempre true no ponto C.
- [x] **count < 10 é sempre false no ponto C.**
- **[x] count < 10 é sempre true no ponto A.**
- [ ] count < 10 é sempre true no ponto B

### 5. O que será impresso quando o trecho abaixo for executado?
### Observação: na impressão um número ficará abaixo do outro e não ao lado. 
~~~python
i = 6
while (i > 0):          
    i = i - 3    
    print (i) 
~~~
- [ ] 3 0 -3
- [ ] 0 -3
- [ ] 6 3 0
- [ ] 6 3 
- [x] **3 0**
