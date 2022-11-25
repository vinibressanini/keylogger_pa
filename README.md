## Python Keylogger

Com o Docker instalado, rode este comando para baixar a imagem do redis e iniciar um container

`docker run -p 6379:6379 --name redis-redisjson redislabs/rejson:latest`

Se tudo der certo o container estará executando. No Docker Desktop, vá até o container inicializado anteriormente e clique em `Open With Terminal`

![image](https://user-images.githubusercontent.com/91560062/199598798-0897983c-3b6d-44d2-9db3-a3fc41175ccd.png)

Uma vez dentro do Redis digite `redis-cli` para entrar. Pronto, a parte do banco está completa.

No VSCode de um clone do projeto. Se por acaso tiver algum erro nas importações do redis e/ou do keyboard, rode os seguintes comandos

`pip install redis`
`pip install keyboard`
`pip install rejson`

Por fim, no terminal rode `python test.py`, a aplicação começará a rodar e já poderá ser testada. No Docker Desktop aberto anteriormente rode o seguinte comando para verificar se as informações esão sendo coletadas

`json.get test`

O retorno será um JSON com o hostname e um array com a hora da captura e o status

![image](https://user-images.githubusercontent.com/91560062/204063668-0bb18178-567f-4e2b-a682-862c1912646a.png)


