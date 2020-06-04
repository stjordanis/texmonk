readme:
	python3 src/readme.py > README.md
	head -n 48 README.md

clean:
	find . -name "*.pdf" -exec rm {} +
	find . -name "*.png" -exec rm {} +
