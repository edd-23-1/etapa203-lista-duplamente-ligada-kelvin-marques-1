# 1. Propósito
---
Esta tarefa tem os seguintes propósitos:
- Desenvolver as habilidades de criação e manipulação de estruturas de dados do tipo lista duplamente ligada ordenada (Doubly Linked List);
- Implementar e validar os conceitos relacionados ao métodos de estruturas de dados lista duplamente ligada ordenada.

# 2. Orientações
---

As subsessões a seguir orientam sobre o uso de soluções as quais poderão auxiliar na realização dessa tarefa, bem como os aspectos gerais relativos à implementação (código fonte) da sua solução.

## 2.1. Instalação do framework pytest
---
A estrutura do código fonte está montada para ser validada com a framework pytest, o qual poderá ser instalado com o comando:

```console
$ pip install pytest
```

Você não está obrigado a instalar o pytest e rodar os testes de validação antes do envio da tarefa, entretanto pode ser bastante útil para que você consiga identificar onde estão os pontos de falhas no seu projeto.

Para realizar um teste de validação da sua implementação, basta executar o seguinte comando:

```console
$ pytest test/test_lista_duplamente_ligada.py -v
```

O pytest permite que você realize o teste sobre métodos específicos da sua estrutura de dados lista duplamente ligada. Portanto, também é válido o comando:

```console
$ pytest test/test_lista_duplamente_ligada.py -k is_empty -v --no-header
```

Para mais detalhes e informações sobre o framework consultar no [link](https://docs.pytest.org/en/7.3.x/contents.html).

## 2.2. Implementação da solução
---

Você deverá implementar os **métodos da classe ListaDuplamenteLigadaOrdenada** no arquivo **lista_duplamente_ligada_ordenada.py**, os quais ainda não foram implementados. Esteja atento ao tipo de retorno de cada método, pois isso irá impactar diretamente na avaliação da sua solução após você enviar o commit com as suas implementações para o repositório remoto.

Após concluir a tarefa, você deverá realizar um **git push** para entregar a sua atividade. Você poderá realizar tantos envios ao repositório remoto quanto desejar. Entretanto, esteja atento ao prazo de entreda da atividade para não realizar a entrega com atraso, pois isso irá impactar sobre a nota da atividade. 

Os testes de validação da pontuação realizados pelo GitHub-Classroom não ocorrem imediatamente após o envio do push para o servidor. Normalmente, o GitHub levará o tempo de alguns segundos para realizar o teste sobre a solução enviada por você. Você deverá atualizar a página no GitHub-Classroom a cada 10s, caso não perceba a mudança no resultado da pontuação, até que o GitHub faça o computo dos seus pontos a partir da execução dos testes sobre a sua entrega.

Esteja atento aos tipos de retorno de cada método, os quais se encontram descritos com _type hint_ no próprio método.

## 2.3. Prazo de entrega
---

O prazo de entrega encontra-se descrito no ambiente do Google Sala de Aula da turma e também do GitHub Classroom.


# 3. Tarefas
---

Segue a relação de tarefas a serem observadas na implementação de cada método e a respectiva pontuação do método destacada em parênteses. Toda a tarefa valerá **15pts**, o que corresponde a **15pts%** da nota da segunda etapa.

- [x] Estudar e analizar os conceitos e técnicas para implementação da estrutura de dados do tipo lista duplamente ligada ordenada
- [ ] **(0pts)** Implementar o método **is_empty()**
  - [ ] Deve retornar um boolean True se não houver itens (Nó) na lista duplamente ligada ordenada ou False, caso contrário
  - OBS: A pontuação da implementação desse método está implícita na pontuação do método que faz uso do mesmo
- [ ] **(0pts)** Implementar o método **is_full()**
  - [ ] Deve retornar um boolean True se houver itens (Nó) na lista duplamente ligada ordenada ou False, caso contrário
  - OBS: A pontuação da implementação desse método está implícita na pontuação do método que faz uso do mesmo
  - [ ] **(0pts)** Implementar o método **frist()**
  - [ ] Deve retornar uma referência para o primeiro item (Nó) da lista duplamente ligada ordenada ou None, caso esteja vazia
  - OBS: A pontuação da implementação desse método está implícita na pontuação do método que faz uso do mesmo
- [ ] **(0pts)** Implementar o método **last()**
  - [ ] Deve retornar um referência para o último item (Nó) da lista duplamente ligada ordenada ou None, caso esteja vazia
  - OBS: A pontuação da implementação desse método está implícita na pontuação do método que faz uso do mesmo
- [ ] **(5pts)** Implementar o método **add()**, o qual deve receber como entrada um valor para criar um nó que deverá ser inserido no início da lista duplamente ligada ordenada
  - [ ] Criar um objeto Nó a partir do valor recebido pelo método
  - [ ] Deve retornar um boolean True se conseguir inserir um item (Nó) em ordem crescente na lista duplamente ligada ordenada
  - [ ] Caso a lista duplamente ligada ordenada tenha alcançado a sua capacidade máxima deverá lançar uma Exception com uma mensagem de erro relativo ao ocorrido, senão o item (Nó) deve ser inserido em ordem crescente na lista duplamente ligada ordenada e método deverá retornar um boolean True
- [ ] **(5pts)** Implementar o método **remove()**, o qual deve receber como entrada um valor para ser buscado na lista duplamente ligada ordenada e remover esse item da lista, caso esteja presente 
  - [ ] Caso a lista duplamente ligada ordenada esteja vazia deverá lançar uma Exception com uma mensagem de erro
  - [ ] Caso o item a ser removido esteja presente na lista duplamente ligada ordenada o item (Nó) da lista duplamente ligada ordenada deverá ser removido e em seguida o método deverá retornar o valor True
  - [ ] Caso o item a ser removido não esteja presente na lista duplamente ligada ordenada o método deverá retornar o valor False
- [ ] **(0pts)** Implementar o método **contains()**, o qual deverá receber como entrar um valor a ser buscado e retornar o valor True ou False como resultado da busca
  - [ ] Caso o valor a ser encontrado esteja presente na lista duplamente ligada ordenada, o método deverá retornar o valor True
  - [ ] Caso o valor a ser encontrado não esteja presente na lista duplamente ligada ordenada, o método deverá retornar o valor False
  - OBS: A pontuação da implementação desse método está implícita na pontuação do método que faz uso do mesmo
- [ ] **(0pts)** Implementar o método **display()**, o qual deve retornar uma lista com os valores (atributo dado) dos itens (Nó) inseridos na lista duplamente ligada ordenada
  - [ ] Caso a lista duplamente ligada ordenada esteja vazia deverá retornar uma lista vazia []
  - [ ] Caso a lista duplamente ligada ordenada possua um ou mais itens, o primeiro elemento da lista deve ser o valor do dado do primeiro item (Nó) na lista duplamente ligada ordenada, seguido das demais valores que compõem a lista duplamente ligada ordenada (do primeiro ao último), nessa ordem
  - OBS: A pontuação da implementação desse método está implícita na pontuação do método que faz uso do mesmo
- [ ] **(0pts)** Implementar o método **size()**, o qual deve retornar um int
  - [ ] O método deverá retornar ZERO, caso a lista duplamente ligada ordenada esteja vazia, ou, caso possua algum item na lista duplamente ligada ordenada, o valor relativo à quantidade de itens presentes na lista duplamente ligada ordenada
  - OBS: A pontuação da implementação desse método está implícita na pontuação do método que faz uso do mesmo
- [ ] **(5pts)** Validar os testes de alteração dos itens (Nós) da lista duplamente ligada ordenada
  - [ ] Testes de alteração dos itens no início da lista duplamente ligada ordenada
  - [ ] Testes de alteração dos itens no meio da lista duplamente ligada ordenada
  - [ ] Testes de alteração dos itens no final da lista duplamente ligada ordenada