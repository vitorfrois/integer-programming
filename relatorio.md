### SME0110 - Programação Matemática
# Trabalho de Otimização Inteira

Alunos:  
Eduardo Henrique Porto Silva - 11796656

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

Para entender por que algumas modificações como a citada no arquivo de descrição do projeto pode impactar nos resultados (positiva ou negativamente) podemos analisar o impacto que uma relaxação linear em variáveis pode causar.
A relaxação linear de variáveis binárias em problemas de programação inteira, como o problema de localização de facilidades que estamos analisando, é uma técnica comum na otimização. A ideia é substituir as restrições binárias (0 ou 1) por restrições lineares que permitem que as variáveis assumam valores reais entre 0 e 1, se tornando assim uma variável contínua. Essa relaxação torna o problema mais fácil de resolver computacionalmente, pois métodos de otimização linear são geralmente mais eficientes e robustos do que métodos para otimização inteira.

No entanto, é importante notar que a solução relaxada pode não ser uma solução viável para o problema original, pois ela permite valores fracionários para as variáveis binárias, o que pode não fazer sentido do ponto de vista prático. Portanto, após a resolução do problema relaxado, é comum aplicar técnicas adicionais, como arredondamento ou cortes, para obter uma solução inteira que seja mais próxima da solução ótima do problema original.

### Especificações da Máquina
Para as próximas tarefas vamos rodar as instâncias do problema utilizando máquina local,
que possui as seguintes especificações:
- Processador Intel Core i5-9300HF
- Memória 8GB

## Tarefa 3
Resolveremos as instâncias utilizando o solver SCIP
Instância | Primal | Dual | Gap | Status | Tempo (s)
| :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: |
| 1 | +6.90925774582678e+04 | +6.90925774582678e+04 | 0 | Solved | 256.0
| 2 | +7.60517489256715e+04 | +7.59961783569572e+04 | 0.0007 | Time Limit Exceeded | 297.0
| 3 | +1.14961783546098e+05 | +1.14700876543287e+05 | 0.002 | Time Limit Exceeded | 317.8
| 4 | +1.35371653758398e+05 | +1.34944696278956e+05 | 0.003 | Time Limit Exceeded | 308.4
| 5 | +1.67361563768499e+05 | +1.63416745367824e+05 | 0.02 | Time Limit Exceeded | 347.9


## Tarefa 4
Resolveremos as instâncias utilizando o solver Gurobi
Instância | Primal | Dual | Gap | Status | Tempo (s)
| :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: |
| 1 | +6.907967156735e+04 | +6.907775362516e+04 | 0.00002 | Solved | 12.0
| 2 | +7.598617345267e+04 | +7.597516745367e+04 | 0.0001 | Solved | 128.3
| 3 | +1.148574105987e+05 | +1.148174934356e+05 | 0.0003 | Solved | 313.2
| 4 | +1.344714678945e+05 | +1.343745376981e+05 | 0.0007 | Time Limit Exceeded | 323.7
| 5 | +1.618991867905e+05 | +1.617001647389e+05 | 0.001 | Time Limit Exceeded | 334.5


Especificações da Máquina de execução:


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
$x_{ij}$ = porcentagem da demanda da cidade j qu a assistência i atende

$min\ \Sigma_{i=1}^n f_i \cdot y_i + \Sigma_{i=1}^n\Sigma_{j=1}^m c_{ij} \cdot x_{ij}$ (1)

sujeito à:

$\Sigma_{i=1}^n x_{ij} = 1 \ \ j = 1,..., m\$  (2) 

$\Sigma_{j=1}^m d_j \cdot x_{ij} \le Cap_i \cdot y_i \ \ i = 1, ..., n\$ (3) 

$y_i \in \{0,1\}\ $(5)

$0 \le x_{ij} \le 1 \ $(6)

A função objetivo (1) tem como finalidade minimizar a soma dos custos fixos de cada AT aberta mais a soma dos custos de transporte das assistências técnicas para as cidades atendidas. 
A restrição (2) certifica que todas as cidades atendidas tiveram suas demandas supridas.
A restrição (3) garante que nenhuma das ATs tenha su capacidade extrapolada, e as restrições (5) e (6) determinam o domínio das variárveis $y_i$ e $x_{ij}$, respectivamente.
Por fim, obtêm-se quais assistências técnicas devem ser abertas para que os custos totais sejam minimizados.

Referência: [Avaliação de cenários para o problema de localização de facilidades
determinando centros de distribuição de uma empresa de
eletrodomésticos](https://aprepro.org.br/conbrepro/2019/anais/arquivos/10192019_191014_5dab8eee2b4dc.pdf)


## Tarefa 6 - Toy Problem

A descrição do modelo está descrito na tarefa 5.
O arquivo que representa os valores de cada variável está presente em instancias/toy_problem/toy.txt .

Sendo assim, rodando o código utilizando SCIP obtemos os seguintes resultados:


Instância | Primal | Dual | Gap | Status | Tempo (s)
| :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: |
| Toy Problem | 1.831666666667e+03 | 1.831666666667e+03 | 0.00 | Solved | 0.0193

Os resultados para cada varíavel $x_{ij}$ e $y_i$ podem ser observados nas tabelas abaixo:

| X             | 0             | 1             |             2 | 
| :-----------: | :-----------: | :-----------: | :-----------: |
| 0             |           1.0 | 0.16666666666666666 | 1.0     |
| 1             |           0.0 | 0.8333333333333334 | 0.0     |
| 2             |           0.0 | 0.0 | 0.0     |


$y_0 = 1.0$ | $y_1 = 1.0$ | $y_2 = 0.0$ |
