# -ModuleD13_homework
Проект выполнен на основе следующего технического задания:
Нам необходимо разработать интернет-ресурс для фанатского сервера одной известной MMORPG — что-то вроде доски объявлений. Пользователи нашего ресурса должны иметь возможность зарегистрироваться в нём по e-mail, получив письмо с кодом подтверждения регистрации. После регистрации им становится доступно создание и редактирование объявлений. Объявления состоят из заголовка и текста, внутри которого могут быть картинки, встроенные видео и другой контент. Пользователи могут отправлять отклики на объявления других пользователей, состоящие из простого текста. При отправке отклика пользователь должен получить e-mail с оповещением о нём. Также пользователю должна быть доступна приватная страница с откликами на его объявления, внутри которой он может фильтровать отклики по объявлениям, удалять их и принимать (при принятии отклика пользователю, оставившему отклик, также должно прийти уведомление). Кроме того, пользователь обязательно должен определить объявление в одну из следующих категорий: Танки, Хилы, ДД, Торговцы, Гилдмастеры, Квестгиверы, Кузнецы, Кожевники, Зельевары, Мастера заклинаний.

Также мы бы хотели иметь возможность отправлять пользователям новостные рассылки.

Заранее спасибо!

Сделано: 
1. Прльзователи имеют возможность регистрироваться на сайте по E-mail
2. При регистрации пользователи получают четырехначный код, который необходимо ввести для подтверждения регистрации
3. Для зарегистрированных пользователей имеется возможность создания и редактирования объявлений, для незарегистрированных только просмотр объявлений и откликов
4. Объявления содержат заголовок и текст, внутри которого имеется возможность вставки картинок и видео (реализовано на основе модуля summernote)
5. Зарегистрированные пользовтели имеют возможность отправлять отклики (простой текст) на объявления других пользователей
6. При отправке отклика автор обхявления получает уведомление об этом
7. Пользователю-автору доступна возможность просмотреть отклики на его объявления, он может фильтровать отклики по объявлениям, удалять отклики и принимать их
8. При "принятии" отклика, пользователю, оставившему отклик на E-mail, отправляется уведомление об этом
9. При публикации и редактировании объявлений имеется возможность определеить его в различные категории из определенного заранее списка
10. У зарегистрированных пользователей имеется возможность подписаться/отписаться на еженедельную рассылку новых объвлений
