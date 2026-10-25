# Pulso — Painel de apuração presidencial 2026

Painel eleitoral responsivo de autoria de **Arthur Medeiros**. Inclui temas claro/escuro, glassmorphism com iluminação azul, quatro visualizações de dados, progresso de totalização e cartões de candidatos. O painel não gera votos fictícios.

- GitHub do criador: https://github.com/Arthurreis99
- Fonte pública de dados: https://resultados.tse.jus.br/
- Endpoint configurado: `https://resultados.tse.jus.br/oficial/ele2026/6258/dados/br/br-c0001-e006258-u.json`
- Portal técnico do TSE: https://www.tse.jus.br/eleicoes/informacoes-tecnicas-sobre-a-divulgacao-de-resultados

## Executar online

Execute a versão online no seu navegador pelo site oficial: https://arthurreis99.github.io/pulso-apuracao

## Executar localmente

A versão local usa `server.py` como uma ponte para consultar o TSE com maior frequência e evita depender de CORS do navegador.

### Windows
1. Instale Python 3: https://www.python.org/downloads/.
2. Extraia todos os arquivos desta pasta.
3. Execute `iniciar.bat`.
4. Abra `http://127.0.0.1:8000` no navegador.

### Linux/macOS
Entre no diretório do projeto e execute `python3 server.py`. Depois abra `http://127.0.0.1:8000`. Encerre com `Ctrl+C`.

## Publicar no GitHub Pages

O GitHub Pages hospeda arquivos estáticos e não executa Python. A pasta `docs/` contém a versão estática do painel. O workflow `.github/workflows/atualizar-apuracao.yml` consulta o TSE, atualiza `docs/data/apuracao.json` em tempo de execução e publica a pasta `docs` via GitHub Pages.

1. Extraia o ZIP e instale o GitHub Desktop: https://desktop.github.com/.
2. No GitHub Desktop, crie um repositório local chamado `pulso-apuracao`, copie para ele o conteúdo desta pasta (incluindo `.github/` e `docs/`), faça um commit e escolha **Publish repository**. Deixe o repositório público.
3. No repositório publicado, abra **Settings → Pages** e defina **Source: GitHub Actions**.
4. Na aba **Actions**, execute manualmente **Sincronizar TSE e publicar Pulso** com **Run workflow**.
5. Quando a execução finalizar com sucesso, abra o endereço indicado em **Settings → Pages**. Para o repositório `pulso-apuracao`, o endereço esperado é `https://arthurreis99.github.io/pulso-apuracao/`.

Consulte `GUIA-GITHUB-PAGES.md` para o tutorial completo, detalhes da interface do GitHub Desktop e dicas de solução de problemas.

### Frequência e limitações
- A página consulta o JSON publicado a cada 30 segundos; a publicação busca o TSE a cada 5 minutos. O agendamento do GitHub Actions pode atrasar, portanto não é uma conexão instantânea de 30 segundos.
- O workflow publica o site mesmo se houver indisponibilidade temporária do TSE, usando o último JSON válido já existente no repositório. O primeiro JSON contém dados vazios intencionalmente.
- O site local consulta através do servidor Python; o modo Pages não executa `server.py`.

## Visualizações
1. Votos por candidato.
2. Participação percentual.
3. Evolução ao longo das atualizações observadas neste navegador.
4. Composição de votos válidos, brancos e nulos.

O histórico de evolução é local ao navegador. Os resultados dependem da disponibilidade da fonte oficial do TSE. O Pulso é um projeto independente e não é afiliado ao Tribunal Superior Eleitoral.
