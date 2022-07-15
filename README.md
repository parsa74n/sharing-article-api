# sharing-article-api

## How start project:


#### Clone the repository :
```bash
$ git clone https://github.com/parsa74n/sharing-article-api.git
$ cd sharing-article-api
```

#### Create a virtualenv and activate it:
 ```bash
$ python3 -m venv venv
$ . venv/bin/activate
```

#### Or on Windows cmd : 
 ```bash
> python3.exe -m venv venv
> venv\Scripts\activate.ps1
```

#### Install the requirements :
```bash
$ pip3 install -r requirements.txt
```




####  Run makemigrations and migrate :
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

#### Run the development server :
```bash
python3 manage.py runserver
```

Open http://127.0.0.1:8000 in your browser. 


#### example (registering)
in postman or other application send post request with json format boby to http://127.0.0.1:8000/accounts/register/ :
```json data example
{
    "username":"example",
    "phone_number":12345,
    "email":"example@email.com",
    "password1":"pass",
    "password2":"pass"
}
```

