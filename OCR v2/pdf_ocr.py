# pdf_ocr.py
from pdf2image import convert_from_path
import pytesseract
from pathlib import Path
import argparse

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--pdf", required=True)
    p.add_argument("--out", default="build/ocr.txt")
    p.add_argument("--tesseract", default=None)
    p.add_argument("--poppler-bin", default=None, help="Path to poppler/bin (optional)")
    args = p.parse_args()

    if args.tesseract:
        pytesseract.pytesseract.tesseract_cmd = args.tesseract

    pages = convert_from_path(args.pdf, poppler_path=args.poppler_bin)
    text = "".join(pytesseract.image_to_string(pg) for pg in pages)

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(text, encoding="utf-8")
    print(f"OCR -> {args.out}")

if __name__ == "__main__":
    main()
