Migrations
```
python manage.py make migrations
python manage.py sqlmigrate news 0001 - sql preview
python manage.py migrate - run migrations
```

CRUD models shess
```
python manage.py shell - open django console

-- CREATE

# via object props
news1 = News()
news1.title = 'news1'
news1.content = 'news1 content'
news1.save()

//------------------------------//

# via News.objects.create
News.objects.create(title='title', content='content')

// -----------------------------//

# via constructor

news = News(title='title', content='content')
news.save()

-- READ

News.objects.all()
News.objects.get(pk=1)
News.objects.filter()
News.objects.exclude()
News.objects.order_by('id') # id ASC, -id DESC

-- UPDATE

news = News.objects.get(pk=1)
news.title = 'new title'
news.save()


-- DELETE

news = News.objects.get(pk=1)
news.delete()

```



