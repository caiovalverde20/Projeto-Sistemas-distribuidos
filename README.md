# Sistema Distribuído com Kafka, Flask e Zookeeper

## Visão Geral
Este projeto implementa um sistema distribuído usando Flask, Kafka e Zookeeper para simular o tratamento e análise de eventos de usuários. O sistema demonstra o gerenciamento seguro de senhas, utilizando hash, a produção e consumo de eventos Kafka e análise de dados em tempo real.

## Motivação
- Trabalho com progração web, então decidi procurar as melhores ferramentas para fazer analise em tempo real de um sistema web, extremamente importante, para cuidarmos das saúde do nosso sistema, detectarmos erros e até mesmo usuarios mal intencionados e tentativas de ataques ao nossos sistema. Neste projeto, Kafka e Zookeeper são mais que ferramentas; são pilares centrais na arquitetura de sistemas distribuídos. Com Kafka, buscamos excelência em processamento de grandes volumes de dados com baixa latência, ideal para aplicações web em escala. Zookeeper, por sua vez, garante a coordenação e confiabilidade do estado do sistema, elementos críticos para a resiliência e estabilidade operacional. Esse duo dinâmico foi escolhido devido à sua relevância e eficácia comprovada no gerenciamento de dados e eventos em tempo real, facilitando a manutenção da integridade e performance do sistema.

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
