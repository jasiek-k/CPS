# CPS

Uruchamianie programu:
>>> python main.py

W zależności od wybranego wariantu należy sprecyzować parametry wywołania:
[S3/S4/S5] [A] [T] [t1] [d] [bins] [f]
[S6/S7/S8] [A] [T] [t1] [d] [kw] [bins] [f]
[S9] [A] [t1] [d] [ts] [bins] [f] 
[S10] [A] [n1] [ns] [l] [bins] [f]  
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

Przykładowe wywołanie programu:

Struktura projektu 
> sin_signal - sygnał sin, sin wyprostowany jednopołówkowo i dwupołówkowo
> impuls_signal - impuls jednostkowy, szum impulsowy
> prost_signal - sygnał prostokątny i prostokątny symetryczny
> skok_signal - skok jednostkowy
> troj_signal - sygnał trójkątny
> impuls_ops - zbiór funkcji przeznaczonych dla przetwarzania impulsów
> signal_ops - zbiór funkcji przeznaczonych dla przetwarzania sygnałów
