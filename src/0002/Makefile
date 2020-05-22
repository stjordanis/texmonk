png: clean
	grep -v '\\documentclass\|\\begin{document}\|\\end{document}' \
	    < ex.tex > ex.tmp
	TEXMFHOME=texmf pdflatex main
	convert -density 300 main.pdf -alpha off main.png
	mv main.pdf "$$(basename $$(pwd)).pdf"
	mv main.png "$$(basename $$(pwd)).png"
	make view FILE="$$(basename $$(pwd)).pdf"
	make view FILE="$$(basename $$(pwd)).png"
	make clean

deps:
	rm -rf texmf texmfvar ~/Library/texlive
	TEXMFHOME=texmf tlmgr init-usertree
	TEXMFHOME=texmf tlmgr --usermode install tcolorbox environ trimspaces

view:
	if command -v xdg-open > /dev/null; then \
	    xdg-open "$(FILE)"; \
	elif command -v open > /dev/null; then \
	    open "$(FILE)"; \
	else \
	    echo Cannot find xdg-open or open; \
	fi

clean:
	rm -rf *.aux *.log *.tmp
