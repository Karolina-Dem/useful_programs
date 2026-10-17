# 11. Co to są kropki kwantowe i jakie mają właściwości?

- 3D struktura
- ruch elektronów jest ograniczony w trzech wymiarach
- najpowszechniejszy model — quantum box (kropka kwantowa w kształcie sześcianu); potencjał na zewnątrz jest nieskończony
- równanie Schrödingera (LaTeX):

$$
-\frac{\hbar^2}{2m}\left(\frac{\partial^2}{\partial x^2}+\frac{\partial^2}{\partial y^2}+\frac{\partial^2}{\partial z^2}\right)\Psi(x,y,z)=E\Psi(x,y,z)
$$

- energia (LaTeX):

$$
E=\frac{\hbar^2 \pi^2}{2m}\left(\frac{n_x^2}{L_x^2}+\frac{n_y^2}{L_y^2}+\frac{n_z^2}{L_z^2}\right)
$$

---

Fallback (zapis, który zawsze zobaczysz na GitHubie bez dodatkowych wtyczek):

- równanie Schrödingera (fallback, czysty tekst):

    -ħ²/(2m) * (∂²/∂x² + ∂²/∂y² + ∂²/∂z²) Ψ(x,y,z) = E Ψ(x,y,z)

- energia (fallback, czysty tekst):

    E = (ħ² π² / (2 m)) * (n_x² / L_x² + n_y² / L_y² + n_z² / L_z²)

---

- poziomy energetyczne są zdegenerowane
- sferyczna kropka kwantowa → rozdzielenie funkcji falowej Ψ na część radialną i kątową (podobieństwo do zagadnienia atomu wodoru w mechanice kwantowej) → rozwiązania: funkcje Bessela typu J_{l+1/2}


# 12. Porównaj właściwości heterostruktur, drutów i kropek kwantowych

- Heterostruktury (2D, warstwy): ograniczenie w jednym wymiarze; gęstość stanów przypomina 2D; często stosowane do tworzenia studni potencjału i tunelowania między warstwami.

- Druty kwantowe (1D): ograniczenie w dwóch wymiarach; przewodzenie wzdłuż jednej osi; gęstość stanów charakterystyczna dla 1D (pikowate cechy), zwiększona rola lokalizacji i rozpraszania.

- Kropki kwantowe (0D): ograniczenie we wszystkich trzech wymiarach; dyskretne poziomy energetyczne (podobne do atomu), duża degeneracja zależna od symetrii; używane jako "sztuczne atomy" w optoelektronice.


---

Uwaga o renderowaniu równań na GitHubie:

- Standardowy widok plików .md na GitHubie nie renderuje LaTeX/MathJax automatycznie. Dlatego dodałem sekcję "Fallback" w czystym tekście — zawsze będzie widoczna na GitHubie.
- Jeśli chcesz, żeby LaTeX był wyrenderowany (ładne formuły), możesz opublikować stronę przez GitHub Pages i dodać MathJax/KaTeX (instrukcje mogę dopisać). Alternatywnie zmienić plik na README w repozytorium z odpowiednią konfiguracją Jekylla.
