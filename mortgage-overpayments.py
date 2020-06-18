import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')


initial = 375000
rate = 0.0149
term = 30

payment_26m = 1290.9
payment_333m = 1661.7
payment_1m = 1660.8

balance = [round(initial * ((1 + rate) ** i)) for i in range(30)]
payments = [round(payment_26m * 12)] * 2 + [round(payment_26m * 2 + payment_333m * 10)] * 1 + [round(payment_333m * 12)] * 26 + [round(payment_1m + payment_333m * 11)]
cumul_pay = np.cumsum(payments)
remaining = [balance[j] - cumul_pay[j] for j in range(term)]

plt.plot(remaining)
plt.title('Outstanding Mortgage Balance')
plt.xlabel('Years')
plt.ylabel('Balance GBP')
plt.show()
