# Instrucoes do projeto

- Este projeto e um portal estatico feito com HTML, CSS e JavaScript puro. Evite adicionar frameworks, dependencias ou ferramentas de build sem necessidade explicita.
- Use `config.json` como fonte de dados do curso e das atividades. Nao duplique nos scripts os dados que ja estao configurados nesse arquivo.
- Ao alterar uma atividade, mantenha coerentes sua entrada em `config.json`, a pasta indicada em `path`, o `README.md` da atividade e os arquivos listados em `attachments`.
- Preserve a estrutura existente em `assignments/` e o estilo dos arquivos proximos. Mantenha o idioma usado no arquivo que estiver editando.
- Preserve os comportamentos e caminhos relativos usados pelas paginas. Ao alterar a interface, confira tanto a lista de atividades quanto a pagina de detalhes.
- Evite inserir em `innerHTML` valores externos ou fornecidos por usuarios; prefira APIs seguras do DOM sempre que possivel.

# Descrição do Projeto

Este projeto é um site educacional para compartilhar tarefas e exercícios de programação com os alunos. Os alunos podem navegar, visualizar e baixar tarefas diretamente pelo portal.

## Estrutura do Projeto

- [`assignments/`](../assignments/) Cada tarefa é armazenada em sua própria subpasta com uma estrutura consistente.
- [`templates/`](../templates/) Templates reutilizáveis para novo conteúdo
- [`assets/`](../assets/) Contém os recursos do site incluindo CSS, JavaScript, imagens e arquivos de configuração
- [`index.html`](../index.html) A página principal do site que serve como um portal estático para navegar e visualizar tarefas. O conteúdo é configurável via arquivo [`config.json`](../config.json) para gerar dinamicamente listas e detalhes das tarefas.

## Diretrizes do Projeto

- Manter estilo consistente em todas as páginas
- Manter nomes de arquivos e pastas descritivos e organizados

## Padrões Educacionais

Ao gerar conteúdo para este projeto:

- **Foco no aprendizado**: Todo conteúdo deve ser elaborado com objetivos de aprendizado claros e níveis de dificuldade apropriados
- **Amigável ao aluno**: Usar linguagem clara e encorajadora que motive os alunos