# Вебсайт "Куда сходить"

 Интерактивная карта Москвы, на которой показаны места, где предлагается проведение активного отдыха, с подробными описаниями и комментариями. 

 ### Где посмотреть
 Вы можете посомтреть пример работы сайта по адресу [breath.pythonanywhere.com](https://breath.pythonanywhere.com/)
 
 ### Как установить

 У вас должен быть установлен Python3. Скачайте репозиторий.  
 Установите зависимости:
 ```
 pip install requirements.txt
 ```
 Настройте переменные окружения. Для этого создайте файл `.env` в корне проекта рядом с файлом `manage.py`.
 Запишите в этот файл секретный ключ своего проекта:
 ```
 SECRET_KEY=[SECRET_KEY]
 ```

 ### Запуск

 Для запуска со своего компьютера создайте базу данных в формате `.sqlite3`, установив миграции:
 ```
 python migrate
 ```
 Создайте аккаунт администратора:
 ```
 python createsuperuser
 ```
 Запустите сервер:
 ```
 python runserver
 ```
 По-умолчанию сайт доступен по адресу [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

 ### Добавление данных через административную часть сайта

 - Перейдите в админку по адресу [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
 - Введите данные аккаунта администратора.

 В разделе `Места` добавьте новое место и заполните название, описание, координаты. Добавьте фотографии.

 ## Для разработчиков

 В файле `.env` вы можете указать следующие параметры:
 `DEBUG` - режим отладки. Принимает булевое значение. По-умолчанию - False.
 `ALLOWED_HOSTS` - При деплое нужно через запятую перечислить имены доменов, на которых будет размещен сайт.

 Данные для объектов на карте формируются в виде JSON и передаются на фронтенд:
 ```python
 # places/views.py

 def index_map(request):
    template = 'index_map.html'
    places_geojson = {
            'type': 'FeatureCollection',
            'features': [],
    }
    for place in Place.objects.all():
        feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.lng, place.lat],
            },
            'properties': {
                'title': place.title,
                'placeId': place.placeId,
                'detailsUrl': reverse('place_details', args=[place.id])
            },
        }
        places_geojson['features'].append(feature)
    context = {'places_geojson': places_geojson}
    
    return render(request, template, context=context)
 ```
 Данные передаются в [формате GeoJSON](https://ru.wikipedia.org/wiki/GeoJSON). Все поля здесь стандартные, кроме `properties`. Внутри `properties` лежат специфичные для проекта данные:

* `title` — название локации
* `placeId` — уникальный идентификатор локации, строка или число
* `detailsUrl` — адрес для скачивания доп. сведений о локации в JSON формате

 Значение поля `placeId` может быть либо строкой, либо числом. Само значение не играет большой роли, важна лишь чтобы оно было уникальным. Фронтенд использует `placeId` чтобы избавиться от дубликатов — если у двух локаций одинаковый `placeId`, то значит это одно и то же место.  

 В поле `detailsUrl` передается ссылка на JSON c подробными сведениями о локации. Данные формируются при передаче `id` локации:

 ```python
 # places/views.py

 def get_place_details(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    place_details = {
        'title': place.details_title,
        'imgs': [unquote(img.image.url) for img in place.imgs.all()],
        'description_short': place.details_description_short,
        'description_long': place.details_description_long,
        'coordinates': {
            'lng': place.lng,
            'lat': place.lat,
        },
    }
    return JsonResponse(place_details, json_dumps_params={'indent': 2,
                                                          'ensure_ascii': False})
 ```

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

Тестовые данные на примере сайта взяты с сайта [KudaGo](https://kudago.com).
