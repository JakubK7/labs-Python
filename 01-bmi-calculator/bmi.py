import winsound

while True: 
 print("Podaj masę ciałą w kg: ")
 m_input = input()
 if m_input == 'stop':
  print('Koniec')
  break
 m = float(input())
 print("Podaj wzorst w cm: ") 
 w  = float(input())
 bmi = m /(w / 100)**2
 bmi = round(bmi, 2)
 if bmi < 18.5:
  print('niedowaga')
  winsound.Beep(400, 400)
 elif 18.5 <= bmi < 25:
  print('waga prawidłowa')
  winsound.Beep(800, 400)
 elif 25 <= bmi < 30:
  print('nadwaga')
  winsound.Beep(600, 400)
 elif  bmi > 30:
  print('otyłość')
  winsound.Beep(300, 600)
 print(f'Twoje bmi wynosi: {bmi}')