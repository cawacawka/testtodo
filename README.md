# todotest

Простой, расширяемый фреймворк для тестирования todomvc
  - Базовый URL http://todomvc.com/examples/react/#/
  - Работает на Windows, Linux
  - Проверено на Chrome, Firefox (расширяемо)

### system requirements
  - chrome и chromedriver(доступен в PATH)
  - firefox, geckodriver(доступен в PATH)
  - Java установлена и доступна в JAVA_HOME (для запуска allure-commandline)
  - Python 3.+ (разработка и тесты 3.7.2)

### python requirements
  - см. в requirements.txt
  
### python requirements install
```sh
pip install -r requirements.txt
```

### Запуск
```sh
python -m pytest <path_to>/testtodo/tests
```
 - опционально можно добавить ключ -n <thread_counts> (пример -n 4, запустит тест в 4 потока, 4 сессии). см. pytest-xdist


### Описание кейсов
 - Автоматизированный набор (Smoke)
 - Остальное, не реализованное

### Описание gitlab ci
 - stage fake_build
 - stage test
 - stage report