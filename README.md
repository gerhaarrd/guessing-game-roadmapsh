# ​ Number Guessing Game (CLI)

[![](https://img.shields.io/badge/Projeto-Number%20Guessing%20Game-blue)](https://roadmap.sh/projects/number-guessing-game)

Um jogo simples de **adivinhação de números** no terminal, inspirado no desafio do [roadmap.sh](https://roadmap.sh/projects/number-guessing-game). O computador seleciona um número aleatório entre 1 e 100, e o jogador deve adivinhá-lo com um número limitado de tentativas, definido pela dificuldade escolhida.

---

##  Regras do Jogo

1. O computador escolhe **aleatoriamente** um número entre **1 e 100**.
2. O jogador escolhe o nível de dificuldade:
   - **Easy** → 10 tentativas  
   - **Medium** → 5 tentativas  
   - **Hard** → 3 tentativas  
3. O jogador faz palpites até:
   - Acertar: o jogo mostra o número de tentativas usadas e o tempo gasto;
   - Errar: indica se o número é **maior** ou **menor** que o palpite.
4. O jogo termina quando o jogador:
   - Acerta o número ou  
   - Esgota as tentativas.

---

##  Funcionalidade Extra

- **Timer** que mede o tempo que o jogador leva para acertar o número.

---

##  Exemplo de Uso

```text
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Please select the difficulty level:
1. Easy (10 attempts)
2. Medium (5 attempts)
3. Hard (3 attempts)
Enter your choice: 2
Great! You have 5 attempts.
Let's start the game!

Enter your guess: 50
Incorrect! The number is less than 50.
You have 4 attempts left.

Enter your guess: 25
Incorrect! The number is greater than 25.
You have 3 attempts left.

Enter your guess: 30
Congratulations! You guessed the correct number in 3 attempts and 12.47 seconds.
