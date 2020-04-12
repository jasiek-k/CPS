1. Uruchamianie programu w zależności od wybranego trybu działania (konwerter analogowo-cyfrowy, bądź cyfrowo analogowy):
> python main.py ADC
> python main.py DAC
---
2. W zależności od wybranego trybu działania należy podać odpowiednie dane, o które pyta program. 
Dla konwertera ADC są to:
czestotliwosc probkowania (w Hz, bez spacji, jedynie liczba);
po zatwierdzeniu należy podać próg kwantyzacji (liczba całkowita), a następnie podać parametry (PUNKT 3)
Dla konwertera DAC należy wybrać metodę rekonstrukcji poprzez wpisanie odpowiedniego symbolu:
[r1] zero-order hold
[r2] first-order hold
[r3] rekonstrukcja w oparciu o funkcje sine
Po zatwierdzeniu należy podać ilość próbek, które zawiera wygenerowany sygnał funkcji określonej parametrami (PUNKT 3)

3. W zależności od wybranego wariantu należy sprecyzować parametry wywołania:
[S1/S2] [A] [t1] [d] [bins] [f] ['T']
[S3/S4/S5] [A] [T] [t1] [d] [bins] [f] ['T']
[S6/S7/S8] [A] [T] [t1] [d] [kw] [bins] [f] ['T']
[S9] [A] [t1] [d] [ts] [bins] [f] ['T']
[S10] [A] [n1] [ns] [l] [bins] [f] ['T']
[S11] [A] [t1] [d] [f] [p] [bins] 
['R'] ['nazwa_pliku'] 
[parametry1] [dodaj/odejmij/mnoz/dziel] [parametry2] [f] ['Z'] (w wersji zadania drugiego operacje arytmetyczne nie zostały uwzględnione)

Gdzie:
S1 - szum o rozkładzie jednostajnym
S2 - szum gaussowski
S3 - sygnał sinusoidalny
S4 - sygnał sinusoidalny wyprostowany jednopołówkowo
S5 - sygnał sinusoidalny wyprostowany dwupołówkowo
S6 - sygnał prostokątny
S7 - sygnał prostokątny symetryczny
S8 - sygnał trójkątny
S9 - skok jednostkowy
S10 - impuls jednostkowy
S11 - szum impulsowy

bins - liczba przedziałów histogramu 
'T' - zapisz wyniku operacji do pliku (należy opuścić jeśli wynik ma nie zostać zapisany)
'R' - operuj na wartościach wczytanych z pliku binarnego
'Z' - zapisz wyniku operacji do pliku - flaga dotyczy jedynie wyniku operacji na 2 sygnałach!
'nazwa_pliku' - cała ścieżka jest potrzebna jeśli plik jest w innym katalogu niż main.py, rozszerzenie zbędne 
---
4. Przykładowe wywołania programu:
S9 3 -1 6 0 5 1 T
S9 3 -1 6 0 5 1 odejmij S3 2 2 2 10 5 1 20 Z
S3 2 2 2 10 5 1 dodaj S9 3 -1 6 0 5 1 20 Z
---
5. Struktura projektu 
./src/ - pliki klas sygnałów oraz operacji z nich korzystających
    > sin_signal - sygnał sin, sin wyprostowany jednopołówkowo i dwupołówkowo
    > impuls_signal - impuls jednostkowy i wszystkie szumy
    > prost_signal - sygnał prostokątny i prostokątny symetryczny
    > skok_signal - skok jednostkowy
    > troj_signal - sygnał trójkątny
    > impuls_ops - zbiór funkcji przeznaczonych dla przetwarzania impulsów
    > signal_ops - zbiór funkcji przeznaczonych dla przetwarzania sygnałów
    > dzialania - zbiór funkcji przeznaczonych dla operowania na 2 sygnałach (dodawanie/odejmowanie etc.)
    > signal_init - zbiór funkcji obsługujących argumenty funkcji
    > signal_disc - zbiór funkcji dla sygnałów dyskretnych, w tym zawierający funkcje rekonstrukcji 
    > signal_cont - zbiór funkcji dla sygnałów ciągłych, w tym zawierający funkcję próbkowania oraz kwantyzacji
./files/ - pliki generowane przez program, stanowią one zapis wcześniejszych operacji. Mogą być wykorzystywane do testowania
    > SX_data - pliki operacji na pojedynczym sygnale (gdzie SX - numer sygnału)
    > SX_SY_data - pliki operacji na 2 sygnałach
