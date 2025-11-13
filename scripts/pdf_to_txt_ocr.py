#!/usr/bin/env python3
"""
Скрипт для конвертации PDF в текстовый формат с использованием OCR
"""
import sys
from pdf2image import convert_from_path
from PIL import Image
import pytesseract

def pdf_to_txt_ocr(pdf_path, txt_path=None, lang='rus+eng'):
    """
    Конвертирует PDF файл в TXT используя OCR
    
    Args:
        pdf_path: путь к PDF файлу
        txt_path: путь к выходному TXT файлу (если None, будет создан автоматически)
        lang: языки для распознавания (по умолчанию русский и английский)
    """
    if txt_path is None:
        txt_path = pdf_path.replace('.pdf', '_ocr.txt')
    
    print(f"Читаю PDF: {pdf_path}")
    print(f"Это может занять некоторое время...")
    
    try:
        # Конвертируем PDF в изображения
        print("Конвертирую PDF в изображения...")
        images = convert_from_path(pdf_path, dpi=300)
        
        print(f"Найдено страниц: {len(images)}")
        
        with open(txt_path, 'w', encoding='utf-8') as txt_file:
            for i, image in enumerate(images, 1):
                print(f"Обрабатываю страницу {i}/{len(images)} (OCR)", end='\r')
                
                # Распознаем текст с изображения
                text = pytesseract.image_to_string(image, lang=lang)
                
                # Записываем заголовок страницы и текст
                txt_file.write(f"\n{'='*80}\n")
                txt_file.write(f"СТРАНИЦА {i}\n")
                txt_file.write(f"{'='*80}\n\n")
                txt_file.write(text)
                txt_file.write("\n\n")
        
        print(f"\n\nГотово! Текст сохранен в: {txt_path}")
        return txt_path
        
    except Exception as e:
        print(f"\nОшибка при обработке PDF: {e}")
        print("\nУбедитесь, что установлены необходимые зависимости:")
        print("  brew install poppler tesseract tesseract-lang")
        print("  pip install pdf2image pytesseract pillow")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Использование: python pdf_to_txt_ocr.py <путь_к_pdf> [путь_к_txt] [язык]")
        print("\nПример:")
        print("  python pdf_to_txt_ocr.py document.pdf")
        print("  python pdf_to_txt_ocr.py document.pdf output.txt")
        print("  python pdf_to_txt_ocr.py document.pdf output.txt rus+eng")
        sys.exit(1)
    
    pdf_file = sys.argv[1]
    txt_file = sys.argv[2] if len(sys.argv) > 2 else None
    lang = sys.argv[3] if len(sys.argv) > 3 else 'rus+eng'
    
    pdf_to_txt_ocr(pdf_file, txt_file, lang)

