from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field


# Create your models here.
# Нам необходимо разработать интернет-ресурс для фанатского сервера одной известной MMORPG — что-то вроде доски
# объявлений.
# Пользователи нашего ресурса должны иметь возможность зарегистрироваться в нём по e-mail, получив
# письмо с кодом подтверждения регистрации.
# После регистрации им становится доступно создание и редактирование объявлений. Объявления состоят из заголовка и
# текста, внутри которого могут быть картинки, встроенные видео и
# другой контент. Пользователи могут отправлять отклики на объявления других пользователей, состоящие из простого
# текста. При отправке отклика пользователь должен получить e-mail с оповещением о нём. Также пользователю должна
# быть доступна приватная страница с откликами на его объявления, внутри которой он может фильтровать отклики по
# объявлениям, удалять их и принимать (при принятии отклика пользователю, оставившему отклик, также должно прийти
# уведомление).
# Кроме того, пользователь обязательно должен определить объявление в одну из следующих категорий: Танки, Хилы, ДД,
# Торговцы, Гилдмастеры, Квестгиверы, Кузнецы, Кожевники, Зельевары, Мастера заклинаний.
#
# Также мы бы хотели иметь возможность отправлять пользователям новостные рассылки.
#
# Заранее спасибо!

TYPES = [('TANKS', 'Танки'),
         ('HILY', 'Хилы'),
         ('DD', 'ДД'),
         ('TRADES_PEOPLE', 'Торговцы'),
         ('GUILD_MATERS', 'Гилдмастеры'),
         ('QUEST_GILVERS', 'Квестгиверы'),
         ('BLACKMITHS', 'Кузнецы'),
         ('TANNERS', 'Кожевники'),
         ('POTION_MAKERS', 'Зельевары'),
         ('SPELL_MASTERS', 'Мастера заклинаний')]


class Category(models.Model):
    topic = models.CharField(max_length=15, choices=TYPES, unique=True, verbose_name='Категория')

    def __str__(self):
        return f'{self.topic}'


class Advertisment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=u'Пользователь')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name=u'Дата создания')
    category = models.ForeignKey(Category, verbose_name=u'Категория', on_delete=models.DO_NOTHING)
    heading = models.CharField(max_length=255, verbose_name=u'Заголовок')
    body = models.TextField(verbose_name=u'Сожержимое')

    def __str__(self):
        return f'{self.user.username}: {self.heading[:30]} - {self.time_create}'


class Comment(models.Model):
    advertisment = models.ForeignKey(Advertisment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=u'Пользователь')
    comment = models.CharField(max_length=255, verbose_name=u'Отклик')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name=u'Время создания')
    hidden = models.BooleanField(default=True, verbose_name=u'Вдимость')

    # скрыть или открыть комментарий
    def hide(self, status):
        self.hidden = status
        self.save()


class Subscriber(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @staticmethod
    def add_subscriber(user):
        Subscriber.objects.create(user=user)

    @staticmethod
    def delete_subscriber(user):
        Subscriber.objects.filter(user=user).delete()

    def __str__(self):
        user = self.user.username
        return f'{user}'


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', default=None, on_delete=models.CASCADE)
    code = models.CharField(max_length=50, blank=True, null=True, default=None)
    date = models.DateField(blank=True, null=True)

    # def get_context_data(self, **kwargs):
    #     # класс для передачи в страницу - категория и признак подписки пользователя
    #     class Sublist:
    #         def __init__(self, news_category, subscribed):
    #             self.category = news_category  # категория
    #             self.is_subscribed = subscribed  # признак подписки пользоывателя на данную категорию
    #
    #     context = super().get_context_data(**kwargs)
    #     # формируем список объектов Sublist(категория, признак подписки) для передачи в страницу
    #     user_cat = list(Subscriber.objects.filter(user=self.request.user).values('category__topic').distinct())
    #     all_cat = list(Category.objects.all().values('topic'))  # список всех категорий
    #     user_cat_list = list(map(lambda cat: cat['category__topic'], user_cat))  # список подписных категорий
    #     subscribed_list = list(map(lambda cat: Sublist(cat['topic'], cat['topic'] in user_cat_list), all_cat))
    #     context['subscribed'] = subscribed_list
    #     return context
