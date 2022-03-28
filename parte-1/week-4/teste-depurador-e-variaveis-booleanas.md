# Depurador e Variáveis Booleanas

### 1. Para que servem os indicadores de passagem?
- [ ] Servem para armazenar uma sequência de números, porém somente se eles estiverem em ordem crescente.
- [ ] Servem para indicar se o número anterior é menor que o próximo número da sequência.
- [ ] Servem para indicar se determinada sequência de número está ou não em ordem crescente
- [x] **Servem para indicar se uma determinada condição passou a ser verdadeira ou não, sendo usada em um laço de repetição**

### 2. O código abaixo utiliza indicador de passagem? Se sim, qual é a variável que está fazendo esse papel? 
~~~python
teste = True
while teste:
    x = int(input("Digite um número: "))
    if x < 0:
        teste = False
~~~
- [ ] Sim. A variável x.
- [ ] Não.
- [x] **Sim. A variável teste.**

### 3. Para que serve um depurador?
- [ ] Para encontrar erros de sintaxe no código
- [ ] Todas as opções estão erradas
- [x] **Para encontrar erros de lógica no código**
- [ ] Para compilar o programa
- [ ] É uma ferramenta usada para escrever o código fonte

### 4. Assinale a(s) alternativa(s) CORRETA(S) sobre o depurador Python apresentado no vídeo:
- [x] **Breakpoints podem ser retirados quando não são mais necessários**
- [ ] O GO serve para executar o programa passo a passo
- [x] **Depurador é utilizado quando se deseja descobrir o erro existente que faz o programa não apresentar o resultado correto** 
- [x] **OVER, ao ser acionado, executa uma linha inteira**

### 5. reakpoint serve para ___________________.
- [ ] mostrar ao usuário onde ele deve parar o programa
- [ ] marcar a linha que você não quer que seja executada
- [x] **marcar um ponto de parada na execução do programa, sendo utilizado junto com o depurador**
- [ ] marcar pontos dentro do programa onde o depurador encontrou erros
