echomessage:
	echo hello

installunstructure:
	brew install libmagic
	brew install poppler
	brew install tesseract
	brew install libxml2
	brew install libxslt
	sudo apt-get install -y poppler-utils
	sudo apt install tesseract-ocr
	sudo apt install libtesseract-dev
	poetry add unstructured[local-inference] unstructured
	poetry add tesseract tesseract-ocr	
	poetry add "detectron2@git+https://github.com/facebookresearch/detectron2.git@v0.6#egg=detectron2"
	poetry add Pillow==9.0.0
	poetry add layoutparser[layoutmodels,tesseract]
	poetry add pdf2image
	poetry add langchain openai cohere gradio huggingface_hub
