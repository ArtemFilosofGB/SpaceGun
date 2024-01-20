# SpaceGun
Стрелялка с использованием Pygame
Это простая игра в стрельбу, созданная с использованием библиотеки Pygame. Игрок управляет пушкой, стреляя в цели и избегая препятствий в небе.

![](SpaceGun.gif)

## Установка
Убедитесь, что у вас установлен Python.
Установите Pygame с помощью следующей команды:
bash
```commandline
pip install pygame

```

### Как играть
Двигайте мышью, чтобы управлять положением пушки.
Левым кликом выстреливайте пулями.
В игре присутствуют двигающиеся цели, звезды и динамичное небо.
Структура программы
Программа состоит из следующих классов:

#### Bullet: Представляет собой пули, выпущенные игроком.
#### Target: Представляет собой двигающиеся цели, которые нужно поразить.
#### Sky: Представляет собой небо с случайными препятствиями.
#### Gun: Представляет собой пушку игрока.
### Управление

Двигайте мышью, чтобы управлять положением пушки.
Левым кликом выстреливайте пулями.
Логика игры
Игра включает таймер, который создает новые цели, звезды и препятствия с определенным интервалом.
Пули исчезают при попадании в цели.
Цели удаляются при попадании в них пуль.
В игре ведется учет счета игрока.
#### Среда разработки
Версия Python: [3.11]
Версия Pygame: [2.5.2]
Не стесняйтесь настраивать и улучшать игру по своему вкусу!