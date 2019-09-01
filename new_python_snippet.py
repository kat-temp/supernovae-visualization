import matplotlib.pyplot as plt

with open('SNType.txt') as f:
    sn_list= f.readlines()

sn_type_dict = {}

for type in ['Ia','Ib','Ic', 'II']:
    sn_type_dict[type] = sum(1 for line in sn_list if type in line)

print(sn_type_dict)

plt.bar(range(len(sn_type_dict)), list(sn_type_dict.values()), align='center')
plt.xticks(range(len(sn_type_dict)), list(sn_type_dict.keys()))
plt.ylim(top=350)
plt.xlabel("Number of Observed Supernovae")
plt.ylabel("Observed Supernovae Type")

plt.show()