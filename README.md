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

O site público fica em `docs/`. O GitHub Pages publica essa pasta diretamente pela branch; o workflow `.github/workflows/atualizar-apuracao.yml` apenas sincroniza o JSON do TSE, evitando concorrência entre dois processos de deploy.

1. No repositório `Arthurreis99/pulso-apuracao`, abra **Settings → Pages**.
2. Em **Build and deployment → Source**, selecione **Deploy from a branch**.
3. Em **Branch**, escolha `main` e a pasta `/docs`; clique em **Save**.
4. Em **Actions**, confira as execuções de **Sincronizar dados oficiais do TSE**. O workflow também aceita execução manual por **Run workflow**.
5. O endereço esperado é [`https://arthurreis99.github.io/pulso-apuracao/`](https://arthurreis99.github.io/pulso-apuracao/).

O `index.html` da raiz redireciona visitantes do GitHub Pages para `/docs/` caso a publicação ainda esteja configurada para a raiz. A versão local no Windows continua usando `server.py` e `iniciar.bat`.

### Frequência e limitações
- A página tenta consultar o arquivo oficial do TSE diretamente a cada 30 segundos e tem duas fontes de fallback: o JSON do repositório e a cópia publicada em `docs/data/apuracao.json`.
- O GitHub Actions atualiza o espelho em intervalos programados de 5 minutos, que podem atrasar. O workflow usa cache-buster e valida o horário do arquivo; se a fonte continuar antiga, preserva a última cópia e a página sinaliza que os dados podem estar desatualizados.
- O GitHub Pages não executa `server.py`. Para executar a versão local, use `iniciar.bat` no Windows.

## Visualizações
1. Votos por candidato.
2. Participação percentual.
3. Evolução ao longo das atualizações observadas neste navegador.
4. Composição de votos válidos, brancos e nulos.

O histórico de evolução é local ao navegador. Os resultados dependem da disponibilidade da fonte oficial do TSE. O Pulso é um projeto independente e não é afiliado ao Tribunal Superior Eleitoral.
