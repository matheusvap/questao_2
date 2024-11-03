# ROS 2 Humble Docker Image

Esta imagem Docker configura um ambiente com ROS 2 Humble Hawksbill, pronto para o desenvolvimento e execução de pacotes ROS 2. Este guia apresenta instruções para construir e executar a imagem.

## Pré-requisitos

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado e em execução no Windows.

## Passos para construir a imagem

1. Clone este repositório ou crie o arquivo `Dockerfile` conforme fornecido.
2. No terminal do Docker, navegue até o diretório onde o `Dockerfile` está localizado.
3. Execute o seguinte comando para construir a imagem:

   ```bash
   docker build -t ros2:humble .

## Executando um container

Para iniciar um container a partir da imagem criada, execute o seguinte comando:

  ```bash
  docker run -it --name ros2_container ros2:humble