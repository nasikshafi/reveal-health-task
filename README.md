# reveal-health-task
Reveal health task to create simple CURD api for an article

Steps to run application 

- install requiements "pip install -r requirements.txt"
- migrate database "python manage.py migrate"
- run server  "python manage.py runserver"


API Description:
1. GET list of Articles 
request url - http://baseurl/article
response - list of article exist else empty list

2. DELETE article 
request url - http://baseurl/article/<title>
response - success message if deleted else not fould 

3. POST - create article 
request url - http://baseurl/article
request body - {
    "title":"testing1",
    "author_id":2,
    "category":"test category1"
    }
response - 201 on successfull create with created data in response 

4.PATCH - update article
request url - http://baseurl/article/<title>
request body -  {
    "title":"testing2",
    "author_id":2,
    "category":"test category2"
    }
response - 200 on success update and 404 if data not found 


