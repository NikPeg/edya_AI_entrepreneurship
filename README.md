# edya_AI_entrepreneurship

Проект для курса "Введение в ИИ предпринимательство" ВШЭ.

## Структура проекта

```
edya_AI_entrepreneurship/
├── lectures/              # Материалы лекций
│   ├── lecture_1/        # Лекция 1
│   ├── lecture_2/        # Лекция 2 (будет добавлена)
│   └── README.md
├── homework/             # Домашние задания
│   ├── homework_1/       # ДЗ 1: Формулирование идеи продукта
│   ├── homework_2/       # ДЗ 2 (будет добавлено)
│   └── README.md
├── scripts/              # Утилиты для работы с материалами
│   ├── pdf_to_txt.py
│   ├── pdf_to_txt_ocr.py
│   └── README.md
├── requirements.txt      # Python зависимости
└── README.md            # Этот файл
```

## Быстрый старт

### Домашнее задание 1
**Описание:** [`homework/homework_1/README.md`](homework/homework_1/README.md)

**Краткое содержание:**
1. Формулируем идею продукта (выбор тренда, анализ отрасли)
2. Уточняем ICP и UVP
3. Заполняем Lean Canvas

---

## Утилиты для работы с PDF

### Описание
Скрипты для извлечения текста из PDF файлов. Подробнее см. [`scripts/README.md`](scripts/README.md)

### Установка зависимостей

1. Убедитесь, что у вас установлен pyenv:
```bash
pyenv --version
```

2. Создайте и активируйте виртуальную среду:
```bash
pyenv virtualenv 3.12.7 edya_ai
pyenv local edya_ai
```

3. Установите системные зависимости (для OCR):
```bash
brew install poppler tesseract tesseract-lang
```

4. Установите Python пакеты:
```bash
pip install -r requirements.txt
```

### Использование

#### Вариант 1: Простое извлечение текста (быстрый, но не всегда работает)

**Базовое использование**:
```bash
python scripts/pdf_to_txt.py lectures/lecture_1/Лекция.pdf
```

**С указанием имени выходного файла**:
```bash
python scripts/pdf_to_txt.py lectures/lecture_1/Лекция.pdf output.txt
```

#### Вариант 2: Извлечение текста с OCR (медленный, но работает с изображениями)

Если текст в PDF сохранен как изображение, используйте скрипт с OCR:

```bash
python scripts/pdf_to_txt_ocr.py lectures/lecture_1/Лекция.pdf
```

**С указанием имени и языков**:
```bash
python scripts/pdf_to_txt_ocr.py lectures/lecture_1/Лекция.pdf output.txt rus+eng
```

### Результат
Скрипты создадут текстовый файл с содержимым PDF, где каждая страница будет отделена заголовком с номером страницы.