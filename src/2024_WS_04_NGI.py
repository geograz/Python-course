# -*- coding: utf-8 -*-
"""
Script for the "Python basics for geoscience and geotechnics"
from the Norwegian Geotechnical Institute. The course is held in October 2024
in 4x4 hour sessions.

This script contains the code that was written during the fourth session
The code is for educational purposes only.
All content of the repository falls under the MIT-license -> see license file.

Author: Dr. Georg H. Erharter, georg.erharter@ngi.no
"""

###########################
# session 4 on 16th October 2024
###########################

### modules, code environments, module documentation

# we us modules with using the "import" keyword and can also abreviate them in
# the same row

# modules should be imported ontop of a script
import matplotlib.pyplot as plt
import numpy as np  # numpy is short for "numerical python" and a math module
import pandas as pd

# numpy works based on arrays and is much faster than classical loops
exemplary_array = np.array([[1, 2, 3, 4, 5],
                            [1, 2, 3, 4, 5]])

# the shape of the array can be queried and individual columns / rows accessed
print(exemplary_array.shape)
print(exemplary_array[:, 1])
print(exemplary_array[1, :])

# number generation
print(np.arange(start=10, stop=30, step=4))
print(np.linspace(start=2, stop=5, num=5))

# exercsie 11
numbers = [1, 2, 3, 1, 3, 3, 2, 1, 4, 6, 4, 1]

print(f'mean value: {round(np.mean(numbers), 2)}')
print(f'median value: {round(np.median(numbers), 2)}')
print(f'variance value: {round(np.var(numbers), 2)}')
print(f'std value: {round(np.std(numbers), 2)}')


# matplotlib example

# let's create some random numbers

N_NUMBERS = 1000


rng = np.random.default_rng()

# exemplary variables of different statistical distributions
x = rng.uniform(0, 5, N_NUMBERS)
y = rng.exponential(2, N_NUMBERS)
z = rng.normal(2.5, 1, N_NUMBERS)

time = np.arange(0, N_NUMBERS)  # seconds

# plotting
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

ax[0].hist(z, edgecolor='black', bins=60, density=True, zorder=30, alpha=.5,
           label='normal', color='forestgreen')
ax[0].hist(x, edgecolor='black', bins=60, density=True, zorder=30, alpha=.5,
           label='uniform')

ax[0].legend()
ax[0].set_xlabel('random numbers')
ax[0].set_ylabel('number of datapoints')
ax[0].grid(alpha=0.5, zorder=10)

ax[1].plot(time, z, label='normal', color='forestgreen', alpha=.5)
ax[1].plot(time, x, label='uniform', alpha=.5)

ax[1].legend()
ax[1].set_xlabel('time')
ax[1].set_ylabel('random numbers')
ax[1].grid(alpha=0.5)

plt.tight_layout()
plt.savefig('test.jpg', dpi=220)

# there are more complex alternatives to plot generation that allow to be more
# creative. E.g.: gridspec


# pandas is a module for data import and export and also for doing mathematical
# operations with data (it is based on mupy). Matplotlib is a module for
# plotting

# example where we use the CPT Dataset Premstaller Geotechnik
# https://www.tugraz.at/en/institutes/ibg/research/computational-geotechnics-group/database
FOLDER = r'C:\folder\where\you\store\data\Database_CPT_PremstallerGeotechnik'
FILE = 'CPT_PremstallerGeotechnik_revised.csv'
# read in file
df = pd.read_csv(fr'{FOLDER}\{FILE}')

# to get basic statistics of dataframe and save to excel file
df_statistics = df.describe()
df_statistics.to_excel('cpt_stats.xlsx')

# you can get column names like this
print(df.columns)

# math can be done with pandas like that
friction_ratio = df['fs (kPa)'] / df['qc (MPa)']

# example to create plots of the qc and fs of 10 of the CPT tests
for ID in range(200, 210):

    df_cpt = df[df['ID'] == ID]

    fig, (ax1, ax2) = plt.subplots(figsize=(8, 6), nrows=1, ncols=2)

    ax1.plot(df_cpt['qc (MPa)'], df_cpt['Depth (m)'])
    ax1.set_ylim(top=0, bottom=df_cpt['Depth (m)'].max())
    ax1.set_xlabel('qc (MPa)')
    ax1.set_ylabel('Depth (m)')
    ax1.grid(alpha=0.5)

    ax2.plot(df_cpt['fs (kPa)'], df_cpt['Depth (m)'])
    ax2.set_ylim(top=0, bottom=df_cpt['Depth (m)'].max())
    ax2.set_xlabel('fs (kPa)')
    ax2.grid(alpha=0.5)

    fig.suptitle(f'CPT test {ID}')

    plt.tight_layout()
    plt.savefig(f'cpt{ID}_test.jpg', dpi=220)
    plt.close()


# Exercise 12
FOLDER = r'C:\folder\where\you\store\data\Database_CPT_PremstallerGeotechnik'
FILE = 'CPT_PremstallerGeotechnik_revised.csv'
df = pd.read_csv(fr'{FOLDER}\{FILE}')

print(f'there are {len(df)} datapoints in the dataset')
print(f'there are {max(df["ID"])+1} soundings in the dataset')

print(df['test_type'].unique())
cpt_count, cptu_count, scpt_count, scptu_count = 0, 0, 0, 0
basins, depths, ids = [], [], []
for id_, df_test in df.groupby('ID'):
    match df_test['test_type'].iloc[0]:  # noqa
        case 'CPT':
            cpt_count += 1
        case 'CPTu':
            cptu_count += 1
        case 'SCPT':
            scpt_count += 1
        case 'SCPTu':
            scptu_count += 1
    basins.append(df_test['basin_valley'].iloc[0])
    depths.append(df_test['Depth (m)'].max())
    ids.append(id_)

print(f'there are {cpt_count} CPT, {cptu_count}, CPTu, {scpt_count} SCPT, {scptu_count} SCPTu in the dataset')
print(f'the tests come from {len(df["basin_valley"].unique())} different sedimentary basins')

basin_names, n_tests = np.unique(basins, return_counts=True)
ind_max = np.argmax(n_tests)
print(f'with {n_tests[ind_max]} the most tests were made in {basin_names[ind_max]}')

ind_max_depth = np.argmax(depths)
print(f'with {depths[ind_max_depth]}, test {ids[ind_max_depth]} is the deepest test')

# Exercise 13
FOLDER = r'C:\folder\where\you\store\data\Database_CPT_PremstallerGeotechnik'
FILE = 'CPT_PremstallerGeotechnik_revised.csv'
df = pd.read_csv(fr'{FOLDER}\{FILE}')

df_CPT1 = df[df['ID'] == 1]
fig, (ax1, ax2) = plt.subplots(figsize=(8, 4), nrows=1, ncols=2)

ax1.scatter(df_CPT1['Fr (%)'], df_CPT1['Qtn (-)'], alpha=0.5, label='raw data',
            c=df_CPT1['SBT (-)'])
ax1.scatter(df_CPT1['Fr (%)'].mean(), df_CPT1['Qtn (-)'].mean(),
            label='average', s=80)
ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.set_xlim(left=0.1, right=10)
ax1.set_ylim(bottom=1, top=1000)
ax1.grid(alpha=0.5)
ax1.set_xlabel('Fr (%)')
ax1.set_ylabel('Qtn (-)')
ax1.legend()

ax2.hist(df[df['SBT (-)'] == 7]['Qtn (-)'], alpha=0.5, edgecolor='black',
         label='soil type 7', density=True)
ax2.hist(df[df['SBT (-)'] == 3]['Qtn (-)'], alpha=0.5, edgecolor='black',
         label='soil type 3', density=True)
ax2.set_xlabel('Qtn (-)')
ax2.legend()

plt.tight_layout()
