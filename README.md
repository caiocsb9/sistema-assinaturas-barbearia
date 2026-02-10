# Sistema de Assinaturas para Barbearias

Sistema desenvolvido para auxiliar barbearias na gestão de clientes, planos de assinatura e histórico de atendimentos, proporcionando maior controle financeiro e fidelização de clientes.

## 📋 Descrição

Este sistema tem como objetivo permitir que barbearias gerenciem seus **planos de assinatura**, **clientes cadastrados** e o **histórico de serviços realizados**. A plataforma possibilita o controle de mensalidades, registro de atendimentos e acompanhamento da frequência dos clientes.

O sistema foi projetado para ser desenvolvido em **Python**, utilizando um banco de dados **NoSQL (MongoDB)**, explorando a flexibilidade do modelo orientado a documentos, ideal para dados semi-estruturados e históricos de uso.

## 🎯 Funcionalidade Principal

- **Gestão de assinaturas de clientes**, permitindo que a barbearia acompanhe planos ativos, vencimentos e histórico de atendimentos.

## 🎯 Funcionalidades Principais

- **Cadastro de Clientes**: Registro de informações pessoais e plano contratado
- **Gestão de Planos de Assinatura**: Criação de planos mensais com diferentes benefícios (quantidade de cortes, serviços incluídos, validade, etc.)
- **Registro de Atendimentos**: Armazenamento do histórico de serviços realizados por cada cliente
- **Controle de Pagamentos**: Acompanhamento de mensalidades pagas, pendentes ou atrasadas
- **Relatórios Básicos**: Consulta de clientes ativos, planos mais utilizados e frequência de atendimentos

## 👤 Cliente do Sistema

- **Público-alvo**: Donos de barbearias de pequeno e médio porte  
- **Necessidade atendida**: Organização de assinaturas, aumento da recorrência financeira e fidelização de clientes

## 🛠 Tecnologias

- **Backend**: Python  
- **Framework Web**: Flask ou FastAPI  
- **Banco de Dados**: MongoDB (NoSQL)  
- **Autenticação**: JWT  
- **Arquitetura**: API RESTful  
- **Formato de Dados**: JSON  

## 📝 Estrutura de Dados

O sistema armazena as seguintes coleções:

- **Clientes**: Dados pessoais, plano ativo e status da assinatura
- **Planos**: Informações dos planos disponíveis (valor, serviços incluídos, validade)
- **Atendimentos**: Histórico de serviços realizados por cliente
- **Pagamentos**: Registros de mensalidades pagas, pendentes ou atrasadas
- **Usuários do Sistema**: Funcionários ou administradores da barbearia

## 🔒 Segurança

- Autenticação via JWT para acesso às funcionalidades do sistema
- Controle de acesso por tipo de usuário (administrador e funcionário)
- Validação de permissões para operações sensíveis

## ⚠️ Observações

- Este sistema é um **projeto acadêmico** desenvolvido para a disciplina **Banco de Dados NoSQL**
- Os dados armazenados são fictícios e utilizados apenas para fins educacionais

📊 Atividade 3: Aggregation Pipeline
Implementei uma esteira de processamento de dados para gerar relatórios gerenciais automáticos para a barbearia:

Relatório de Planos: Utiliza o estágio $group para contar quantos clientes estão vinculados a cada plano (VIP, Mensal, etc).

Relatório Financeiro: Combina os estágios $match (para filtrar apenas clientes ativos) e $group (para somar o faturamento total da barbearia).
