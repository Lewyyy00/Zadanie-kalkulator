
print('Cześć i czołem, masz przed sobą najprostrzy kalkualtor na świecie.')
while True:
    what_calculation = input("Typy obliczeń: \n 1.Dodawanie \n 2.Odejmowanie \n 3.Mnożenie \n 4.Dzielenie \n Wybierz proszę typ działania, który w tej chwili potrzebujesz:")
    if what_calculation in ('1','2','3','4'):
        break
    print("Błedna cyfra, wybierz cyfrę od 1 do 4")
if what_calculation == '1':
    what_numbers = input("Podaj proszę dwie liczby, które chcesz policzyć. Pamiętaj aby odizelić je przecinkiem:")
    Split_numbers = what_numbers.split(",")
    First_number = int(Split_numbers[0])
    Second_number = int(Split_numbers[1])
    calculation = First_number + Second_number
    print(calculation)
elif what_calculation == '2':
    what_numbers = input("Podaj proszę dwie liczby, które chcesz policzyć. Pamiętaj aby odizelić je przecinkiem:")
    pass
elif what_calculation == '3':
    what_numbers = input("Podaj proszę dwie liczby, które chcesz policzyć. Pamiętaj aby odizelić je przecinkiem:")
    pass
elif what_calculation == '4':
    what_numbers = input("Podaj proszę dwie liczby, które chcesz policzyć. Pamiętaj aby odizelić je przecinkiem:")
    pass

