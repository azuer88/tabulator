## tabulator

Allows panel of judges to input contestant scores for automatic tabulation of winners


# Development Setup

1. Install pre-requisite development tools:

  a. Git
  b. pip


2. Install virtualenvwrapper: (see (http://virtualenvwrapper.readthedocs.org/en/latest/install.html) [virtualenvwrapper docs]


3. Create a virtualenv project
   ```mkvirtualenv tabulator```


4. Install the dependencies in the 'requirements.txt'
    ```pip install -r requirements.txt```
   N.B.: make sure you install libxml2-dev, libxslt-dev, and python-dev


5. create database
    ```
    ./manage.py makemigrations 
    ./manage.py migrate
    ./manage.py migrate contest
    ```


6. create super user
    ```./manage.py createsuperuser```


7. load fixtures, it seems initial_data is no longer automatically loaded.
    ```./manage.py loaddata initial_data```

