# Use a imagem oficial do Ubuntu como base
FROM ubuntu:22.04

# Variável de ambiente para selecionar a versão do ROS 2
ENV ROS_DISTRO=humble

# Atualizar e instalar pacotes básicos
RUN apt-get update && \
    apt-get install -y \
        locales \
        curl \
        gnupg \
        lsb-release && \
    locale-gen en_US en_US.UTF-8 && \
    update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8 && \
    export LANG=en_US.UTF-8

# Adicionar as chaves GPG e o repositório do ROS 2
RUN curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | apt-key add - && \
    sh -c 'echo "deb [arch=$(dpkg --print-architecture)] https://mirrors.tuna.tsinghua.edu.cn/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2-latest.list'

# Instalar ROS 2 e as ferramentas de desenvolvimento
RUN apt-get update && \
    apt-get install -y \
        ros-$ROS_DISTRO-desktop \
        python3-argcomplete \
        python3-colcon-common-extensions \
        python3-pip \
        build-essential \
        git

# Instalar ferramentas e dependências adicionais
RUN apt-get install -y \
    ros-$ROS_DISTRO-rmw-cyclonedds-cpp \
    ros-$ROS_DISTRO-demo-nodes-cpp \
    ros-$ROS_DISTRO-demo-nodes-py

# Configurar o ambiente ROS
SHELL ["/bin/bash", "-c"]
RUN echo "source /opt/ros/$ROS_DISTRO/setup.bash" >> ~/.bashrc

# Definir ponto de entrada para o ambiente do ROS 2
ENTRYPOINT ["bash", "-c", "source /opt/ros/$ROS_DISTRO/setup.bash && exec \"$@\"", "--"]

# Exemplo de comando de execução padrão
CMD ["bash"]
