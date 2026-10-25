# Configurar o chat comunitário do Pulso

O widget já está no site. Para enviar e carregar mensagens em tempo real, conecte-o a um **Firebase Realtime Database**. O HTML e este arquivo de configuração continuam no GitHub Pages; as mensagens ficam no banco em tempo real. Não coloque um token pessoal do GitHub no navegador: qualquer visitante poderia extraí-lo e modificar o repositório.

## 1. Criar o projeto Firebase

1. Abra https://console.firebase.google.com/ e crie um projeto, por exemplo, `pulso-chat`.
2. Em **Visão geral do projeto**, adicione um aplicativo **Web** (ícone `</>`). Dê um nome como `Pulso Chat`.
3. Na configuração do app Web, copie os valores `apiKey`, `authDomain`, `databaseURL`, `projectId` e `appId`.

## 2. Ativar login anônimo

Em **Authentication → Sign-in method**, habilite **Anonymous / Anônimo**. O visitante não precisa preencher cadastro: isso só dá ao banco uma identidade anônima por navegador, necessária para aplicar regras de acesso.

## 3. Criar o banco em tempo real

Em **Build → Realtime Database**, clique para criar o banco e escolha a região. Abra a aba **Rules / Regras** e substitua as regras pelo JSON abaixo. Clique em **Publish / Publicar**.

```json
{
  "rules": {
    "messages": {
      ".read": "auth != null",
      ".indexOn": ["createdAt"],
      "$messageId": {
        ".write": "auth != null && !data.exists()",
        ".validate": "newData.hasChildren(['name', 'text', 'senderId', 'createdAt'])",
        "name": {
          ".validate": "newData.isString() && newData.val().length > 0 && newData.val().length <= 32"
        },
        "text": {
          ".validate": "newData.isString() && newData.val().length > 0 && newData.val().length <= 500"
        },
        "senderId": {
          ".validate": "newData.isString() && newData.val() === auth.uid"
        },
        "createdAt": {
          ".validate": "newData.isNumber()"
        },
        "$other": {
          ".validate": false
        }
      }
    },
    "presence": {
      ".read": "auth != null",
      "$uid": {
        ".write": "auth != null && auth.uid === $uid",
        "$connectionId": {
          ".validate": "newData.val() === true"
        }
      }
    }
  }
}
```

Essas regras exigem autenticação anônima, deixam o histórico legível para visitantes autenticados, validam tamanho e tipo das mensagens e impedem que o cliente edite mensagens já criadas. O chat ainda é público: não publique informações pessoais. As regras não constituem um sistema completo de prevenção a spam.

## 4. Colar a configuração no repositório

Abra `docs/chat-config.js` no GitHub e preencha os cinco campos com os valores reais do app Web. O `databaseURL` precisa ser exatamente o mostrado na página do Realtime Database (o formato varia por região). Salve a alteração. Não apague nem altere os campos de configuração do HTML.

Exemplo de formato (valores ilustrativos, não use estes):

```js
window.PULSO_FIREBASE_CONFIG = {
  apiKey: "AIza...",
  authDomain: "pulso-chat.firebaseapp.com",
  databaseURL: "https://pulso-chat-default-rtdb.firebaseio.com",
  projectId: "pulso-chat",
  appId: "1:123456789:web:abc123"
};
```

## 5. Testar

Depois que o GitHub Pages publicar a alteração, abra o Pulso em duas janelas/dispositivos. Envie mensagens entre elas, feche o chat em uma delas e confirme o contador verde de mensagens novas. O indicador de presença conta navegadores autenticados anonimamente com conexão ativa.

O plano gratuito Spark do Firebase não exige inserir cartão para começar, mas tem limites de uso. Acompanhe as cotas do projeto no console.
