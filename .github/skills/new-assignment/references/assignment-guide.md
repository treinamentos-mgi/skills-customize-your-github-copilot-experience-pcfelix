# Guia para criar atividades

Use este guia para definir uma atividade clara, adequada ao curso e viável para os alunos concluírem.

## Definir objetivo e escopo

- Organize a atividade em torno de um conceito principal, como variáveis, condicionais, laços, funções, classes ou análise de dados.
- Escreva o objetivo como uma habilidade que o aluno demonstrará ao concluir a atividade.
- Considere o conteúdo das atividades existentes para evitar exigir conceitos que ainda não foram apresentados. Se um pré-requisito for necessário, declare-o.
- Mantenha cada tarefa pequena o bastante para que o aluno consiga implementar e verificar o resultado incrementalmente.
- Divida trabalhos maiores em tarefas sequenciais, cada uma com uma entrega observável.

## Ajustar a dificuldade

- **Inicial:** pratique um ou poucos conceitos já introduzidos, com entradas, saídas e passos bem definidos.
- **Intermediária:** combine conceitos conhecidos em uma solução com várias etapas, mantendo claro o resultado esperado.
- **Avançada:** proponha decisões de implementação e integração de conceitos, mas explicite os critérios de conclusão e os pré-requisitos.

Não aumente a dificuldade apenas adicionando bibliotecas, muitos requisitos ou configurações. Inclua dependências externas somente quando forem necessárias para o objetivo e explique como elas serão usadas.

## Escrever tarefas e requisitos

- Siga a estrutura e os títulos do [template de atividade](../../../../templates/assignment-template.md).
- Descreva ações concretas para o aluno, evitando instruções vagas como “explore o tema” sem uma entrega definida.
- Faça cada requisito ser verificável: indique o comportamento esperado, os dados envolvidos e, quando útil, exemplos de entrada e saída.
- Inclua casos importantes, como valores inválidos ou limites, apenas quando fizerem parte do objetivo da atividade.
- Garanta que os requisitos não dependam de informações ou arquivos que não foram fornecidos.

## Decidir se deve incluir código inicial

Inclua `starter-code.py` quando ele ajudar o aluno a começar, por exemplo, ao fornecer assinaturas de funções, estrutura de um programa ou configuração repetitiva. Para exercícios curtos, deixe o aluno começar do zero se isso fizer parte do aprendizado.

Quando houver código inicial:

- Mantenha-o executável ou indique claramente os pontos que o aluno precisa completar.
- Use nomes de funções, parâmetros e variáveis coerentes com os requisitos do README.
- Inclua apenas imports, estruturas e dados necessários para a atividade.
- Não forneça a solução completa, salvo se o usuário solicitar explicitamente uma solução ou exemplo resolvido.

## Usar dados e anexos

- Inclua `data.csv` quando os alunos precisarem de um conjunto de dados fornecido para completar a atividade; mantenha-o pequeno e adequado ao objetivo.
- Liste em `config.json` cada arquivo que deve aparecer como anexo para download, com nome de exibição e tipo corretos.
- Não crie anexos redundantes nem invente arquivos que a atividade não utiliza.

## Revisão final

- O objetivo corresponde ao que as tarefas ensinam?
- Cada requisito pode ser conferido pelo aluno ou por uma revisão simples?
- O README, o código inicial e os dados descrevem a mesma atividade?
- Os nomes e caminhos dos arquivos correspondem ao diretório e aos anexos registrados em `config.json`?
- O texto é acolhedor, está no idioma adequado e não revela a solução antes de o aluno tentar?

# Assignment Design Guide

Orientações para desenhar conteúdo de assignment: o que ensinar e como definir o escopo. Para formatação e estrutura em markdown, os arquivos de instruções do projeto já tratam isso automaticamente.

## Difficulty & Scope

- Defina de 2 a 4 tarefas por assignment que evoluam entre si
- Comece com algo que um aluno consiga terminar em menos de 10 minutos e depois aumente a complexidade
- A última tarefa pode ser um objetivo ambicioso, mas as anteriores devem construir confiança
- Foque em um conceito central por assignment (ex.: "loops", não "loops + file I/O + error handling")

## Starter Code

Inclua starter code quando:

- A assignment precisar de boilerplate que o estudante não deve escrever do zero
- Você quiser que os estudantes sigam uma assinatura de função ou estrutura específica

Evite quando o objetivo for escrever algo do zero (ex.: "write a script that...").

## Exemplos de Tópicos por Dificuldade

- **Beginner**: variables, conditionals, loops, string formatting
- **Intermediate**: functions, lists/dicts, file I/O, basic classes
- **Advanced**: APIs, data analysis, testing, web frameworks
