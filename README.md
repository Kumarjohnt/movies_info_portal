## Movies Info Portal


**Tools And Technology Used**

1. Python3
2. Django
3. Django Rest Framework
4. PostgreSQL

**Notes**

* I am asuming that you already installed Python3, Git and PostgreSQL(11) in you system.
* Create a `env.py` as like as `example_env.py`.
* You have a database with same credentials as in `env.py`. If not then configure your own `env.py` file.
* You can run this project by simply downloading and executing `run.sh` script.
* Please execute `python manage.py shell` to scrap and seed initial data. 
 

**Bash File Execution Command**
> **`bash run.sh`**
> 

**Manually Project Execution Commands**
> **`pip install -r requirements.txt`**
>
> **`python manage.py makemigrations`**\
> **`python manage.py migrate`**
>
> **`python manage.py shell`**\
> **`from data_processor.processor import data_processor`**\
> **`data_processor()`**\
> **`exit()`**
>
> **`python manage.py runserver`**
> 

**When Python Shell Terminal Appears Please Execute This Commands**
> **from data_processor.processor import data_processor**\
> **data_processor()**


**After Complete Scraping Please Execute This Command To Exit From Python Shell**
> **exit()**

**Sample API Urls**

- http://127.0.0.1:8000/movie-info/api/v1/movies-list/?page=1&page_size=20

- http://127.0.0.1:8000/movie-info/api/v1/movie-details/1/
