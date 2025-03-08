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