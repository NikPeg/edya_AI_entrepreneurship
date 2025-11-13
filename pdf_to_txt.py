#!/usr/bin/env python3
"""
Скрипт для конвертации PDF в текстовый формат
"""
import sys
import pdfplumber

def pdf_to_txt(pdf_path, txt_path=None):
    """
    Конвертирует PDF файл в TXT
    
    Args:
        pdf_path: путь к PDF файлу
        txt_path: путь к выходному TXT файлу (если None, будет создан автоматически)
    """
    if txt_path is None:
        txt_path = pdf_path.replace('.pdf', '.txt')
    
    print(f"Читаю PDF: {pdf_path}")
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            print(f"Найдено страниц: {len(pdf.pages)}")
            
            with open(txt_path, 'w', encoding='utf-8') as txt_file:
                for i, page in enumerate(pdf.pages, 1):
                    print(f"Обрабатываю страницу {i}/{len(pdf.pages)}", end='\r')
                    
                    # Извлекаем текст со страницы
                    text = page.extract_text()
                    
                    if text:
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
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Использование: python pdf_to_txt.py <путь_к_pdf> [путь_к_txt]")
        print("\nПример:")
        print("  python pdf_to_txt.py document.pdf")
        print("  python pdf_to_txt.py document.pdf output.txt")
        sys.exit(1)
    
    pdf_file = sys.argv[1]
    txt_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    pdf_to_txt(pdf_file, txt_file)

