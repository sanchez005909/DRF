from rest_framework.serializers import ValidationError


class URLValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        url = dict(value).get(self.field)
        print(url)
        domen = url.split('/')[2]
        if domen not in ['youtube.com', 'www.youtube.com']:
            raise ValidationError('Ссылка на сторонний ресурс запрещена. Прикрепите, пожалуйста, ссылку на youtube!')
