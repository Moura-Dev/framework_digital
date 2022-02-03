# Desafio Framework_digital

### Pré-requisitos
* [ ] Python 3.x 
* [ ] Virtualenv

### Criando Virtualenv
```
python3-m virtualenv venv
```

### Instalando as bibliotecas

```
pip install -r requirements.txt
```

### Executando o projeto

```
export FLASK_APP="manage.py" webscraping.py
flask run
```

### Logger

Aplicação salvara o logger nos arquivos:
```
sucess.log
error.log

```


### Endpoint Login
```
http://localhost:5000/login/
Basic Auth
Username: framework_digital
Password: secret

Return 
{token: token}
```



### Endpoint Request Json Place holder
```
http://localhost:5000/
Bearer Auth
token
```