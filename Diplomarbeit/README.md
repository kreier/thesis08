# Recreate Diplomarbeit in 2025

Unfortunately the original `.TEX` file was lost, I only have my rendered PDF file from 2008 and some printouts. In 2023 and 2025 I wanted to recreate the original TEX, here are the steps:

## Install software

The rendering in 2025 is done by `texlive-latex-base`. First error is the missing **OT2** support for cyrillic, so the first steps are

``` sh
sudo apt install texlive-latex-base
sudo apt install texlive-lang-cyrillic
```

I used Palatino for my Diploma thesis, and it need to be installed too (more than 2 Gigabyte?). And I used babel used to provide **ngerman** (Neue Rechtschreibung, post‑1996 spelling rules) for automatic line breaks.

``` sh
sudo apt install texlive-fonts-recommended texlive-fonts-extra
sudo apt install texlive-lang-german
```

## Remove outdated packages

Back in 2008 utf-8 was not yet widely supported. So I needed to include some extra packages to work in utf-8. By 2020 it is natively supported by LaTeX, and the old packages could cause errors or have unfixed bugs. Therefore in line 8 and 9:

``` tex
\usepackage{ucs}                % - Modern LaTeX (2020+) already assumes UTF‑8 by default, so you don’t need ucs or utf8x.
\usepackage[utf8x]{inputenc}
```

Even subscript is now implemented in a good way, my definition has to go:

``` LaTeX
   \DeclareRobustCommand*\textsubscript[1]{%
     \@textsubscript{\selectfont#1}}
   \newcommand{\@textsubscript}[1]{%
     {\m@th\ensuremath{_{\mbox{\fontsize\sf@size\z@#1}}}}}
```

## Add missing text and pictures

The translation to English was not finished, but I still have the `.TEX` file that was based on the original one. This is my starting point to recreate a new `Diplomarbeit.tex`
