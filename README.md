

# 🛸 ProjectOVNIA

![jQIkv9s](https://github.com/user-attachments/assets/34e197cb-f018-4370-a5aa-105e65c8bf61)


Submódulo de inteligência artificial desenvolvido para ser implementado no [Whois Alien](https://github.com/christopherrissardi/Whois-Alien-Bot) e extraído para testes independentes. Inicialmente, o mecanismo de IA utilizava os motores do [gpt4free](https://github.com/xtekky/gpt4free), mas isso se mostrou inviável, pois o gpt4free dependia de cookies de sessão para funcionar. Toda vez que o histórico do navegador era limpo, o cookie era alterado, interrompendo o uso contínuo.

Testei várias maneiras de integrar o chatbot, mas não encontrei uma solução viável e confiável para esse problema.

Embora o uso dos cookies tornasse a implementação funcional, todos os prompts enviados pelos usuários no servidor eram visíveis para mim, pois o sistema funcionava com meu navegador como "intermediador". Isso levantou sérias questões éticas e de privacidade, já que os dados dos usuários ficariam vinculados à minha conta, o que considero uma invasão de privacidade.

Esse mini-projeto foi feito apenas como um experimento para testar funcionalidades de um repositório de terceiros. Não levei a implementação adiante, pois não concordo com a ideia de centralizar cookies de sessão em uma única pessoa, especialmente em um contexto comunitário.

Se, na época em que eu estava testando, existisse um método alternativo ao uso de cookies, eu provavelmente teria implementado o projeto de forma definitiva. No entanto, confesso que, durante os testes, esse foi o único método que encontrei para fazê-lo funcionar.

---

- Consulte o repositório do gpt4free: https://github.com/xtekky/gpt4free
- Repositório do Projeto: https://github.com/christopherrissardi/Ovnia-IA
