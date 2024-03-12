# Case-study #3
# Developers: Saipulaev A., Batrakova C., Tolstov J.
#
import ru_local as ru

max_month = 12

category = int(input(f'{ru.SUB}'))


if category == 3:
    def parent():
        '''
        The function determines amount of tax payments  for parent.
        '''
        amount = 0
        tax_free = 0
        with_tax = 0
        sum_tax = 0
        excess_tax = 0
        monthly = 0
        for month in range(1, max_month + 1):
            value = float(input(f'{ru.INCOME}{ru.NAME[month]}:'))
            amount += value
        for month in range(1, max_month + 1):
            without_tax = float(input(f'{ru.ITS_NOT_TAXABLE}{ru.NAME[month]}:'))
            tax_free += without_tax
            difference = amount - without_tax
            with_tax = difference
            if difference <= 12950:
                excess_tax = difference * 0.1
            elif difference <= 49400:
                excess_tax = 12950 * 0.1 +(difference - 12950) * 0.15
            elif difference <= 127550:
                excess_tax = 12950 * 0.1 + 36450 * 0.15 + (difference - 49400) * 0.25
            elif difference <= 206600:
                excess_tax = 12950 * 0.1 + 36450 * 0.15 + 78150 * 0.25 + (difference - 127550) * 0.28
            elif difference <= 405100:
                excess_tax = 12950 * 0.1 + 36450 * 0.15 + 78150 * 0.25 + 79050 * 0.28 + (difference - 206600) * 0.33
            elif difference <= 432200:
                excess_tax = 12950 * 0.1 + 36450 * 0.15 + 78150 * 0.25 + 79050 * 0.28 + 198500 * 0.33 + (difference - 405100) * 0.35
            elif difference - 432200 >= 1:
                excess_tax = 12950 * 0.1 + 36450 * 0.15 + 78150 * 0.25 + 79050 * 0.28 + 198500 * 0.33 + 27100 * 0.35 + (difference - 432200) * 0.396
            sum_tax = excess_tax
            monthly = sum_tax / 12


        print(f'{ru.FREE_INCOME}{tax_free}')
        print(f'{ru.NOT_FREE_INCOME}{with_tax}')
        print(f'{ru.MONTHLY_PAY}{monthly}')
        print(f'{ru.YEARLY_PAY}{sum_tax}')


    parent()

elif category == 2:
    def married_couple():
        '''
        The function determines amount of tax payments  for married couple.
        '''
        amount = 0
        tax_free = 0
        with_tax = 0
        sum_tax = 0
        excess_tax = 0
        monthly = 0
        for month in range(1, max_month + 1):
            value = float(input(f'{ru.INCOME}{ru.NAME[month]}:'))
            amount += value
        for month in range(1, max_month + 1):
            without_tax = float(input(f'{ru.ITS_NOT_TAXABLE}{ru.NAME[month]}:'))
            tax_free += without_tax
            difference = amount - without_tax
            with_tax = difference
            if difference <= 18150:
                excess_tax = difference * 0.1
            elif difference <= 73800:
                excess_tax = 18150 * 0.1 + (difference - 18150) * 0.15
            elif difference <= 148850:
                excess_tax = 18150 * 0.1 + 55650 * 0.15 + (difference - 73800) * 0.25
            elif difference <= 226850:
                excess_tax = 18150 * 0.1 + 55650 * 0.15 + 75050 * 0.25 + (difference - 148850) * 0.28
            elif difference <= 405100:
                excess_tax = 18150 * 0.1 + 55650 * 0.15 + 75050 * 0.25 + 79050 * 0.28 + (difference - 226850) * 0.33
            elif difference <= 457600:
                excess_tax = 18150 * 0.1 + 55650 * 0.15 + 75050 * 0.25 + 79050 * 0.28 + 178250 * 0.33 + (difference - 405100) * 0.35
            elif difference >= 457601:
                excess_tax = 18150 * 0.1 + 55650 * 0.15 + 75050 * 0.25 + 79050 * 0.28 + 178250 * 0.33 + 52500 * 0.35 + (difference - 457600) * 0.396
            sum_tax = excess_tax
            monthly = sum_tax / 12
        print(f'{ru.FREE_INCOME}{tax_free}')
        print(f'{ru.NOT_FREE_INCOME}{with_tax}')
        print(f'{ru.MONTHLY_PAY}{monthly}')
        print(f'{ru.YEARLY_PAY}{sum_tax}')


    married_couple()

elif category == 1:
    def one_subject():
        '''
        The function determines amount of tax payments  for one subject.
        '''
        amount = 0
        tax_free = 0
        with_tax = 0
        sum_tax = 0
        excess_tax = 0
        monthly = 0
        for month in range(1, max_month + 1):
            value = float(input(f'{ru.INCOME}{ru.NAME[month]}:'))
            amount += value
        for month in range(1, max_month + 1):
            without_tax = float(input(f'{ru.ITS_NOT_TAXABLE}{ru.NAME[month]}:'))
            tax_free += without_tax
            difference = amount - without_tax
            with_tax = difference
            if difference <= 9075:
                excess_tax = difference * 0.1
            elif difference <= 36900:
                excess_tax = 9075 * 0.1 + (difference - 9075) * 0.15
            elif difference <= 89350:
                excess_tax = 9075 * 0.1 + 27825 * 0.15 + (difference - 36900) * 0.25
            elif difference <= 186350:
                excess_tax = 9075 * 0.1 + 27825 * 0.15 + 52450 * 0.25 + (difference - 89350) * 0.28
            elif difference <= 405100:
                excess_tax = 9075 * 0.1 + 27825 * 0.15 + 52450 * 0.25 + 97000 * 0.28 + (difference - 186350) * 0.33
            elif difference <= 406750:
                excess_tax = 9075 * 0.1 + 27825 * 0.15 + 52450 * 0.25 + 97000 * 0.28 + 218750 * 0.33 + (
                            difference - 405100) * 0.35
            elif difference - 406750 >= 1:
                excess_tax = 9075 * 0.1 + 27825 * 0.15 + 52400 * 0.25 + 97000 * 0.28 + 218750 * 0.33 + 1650 * 0.35 + (
                            difference - 406750) * 0.396
            sum_tax = excess_tax
            monthly = sum_tax / 12
        print(f'{ru.FREE_INCOME}{tax_free}')
        print(f'{ru.NOT_FREE_INCOME}{with_tax}')
        print(f'{ru.MONTHLY_PAY}{monthly}')
        print(f'{ru.YEARLY_PAY}{sum_tax}')


    one_subject()

else:
    print('Такой категории нет')