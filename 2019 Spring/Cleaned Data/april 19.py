```python
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import scipy.optimize as opt
import aguaclara.research.procoda_parser as pp
import numpy as np
file_location = "2019 Spring/Cleaned Data/march8.xlsx"

data = pd.read_excel(file_location)
data = pp.remove_notes(data)
time = pd.to_numeric(data["time"])
effluent_turbidity = pd.to_numeric(data["Effluent Turbidity "])

def exp_func(x, a, b, c):
  return a * np.exp(b * x) + c

optimal_parameters, covariance = opt.curve_fit(exp_func, time, effluent_turbidity)

reglineexp = exp_func(time, *optimal_parameters)

linreg = stats.linregress(time, effluent_turbidity)
slope, intercept, r_value = linreg[0:3]
reglinelin = time*slope + intercept

print("Slope:", slope)
print("Intercept:", intercept)
print("R-squared:", r_value ** 2)

plt.plot(time, effluent_turbidity, "bo")
plt.plot(time,reglinelin)
plt.plot(time,reglineexp)
plt.title("Baseline Experiment: Old Tube Settler at 2 mm/s Upflow Velocity")
plt.xlabel("Time (hours)")
plt.ylabel("Effluent Turbidity (NTU)")
```

```python
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
file_location = "2019 Spring/Cleaned Data/april 19 exp control 3mms upflow.xlsx"

data = pd.read_excel(file_location)
time1 = data["Time"][0:10000]
time2 = data["Time"][11500:25000]
time_combined = time1.append(time2)
effluent_turbidity1 = data["Effluent Turbidity"][0:10000]
effluent_turbidity2 = data["Effluent Turbidity"][11500:25000]
effluent_turbidity_combined = effluent_turbidity1.append(effluent_turbidity2)

linreg = stats.linregress(time_combined, effluent_turbidity_combined)
slope, intercept, r_value = linreg[0:3]
regline = time_combined*slope + intercept

print("Slope:", slope)
print("Intercept:", intercept)
print("R-squared:", r_value ** 2)

#plt.plot(time,effluent_turbidity, "bo")
plt.plot(time_combined, effluent_turbidity_combined, "bo")
plt.plot(time_combined,regline)
plt.title("Baseline Experiment: New Tube Settler at 3 mm/s Upflow Velocity")
plt.xlabel("Time (hours)")
plt.ylabel("Effluent Turbidity (NTU)")
```

```python
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import numpy as np
file_location = "2019 Spring/Cleaned Data/march 11 exp w stackedcyl 2mms upflow.xlsx"

data = pd.read_excel(file_location)
time = data["time"][0:36700]
effluent_turbidity = data["Effluent Turbidity"][0:36700]

linreg = stats.linregress(time, effluent_turbidity)
slope, intercept, r_value = linreg[0:3]
regline = time*slope + intercept

print("Slope:", slope)
print("Intercept:", intercept)
print("R-squared:", r_value ** 2)

def exp_func(x, a, b, c):
  return a * np.exp(b * x) + c

optimal_parameters, covariance = opt.curve_fit(exp_func, time, effluent_turbidity)

reglineexp = exp_func(time, *optimal_parameters)

plt.plot(time, effluent_turbidity, "bo")
plt.plot(time,regline)
plt.plot(time,reglineexp)
plt.title("Old Tube Settler with Stacked Cylinder at 2 mm/s Upflow Velocity")
plt.xlabel("Time (hours)")
plt.ylabel("Effluent Turbidity (NTU)")
```

```python
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import numpy as np
file_location = "C:/Users/mlee0/github/HRS-Bot-Geo/2019 Spring/Cleaned Data/april 11 exp w lincyl 2 mms upflow.xlsx"

data = pd.read_excel(file_location)
time = data["Time"][0:73647]
effluent_turbidity = data["Effluent Turbidity"][0:73647]

linreg = stats.linregress(time, effluent_turbidity)
slope, intercept, r_value = linreg[0:3]
regline = time*slope + intercept

print("Slope:", slope)
print("Intercept:", intercept)
print("R-squared:", r_value ** 2)


plt.plot(time, effluent_turbidity, "bo")
plt.plot(time,regline)
plt.title("Experiment with New Tube Settler with Linear Cylinder at 2 mm/s Upflow Velocity")
plt.xlabel("Time (hours)")
plt.ylabel("Effluent Turbidity (NTU)")
```

```python
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import numpy as np
import aguaclara.research.procoda_parser as pp
file_location = "C:/Users/mlee0/github/HRS-Bot-Geo/2019 Spring/Cleaned Data/april 13 exp control 2 mms upflow.xlsx"

data = pd.read_excel(file_location)
data = pp.remove_notes(data)
time = data["Time"]
effluent_turbidity = data["Effluent Turbidity"]

linreg = stats.linregress(time, effluent_turbidity)
slope, intercept, r_value = linreg[0:3]
regline = time*slope + intercept

print("Slope:", slope)
print("Intercept:", intercept)
print("R-squared:", r_value ** 2)

def exp_func(x, a, b, c):
  return a * np.exp(b * x) + c

optimal_parameters, covariance = opt.curve_fit(exp_func, time, effluent_turbidity)

reglineexp = exp_func(time, *optimal_parameters)

plt.plot(time, effluent_turbidity, "bo")
plt.plot(time,regline)
plt.plot(time,reglineexp)
plt.title("Baseline Experiment: New Tube Settler at 2 mm/s Upflow Velocity")
plt.xlabel("Time (hours)")
plt.ylabel("Effluent Turbidity (NTU)")
```
