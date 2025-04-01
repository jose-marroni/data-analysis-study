# Estudo de Analise de Dados
Repositório destinado ao estudo de analise de dados do curso da EBAC

## Explicação das atividades realizadas no modulo 1:

#Criando diretório atividade
root@LAPTOP-4J28AV5A:~# mkdir /home/jose/modulo1/linux/atividade

#Entrando no diretório atividade
root@LAPTOP-4J28AV5A:~# cd /modulo1/linux/atividade

#Criando arquivo .sh
root@LAPTOP-4J28AV5A:/home/jose/modulo1/linux/atividade# nano tarefa.sh

#Dando permissão de execução 
root@LAPTOP-4J28AV5A:/home/jose/modulo1/linux/atividade# chmod 744 tarefa.sh
root@LAPTOP-4J28AV5A:/home/jose/modulo1/linux/atividade# ll
total 16
drwxr-xr-x 2 root root 4096 Nov  8 12:42 ./
drwxr-xr-x 3 root root 4096 Nov  8 12:34 ../
-rw-r--r-- 1 root root  645 Nov  8 12:16 calculadora.py
-rwxr--r-- 1 root root  250 Nov  8 12:42 tarefa.sh*
root@LAPTOP-4J28AV5A:/home/jose/modulo1/linux/atividade#

#Execução do script da calculadora 
root@LAPTOP-4J28AV5A:/home/jose/modulo1/linux/atividade# ./tarefa.sh
Iniociando a calculadora
Informando o diretorio atual: /home/jose/modulo1/linux/atividade
 Calculadora ativa informe os numeros e selecione a operação
Digite o primeiro numero: 2
Digite o segundo numero: 2
selecione a operação onde soma é 0, subitracao é 1, divisao é 2, multiplica é 3: 3
4.0
