# Trabalho de Otimização Inteira
- [@vitorfrois](github.com/vitorfrois)
- [@baqueta]()
- [@thais]()
- [@dudu]()
- [@sampai](https://github.com/GusSampaio)

### Descrição
O problema de localização de facilidades é um problema clássico de otimização que
pode ser abordado de várias formas. Apresentamos duas abordagens clássicas.
A primeira visa atender a demanda dos clientes minimizando a soma dos custos fixos
de instalação das facilidades e dos custos de transportes. Na segunda, o objetivo é
maximizar o lucro gerado pelas facilidades abertas.

### facilities_solver.py
O script python conta com algumas opções. Para consultar rode
```$~ python facilities_solver.py``` no terminal:

``` bash
usage: Facilities Solver [-h] [-f FOLDER] [-s SOLVER] [-t TIMELIMIT] [-p PROBLEM] [-v]

Given an instance of the facilities problem, solve it

options:
  -h, --help            show this help message and exit
  -f FOLDER, --folder FOLDER
                        Folder where instances are stored
  -s SOLVER, --solver SOLVER
                        Available solvers: ['GUROBI_CMD', 'PULP_CBC_CMD', 'SCIP_CMD']
  -t TIMELIMIT, --timelimit TIMELIMIT
                        Time limit in seconds
  -p PROBLEM, --problem PROBLEM
                        Problem version to use (1 or 2)
  -v, --verbose
```

Exemplo de uso:

```python facilities_solver.py -f instancias/ -t 5 -s SCIP_CMD -p 2```


### Tarefas
De acordo com o PDF
- [ ] Tarefa 1
- [ ] Tarefa 2
- [ ] Tarefa 3
- [ ] Tarefa 4
- [ ] Tarefa 5
- [ ] Tarefa 6

