# Metaanaliza zbiorów danych do zastosowań w uczeniu maszynowym

[![build](https://github.com/mMosiur/Licencjat-Informatyka/actions/workflows/build.yml/badge.svg)](https://github.com/mMosiur/Licencjat-Informatyka/actions/workflows/build.yml)

Kod źródłowy pracy licencjackiej z kierunku Informatyka na Uniwersytecie Marii Curie-Skłodowskiej w Lublinie.

Autor: Mateusz Piotr Moruś

Praca pisana pod przewodnictwem [dr hab. Grzegorza Wójcika](https://gmwojcik.pl/).

## Najnowsze wydanie

Najnowsza wersja pracy do pobrania [tutaj](https://github.com/mMosiur/Licencjat-Informatyka/releases/download/latest/Licencjat.pdf).

## Kompilacja

Wymagany `texlive` wraz z narzędziem do kompilacji `latexmk`

``` bash
cd Source
latexmk -synctex=1 -interaction=nonstopmode -file-line-error -pdf thesis.tex
```
