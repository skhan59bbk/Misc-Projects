'''
Rough analysis of the impact of overpayments
to life of mortgage balance
'''

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')


initial = 375000
rate = 0.0149
term = 30

# without overpayment

payment_26m = 1290.9
payment_333m = 1661.7
payment_1m = 1660.8 

balance = [round(initial * ((1 + rate) ** i)) for i in range(30)]
payments = [round(payment_26m * 12)] * 2 + [round(payment_26m * 2 + payment_333m * 10)] * 1 + [round(payment_333m * 12)] * 26 + [round(payment_1m + payment_333m * 11)]
cumul_pay = np.cumsum(payments)
remaining = [balance[j] - cumul_pay[j] for j in range(term)]



# with overpayment

overpayment = int(input('How much to overpay per month?  '))

payment_26m_over = 1290.9 + overpayment
payment_333m_over = 1661.7 + overpayment
payment_1m_over = 1660.8 

balance_over = [round(initial * ((1 + rate) ** i)) for i in range(30)]
payments_over = [round(payment_26m_over * 12)] * 2 + [round(payment_26m_over * 2 + payment_333m_over * 10)] * 1 + [round(payment_333m_over * 12)] * 26 + [round(payment_1m_over + payment_333m_over * 11)]
cumul_pay_over = np.cumsum(payments_over)
remaining_over = [balance_over[j] - cumul_pay_over[j] for j in range(term)]


# plotting

plt.plot(remaining, label='Standard')
plt.plot(remaining_over, color='blue', label='Overpay £'+str(overpayment)+'/mth')
plt.title('Outstanding Mortgage Balance')
plt.xlabel('Years')
plt.ylabel('Balance GBP')
plt.ylim(0,380000)
plt.legend()
plt.show()
