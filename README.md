Модульное тестирование задание номер 6

---

- Шаг 1: Установка и настройка Appium

1. Установка Appium

```shell
npm install -g appium
```

---

2. Запустить Appium сервер

```shell
appium
```

---

Шаг 2: Установка эмулятора для Android

3. Установите Android Studio и настройте эмулятор:

1. Запустите Android Studio.

2. Перейдите в раздел AVD Manager и создайте новый виртуальный девайс.

3. Настройте его и запустите.

---

Шаг 3: Установка APK-файла калькулятора

1. Скачать APK-файл Google Calculator с Uptodown (или используйте встроенный калькулятор).

2. Установить APK-файл на эмулятор:

```shell
adb install path/to/calculator.apk
```

---

Шаг 4: Написание тестов

1. Установить необходимые библиотеки:

```shell
pip install Appium-Python-Client
```

---

Шаг 5: Запуск тестов

1. Запустите тесты с использованием командной строки:

```shell
python -m unittest tests/test_calculator.py
```

---
