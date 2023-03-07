echomessage:
	echo hello

installunstructure:
	brew install libmagic
	brew install poppler
	brew install tesseract
	brew install libxml2
	brew install libxslt
	sudo apt-get install -y poppler-utils
	sudo apt install -y tesseract-ocr
	sudo apt install -y libtesseract-dev
	poetry add unstructured[local-inference] unstructured
installunstructureviapip:	
	pip install langchain openai cohere gradio huggingface_hub
	pip install tesseract tesseract-ocr	
	pip install "detectron2@git+https://github.com/facebookresearch/detectron2.git@v0.6#egg=detectron2"
	pip install Pillow==9.0.0
	pip install layoutparser[layoutmodels,tesseract]
	pip install pdf2image
