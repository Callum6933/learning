# defaults you can override on the command line
PDF           ?= input.pdf
TESSERACT     ?= /opt/homebrew/bin/tesseract
POPLER_BIN    ?=
CHUNK_DIR     ?= chunks
BUILD_DIR     ?= build
OCR_TXT       ?= $(BUILD_DIR)/ocr.txt
PRECLEAN_TXT  ?= $(BUILD_DIR)/preclean.txt
FINAL         ?= $(BUILD_DIR)/final.txt
MODEL         ?= openai/gpt-5-nano
CHUNK_SIZE    ?= 4000

.PHONY: all run clean
all: run
run:
	mkdir -p $(BUILD_DIR)
	python3 pdf_ocr.py --pdf "$(PDF)" --out "$(OCR_TXT)" --tesseract "$(TESSERACT)" $(if $(POPLER_BIN),--poppler-bin "$(POPLER_BIN)")
	python3 clean.py --in "$(OCR_TXT)" --out "$(PRECLEAN_TXT)" --chunk-dir "$(CHUNK_DIR)" --chunk-size $(CHUNK_SIZE)
	OPENROUTER_API_KEY=$$OPENROUTER_API_KEY python3 batch_narration.py --chunk-dir "$(CHUNK_DIR)" --out "$(FINAL)" --model "$(MODEL)"
	@echo "Done -> $(FINAL)"

clean:
	rm -rf "$(BUILD_DIR)" "$(CHUNK_DIR)"
