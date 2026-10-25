# Publicar o Pulso no GitHub e no GitHub Pages

Este projeto tem dois modos: `index.html`/`server.py` para executar localmente e `docs/` para publicação estática no GitHub Pages.

## 1. Baixar os arquivos

1. Baixe `Pulso-GitHub-Pages-atualizado.zip` e extraia o conteúdo.
2. Abra a pasta extraída `pulso-apuracao`. Nela estão `index.html`, `server.py`, `docs`, `.github` e outros arquivos.

## 2. Enviar o projeto ao GitHub (método recomendado: GitHub Desktop)

Este método inclui a pasta oculta `.github`, necessária para a automação, e evita ter que enviar cada arquivo separadamente.

1. Baixe e instale o GitHub Desktop: https://desktop.github.com/.
2. Abra o GitHub Desktop e entre na sua conta GitHub.
3. No menu, escolha **File → New repository**.
4. Preencha **Name** com `pulso-apuracao`. Em **Local path**, escolha a pasta onde você costuma guardar seus projetos, por exemplo `Documents\GitHub`. O programa criará dentro dela uma pasta `pulso-apuracao`.
5. Para evitar arquivos conflitantes, deixe desmarcada a opção de iniciar o repositório com README e escolha **None** para `.gitignore` e licença. Clique em **Create repository**.
6. No Explorador de Arquivos, abra a pasta `pulso-apuracao` que veio do ZIP. Selecione **todo o conteúdo de dentro dela**, inclusive `.github` e `docs`, e copie.
7. No GitHub Desktop, use **Repository → Show in Explorer** para abrir a pasta do repositório local recém-criado. Cole ali todo o conteúdo copiado. Não coloque a pasta extraída `pulso-apuracao` como uma subpasta: copie os arquivos e pastas que estão dentro dela.
8. Se não conseguir ver a pasta `.github` no Explorador do Windows, ative **Exibir → Mostrar → Itens ocultos**. Confirme também no GitHub Desktop que aparece `.github/workflows/atualizar-apuracao.yml` entre os arquivos alterados.
9. Volte ao GitHub Desktop. Na área **Summary**, escreva `Publica primeira versão do Pulso` e clique em **Commit to main**.
10. Clique em **Publish repository**. Desmarque **Keep this code private** para que o repositório seja público e confirme a publicação. Com isso, o projeto será enviado para sua conta GitHub.

Depois de publicar, o código deverá aparecer em `https://github.com/Arthurreis99/pulso-apuracao`.

### Se o repositório já foi criado no site

No GitHub Desktop, escolha **File → Clone repository**, selecione `Arthurreis99/pulso-apuracao` e clone-o para o computador. Copie o conteúdo da pasta extraída para a pasta clonada, faça um commit e clique em **Push origin**.

### Alternativa com o terminal

Se você já usa Git, abra um terminal na raiz da pasta do projeto e execute `git init`, `git add .`, `git commit -m "Publica primeira versão do Pulso"`, `git branch -M main`, `git remote add origin https://github.com/Arthurreis99/pulso-apuracao.git` e `git push -u origin main`. Use esse caminho apenas se o repositório remoto ainda não existir ou estiver vazio; se `origin` já existir, não repita `git remote add origin`.

## 3. Configurar o Pages

1. Abra o repositório `https://github.com/Arthurreis99/pulso-apuracao`.
2. Entre em **Settings → Pages**.
3. Em **Build and deployment → Source**, escolha **GitHub Actions** (não escolha “Deploy from a branch”).
4. O workflow do projeto publica a pasta `docs` como artefato do Pages automaticamente. Faça isso depois que os arquivos já estiverem enviados.

## 4. Executar a primeira publicação

1. Abra a aba **Actions** do repositório.
2. Se aparecer a mensagem para permitir workflows, clique para habilitar as GitHub Actions.
3. Na lateral, escolha **Sincronizar TSE e publicar Pulso**.
4. Clique em **Run workflow**, mantenha a branch `main` e confirme **Run workflow**.
5. Abra a execução que aparecer. Aguarde que o trabalho fique verde com o ícone de sucesso. Entre no trabalho `publicar` para ver as etapas.
6. Volte a **Settings → Pages**. O GitHub mostrará o endereço do site assim que publicar.

Se o repositório se chamar `pulso-apuracao`, o endereço esperado é `https://arthurreis99.github.io/pulso-apuracao/`.

## Como funciona a atualização

- O workflow consulta o endpoint público do TSE e valida a estrutura do JSON.
- Em caso de sucesso, o arquivo atualizado é incorporado na publicação do Pages.
- Se o TSE estiver indisponível ou retornar dados inválidos, a publicação usa o último JSON válido que já estiver no repositório e registra um aviso na execução.
- O agendamento tenta publicar a cada 5 minutos. O GitHub pode atrasar execuções agendadas; isso não é um fluxo instantâneo. A página verifica o JSON publicado a cada 30 segundos.
- O Pages não executa `server.py`. Para executar a versão local com consulta mais frequente, use `iniciar.bat` no Windows.
- A pasta `docs` contém o `index.html` estático, o JSON de dados e o arquivo `.nojekyll`.

## Se der erro

- **O site mostra 404:** confira se está usando `Settings → Pages → Source: GitHub Actions`, e se a execução de publicação terminou com sucesso.
- **Não aparece o workflow na aba Actions:** confirme que `.github/workflows/atualizar-apuracao.yml` foi enviado ao repositório, que GitHub Actions está habilitado e que a branch padrão é `main`.
- **A publicação funciona, mas não aparecem votos:** abra a execução do workflow e leia a etapa de consulta ao TSE. O arquivo inicial é intencionalmente vazio para não simular resultados.
- **O site exibe versão antiga:** atualize sem cache com `Ctrl+F5` e consulte a execução mais recente na aba Actions.
- **O workflow falha na etapa do deploy:** confira `Settings → Pages` e as permissões de GitHub Actions; o workflow declara as permissões `pages: write` e `id-token: write`.

## Links

- Perfil do criador: https://github.com/Arthurreis99
- Criar repositório: https://github.com/new
- Documentação Pages: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
- Dados públicos do TSE: https://resultados.tse.jus.br/
