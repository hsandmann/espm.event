# ESPM - Serviço de Transferência de Estilo

## Setup

Para utilizar o código deste repositório, siga as instruções a seguir:

Crie um ambiente virtual do Python:

    $ python3 -m venv env

Ative o ambiente virtual (**você deve fazer isso sempre que for executar algum script deste repositório**). No Windows:

    $ env\Scripts\activate

No Linux/MacOS:

    $ . env/bin/activate

Instale as dependências com:

    $ pip install -r requirements.txt

# Script de Execução

O script `main.py` é responsável por aplicar o filtro à imagem escolhida.

Para executar o script, faça:

    $ python3 main.py <filename> <style>

onde:

- `filename`: nome do arquivo para aplicar o filtro, sem a extensão (apenas **.JPG**);
- `style`: nome do arquivo de estilo

ao final da execução, o script deve gravar no diretório `out` um arquivo com o seguinte padrão:

    <filename>.<style>.jpg

## Estrutura de Diretórios

```
├── in
├── out
├── styles
└── weights
```
Sendo:
- `in`: imagens para aplicar o filtro;
- `out`: imagens com os filtros já aplicados;
- `styles`: imgens com as pinturas referências dos artistas;
- `weights`: pesos de conhecimentos da rede neural de transferência.

## Exemplo de Execução

Para:

```
├── in
│   └── carlos.jpg
├── out
└── styles
    ├── dali.jpg
    ├── kandinsky.jpg
    ├── monet.jpg
    ├── munch.jpg
    ├── rembrandt.jpg
    └── vangogh.jpg
```

Ao executar:

    $ python3 main.py carlos monet

O resultado será:

```
├── in
│   └── carlos.jpg
├── out
│   └── carlos.monet.jpg
└── styles
    ├── dali.jpg
    ├── kandinsky.jpg
    ├── monet.jpg
    ├── munch.jpg
    ├── rembrandt.jpg
    └── vangogh.jpg
```
