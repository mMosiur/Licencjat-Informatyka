FROM texlive/texlive:latest

COPY Source .

CMD ["bash"]

RUN ["latexmk", "-synctex=1", "-interaction=nonstopmode", "-file-line-error", "-pdf", "thesis.tex"]
