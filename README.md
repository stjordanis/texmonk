TeX Monk
========

This repository contains LaTeX examples used in the TeX Monk posts on
Twitter at <https://twitter.com/texmonk>.

<!-- This README file is generated automatically using src/readme.py -->


## 0003

In TeX and LaTeX, the dollar symbol delimits mathematics formulas. Use the
escape sequence `\$` to typeset literal dollar symbol.

Example:

```tex
\documentclass{article}
\begin{document}
Euler's identity: $ e^{i \pi} + 1 = 0 $.

I have \$10.
\end{document}
```

![LaTeX Example Screenshot 0003][IMG0003]

[IMG0003]: https://opendocs.github.io/texmonk/png/0003.png


## 0002

In TeX and LaTeX, the hash symbol denotes macro parameters, e.g., `#1`,
`#2`, etc. Use the escape sequence `\#` to typeset literal hash symbol.

Example:

```tex
\documentclass{article}
\begin{document}
\newcommand{\hello}[1]{hello, #1}  % #1 - macro parameter
\hello{world}                      % macro usage
\#                                 % literal hash sign
\end{document}
```

![LaTeX Example Screenshot 0002][IMG0002]

[IMG0002]: https://opendocs.github.io/texmonk/png/0002.png


## 0001

After setting up TeX Live, create a document. Paste this into a file
named `foo.tex`:

```tex
\documentclass{article}
\begin{document}
Lorem ipsum
\end{document}
```

Then run this:

```shell
pdflatex foo
```

Open `foo.pdf` to see the output.

![LaTeX Example Screenshot 0001][IMG0001]

[IMG0001]: https://opendocs.github.io/texmonk/png/0001.png


License
-------

This is free and open source software. You can use, copy, modify,
merge, publish, distribute, sublicense, and/or sell copies of it,
under the terms of the MIT License. See [LICENSE.md][L] for details.

This software is provided "AS IS", WITHOUT WARRANTY OF ANY KIND,
express or implied. See [LICENSE.md][L] for details.
