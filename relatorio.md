SME0110 - Programação Matemática
# Trabalho de Otimização Inteira

Alunos:  
Eduardo Henrique Porto Silva - 
Gustavo Sampaio Lima - 12623992  
Pedro Rossi Silva Rodrigues - 11871775
Vitor Amorim Fróis - 12543440
Thaís Ribeiro Lauriano - 12542518 

## Tarefa 1

## Tarefa 2

## Tarefa 3

## Tarefa 4SME0110 - Programação Matemática
# Trabalho de Otimização Inteira

Alunos:  
Eduardo Henrique Porto Silva  
Gustavo Sampaio Lima - 12623992  
Pedro Rossi da Silva Rodrigues  
Vitor Amorim Fróis  
Thaís Ribeiro Lauriano - 12542518

## Tarefa 1

## Tarefa 2

## Tarefa 3

## Tarefa 4

## Tarefa 5 - Aplicação

A aplicação escolhida para o problema de localização de facilidades foi a determinação de assistências técnicas de uma empresa de eletrodomésticos.  
Como esta aplicação se trata de um problema
logístico de uma empresa que entrega produtos para todo o Brasil, cada cidade será identificada como um cliente $j$.  
Ademais, as facilidades são todas assistências
técnicas da empresa. Assim, cada cliente será representado por uma cidade e pode ser alocado para uma ou mais facilidades cujas capacidades são limitadas.  
O modelo matemático que usaremos é o mesmo descrito no enunciado do trabalho, e todos os parâmetros do modelo são apresentados na Tabela 1.

| Parâmetro      | Significado |
| :-----------: | :-----------: |
| $i$     | índices de clientes (cidades)|
|$j$   | índices de assistências técnicas (ATs)|
| $f_i$     | custo fixo da $AT_i$|
| $c_ij$     | custo de transporte da $AT_i$ para a cidade $j$|
|$d_j$   | demanda da cidade $j$|
| $Cap_i$     | capacidade da $AT_i$|
|$n$   | quantidade de ATs abertas|     
|$m$   | quantidade de cidades atendidas|
Tabela 1 – Parâmetros da aplicação

Esse modelo também usa duas variáveis de decisão, uma binária ($y_i$) e uma livre que são as
seguintes:  

$y_i$ = 1 se a assistência i for aberta e 0 caso contrário  
$x_{ij}$ = 1 se a assistência i atender a cidade j e 0 caso contrário

$ min\ \Sigma_{i=1}^n f_i \cdot y_i + \Sigma_{i=1}^n\Sigma_{j=1}^m c_{ij} \cdot x_{ij}\ $ (1)


sujeito à:

>>  $\Sigma_{i=1}^n x_{ij} = 1 \ \ j = 1,..., m\ $  (2) 

>>  $\Sigma_{j=1}^m d_j \cdot x_{ij} \le Cap_i \ \ i = 1, ..., n\ $ 
  (3) 

>>  $x_{ij} \le y_i \ \ i = 1, ..., n; \  j = 1,..., m\ $(4)

>> $y_i \in \{0,1\}\ $(5)

>>  $0 \le x_{ij} \le 1 \ $(6)

A função objetivo (1) tem como finalidade minimizar a soma dos custos fixos de cada AT aberta mais a soma dos custos de transporte das assistências técnicas para as cidades atendidas. 
A restrição (2) certifica que todas as cidades atendidas tiveram suas demandas supridas.
As restrições (3) e (4) garantem que nenhuma das ATs tenha su capacidade extrapolada, e as restrições (5) e (6) determinam o domínio das variárveis $y_i$ e $x_{ij}$, respectivamente.
Por fim, obtêm-se quais assistências técnicas devem ser abertas para que os custos totais sejam minimizados.

Referência: [Avaliação de cenários para o problema de localização de facilidades
determinando centros de distribuição de uma empresa de
eletrodomésticos](https://aprepro.org.br/conbrepro/2019/anais/arquivos/10192019_191014_5dab8eee2b4dc.pdf)


## Tarefa 6 - Toy Problem



## Tarefa 5

A aplicação escolhida para o problema de localização de facilidades foi a determinação de assistências técnicas de uma empresa de eletrodomésticos.  
Como esta aplicação se trata de um problema
logístico de uma empresa que entrega produtos para todo o Brasil, cada cidade será identificada como um cliente $j$.  
Ademais, as possíveis facilidades são todas assistências
técnicas da empresa, que consistem em mais de 400 unidades.
A metodologia utilizada para o presente problema é localização de facilidades com capacidade limitada e fonte única. Assim, cada cliente será representado por uma cidade e deve ser
alocado para exatamente uma facilidade cujas capacidades são limitadas.  
$J$ é o conjunto dos clientes $j$, ou seja, as cidades as quais a empresa entrega produtos. O índice $i$ representa todos os candidatos a serem escolhidos para serem transformados em assistências técnicas. A representação $D_j$ é a demanda de produtos devolvidos de cada cidade, e $q_i$ a capacidade da assistência técnica $i$.  
Os custos também devem ser considerados, assim, $c_{ij}$ é o custo relacionado com o transporte dos produtos do cliente $j$ até a assistência técnica $i$, e $f_i$ e $V_i$ são o custo fixo e o custo variável da assistência técnica $i$, respectivamente.  
A quantidade de facilidades abertas é representada por p, e os parâmetros do modelo são apresentados na Tabela 1.

| Parâmetro      | Significado |
| ----------- | ----------- |
| $i$     | índices de clientes (cidades)|
|$j$   | índices de assistências técnicas (AT)|
| $f_i$     | custo fixo da $AT_i$|
|$V_i$   | cuto variável de manuseio de itens na $AT_i$|
| $c_ij$     | custo de transporte da $AT_i$ para a cidade $j$|
|$D_j$   | demanda da cidade $j$|
| $Q_i$     | capacidade da $AT_j$|
|$p$   | quantidade de ATs abertas|
|$M$   | número muito grande|
Tabela 1 – Parâmetros da aplicação

Esse modelo também usa as três variáveis de decisão, duas binárias e uma livre que são as
seguintes:  
$y_i$ = { 1 se a assistência i for aberta e 0 caso contrário  
$x_{ij}$ = { 1 se a assistência i servir a cidade j e 0 caso contrário  
$q_i$ = capacidade utilizada na assistência i  

O modelo matemático é o seguinte:  
$ min\ \Sigma_{i=1}^{p}$
𝑀𝑖𝑛∑𝑓𝑖
𝑖∈𝐼
𝑦𝑖 + ∑𝑉𝑖𝑞𝑖
𝑖∈𝐼
+ ∑∑𝑐𝑖𝑗
𝑗∈𝐽
𝐷𝑗 𝑥𝑖𝑗
𝑖∈𝐼
(1)
𝑆𝑢𝑗𝑒𝑖𝑡𝑜 à:
𝑞𝑖 ≤ 𝑄𝑀𝑎𝑥𝑖
(2)
∑𝑥𝑖𝑗
𝑖∈𝐼
= 1, ∀ 𝑗 ∈ 𝐽, (3)
∑𝑦𝑖
𝑖∈𝐼
= 𝑝, (4)
∑𝐷𝑗𝑥𝑖𝑗
𝑗∈𝐽
= 𝑞𝑖
, ∀ 𝑖 (5)
∑𝑥𝑖𝑗
𝑗∈𝐽
≤ 𝑀 𝑦𝑖
, ∀ 𝑖 (6)
𝑥𝑖𝑗 ∈ 𝐵
|𝐼||𝐽|
, 𝑦𝑖 ∈ 𝐵
|𝐼|
, 𝑞𝑖 ∈ 𝑅 (7)
A função objetivo (1) tem como finalidade minimizar os custos fixos dos centos de
distribuições, os custos relacionados às atribuições dos clientes até as facilidades e os custos
variáveis de cada CD. A restrição (2) garante que a capacidade utilizada no CD i é menor que
a capacidade total do CD. A restrição (3) garante que cada cliente j é designado a apenas 1
facilidade. E a restrição (4) garante que apenas p facilidades serão escolhidas. A restrição (5)
informa a capacidade do CD e a (6) verifica se o CD i está sendo utilizado. A restrição (7) indica
os tipos de variáveis.
O modelo deve ser resolvido três vezes, levando em consideração as diferentes quantidades
de CDs desejados pela empresa para se investir, ou seja, p poderá assumir os valores 3, 4 ou
5. Por fim, obtêm-se quais cidades devem ter seus produtos devolvidos para cada CD e quais
assistências técnicas devem ser transformadas em CDs.

Referência: [Avaliação de cenários para o problema de localização de facilidades
determinando centros de distribuição de uma empresa de
eletrodomésticos](https://aprepro.org.br/conbrepro/2019/anais/arquivos/10192019_191014_5dab8eee2b4dc.pdf)


## Tarefa 6