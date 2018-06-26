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

Results of experiment over 144 months, where the result is only printed every 12 months and you put in £100 a month:

Month 12 Wealthsimple: £1592 Vanguard: £1664
Removing the £100 this would be, Wealthsimple: £392 Vanguard: £464
Month 24 Wealthsimple: £4450 Vanguard: £4936
Removing the £100 this would be, Wealthsimple: £2050 Vanguard: £2536
the fee is applied
Month 36 Wealthsimple: £9517 Vanguard: £11372
Removing the £100 this would be, Wealthsimple: £5917 Vanguard: £7772
the fee is applied
Month 48 Wealthsimple: £18551 Vanguard: £24030
Removing the £100 this would be, Wealthsimple: £13751 Vanguard: £19230
the fee is applied
Month 60 Wealthsimple: £34663 Vanguard: £48922
Removing the £100 this would be, Wealthsimple: £28663 Vanguard: £42922
the fee is applied
Month 72 Wealthsimple: £63394 Vanguard: £97877
Removing the £100 this would be, Wealthsimple: £56194 Vanguard: £90677
the fee is applied
Month 84 Wealthsimple: £114631 Vanguard: £194154
Removing the £100 this would be, Wealthsimple: £106231 Vanguard: £185754
the fee is applied
Month 96 Wealthsimple: £206000 Vanguard: £383499
Removing the £100 this would be, Wealthsimple: £196400 Vanguard: £373899
the fee is applied
Month 108 Wealthsimple: £368937 Vanguard: £755875
Removing the £100 this would be, Wealthsimple: £358137 Vanguard: £745075
the fee is applied
Month 120 Wealthsimple: £659500 Vanguard: £1488212
Removing the £100 this would be, Wealthsimple: £647500 Vanguard: £1476212
the fee is applied
Month 132 Wealthsimple: £1177657 Vanguard: £2928470
Removing the £100 this would be, Wealthsimple: £1164457 Vanguard: £2915270
the fee is applied
Month 144 Wealthsimple: £2101680 Vanguard: £5760966
Removing the £100 this would be, Wealthsimple: £2087280 Vanguard: £5746566

** RESULTS OF FIRST YEAR **
Each month is printed here:

Month 1 Wealthsimple: £100 Vanguard: £100
Month 2 Wealthsimple: £205 Vanguard: £207
Month 3 Wealthsimple: £315 Vanguard: £320
Month 4 Wealthsimple: £431 Vanguard: £442
Month 5 Wealthsimple: £553 Vanguard: £571
Month 6 Wealthsimple: £680 Vanguard: £709
Month 7 Wealthsimple: £814 Vanguard: £857
Month 8 Wealthsimple: £955 Vanguard: £1014
Month 9 Wealthsimple: £1103 Vanguard: £1181
Month 10 Wealthsimple: £1258 Vanguard: £1360
Month 11 Wealthsimple: £1421 Vanguard: £1551
Month 12 Wealthsimple: £1592 Vanguard: £1747

Conclusion: Although Wealthsimple may seem like the better option, going with Vanguard from the get-go gets you the good returns.

But this is assuming Vanguard will return 8%. If they return 7%, Vanguard will still be better to go with.
If they return 6%, Wealthsimple would be better to go with for the first 4 years.

You do not know how the market will behave, however, look here:

Month 12 Wealthsimple: £1592 Vanguard: £1585
Removing the £100 this would be, Wealthsimple: £392 Vanguard: £385
Month 24 Wealthsimple: £4450 Vanguard: £4421
Removing the £100 this would be, Wealthsimple: £2050 Vanguard: £2021
the fee is applied
Month 36 Wealthsimple: £9517 Vanguard: £9493
Removing the £100 this would be, Wealthsimple: £5917 Vanguard: £5893

Assuming you put £100 in each month you'll reach the £5k limit by the start of the third year.
The money you earn from wealthsimple is £29 more than Vanguard. After the third year Wealthsimple is still worth it
but they don't make **that** much money more, just £24 more.

After the fourth year, the results look like this:

Removing the £100 this would be, Wealthsimple: £13751 Vanguard: £13765

Vanguard is now worth more.

In total, you're set to make around £50 more if you went with Wealthsimple than if you went with Vanguard at the start.
Assuming you input £100 per month. If you put in more than £100 a month, you'll reach the £5k limit faster which means that
Vanguard will take over as the most worthwhile in a year or two.
"""

class vanguard():
    def __init__(self):
        self.fee = 0.4
        self.monthlyReturn = 0.6 / 12.0
        self.total = 0.0

    # function to add £100 to this fund
    def add100(self, year):
        # if year is true (it's the 12th month)
        self.total = self.total + 100 + (self.total * self.monthlyReturn)
        if year:
            # take away the fee
            self.total = self.total - ((self.total * self.fee) / 100.0)

class wealthSimple():
    def __init__(self):
        self.fee = 0.7
        self.monthlyReturn = 0.6 / 12.0
        self.total = 0.0
    
    def add100(self, year):
        self.total = self.total + 100 + (self.total * self.monthlyReturn)
        if year:
            if self.total < 5000:
                self.total = self.total
            else:
                print("the fee is applied")
                self.total = self.total - ((self.total * self.fee) / 100.0)

wealthSimple = wealthSimple()
vanguard = vanguard()

for i in range(1, 145):
    year = False
    if i % 12 == 0 and i is not 0:
        year = True
    wealthSimple.add100(year)
    vanguard.add100(year)
    if year:
        print("Month " + str(i) + " Wealthsimple: £" + str(round(wealthSimple.total)) + " Vanguard: £" + str(round(vanguard.total)))
        print("Removing the £100 this would be, Wealthsimple: £" + str(round(wealthSimple.total - (100 * i))) + " Vanguard: £" + str(round(vanguard.total - (100 * i))))