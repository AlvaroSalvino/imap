# Polos_Malta_Map

## Um mapa interativo para gerenciar os polos da rede de faculdades Malta.

![Visão Inicial do Mapa](static/assets/imagens%20publicas/inicio.PNG)

## O que é o **iMap**?
O **iMap** é uma aplicação privada e interativa, desenvolvida para facilitar o controle de projetos e localizações geográficas de forma eficiente, independentemente de onde você esteja.

Esta versão específica foi criada para o gerenciamento dos polos de uma rede de faculdades. O aplicativo é compatível com diferentes dispositivos, incluindo:
- Computadores (Windows, Linux),
- Smartphones,
- Tablets.

---

## Funcionalidades principais

### Telas da Aplicação
O aplicativo possui **quatro telas principais**, cada uma com uma funcionalidade específica:
1. **Tela inicial**: Página de entrada da aplicação.
2. **Escolha de caminho**: Direciona o usuário para diferentes funcionalidades.
3. **Mapa interativo**: Visualização e exploração do mapa.
4. **Cadastro de nova localização**: Inserção de novos polos diretamente no mapa.

![Visualizando o Interior da Aplicação](static/assets/imagens%20publicas/home.PNG)

---

### Mapa Interativo e Funcionalidades

![Mapa de Polos](static/assets/imagens%20publicas/mapa.PNG)

O mapa oferece diversas funcionalidades para facilitar a navegação e exploração:
- **Zoom interativo**;
- **Pins demonstrativos**: Marcam os locais cadastrados;
- **Filtros**: Refine sua busca por critérios específicos;
- **Barra de pesquisa**: Localize rapidamente polos ou cidades.

---

### Cadastro de Novos Locais

![Inserção de Localidade](static/assets/imagens%20publicas/insercao.PNG)

O sistema permite o cadastro de novos polos de maneira simples e automatizada:
- Utilize a **API de geolocalização** integrada para capturar automaticamente a latitude e longitude.
- Basta informar o nome do local (Estado, Cidade, Bairro ou Estabelecimento) e a aplicação se encarrega do restante.

---

## Informações Técnicas

O **Polos_Malta_Map** foi desenvolvido utilizando o framework **Flask**. Confira abaixo os principais detalhes técnicos da aplicação:

1. **API Interna (app.py)**  
   - Lida com operações [GET] e [POST] para gerenciar informações, como:
     - Nome do responsável pelo polo.
     - Localização baseada na cidade associada.

2. **APIs Externas Utilizadas**
   - **GeoPy Geocoders (Bing)**  
     - Fornece dados de latitude e longitude a partir do nome da cidade cadastrada.
   - **Folium**  
     - Gera um mapa interativo e visualmente intuitivo.  
     - Com base nos dados de latitude e longitude, insere automaticamente um **Pin** no local correto no mapa.

Essas funcionalidades oferecem uma experiência completa e eficiente para o planejamento e gestão estratégica dos polos da faculdade.

---

Sinta-se à vontade para explorar, contribuir ou adaptar o projeto conforme suas necessidades! 😊
