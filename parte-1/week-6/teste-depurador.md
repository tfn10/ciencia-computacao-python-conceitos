# Depurador

### 1. Sobre as formas de execução dentro do depurador, é certo afirmar que: (assinale todas as alternativas CORRETAS)
- [x] **Go: executa o programa inteiro
Não é possível mostrar a execução passo a passo de uma função**
- [ ] Todas as demais alternativas estão erradas
- [x] **OVER: executa uma linha inteira e se nela tiver uma chamada de função, ela é executada por completo, de uma só vez, sem mostrar o passo a passo dentro dela**
- [x] **STEP: executa uma linha inteira e se nela tiver uma chamada de função, ele entra na função e executa passo a passo**

### 2. O quê acontece se eu não selecionar a opção “source” do depurador?
- [ ] O depurador não mostrará os valores das variáveis durante a execução do código
- [ ] O depurador não irá executar
- [x] **O depurador não marcará dentro do código fonte a linha que está sendo executada**
- [ ] O depurador
não dará novas opções de fontes de dados  

### 3. O comando print é uma função.
### Se eu estiver executando a linha que chama essa função, como por exemplo print (“teste”), qual o botão que deverá ser acionado no depurador para entrar nessa função e mostrar passo a passo sua execução?
- [ ] Over
- [ ] Quit
- [ ] Go
- [x] **Step**

### 4. Analise o programa abaixo e assinale as afirmações CORRETAS: 
~~~python
def soma(num1, num2, num3):
    return num1 + num2 + num3

def main():
    n1 = float(input("Primeiro número = "))
    n2 = float(input("Segundo número = "))
    n3 = float(input("Terceiro número = "))
    print (soma(n1, n2, n3))

main()
~~~
- [x] **O programa começará a ser executado pela função main**
- [x] **As variáveis num1, num2 e num3 só aparecerão no depurador quando a função soma estiver sendo executada**
- [ ] O programa começará a ser executado pela função soma
- [ ] As variáveis n1, n2 e n3 são globais, ou seja, aparecerão no depurador independente
de qual função estará sendo executada
- [ ] Todas as alternativas estão INCORRETAS
- [ ] Esse programa não será executado porque a função soma está sendo chamada dentro de um print. Dará erro de sintaxe
