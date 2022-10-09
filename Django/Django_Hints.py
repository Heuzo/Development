# Вызов консоли django  >> python manage.py shell

# Способы создания записи в БД (Объекта модели)
#
#
# Способ 1:
news1 = News(title="Новость 1", content="Контент новости 1") 
news1.save()  

# Способ 2:
news1 = News()
news1.title = "Новость 1"
news1.content = "Контент новости 1"

# Способ 3:
news1 = News.objects.create(title="Новость 1", content="Контент новости 1") # Создаем объект с нужными данными и тут же сохраняем его

# Вывести выполненные запросы к БД (from django.db import connection) >> connection.queries

# Вывести все объекты (записи в БД) класса News >> News.objects.all() 
News.objects.all()

news = _   # Присваивает переменной значение предыдущего ответа/результата

# Проитерироваться по объектам класса, которые собраны в переменной news, и вывести их Название и флаг is_published
for item in news:
	print(item.title, item.is_published)

# --------Вывод----------
# Новость 1 True 
# Новость 2 True
# Ноовсть 3 True
# Новость 4 True
# Новость 5 True
# -----------------------
# Фильтрация объектов (записей БД) по определенному параметр >> News.objects.filter()
News.objects.filter(title='Новость 5')

for item in news:
	item.title = f'News {item.pk}'
	item.content = f'Content of news {item.pk}'
	print(item.title, item.content)
	item.save()
