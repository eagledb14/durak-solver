from deck import Deck
from heuristic import get_high_heuristic
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
import numpy as np
import random

d = Deck()
score = {}
tries = 10_000
for _ in range(tries):
    s = random.randint(1,10)

    if len(d) < s:
        d = Deck()

    h = d.draw(s)
    hu = get_high_heuristic(h, d.trump_card)
    if hu in score:
        score[hu] += 1
    else:
        score[hu] = 1


items = sorted(score.items(), key=lambda x: x[0])
keys = np.array([item[0] for item in items])
values = np.array([(item[1] / tries) * 100 for item in items])

key_smooth = np.linspace(keys.min(), keys.max(), 1000)
spl = make_interp_spline(keys, values, k=3)
values_smooth = spl(key_smooth)

plt.plot(key_smooth, values_smooth)

plt.title('High Heuristic spread')
plt.ylabel('Score Frequency (%)')
plt.xlabel('Heuristic score')

plt.show()

