---
name: new-assignment
description: "Use when creating or scaffolding a new programming assignment, exercise, or student task in assignments/. Keeps the README, starter files, attachments, and config.json consistent with this project."
argument-hint: "Describe the assignment topic, learning goals, and any required files"
---

# Criar uma atividade

Crie uma nova atividade de programação para o portal do curso, seguindo a estrutura do projeto e mantendo todos os arquivos relacionados consistentes.

## Quando usar

- Criar uma nova atividade ou exercício para os alunos.
- Preparar o README, o código inicial ou os dados de uma atividade.
- Adicionar uma atividade nova ao catálogo do portal.

## Procedimento

1. Leia as instruções aplicáveis em [assignments.instructions.md](../../instructions/assignments.instructions.md), o [template de atividade](../../../templates/assignment-template.md) e o [config.json](../../../config.json). Consulte também atividades próximas para adequar o nível, o idioma e o estilo.
2. Defina um identificador curto em `kebab-case` para a pasta em `assignments/<id>/`. Confira se o identificador ainda não está em uso.
3. Crie `README.md` usando a estrutura e os títulos do template. Escreva um objetivo claro e divida o exercício em tarefas com descrições e requisitos específicos e verificáveis.
4. Crie somente os arquivos de apoio necessários. Quando houver código inicial, deixe pontos de implementação para o aluno e não inclua uma solução completa, salvo solicitação explícita. Inclua dados ou anexos apenas quando forem necessários para concluir a atividade.
5. Adicione uma entrada da atividade em `config.json` com `id`, `title`, `description` e `path`. Inclua `dueDate` somente se informada e liste em `attachments` cada arquivo que o portal deve disponibilizar para download.
6. Verifique a consistência: o `id` deve corresponder ao nome da pasta, `path` deve apontar para ela, o README e todos os anexos configurados devem existir, e os requisitos devem corresponder aos arquivos de apoio.
7. Resuma os arquivos criados e as alterações feitas no catálogo.

## Convenções

- Preserve a estrutura do portal estático; não adicione frameworks ou dependências para uma atividade sem necessidade explícita.
- Mantenha o idioma usado nos arquivos da atividade e use linguagem clara, acolhedora e apropriada ao nível dos alunos.
- Não invente prazos, anexos ou requisitos não pedidos. Se faltar uma decisão essencial para elaborar um exercício correto, pergunte antes de criá-lo.
- Crie arquivos de atividade com nomes descritivos e compatíveis com as convenções do projeto, como `README.md`, `starter-code.py` e `data.csv`.

---
name: new-assignment
description: Crie uma nova assignment de programação para estudantes da Mergington High School. Use esta skill sempre que o usuário quiser criar, adicionar, estruturar ou gerar uma nova assignment, exercício ou homework, mesmo que não use explicitamente a palavra "assignment".
---

# Criar Nova Tarefa de Programação

As assignments ficam em `assignments/<id>/`, e o site lê `config.json` para exibi-las. Siga estas etapas para criar ambos.

## Etapa 1: Coletar Requisitos

Se o usuário não tiver especificado, pergunte qual conceito de programação a assignment deve abordar.

> 📖 Leia [references/assignment-guide.md](references/assignment-guide.md) para orientações sobre dificuldade, escopo e quando incluir starter code.

## Etapa 2: Criar a Assignment

1. Crie `assignments/<kebab-case-id>/README.md` seguindo o [assignment template](../../../templates/assignment-template.md)
2. (Opcional) Adicione starter code ou arquivos de dados no mesmo diretório

## Etapa 3: Registrar no Website

Use os scripts incluídos; NÃO edite `config.json` manualmente.

**Registrar a assignment:**

    node .github/skills/new-assignment/scripts/update-config.js <id> "<title>" "<description>" [YYYY-MM-DD]

Informe a data de entrega no formato `YYYY-MM-DD` somente se o usuário tiver especificado um prazo.

**Registrar cada arquivo como attachment** (starter code, arquivos de dados etc.):

    node .github/skills/new-assignment/scripts/add-attachment.js <id> "<display-name>" <filename> <type>

Tipos comuns: `python`, `csv`, `json`, `txt`, `html`

## Etapa 4: Verificar

Confirme que a assignment foi registrada corretamente: verifique se `config.json` contém a nova entrada e se todos os arquivos criados existem no disco.