import matplotlib.pyplot as plt

blood_sugar_men = [113, 85, 90, 150, 149, 88, 93, 115, 135, 80, 77, 82, 129]

blood_sugar_women = [67, 98, 89, 120, 133, 150, 84, 69, 65, 102, 111, 140, 155]

type = [blood_sugar_men, blood_sugar_women]
colors = ['g', 'r']
label = ['Men','Women']
bins = [60, 80, 100, 120, 140, 160]

# Status
#80 --> 100 : Normal
#100 --> 120 : Prediabetes
#120 --> 160 : Diabetes

plt.hist(type, bins=bins, rwidth=0.95, color=colors, label=label, orientation='horizontal')

plt.title("Blood Sugar Level Distribution")
plt.legend()
plt.show()