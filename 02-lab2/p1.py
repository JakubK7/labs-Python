dane = input('Podaj ciąg liczb całkwowitych oddzielonych spacjmi')

if dane.strip() == '':
   print('Nie wprowadzono żadnych liczb!!')
else: 
   try:

    liczby = [int(x) for x in dane.split()]

    ilosc = len(liczby)
    suma = sum(liczby)
    srednia = suma / ilosc if ilosc > 0 else 0 

    dodatnie = sum(1 for x in liczby if x > 0)
    ujemne = sum(1 for x in liczby if x < 0)
    zera = sum(1 for x in liczby if x == 0)

    max = max(liczby)
    min = min(liczby)

    print('\n--- Przekształcanie i analiza liczb ---')
    print(f'Lista liczb: {liczby}')
    print(f'Ilość liczb: {ilosc}')
    print(f'Suma: {suma}')
    print(f'Średnia: {srednia}')
    print(f'Ilość liczb dodatnich: {dodatnie}')
    print(f'Ilość liczb ujemnych: {ujemne}')
    print(f'Ilość zer: {zera}')
    print(f'Największa liczba: {max}')
    print(f'Najmniejsza liczba: {min}')

   except ValueError:
    print('Błąd: prosze wprowadzić tylko liczby całkowite oddzielone spacjami.')


