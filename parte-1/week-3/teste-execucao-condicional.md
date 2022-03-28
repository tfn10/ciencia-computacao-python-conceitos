# Execução Condicional

### 1. O que é impresso ao digitar: 1 + 1 + 1 == 3?
- [ ] False.
- [ ] Não há garantias de que 1+1+1 == 3 é verdadeiro.
- [x] **True.**
- [ ] 6

### 2. Considere que a variável is_ready é do tipo booleano. Qual declaração está correta e é a forma mais sucinta de testar se is_ready é verdadeiro?
- [ ] if (is_ready  = True):
- [x] **if (is_ready):**
- [ ] if (not is_ready  = False):
- [ ] if (is_ready  == True):
- [ ] if (not is_ready  == False):

### 3. A linguagem Python permite o uso de funções matemáticas. Porém, não são nativas da linguagem e ficam localizadas em módulos externos.
### Para se usar a função sqrt, por exemplo, é necessário usar o seguinte comando:
- [ ] export math
- [ ] use math
- [x] **import math**
- [ ] include <math.h>

### 4. Considere o trecho de comandos abaixo. Qual o número da linha que será responsável pela saída (apresentação do resultado ao usuário) desse código?
~~~python
1.	texto = "computação"
2.	if len(texto) > 10:
3.	    print ("texto com mais de 10 caracteres")
4.	else:
5.	    print ("texto com 10 ou menos caracteres")
~~~
- [ ] nem linha 3, nem 5.
- [ ] linha 3.
- [ ] linhas 3 e 5.
- [x] **linha 5.**

### 5. A legislação de trânsito do Brasil permite que apenas pessoas com no mínimo 18 anos possam habilitar-se para dirigir.
### Considere que exista uma variável idade e você deverá testar se o usuário pode dirigir ou não e, em seguida, exibir uma mensagem correspondente à sua situação. Todas as opções abaixo dão o resultado correto, porém, qual delas utiliza melhor o recurso do if..else?
~~~python
I: if (idade < 18): 
      print ("Não pode tirar carteira de habilitação")
   if (idade >= 18):
      print ("Pode tirar a carteira de habilitação")
      
II: if (idade < 18): 
       print ("Não pode tirar carteira de habilitação")
    else: 
       print ("Pode tirar a carteira de habilitação")
       
III: if (idade < 18): 
          print (" Não pode tirar carteira de habilitação")
     else: 
         if (idade >= 18): 
               print ("Pode tirar a carteira de habilitação")

IV: if (idade < 18): 
       print ("Não pode tirar carteira de habilitação")
    else: 
      if (idade == 18): 
          print ("Pode tirar a carteira de habilitação")
      else: 
           if (idade > 18): 
               print ("Pode tirar a carteira de habilitação")
~~~
- [x] **II**
- [ ] III
- [ ] I
- [ ] Nenhuma das alternativas
- [ ] IV

### 6. Após executar a atribuição x = 10, qual afirmativa é verdadeira?
- [ ] not(x == 10)
- [ ] x != 10
- [ ] x == 20
- [x] **x != 20**

### 7. Qual(is) dos seguintes comandos é(são) equivalente(s) a x != y?
- [x] **not (x == y)**
- [ ] x > y and x < y
- [ ] x >= y or x <= y
- [ ] **x > y or x < y**

### 8. Considere a=0, b = 2 e c = 1. O que será impresso pelos comandos abaixo? (Primeiro ajuste corretamente a indentação.)
~~~python
if (a > 0):
    if (b > 0):
        print ("Tudo ok para decolagem!")
    else:
        print ("Tanque principal vazio; voando com combustível reserva!")
else:
    if (c > 0):
        print ("Foguete não tem piloto, mas há outros foguetes disponíveis!")
~~~
- [ ] Tanque principal vazio; voando com combustível reserva!
- [ ] Tudo ok para decolagem!
- [x] **Foguete não tem piloto, mas há outros foguetes disponíveis!**
- [ ] nada.
