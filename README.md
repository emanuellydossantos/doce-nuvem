# Doce Nuvem 🧁

### Um pedacinho de felicidade em cada cupcake.

**Projeto Integrador Transdisciplinar II – Engenharia de Software**

> **Versão para avaliação: 2ª versão (PIT II)**
> Esta versão apresenta a aplicação atualizada e aprimorada após os testes realizados com cinco participantes. Foram implementadas correções e melhorias de navegação, funcionalidades e apresentação visual. **Esta é a versão que deve ser considerada para avaliação do projeto.**

## 1. Apresentação do projeto

O Doce Nuvem é um projeto de desenvolvimento de um site para uma loja fictícia de cupcakes. A proposta é oferecer uma página simples e organizada, na qual os usuários possam visualizar os produtos disponíveis, adicionar itens ao carrinho e realizar um pedido simulado.

O projeto foi desenvolvido como continuidade do Projeto Integrador Transdisciplinar I (PIT I), no qual foram elaborados os primeiros planejamentos da aplicação, incluindo mapa conceitual, mapa navegacional, wireframes e mockups.

No PIT II, o planejamento inicial foi utilizado como base para o desenvolvimento de uma aplicação web funcional, com recursos de cadastro, login, catálogo de produtos, carrinho de compras e histórico de pedidos.

## 2. Objetivos

O principal objetivo do projeto é desenvolver uma aplicação web simples para simular o funcionamento de uma loja virtual de cupcakes.

Entre os objetivos específicos estão:

- Criar uma interface visual organizada e de fácil utilização.
- Permitir que os usuários realizem cadastro e login.
- Apresentar um catálogo com diferentes sabores de cupcakes.
- Permitir adicionar, remover e alterar a quantidade de produtos no carrinho.
- Calcular automaticamente o valor total da compra.
- Simular a finalização de um pedido.
- Permitir a consulta dos pedidos realizados pelo usuário.

## 3. Planejamento do PIT I

Durante o PIT I, foi realizada a etapa inicial de planejamento da aplicação, com foco na interface, na organização das informações e na navegação entre as telas.

Foram desenvolvidos os seguintes materiais:

- **Mapa conceitual:** utilizado para organizar as principais ideias e funcionalidades do sistema.
- **Mapa navegacional:** elaborado para representar os caminhos que o usuário pode percorrer durante a utilização do site.
- **Wireframes:** utilizados para planejar a disposição dos elementos nas telas.
- **Mockups:** desenvolvidos para representar visualmente a aparência da aplicação.

Esses materiais serviram como referência para o desenvolvimento realizado no PIT II.

## 4. Tecnologias utilizadas

Para o desenvolvimento do Doce Nuvem, foram utilizadas as seguintes tecnologias:

- **HTML:** estrutura das páginas do site.
- **CSS:** estilização e organização visual das páginas.
- **JavaScript:** apoio à interatividade da aplicação.
- **Python:** linguagem utilizada no desenvolvimento do back-end.
- **Flask:** framework utilizado para criar as rotas e integrar as funcionalidades do sistema.
- **SQLite:** banco de dados utilizado para armazenar informações dos usuários e pedidos.
- **Visual Studio Code:** ambiente utilizado para edição e desenvolvimento do código.
- **GitHub:** plataforma utilizada para armazenar e disponibilizar o projeto.

## 5. Funcionalidades implementadas

O sistema conta com as seguintes funcionalidades:

### 5.1 Página inicial e catálogo

A página inicial apresenta a loja Doce Nuvem e seus produtos. O catálogo disponibiliza cinco opções de cupcakes:

- Cupcake de Baunilha – R$ 6,00.
- Cupcake de Chocolate – R$ 6,00.
- Cupcake de Morango – R$ 7,00.
- Cupcake de Limão Siciliano – R$ 7,00.
- Cupcake Red Velvet – R$ 8,00.

Cada produto possui imagem, nome, descrição e preço.

### 5.2 Cadastro de usuários

O sistema permite que novos usuários realizem um cadastro utilizando e-mail e senha.

Os e-mails são armazenados com identificação única, evitando cadastros duplicados.

### 5.3 Login e autenticação

O usuário cadastrado pode acessar sua conta por meio da tela de login.

As senhas são armazenadas no banco de dados utilizando hash, em vez de serem salvas diretamente em texto. O sistema também utiliza sessões para controlar o acesso às funcionalidades que exigem autenticação.

### 5.4 Carrinho de compras

Após realizar o login, o usuário pode adicionar produtos ao carrinho, visualizar os itens selecionados, alterar suas quantidades e remover produtos quando necessário.

O sistema calcula o subtotal dos itens e o valor total da compra, atualizando os valores conforme as alterações realizadas.

### 5.5 Finalização do pedido

O usuário pode finalizar o pedido por meio de uma funcionalidade de simulação de compra.

Após a finalização, o pedido é registrado no banco de dados e o usuário recebe uma página de confirmação.

**Observação:** o projeto não realiza pagamentos reais. A finalização é apenas uma simulação do processo de compra.

### 5.6 Histórico de pedidos

O sistema permite que o usuário consulte os pedidos realizados anteriormente.

As informações são apresentadas de acordo com a conta que está conectada, evitando que um usuário consulte os pedidos de outra pessoa.

## 6. Requisitos do sistema

### 6.1 Requisitos funcionais

Os requisitos funcionais representam as ações que o sistema deve permitir realizar.

- RF01 – Permitir a visualização do catálogo de cupcakes.
- RF02 – Permitir o cadastro de novos usuários.
- RF03 – Permitir que usuários cadastrados realizem login.
- RF04 – Permitir o encerramento da sessão.
- RF05 – Permitir adicionar produtos ao carrinho.
- RF06 – Permitir remover produtos do carrinho.
- RF07 – Permitir alterar a quantidade de produtos no carrinho.
- RF08 – Calcular o subtotal e o valor total dos produtos selecionados.
- RF09 – Permitir a finalização simulada de pedidos.
- RF10 – Registrar os pedidos no banco de dados.
- RF11 – Permitir a consulta do histórico de pedidos do usuário.

### 6.2 Requisitos não funcionais

Os requisitos não funcionais estão relacionados à qualidade e às características da aplicação.

- RNF01 – Apresentar uma interface simples e organizada.
- RNF02 – Permitir a utilização por meio de um navegador web.
- RNF03 – Armazenar os dados dos usuários e pedidos em banco de dados.
- RNF04 – Utilizar hash para armazenar as senhas.
- RNF05 – Restringir o acesso às funcionalidades que exigem autenticação.
- RNF06 – Manter a organização dos arquivos e códigos do projeto.

## 7. Banco de dados

Para armazenar as informações da aplicação, foi utilizado o SQLite, um banco de dados que permite trabalhar com os dados sem a necessidade de instalar um servidor de banco de dados separado.

O banco de dados utilizado no projeto é chamado `docenuvem.db`.

Entre as principais informações armazenadas estão:

- **Usuários:** identificador, e-mail, senha em formato hash e data de criação.
- **Pedidos:** informações relacionadas aos pedidos realizados pelos usuários.
- **Itens dos pedidos:** produtos, quantidades e valores associados a cada pedido.

A estrutura permite relacionar os pedidos aos respectivos usuários e armazenar os produtos que fizeram parte de cada compra.

## 8. Organização do projeto

O projeto foi organizado da seguinte maneira:

```text
doce-nuvem/
│
├── static/
│   ├── imagens/
│   │   ├── imagens dos cupcakes
│   │   ├── ícones da aplicação
│   │   └── imagem de fundo
│   │
│   └── style.css
│
├── templates/
│   ├── login.html
│   ├── cadastro.html
│   ├── inicio.html
│   ├── carrinho.html
│   ├── pedido_confirmado.html
│   └── meus_pedidos.html
│
├── app.py
├── criar_usuario.py
├── requirements.txt
├── README.md
└── .gitignore
```

O banco de dados e o ambiente virtual são utilizados localmente e não precisam ser enviados ao repositório.

## 9. Desenvolvimento e implementação

No PIT II, o planejamento realizado anteriormente foi utilizado como referência para a construção do site.

O desenvolvimento foi realizado por etapas, começando pela estrutura das páginas e pela organização dos arquivos. Em seguida, foram implementadas as funcionalidades de cadastro, login, catálogo, carrinho e pedidos.

O Flask foi utilizado para conectar as páginas HTML ao código Python e ao banco de dados SQLite.

Durante o desenvolvimento, também foram realizados ajustes e correções para resolver problemas encontrados nas rotas, na navegação e no funcionamento das funcionalidades.

Após a implementação das funcionalidades principais, foram realizados ajustes na apresentação visual das páginas, na organização do CSS e na navegação, buscando melhorar a experiência de utilização.

## 10. Testes e validação

Os testes foram realizados durante o desenvolvimento para verificar se as funcionalidades apresentavam o comportamento esperado.

Entre os pontos verificados estão:

- Cadastro de um novo usuário.
- Tentativa de cadastro com e-mail já existente.
- Login com dados corretos e incorretos.
- Acesso ao carrinho somente após autenticação.
- Adição, remoção e alteração da quantidade de produtos.
- Cálculo do valor total da compra.
- Finalização e registro de um pedido.
- Consulta ao histórico de pedidos.
- Verificação de que cada usuário visualiza somente seus próprios pedidos.

Além dos testes realizados durante o desenvolvimento, foi realizada uma avaliação com cinco participantes, com o objetivo de observar o funcionamento do sistema e identificar possíveis dificuldades de utilização.

Entre os retornos recebidos, foram observados os seguintes pontos:

- O cadastro e o login foram utilizados corretamente.
- A validação de e-mails duplicados foi identificada como um comportamento adequado.
- O acesso às funcionalidades que exigem autenticação foi observado durante a utilização.
- Foi identificada uma dificuldade relacionada ao direcionamento do usuário após o login e à visibilidade da opção de sair da conta.
- O funcionamento do carrinho, incluindo o cálculo dos valores, foi observado durante os testes.
- Também foi observado o comportamento do carrinho após a finalização do pedido e a consulta do pedido na página de histórico.

Com base nas observações, foram realizados ajustes na navegação após o login e na apresentação visual da opção de encerramento da sessão. Também foram feitos aprimoramentos na organização visual das páginas.

A avaliação contribuiu para identificar pontos que poderiam ser melhorados e orientar os ajustes realizados na aplicação.

## 11. Resultados e discussão

O desenvolvimento do PIT II permitiu transformar o planejamento visual elaborado no PIT I em uma aplicação web com funcionalidades implementadas.

O Doce Nuvem passou a contar com cadastro e autenticação de usuários, catálogo de produtos, carrinho de compras, alteração de quantidades, finalização simulada de pedidos e histórico de compras.

A avaliação realizada com cinco participantes contribuiu para observar o funcionamento da aplicação e identificar pontos de melhoria relacionados à navegação e à apresentação dos elementos da interface.

As correções realizadas após essa etapa buscaram tornar a utilização do sistema mais clara e organizada, especialmente no acesso à conta e na navegação entre as páginas.

Durante a implementação, também foram identificados desafios relacionados à integração entre as páginas, às rotas do Flask e ao armazenamento das informações. Esses problemas foram tratados durante o desenvolvimento, contribuindo para o aprendizado prático.

Como possibilidades de melhorias futuras, podem ser consideradas a implementação de pagamentos reais, acompanhamento de entregas, avaliações dos produtos e aprimoramentos na experiência de navegação.

## 12. Conclusão

O projeto Doce Nuvem possibilitou aplicar na prática conhecimentos estudados durante a graduação em Engenharia de Software.

A continuidade do trabalho iniciado no PIT I permitiu avançar do planejamento da interface para o desenvolvimento de uma aplicação web com funcionalidades de uma loja virtual.

A implementação das funcionalidades, os testes realizados e a avaliação com participantes contribuíram para identificar dificuldades e realizar melhorias no sistema.

Apesar dos desafios encontrados durante a programação, o desenvolvimento contribuiu para ampliar os conhecimentos sobre Python, Flask, HTML, CSS, JavaScript e banco de dados SQLite.

Conclui-se que os objetivos de desenvolver uma aplicação demonstrativa para a venda de cupcakes foram alcançados nas funcionalidades implementadas, permanecendo possibilidades de melhorias e novas funcionalidades para versões futuras.

## 13. Acesso à aplicação

**Repositório do projeto:**  
https://github.com/emanuellydossantos/doce-nuvem

**Link da solução em funcionamento:**  
A ser inserido

## 14. Como executar o projeto localmente

Para executar o projeto localmente, é necessário ter o Python instalado.

**1. Clone o repositório:**

```bash
git clone https://github.com/emanuellydossantos/doce-nuvem.git
```

**2. Entre na pasta do projeto:**

```bash
cd doce-nuvem
```

**3. Crie um ambiente virtual:**

```bash
python -m venv .venv
```

**4. Ative o ambiente virtual no Windows:**

```bash
.venv\Scripts\activate
```

**5. Instale as dependências:**

```bash
pip install -r requirements.txt
```

**6. Execute a aplicação:**

```bash
python app.py
```

**7. Acesse o endereço no navegador:**

```text
http://127.0.0.1:5000/
```

O banco de dados é inicializado pela aplicação quando necessário.