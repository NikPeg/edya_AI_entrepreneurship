# Скрипты для работы с материалами курса

Утилиты для обработки и конвертации материалов курса.

## Доступные скрипты

### pptx_to_txt.py
Извлечение текста из PowerPoint презентаций (PPTX).

**Использование:**
```bash
python scripts/pptx_to_txt.py <путь_к_pptx> [путь_к_txt]
```

**Примеры:**
```bash
# Базовое использование
python scripts/pptx_to_txt.py homework/homework_1/presentation.pptx

# С указанием выходного файла
python scripts/pptx_to_txt.py homework/homework_1/presentation.pptx output.txt
```

**Особенности:**
- Быстрый и надежный
- Извлекает весь текст из всех слайдов
- Сохраняет структуру по слайдам
- Не требует дополнительных системных зависимостей

### pdf_to_txt.py
Простое извлечение текста из PDF файлов.

**Использование:**
```bash
python scripts/pdf_to_txt.py <путь_к_pdf> [путь_к_txt]
```

**Особенности:**
- Быстрый
- Работает только если текст в PDF доступен напрямую
- Не работает с PDF, где текст сохранен как изображение

### pdf_to_txt_ocr.py
Извлечение текста из PDF с использованием OCR (оптическое распознавание).

**Использование:**
```bash
python scripts/pdf_to_txt_ocr.py <путь_к_pdf> [путь_к_txt] [язык]
```

**Примеры:**
```bash
# Базовое использование (по умолчанию rus+eng)
python scripts/pdf_to_txt_ocr.py lectures/lecture_1/Лекция.pdf

# С указанием выходного файла
python scripts/pdf_to_txt_ocr.py lectures/lecture_1/Лекция.pdf output.txt

# С указанием только русского языка
python scripts/pdf_to_txt_ocr.py lectures/lecture_1/Лекция.pdf output.txt rus
```

**Особенности:**
- Медленнее, но работает с любыми PDF
- Использует Tesseract OCR для распознавания текста
- Поддерживает множество языков
- Требует установки системных зависимостей (см. главный README)

## Требования

См. файл `requirements.txt` в корне проекта и инструкции по установке в главном README.md

