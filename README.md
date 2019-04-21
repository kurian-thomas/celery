
# Scrapy project with celery beat schedule
This repository contains the code for scraping book details from flipkart in a scheduled manner using user agents

## Technologies used
1. python3
1. Scrapy
1. Redis (Broker)
1. Celery (Scheduler)

## Steps for running

1. #### Clone the repository
    > git clone https://github.com/kurian-thomas/celery

1. #### Create a virtual environment if required
    > virtual env -p python3 env
    ##### activate the virtual environment
    > source env/bin/activate
    
1. #### Install the requirements
    > pip install -r requirements.txt

1. #### Install redis if not installed and make sure it is running in port number 6379
    > sudo apt-get install redis
    ##### Check if redis is installed
    > $ redis-cli ping
    ##### (should return PONG)

1. #### Set up local database
    install mysql

    $ pip install mysqlclient

    go to mysql.py and flipkart_spider.py file 
        add your username,password and database in the empty quotes
    $ python mysql.py 


1. ####  Run celery with beat schedule
    > celery -A celery_script worker --loglevel=info -B 


