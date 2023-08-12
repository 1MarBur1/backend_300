from dataclasses import dataclass

@dataclass
class lexicon:
    #фразы
    start = '<b>Приветствую!</b>\nТы попал в приложение, помогающее улучшать экологию Екатеринбурга'
    create_point = 'Чтобы создать точку, следуй инструкциям ниже\n 1. Отправь координаты'
    sorry = 'Я тебя не понимаю'
    cancel = 'Успешно отменено'

    # кнопки
    webapp_button = 'Открыть приложение'
    create_point_button = 'Создать точку'
    create_appeal_button = 'Создать обращение'
    continue_button = 'Далее'
    cancel_button = 'Отмена'


