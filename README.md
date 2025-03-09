WebScraper Project on Python.

# Working with Python Virtual Environment
create virtual environment
```
PS> py -m venv venv\
```

activate it
```
PS> venv\Scripts\activate
```

install packages into it
```
(venv) PS> python -m pip install <package-name>
```

deactivate it
```
(venv) PS> deactivate
```

# Working with scrapy
**Install**
```
(venv) $ python -m pip install scrapy
```
test that its installed 
```
scrapy 
```
**Create new project in Scrapy**
```
(venv) $ scrapy startproject <project-name>
```
**Test data extraction with Scrapy Shell**
```
(venv) $ scrapy shell https://google.com
```

**Create items that will hold scraped data**
File: projectname/items.py
```Python
import scrapy

class BooksItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
```
**Create spider**
```
(venv) $ cd books/
(venv) $ scrapy genspider book https://books.toscrape.com/
Created spider 'book' using template 'basic' in module:
  books.spiders.book
```
**Run spider**
```
(venv) $ cd books/
(venv) $ scrapy crawl <spider-name>
```
**Configure Pipeline**
- (After MongoDB is configured)
- in the pipelines.py create a class with methods from_crawler, open_spider, close_spider, process_item
  - process_item should contain the logic to clean item's data and save it into the database 
- in settings.py configure ITEM_PIPELINES dict - key should be identifier of a newly created Pipeline class and as a value should be priority, that this pipeline should have.

# Working with MongoDB (ver 8.0.5)
- install MongoDB Server (mongod)
- install MongoDB Shell (mongosh)

**Open shell and create database "laptops_db" and a collection "laptops" within it**
```
$> mongosh
test> use laptops_db
switched to db laptops_db
laptops_db> db.createCollection("laptops")
{ ok: 1 }
laptops_db> show collections
laptops
```

# Connect to MongoDB from Python code
**Install pymongo library**
```
(venv) $ python -m pip install pymongo
```
**Add connection info**
- in the settings.py (scrapy_project1/settings.py) add connection info
```
MONGO_URI = "mongodb://localhost:27017"
MONGO_DATABASE = "laptops_db"
```
**Check that items are inserted in the database**
```
laptops_db> db.laptops.countDocuments()
```