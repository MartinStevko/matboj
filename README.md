# Matboj

Below you can find manual how to setup `matboj` project locally on your own computer.

First of all, download ZIPped `matboj` project from GitHub using big green button. Then unzip it.

## Requirements installation

 - Python (3 or later, version 3.7.0 recommended)
 - Django (version 2.1 or later)
 - virtual enviroment (not necessary)


## Python installation

### Windows machine
Install Python from https://www.python.org/downloads/ and then in CMD type:

### Linux machine
In Bash type:

```bash
sudo apt install pip
```


## Virtual enviroment setup

You can skip this step if you don't want to install virtual enviroment.

### Windows machine
In CMD type:

```cmd
py -m pip install virtualenv
```

Create virtual enviroment
```cmd
py -m venv ENV_NAME
```

Activate your virtual environment:
```cmd
ENV_NAME\Scripts\activate
```

### Linux machine
In Bash type:

```bash
python3 -m pip install virtualenv
```

Create virtual enviroment
```cmd
virtualenv -p python3 ENV_NAME
```
and allow remote acces for desired port:
```bash
iptables -I INPUT -p tcp -m tcp --dport PORT_NUMBER -j ACCEPT
```

Activate your virtual environment:
```bash
source ENV_NAME/bin/activate
```


## Django setup

### Windows machine
In CMD type:

```cmd
py -m pip install django==2.1
```

### Linux machine
In Bash type:

```bash
python3 -m pip install Django==2.1
```


## Base database creation

First go to `matboj-master` directory. 
Afterwards make and then apply migrations. You can do it by typing:

- for Windows in CMD:
    ```
    python manage.py makemigrations diary
    ```
    ```
    python manage.py migrate
    ```

- or for Linux in Bash:
    ```
    python manage.py makemigrations diary
    ```
    ```
    python manage.py migrate
    ```


## Run server

### Windows machine

In CMD:

1. Go to `matboj-master` directory
2. Activate your virtual environment:
```cmd
ENV_NAME\Scripts\activate
```
3. Run server on your desired port:
```cmd
python manage.py runserver 0.0.0.0:PORT_NUMBER
```

### Linux machine

1. Login as root user

In Terminal:

2. Go to `matboj-master` directory
3. Activate your virtual environment:
```bash
source ENV_NAME/bin/activate
```
4. Run server on your desired port:
```bash
python manage.py runserver 0.0.0.0:PORT_NUMBER
```

## Application access

After all that you can access to admin site by typing `localhost:PORT_NUMBER/admin/` and to app by typing `localhost:PORT_NUMBER/matboje/` (`localhost` can be substituted by an IP address of server e.g. `192.168.1.47`).
