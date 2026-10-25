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

O projeto mantém o site estático na pasta `docs/`. A publicação deve usar o recurso nativo do GitHub Pages por branch; o workflow sincroniza os dados e não faz deploy separado, para evitar conflito entre publicadores.

1. Abra o repositório `https://github.com/Arthurreis99/pulso-apuracao`.
2. Entre em **Settings → Pages**.
3. Em **Build and deployment → Source**, selecione **Deploy from a branch**.
4. Em **Branch**, selecione `main` e a pasta `/docs`; clique em **Save**.
5. O site esperado é `https://arthurreis99.github.io/pulso-apuracao/`.

Se a opção já estiver em `main / (root)`, o `index.html` da raiz redireciona automaticamente os visitantes do GitHub Pages para `/docs/`. A configuração recomendada, porém, é `main /docs`.

## 4. Verificar a sincronização de dados

1. Abra a aba **Actions** do repositório.
2. Procure **Sincronizar dados oficiais do TSE**.
3. A rotina é agendada para tentar atualizar o arquivo a cada 5 minutos. Para uma verificação imediata, abra a execução e clique em **Run workflow** com a branch `main`.
4. Abra o log da etapa **Consultar dados atuais do TSE (com cache-buster)**. Ela valida a estrutura do JSON e o horário indicado pelo TSE; se a resposta estiver antiga, preserva o último arquivo válido em vez de substituir os dados por uma cópia obsoleta.

A página também consulta o endpoint oficial do TSE diretamente no navegador a cada 30 segundos, usando o espelho do GitHub como fallback. Esse intervalo depende do navegador, da disponibilidade do TSE e da possibilidade de acesso entre domínios; não é uma garantia de atualização instantânea. Se não conseguir obter dados recentes, o painel avisa que a leitura pode estar desatualizada.

## Se der erro

- **O site mostra 404:** confira se está usando `Settings → Pages → Deploy from a branch → main /docs` e aguarde a execução nativa `pages build and deployment` terminar com sucesso.
- **Não aparece o workflow na aba Actions:** confirme que `.github/workflows/atualizar-apuracao.yml` foi enviado ao repositório, que GitHub Actions está habilitado e que a branch padrão é `main`.
- **A publicação funciona, mas não aparecem votos:** abra a execução de `Sincronizar dados oficiais do TSE` e leia a etapa de consulta. No site, confira o horário oficial e a fonte usada. Se a fonte do TSE estiver desatualizada, o painel mostra um aviso em vez de inventar votos.
- **O site exibe versão antiga:** atualize sem cache com `Ctrl+F5` e consulte a execução mais recente na aba Actions.
- **A publicação falha:** confira a execução nativa `pages build and deployment`. O workflow de sincronização de dados não faz deploy próprio, para evitar concorrência.

## Links

- Perfil do criador: https://github.com/Arthurreis99
- Criar repositório: https://github.com/new
- Documentação Pages: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
- Dados públicos do TSE: https://resultados.tse.jus.br/
