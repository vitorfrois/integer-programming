### SME0110 - Programação Matemática
# Trabalho de Otimização Inteira

Alunos:  
Eduardo Henrique Porto Silva - 

Gustavo Sampaio Lima - 12623992  

Pedro Rossi Silva Rodrigues - 11871775

Vitor Amorim Fróis - 12543440

Thaís Ribeiro Lauriano - 12542518 

## Tarefa 1
Para a tarefa 1 utilizamos a linguagem Python em conjunto a biblioteca Pulp. Todo o código para a resolução dos problemas está no arquivo `facilities_solver.py`. Com a ajuda de classes conseguimos ler o arquivo de instâncias, e armazenar o conteúdo em variáveis com a função abaixo:
``` python
def read_problem_instance(self, filename: str):
```
e logo em seguida escrevemos o problema de forma pythonica com a classe `pulp.LpProblem()`. Abaixo estão listados os principais eventos da função


Criando as variáveis de decisão $x$ e $y$.
```python
def create_minimize_pulp_problem_1(self) -> LpProblem:
  prob = LpProblem("Facilities", LpMinimize)

  x_vars = {}
  y_vars = {}

  for i in range(0, self.n):
      y_vars[get_index_string(i)] = LpVariable(f'y_{get_index_string(i)}', 0, 1, cat='Integer')
      for j in range(0, self.m):
          x_vars[get_index_string(i, j)] = LpVariable(f'x_{get_index_string(i, j)}', 0, 1)
```

Adicionando a função objetivo ao nosso problema.
```python
prob += (
  lpSum([self.f[i] * y_vars[get_index_string(i)] for i in range(self.n)]) +
  lpSum([(self.c)[j][i] * x_vars[get_index_string(i, j)] for i in range(self.n) for j in range(self.m)]),
  "Objective Func",
)
```

Por fim adicionamos as duas restrições descritas no trabalho.
```python
for j in range(self.m):
  prob += (
      lpSum([x_vars[get_index_string(i, j)] for i in range(self.n)]) == 1,
      f"Demanda 1.{j}",
  )

for i in range(self.n):
  prob += (
      lpSum([(self.d[j] * x_vars[get_index_string(i, j)]) for j in range(self.m)]) <= self.cap[i] * y_vars[get_index_string(i)],
      f"Demanda 2.{i}"
  )
```

## Tarefa 2
Para a segunda tarefa, vamos utilizar os mesmos valores da instância. Por conta da pequena diferença nas restrições, vamos criar uma nova função, chamada `create_minimize_pulp_problem_2()`, explicada abaixo:

Criamos o problema `LpProblem` como na primeira tarefa. Dessa vez vamos garantir que $y \in [0, 1]$ ao omitir `cat='Integer'` nos parâmetros da função `LpVariable()`.
```python
def create_minimize_pulp_problem_2(self) -> LpProblem:
  prob = LpProblem("Facilities", LpMinimize)

  x_vars = {}
  y_vars = {}

  for i in range(0, self.n):
    y_vars[get_index_string(i)] = LpVariable(f'y_{get_index_string(i)}',0,1)
      for j in range(0, self.m):
        x_vars[get_index_string(i, j)] = LpVariable(f'x_{get_index_string(i, j)}', 0, 1)
```

E adicionamos uma restrição extra
```python
for i in range(self.n):
  for j in range(self.m):
    prob += (
      x_vars[get_index_string(i, j)] <= y_vars[get_index_string(i)],
      f"Demanda 3.{i}_{j}"
    )
```

Além disso, o trecho de código que especifica a criação das variáveis em :
```python
def create_minimize_pulp_problem_1(self) -> LpProblem:
  prob = LpProblem("Facilities", LpMinimize)

  x_vars = {}
  y_vars = {}

  for i in range(0, self.n):
      y_vars[get_index_string(i)] = LpVariable(f'y_{get_index_string(i)}', 0, 1, cat='Integer')
      for j in range(0, self.m):
          x_vars[get_index_string(i, j)] = LpVariable(f'x_{get_index_string(i, j)}', 0, 1)
```

foi alterado retirando a necessidade de que Yi assuma valores inteiros, resultando na alteração pela linha a seguir:
```python
y_vars[get_index_string(i)] = LpVariable(f'y_{get_index_string(i)}', 0, 1)
```

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

$min\ \Sigma_{i=1}^n f_i \cdot y_i + \Sigma_{i=1}^n\Sigma_{j=1}^m c_{ij} \cdot x_{ij}\$ (1)

sujeito à:

$\Sigma_{i=1}^n x_{ij} = 1 \ \ j = 1,..., m\$  (2) 

$\Sigma_{j=1}^m d_j \cdot x_{ij} \le Cap_i \ \ i = 1, ..., n\ $ 
  (3) 

$x_{ij} \le y_i \ \ i = 1, ..., n; \  j = 1,..., m\ $(4)

$y_i \in \{0,1\}\ $(5)

$0 \le x_{ij} \le 1 \ $(6)

A função objetivo (1) tem como finalidade minimizar a soma dos custos fixos de cada AT aberta mais a soma dos custos de transporte das assistências técnicas para as cidades atendidas. 
A restrição (2) certifica que todas as cidades atendidas tiveram suas demandas supridas.
As restrições (3) e (4) garantem que nenhuma das ATs tenha su capacidade extrapolada, e as restrições (5) e (6) determinam o domínio das variárveis $y_i$ e $x_{ij}$, respectivamente.
Por fim, obtêm-se quais assistências técnicas devem ser abertas para que os custos totais sejam minimizados.

Referência: [Avaliação de cenários para o problema de localização de facilidades
determinando centros de distribuição de uma empresa de
eletrodomésticos](https://aprepro.org.br/conbrepro/2019/anais/arquivos/10192019_191014_5dab8eee2b4dc.pdf)


## Tarefa 6 - Toy Problem

A descrição do modelo está descrito na tarefa 5.
O arquivo que representa os valores de cada variável está presente em toy_problem_instance/toy_problem.txt
A partir dos dados criados, codificamos o arquivo toy_problem_solver.py que basicamente é uma descrição semelhante ao efetuado na tarefa 1 do presente projeto.

Sendo assim, rodando o código utilizando SCIP obtemos os seguintes resultados:

