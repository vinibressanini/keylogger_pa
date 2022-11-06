## Python Keylogger

Primeiro, com o Docker instalado, rode o seguinte comando no CMD para baixar uma imagem do Redis

`docker pull redis`

Rode `docker images` e veja o que está escrito na tag da imagem do Redis

![image](https://user-images.githubusercontent.com/91560062/199598053-ab8e4be9-9709-42d9-8c3c-b496e841aef6.png)

Depois esse para rodar um container. Após o `redis:` coloque a tag

`docker run -d -p 6379:6379 -i -t redis:latest` 

Se tudo der certo o container estará executando. No Docker Desktop, vá até o container inicializado anteriormente e clique em `Open With Terminal`

![image](https://user-images.githubusercontent.com/91560062/199598798-0897983c-3b6d-44d2-9db3-a3fc41175ccd.png)

Uma vez dentro do Redis digite `redis-cli` para entrar. Pronto, a parte do banco está completa.

No VSCode de um clone do projeto. Se por acaso tiver algum erro nas importações do redis e/ou do keyboard, rode os seguintes comandos

`pip install redis`
`pip install keyboard`

Por fim, no termimal rode `python test.py`, a aplicação começará a rodar e já poderá ser testada. No Docker Desktop aberto anteriormente rode o seguinte comando para verificar se as informações etão sendo coletadas

`LRANGE activity 0 -1`

O resultado deverá ser parecido com isso

![image](https://user-images.githubusercontent.com/91560062/200194978-a74d6298-fda0-474f-a39a-0390659aadee.png)

