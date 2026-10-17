# Markdown — Przykładowe README

## Krótka sekcja
To jest krótki tekst w pierwszej podsekcji. Zawiera **pogrubiony** tekst oraz *pochylony* fragment.

## Druga sekcja
Druga podsekcja z krótkim opisem i jednym ~~przekreślonym~~ fragmentem.

- Punkt listy A
- Punkt listy B
- Punkt listy C

1. Najpierw przygotuj dane
2. Następnie wykonaj obliczenia
3. Na końcu zapisz wynik

- [x] utworzono notebook
- [x] wykonano obliczenia
- [ ] sprawdzono wynik

Tabela przykładowa:

| Narzędzie | Typ pliku | Zastosowanie |
| --- | --- | --- |
| Markdown | .md | dokumentacja |
| Colab | .ipynb | obliczenia |

Link do Google Colab: [Google Colab](http://colab.research.google.com)

Krótki fragment kodu w Pythonie:

```python
def hello(name):
    return f"Hello, {name}!"

print(hello("Świecie"))
```

Trzy wzory matematyczne w tekście: $a^2 + b^2 = c^2$, $E = mc^2$, $A = \pi r^2$.

Trzy wzory jako osobne bloki wycentrowane:

$$
a^2 + b^2 = c^2
$$

$$
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$

$$
A = \pi r^2
$$

Osadzony obrazek:

![Wykres zależności y od x](files/wykres.png)
