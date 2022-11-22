## Python Keylogger

Com o Docker instalado, rode este comando para baixar a imagem do redis e iniciar um container

`docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest`

Se tudo der certo o container estará executando. No Docker Desktop, vá até o container inicializado anteriormente e clique em `Open With Terminal`

![image](https://user-images.githubusercontent.com/91560062/199598798-0897983c-3b6d-44d2-9db3-a3fc41175ccd.png)

Uma vez dentro do Redis digite `redis-cli` para entrar. Pronto, a parte do banco está completa.

No VSCode de um clone do projeto. Se por acaso tiver algum erro nas importações do redis e/ou do keyboard, rode os seguintes comandos

`pip install redis`
`pip install keyboard`

Por fim, no terminal rode `python test.py`, a aplicação começará a rodar e já poderá ser testada. No Docker Desktop aberto anteriormente rode o seguinte comando para verificar se as informações esão sendo coletadas

`json.get activity`

Por enquanto só retornará a última verificação de atividade em formato JSON

