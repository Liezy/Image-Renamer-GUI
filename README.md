# Image Renamer GUI

## 📜 Descrição
O **Image Renamer GUI** é uma aplicação Python com interface gráfica moderna e intuitiva que permite renomear imagens selecionadas, utilizando a data de criação presente nos metadados das imagens e um número aleatório. Além disso, as imagens renomeadas são copiadas para uma pasta específica, e um log contendo os nomes antigos e novos é gerado para rastreamento.

---

## 🎨 Funcionalidades
- Renomeação de imagens com base na data de criação (extraída dos metadados EXIF) e um número aleatório.
- Cópia das imagens renomeadas para uma pasta de saída configurada.
- Geração de um log com os nomes antigos e novos em um arquivo `.txt`.
- Suporte para diversos formatos de imagem, como **JPEG**, **PNG**, entre outros.
- Interface gráfica amigável e moderna, desenvolvida com **tkinter**.

---

## 📂 Estrutura do Projeto
image_renamer/ 
    ├── images/ # Pasta com as imagens originais 
    ├── output/ # Pasta para salvar as imagens renomeadas 
    ├── logs/ # Pasta para armazenar o log de renomeação 
    ├── main.py # Arquivo principal da aplicação 
    ├── requirements.txt # Dependências do projeto 
    ├── README.md # Documentação do projeto 
    └── .gitignore # Arquivos e pastas ignorados no Git


---

## 🚀 Como Executar o Projeto

### 1. Pré-requisitos
Certifique-se de ter o **Python 3.7+** instalado em sua máquina. Para instalar as dependências, execute:

```bash
pip install -r requirements.txt
```
## Inicializando a Aplicação
Clone este repositório:

```bash
git clone https://github.com/Liezy/Image-Renamer-GUI.git
cd Image-Renamer-GUI
```
## Execute o programa:

```bash
Copiar código
python main.py
```
## 🖥️ Interface Gráfica
# A interface gráfica permite:

- Selecionar imagens a partir de um file dialog.
- Escolher uma pasta de saída para as imagens renomeadas.
- Renomear as imagens com um clique.

## 🛠️ Tecnologias Utilizadas
- Python: Linguagem de programação principal.
- Pillow: Biblioteca para manipulação de imagens.
- tkinter: Criação da interface gráfica.
- shutil: Gerenciamento de arquivos.
## 📝 Log de Alterações
O programa gera automaticamente um log com os nomes antigos e novos das imagens renomeadas no arquivo logs/rename_log.txt.

## 🧑‍💻 Autor
Desenvolvido por Eliézer Alencar.