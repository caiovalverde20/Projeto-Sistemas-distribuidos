# Sistema Distribuído com Kafka, Flask e Zookeeper

## Visão Geral
Este projeto implementa um sistema distribuído usando Flask, Kafka e Zookeeper para simular o tratamento e análise de eventos de usuários. O sistema demonstra o gerenciamento seguro de senhas, utilizando hash, a produção e consumo de eventos Kafka e análise de dados em tempo real.

## Motivação
- Além do kafka ser projetado para lidar com grandes fluxos e baixa latencia, que seria o caso nescessario se fosse um verdadeiro sistema web, kafka e zookeeper foram as duas tecnologias que utilizei durante a cadeira para seguir os guias. Também trabalho com programação web e procurei o que poderia fazer juntando eles, e cheguei nesse monitoramento do sistema, super importante atualmente, para manter a saude da aplicação, encontrar e erros e usuarios mal intencionados

## Principais Funcionalidades
- **Produtor de Eventos**: Uma aplicação Flask que aceita entradas de usuários, faz o hash de senhas e envia esses eventos para um tópico Kafka.
- **Consumidor de Eventos**: Um consumidor Kafka que recebe eventos para análise em tempo real, incluindo contagem de tipos de eventos, cálculo da duração entre eventos e rastreamento de tentativas de login.
- **Análise de Eventos em Tempo Real**: Analisa a frequência, padrões temporais e taxas de sucesso de diferentes tipos de eventos, focando especialmente em tentativas de login e erros de sistema.
- **Interface Web**: Uma interface HTML simples para simular interação do usuário e geração de eventos.
- **Ambiente Dockerizado**: Utiliza o Docker Compose para configurar Kafka e Zookeeper, garantindo fácil implantação e escalabilidade.

## Tecnologias Utilizadas
- **Flask**: Lida com solicitações HTTP de entrada, processa dados e produz eventos Kafka.
- **Kafka**: Enfileira mensagens e as entrega aos consumidores.
- **Zookeeper**: Para coordenação e gerenciamento de configuração dos serviços Kafka.
- **Docker**: Para a conteinerização do Kafka e Zookeeper.
- **JavaScript**: Para manipulação de eventos no frontend.
- **Cryptography**: Para o hash de senhas de forma segura.

## Instalação

### Pré-requisitos
- Docker e Docker Compose
- Python 3.8+
- Node.js 

### Como rodar o projeto
- Docker-compose up -d
- Python server.py
- Python consumer.py e python analysis_consumer.py
- Abrir manualmente o HTML


## Video demonstrativo
- https://drive.google.com/file/d/1QPEZk0Hrf__FWd6SpHTkTSl6fEiD5FXo/view
