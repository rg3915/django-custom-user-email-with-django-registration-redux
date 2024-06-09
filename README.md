# django-custom-user-email-with-django-registration-redux

Django com usuário customizado para fazer login com email.

E usa [django-registration-redux](https://django-registration-redux.readthedocs.io/en/latest/) para fazer o gerenciamento de login, reset de senha, entre outros.


**Github:** https://github.com/macropin/django-registration

**Doc:** https://django-registration-redux.readthedocs.io/en/latest/

## Este projeto foi feito com:

* [Django 5.0.6](https://www.djangoproject.com/)
* [django-registration-redux](https://django-registration-redux.readthedocs.io/en/latest/)

## Instalação

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/rg3915/django-custom-user-email-with-django-registration-redux.git
cd django-custom-user-email-with-django-registration-redux

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

python contrib/env_gen.py

python manage.py migrate
python manage.py createsuperuser --username="admin" --email=""

python manage.py runserver
```

Baseado em [django-custom-login-email](https://github.com/rg3915/django-custom-login-email)

<a href="https://youtu.be/dXdMD3LBUvA">
    <img src="img/youtube.png">
</a>
