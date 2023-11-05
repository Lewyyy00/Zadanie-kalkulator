import logging
logging.basicConfig(level=logging.INFO)  
log = logging.getLogger('my_logger')

print('Cześć i czołem, masz przed sobą najprostrzy kalkualtor na świecie.')
while True:
    what_calculation = input("Typy obliczeń: \n 1.Dodawanie \n 2.Odejmowanie \n 3.Mnożenie \n 4.Dzielenie \n Wybierz proszę typ działania, który w tej chwili potrzebujesz:")
    if what_calculation in ('1','2','3','4'):
        break
    print("Błedna cyfra, wybierz cyfrę od 1 do 4")

if what_calculation == '1':
    How_many_numbers = int(input("Podaj ilość liczb, które chcesz uzyć w obliczeniach:"))
    what_numbers = input(f"Podaj proszę {How_many_numbers} liczb/y, które chcesz dodać. Pamiętaj aby odzielić je przecinkiem:")
    Split_numbers = what_numbers.split(",")
    suma = 0
    logged_number = []
    for i in range(How_many_numbers):
        number = int(Split_numbers[i])
        suma += number

        logged_number.append(number)
    logging.info(f"Dodajesz ze sobą liczby {logged_number} ")
    print(f"Twój wynik to {suma}")

elif what_calculation == '2':
    what_numbers = input("Podaj proszę dwie liczby, które chcesz odjąć. Pamiętaj aby odzielić je przecinkiem:")
    Split_numbers = what_numbers.split(",")
    First_number = float(Split_numbers[0])
    Second_number = float(Split_numbers[1])
    calculation = First_number - Second_number

    logging.info(f"Odejmujesz {First_number} z {Second_number}")
    print(f"Twój wynik to {calculation}")

elif what_calculation == '3':
    How_many_numbers = int(input("Podaj ilość liczb, które chcesz uzyć w obliczeniach:"))
    what_numbers = input(f"Podaj proszę {How_many_numbers} liczb/y, które chcesz pomnożyć. Pamiętaj aby odzielić je przecinkiem:")
    Split_numbers = what_numbers.split(",")
    suma = 1
    logged_number = []
    for i in range(How_many_numbers):
        number = int(Split_numbers[i])
        suma *= number 

        logged_number.append(number)
    logging.info(f"Dodajesz ze sobą liczby {logged_number} ")
    print(f"Twój wynik to {suma}")

elif what_calculation == '4':
    what_numbers = input("Podaj proszę dwie liczby, które chcesz podzielić. Pamiętaj aby odzielić je przecinkiem:")
    Split_numbers = what_numbers.split(",")
    First_number = float(Split_numbers[0])
    Second_number = float(Split_numbers[1])
    calculation = First_number / Second_number

    logging.info(f"Dzielisz {First_number} z {Second_number}")
    print(f"Twój wynik to {calculation}")

