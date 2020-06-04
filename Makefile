SUBST = The content of this website has been generated from\
<https:\/\/github.com\/susam\/texmonk>.

readme:
	python3 src/readme.py > README.md
	make site-readme
	head -n 48 README.md

site-readme:
	sed -e "s/repository/website/g; s/<!-- This README.*/$(SUBST)/" \
	    README.md > ../site-texmonk/README.md

clean:
	find . -name "*.pdf" -exec rm {} +
	find . -name "*.png" -exec rm {} +
