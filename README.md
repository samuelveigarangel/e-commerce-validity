# E-commerce para produtos perto da validade
(licensa)

## Apêndice
* [Sobre o projeto](#sobre-o-projeto)
* [Partes do sistema](#partes-do-sistema)
    * [Início](#início)
    * [Produto](#produto)
    * [Carrinho](#carrinho)
    * [Checkout](#checkout)
    * [Usuário](#usuário)
    * [Lojista](#lojista)
* [Tecnologias usadas](#tecnologias-usadas)
* [Implantação em produção](#implantação-em-produção)
* [Dificuldades e melhorias futuras](#dificuldades-e-melhorias-futuras)
    * [Dificuldades](#dificuldades)
    * [Melhorias futuras](#melhorias-futuras)
* [Como executar o projeto](#como-executar-o-projeto)
# Sobre o projeto

Um projeto para vender as melhores ofertas de produtos perto da validade. Inicialmente, apenas alimentos estão disponíveis no site. 

Qualquer empresa que revenda alimentos, poderá ser parceira do site. Então, cada produto estará associado algum supermercado. A ideia é mostrar para os clientes os produtos com as melhores ofertas perto de sua localidade. Com um portal dedicado aos lojistas, eles poderão ver seus pedidos, além de poder cadastrar novos produtos no site.



<br></br>
# Início

O início é composto por uma navbar, body que mostra os ultimos produtos com opções para selecionar o tipo de produto e um footer.

Navbar: Há um botão que te leva ao inicio, um campo para procurar os produtos pelo nome, botão para ver seu carrinho e um botão para realizar o login ou entrar no perfil do usuário.

Body: No corpo do site é mostrado os ultimos produtos que foram cadastrados no sistema de todas as lojas. Cada produto há um botão adicionar que adicionar o produto ao carrinho e te leva direto ao carrinho.

footer: Informações gerais sobre a loja.

![inicio-gif-maker](https://user-images.githubusercontent.com/82840278/191866288-2724a833-4b72-4ba5-914e-3b22f6a76dfd.gif)


<br></br>
# Produto
Você pode adicionar um produto atráves da página principal pelo botão adicionar ou pela página do produto. Na página do produto, há mais informações sobre o produto, como a descrição e o endereço da loja do produto, além do preço. Vale notar que após o vencimento do produto, não é mais possível acessa a página e adicionar ao carrinho.

![ezgif com-gif-maker (3)](https://user-images.githubusercontent.com/82840278/191866856-c3972e69-9831-4cd7-ac6b-69de7f85a93a.gif)

<br></br>
# Carrinho
Em primeiro instante, a lógica do carrinho foi desenvolvida com escrita e leitura no banco de dados. Só por adicionar um produto no carrinho, era realizado tais operações. Após perceber que isso poderia gerar inconsistências no banco de dados, dado um grande volume de escritas, a lógica do carrinho agora se baseia em sessions. Quando é adicionado um produto, há apenas uma leitura no banco de dados para recuperar os valores e quantidade disponível do produto.

![ezgif com-gif-maker (6)](https://user-images.githubusercontent.com/82840278/191868334-036bf727-4a0c-4b4b-995a-7b7c5890c806.gif)




<br></br>
# Checkout
Antes de finalizar o pedido, é verificado se todos os pedidos são da mesma loja, se sim, é finalizado o pedido e criado uma ordem para loja que gera um número único de pedido. O usuário poderá chegar na loja e apresentar esse número. A ideia é que se o usuário não realizar o pagamento, o pedido será cancelado e ficará disponível novamente.

![ezgif com-gif-maker (7)](https://user-images.githubusercontent.com/82840278/191868615-170744e2-818b-4dfb-aa5c-15b7011cbdc4.gif)

<br></br>
# Usuário
O usuário dispõe de uma interface para visualizar seus dados pessoais e suas compras.

![ezgif com-gif-maker (8)](https://user-images.githubusercontent.com/82840278/191869031-b103164a-6da0-4362-86cf-3ca08d4c32ed.gif)

<br></br>
# Lojista
O sistema possui uma parte dedicada ao lojista que deseja anunciar. Nele, há histórico de ordens, ultimas ordens e o cadastro novos produtos. Usuários marcados como cliente, não conseguem visualizar esse portal. 

<br></br>
# Tecnologia usadas
## Backend
- python
- Django
## Frontend
- Html
- Css
- Bootstrap
- Javascript

# Implantação em produção
Utilizei heroku como serviço de hospedagem e AWS S3 para hospedar as fotos dos produtos que são inseridos pelo lojistas. 

# Dificuldades e melhorias futuras
## Dificuldades
- Alguma das dificuldades no deploy, foi utilizar tanto arquivos estáticos e media. Por padrão, heroku só aceita arquivos que são enviado no git. Portanto, para fazer o upload de arquivos no sistema, é preciso utilizar outro serviço de hospedagem. O aws S3 é uma ótima escolha, porém, há uma configuração extra para apontar os arquivos de media para outro bucket que não seja o de arquivos estáticos. 

## Melhorias futuras
- Adicionar a parte de pagamento e entrega de produtos.
- Colocar ofertas especiais no início.
- Mostrar apenas produtos baseado na localização do usuário. Site vai indentificar a região do usuário.
- Chat online com o lojista.
- Adicionar funcionalidade que não permite realizar a comprar se não haver mais produtos em estoque.

<br></br>
# Como executar o projeto
```bash
# clonar repositório
git clone https://github.com/samuelveigarangel/estudio-paintblack.git

# Abra o prompt de comando e vá para pasta do projeto

# Crie um ambiente virtual
python -m venv venv

# Ative seu ambiente virtual
venv\scripts\activate

# Instale os requerimentos 
pip install -r requirements.txt

# Faça o migrate para criar a dabatase
py manage.py migrate

# Crie um super user
python manage.py createsuperuser

# Colete os arquivos estáticos
python manage.py collectstatic

# Execute o projeto 
python manage.py runserver

```