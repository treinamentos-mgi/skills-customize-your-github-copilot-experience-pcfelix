---
applyTo: "assignments/**"
---

# Instrucoes para atividades

- Siga a estrutura e os titulos de `templates/assignment-template.md`: objetivo, tarefas, descricao e requisitos.
- Escreva objetivos claros e requisitos concretos que possam ser verificados pelo aluno.
- Use linguagem simples, acolhedora e adequada ao nivel da atividade. Mantenha o idioma e o estilo dos arquivos existentes na pasta.
- Garanta que cada atividade tenha uma pasta propria e que os nomes e caminhos dos arquivos sejam descritivos.
- Ao criar ou alterar um `README.md`, mantenha o conteudo coerente com o codigo inicial e os demais arquivos da atividade.
- Mantenha o codigo inicial simples e relacionado diretamente aos requisitos. Nao inclua uma solucao completa, a menos que seja solicitada.
- Se os arquivos ou caminhos da atividade mudarem, atualize tambem a entrada correspondente em `config.json`, incluindo `path` e `attachments` quando aplicavel.

---
description: "Instruções para usar sempre que criar ou editar arquivos markdown de assignment, garantindo consistência e clareza para os alunos."
applyTo: "assignments/**/*.md"
---

# Diretrizes de Estrutura para Markdowns de Tarefas

Todos os arquivos markdown de tarefas devem seguir estas diretrizes:

## 1. Uso do Template

- Os arquivos markdown de tarefas devem seguir a estrutura em [`templates/assignment-template.md`](../../templates/assignment-template.md).
- A tarefa deve ser criada como um arquivo `README.md`
- Não remova ou pule seções obrigatórias do template.

## 2. Orientação das Seções

Os cabeçalhos das seções devem usar EXATAMENTE o mesmo texto do template, incluindo os ícones emoji. NÃO traduza os cabeçalhos.

- `# 📘 Assignment: [Assignment Title]` — Substitua `[Assignment Title]` por um nome curto e descritivo (ex: `Python Basics`, `Loops and Conditionals`, `Functions and Modules`).
- `## 🎯 Objective` — Escreva 1-2 frases resumindo o que o aluno aprenderá ou realizará. Foque nas principais habilidades ou conceitos.
- `## 📝 Tasks` — Para cada tarefa, use `### 🛠️ [Task Title]`:
   - Use um nome de tarefa específico e orientado à ação
   - Na Descrição, indique claramente o que o aluno deve fazer.
   - Nos Requisitos, use bullet points para listar os resultados ou funcionalidades esperadas. Seja específico e mensurável
   - Forneça exemplos de entrada/saída em blocos de código se útil.

Não inclua seções extras a menos que explicitamente especificado.