place = input('Where will you work? Japan? The UK? Canada?').lower()

def uk():
    list1 = [0,12.5,50,150]
    list2 = [0,0.2,0.4,0.45]
    age = 24
    investment_return_rate = 0.1
    inflation_rate = 0.03
    net_worth = 0
    income_increase_rate = 0.08
    # (Rent Eatin eatout&soc Piano Transport night buy)*12+travel 
    annual_spending = (0.65+0.15+0.3+0.3+0.05+0.35*0+0.15)*12+2.5
    fresh = float(input('What is your fresh grad before tax annual salary?(in k GBP)'))

    while age <= 29:
        annual_salary = fresh*(1+income_increase_rate)**(age-25)
        b = 0
        for i in range(len(list1)-1):
            a = (min(annual_salary,list1[i+1]) - list1[i])*(list2[i])
            b += a
            if list1[i+1] > annual_salary:
                break
        if annual_salary > list1[3]:
            b += (annual_salary - list1[3]) * list2[3]
        after_tax = annual_salary - b
        net_worth = (net_worth + after_tax - annual_spending * (1+inflation_rate)**(age-23)) * (1 + investment_return_rate)
        print('Your after tax salary when you are ', age,' will be', after_tax, '(in k GBP).')
        print('Your net worth when you are ', age,' will be', net_worth, '(in k GBP).')
        print('The buying power of your net worth (as of 2021) when you are ', age,' will be', (net_worth) / (1+inflation_rate)**(age-23), '(in k GBP).',end="\n\n")
        #print('The buying power of your net worth (as of 2021) when you are ', age,' will be', (net_worth) * 1.07146942 / (1+inflation_rate)**(age-23), '(in 10k HKD).')
        age += 1

def japan():
    age = 24
    investment_return_rate = 0.1
    inflation_rate = 0.01
    net_worth = 0
    list1 = [65, 180, 360, 660, 1000, 1500]
    list2 = [0, 0.4, 0.3, 0.2, 0.1, 0.05]
    list3 = [65, 0, 18, 54, 120,170]
    list4 = [195, 330, 695, 900, 1800]
    list5 = [0.05, 0.1, 0.2, 0.23, 0.33]
    list6 = [0, 9.75, 42.75, 63.6, 153.6]
    B = 0
    ans1 = input('你要唔要養 收入103萬以下配偶? (Y/N):').lower()
    if ans1 == "y":
        B += 38
    ans2 = input('你要唔要養 收入103~141萬配偶? (Y/N):').lower()
    if ans2 == "y":
        B += 38
    ans3 = input('你要唔要養 配偶者以外的扶養? (Y/N):').lower()
    if ans3 == "y":
        B += 38
    ans4 = input('你要唔要養 特定扶養? (Y/N):').lower()
    if ans4 == "y":
        B += 63
    ans5 = input('你要唔要養 70歲以上同居親屬? (Y/N):').lower()
    if ans5 == "y":
        B += 58
    ans6 = input('你要唔要養 殘障者? (Y/N):').lower()
    if ans6 == "y":
        B += 27

    C = float(input('Your annual insurance fee is (in 10k￥): '))+38

    while age <= 65:
        annual_salary = (1.98769*(age-24)+32.48974) *12
        annual_spending = (28.2 * 12)*((1+inflation_rate)**(age-24))
        for i in range(len(list1)):
            if annual_salary < list1[i]:
                A = annual_salary * list2[i] + list3[i]
                break
            if annual_salary >= 1500:
                A = 245
        payable = annual_salary - A - B - C
        for i in range(len(list4)):
            if payable < list4[i]:
                D = payable * list5[i] - list6[i]
                break
            if payable >= 1800:
                D = payable * 0.4 -279.6
        total_tax =  D * 1.021 + payable * 0.1
        after_tax = annual_salary - total_tax
        net_worth = (net_worth + after_tax - annual_spending) * (1 + investment_return_rate)
        print('The buying power of your net worth (as of 2021) when you are ', age,' will be', (net_worth) * 0.0708797228 / (1+inflation_rate)**(age-23), '(in 10k HKD).')
        age += 1

def canada():
    list1 = [0,48.535,97.069,150.473,214.368]
    list2 = [0.15,0.205,0.26,0.29,0.33]
    age = 24
    investment_return_rate = 0.08
    inflation_rate = 0.03
    net_worth = 0
    income_increase_rate = 0.05
    # (Rent eatin eatout&soc Transport mobile buy)*12+travel+other
    annual_spending = (1+0.6+0.04*2*4.35+0.1+0.05+0.2)*12+2+2
    fresh = float(input('What is your before tax annual salary?(in k CAD)'))

    while age <= 31:
        annual_salary = fresh*(1+income_increase_rate)**(age-24)
        b = 0
        for i in range(len(list1)-1):
            a = (min(annual_salary,list1[i+1]) - list1[i])*(list2[i])
            b += a
            if list1[i+1] > annual_salary:
                break
        if annual_salary > list1[3]:
            b += (annual_salary - list1[3]) * list2[3]
        after_tax = annual_salary - b
        net_worth = (net_worth + after_tax - annual_spending * (1+inflation_rate)**(age-24)) * (1 + investment_return_rate)
        print('Your annul after tax salary when you are ', age,' will be', after_tax, '(in k CAD).')
        print('Your real monthly after tax salary when you are ', age,' will be', after_tax, '(in k CAD).')
        print('Your net worth when you are ', age,' will be', net_worth, '(in k CAD).')
        print('The buying power of your net worth (as of 2022) when you are ', age,' will be', (net_worth) / (1+inflation_rate)**(age-24), '(in k CAD).')
        print('The buying power of your net worth (as of 2022) when you are ', age,' will be', (net_worth) * 0.57066865 / (1+inflation_rate)**(age-24), '(in k GBP).',end="\n\n")
        age += 1


if place == 'japan':
    japan()
if place == 'the uk':
    uk()
if place == 'canada':
    canada()
