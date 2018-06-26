"""
I have 2 investment choices:

Wealthsimple with free fee of under £6100 but with a return is 6%
and Vanguard with a fee of 0.40% fee but return of 8%

What is the best one to choose?

Numbers taken from:

** VANGUARD **

Their life stratergy report
https://vanguard.co.uk/documents/adv/literature/lifestrategy-funds-performance.pdf
I plan on using 80% equity, 20% bonds in their life stratergy
Assuming past performance indicates future performance (which it doesn't, but just for the maths)
This returns 8.61% annually

** WEALTHSIMPLE **

Wealthsimple is a robo advisor. In their mid-range portfolio (60% equity, 40% bonds) their average return is around 6%
They do not charge a fee under £5000, whereas Vanguard does.

I wanted to find out if it was worth it to go with Vanguard for the fee or Wealthsimple

Results of experiment over 144 months, where the result is only printed every 12 months and you put in £100 a month are below.

Year 1 Wealthsimple: £1203 Vanguard: £1202
Interest is Wealthsimple: £4 Vanguard: £6
Year 2 Wealthsimple: £2414 Vanguard: £2412
Interest is Wealthsimple: £15 Vanguard: £22
Year 3 Wealthsimple: £3632 Vanguard: £3630
Interest is Wealthsimple: £33 Vanguard: £48
Year 4 Wealthsimple: £4857 Vanguard: £4855
Interest is Wealthsimple: £59 Vanguard: £85
Year 5 Wealthsimple: £6089 Vanguard: £6088
Interest is Wealthsimple: £92 Vanguard: £133
Year 6 Wealthsimple: £7278 Vanguard: £7329
Interest is Wealthsimple: £133 Vanguard: £191
Year 7 Wealthsimple: £8465 Vanguard: £8579
Interest is Wealthsimple: £181 Vanguard: £260
Year 8 Wealthsimple: £9652 Vanguard: £9836
Interest is Wealthsimple: £236 Vanguard: £340
Year 9 Wealthsimple: £10837 Vanguard: £11101
Interest is Wealthsimple: £298 Vanguard: £431
Year 10 Wealthsimple: £12020 Vanguard: £12375
Interest is Wealthsimple: £367 Vanguard: £532
Year 11 Wealthsimple: £13203 Vanguard: £13656
Interest is Wealthsimple: £443 Vanguard: £645
Year 12 Wealthsimple: £14384 Vanguard: £14946
Interest is Wealthsimple: £526 Vanguard: £769

Even though Vanguard earns more interest, for the first 6 years Wealthsimple will give you more money.
Although it's not a lot more, it's still more.


"""

YEARS_TO_INVEST = 12
# computers count from 0
MONTHS_TO_INVEST = YEARS_TO_INVEST * 12 + 1
START_WITH = 0.00
ADD_MONTHLY = 100

# how much fee free you get in wealth simple
# £5000 fee free for every friend you refer
WEALTHSIMPLE_FEE_FREE = 6100
WEALTHSIMPLE_YEAR_RETURN = 0.6

# based on vanguard life stratergy 80 / 20
VANGUARD_YEAR_RETURN = 0.861

class vanguard():
    def __init__(self):
        self.fee = 0.22
        self.monthlyReturn = VANGUARD_YEAR_RETURN / 12.0
        self.total = START_WITH
        self.interest = 0.00

    # function to add £100 to this fund
    def add100(self, year):
        # if year is true (it's the 12th month)
        #self.total = self.total + 100 + percentage(self.total, 0.861)
        self.total = self.total + ADD_MONTHLY + percentage(self.monthlyReturn, self.total)
        self.interest = self.interest + percentage(self.monthlyReturn, self.total)
        if year:
            # take away the fee
            self.total = self.total - percentage(self.fee, self.total)


class wealthSimple():
    def __init__(self):
        self.fee = 0.7
        self.monthlyReturn = WEALTHSIMPLE_YEAR_RETURN / 12.0
        self.total = 0.0
        self.interest = 0.0
    
    def add100(self, year):
        self.total = self.total + ADD_MONTHLY + percentage(self.monthlyReturn, self.total)
        self.interest = self.interest + percentage(self.monthlyReturn, self.total)
        if year:
            if self.total < WEALTHSIMPLE_FEE_FREE:
                self.total = self.total
            else:
                self.total = self.total - percentage(self.fee, self.total)

def percentage(percent, whole):
    return (percent * whole) / 100.0

wealthSimple = wealthSimple()
vanguard = vanguard()

year_num = 0
for i in range(1, MONTHS_TO_INVEST):
    year = False
    if i % 12 == 0 and i is not 0:
        year = True
        year_num = year_num +  1
    wealthSimple.add100(year)
    vanguard.add100(year)
    if year:
        print("Year " + str(year_num) + " Wealthsimple: £" + str(round(wealthSimple.total)) + " Vanguard: £" + str(round(vanguard.total)))
        print("Interest is Wealthsimple: £" + str(round(wealthSimple.interest)) + " Vanguard: £" + str(round(vanguard.interest)))