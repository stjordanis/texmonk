readme:
	python3 src/readme.py > README.md
	cat README.md

clean:
	find . -name "*.pdf" -exec rm {} +
	find . -name "*.png" -exec rm {} +
