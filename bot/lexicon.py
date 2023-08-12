from dataclasses import dataclass

@dataclass
class lexicon:
    #фразы
    start = '<b>Приветствую!</b>\nВы попали в приложение, помогающее улучшать экологию Екатеринбурга.  '
    create_point = 'Чтобы создать точку, следуйте инструкциям ниже\n 1. Отправьте координаты'
    sorry = 'Я Вас не понимаю'
    cancel = 'Успешно отменено'

    # кнопки
    webapp_button = 'Открыть приложение'
    create_point_button = 'Создать точку'
    create_appeal_button = 'Создать обращение'
    continue_button = 'Далее'
    cancel_button = 'Отмена'


