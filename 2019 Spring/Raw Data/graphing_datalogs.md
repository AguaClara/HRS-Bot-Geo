The following codes were used to plot the graphs of effluent turbidity versus time using the data collected by the Spring 2019 HRS Bottom Geometry team.

####Baseline Experiment: Old Tube Settler at 2mm/s Upflow Velocity
```python
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import numpy as np
import aguaclara.research.procoda_parser as pp

data_path = "2019 Spring/Raw Data/"
columns = pp.get_data_by_time(path=data_path, columns=[0, 2],
                              dates=["3-8-2019", "3-9-2019"], start_time="20:00", end_time="16:00")
time = columns[0]
effluent_turbidity = columns[1]
elapsed_time = (np.array(time)-time[0])*24

plt.title("Baseline Experiment: Old Tube Settler at 2mm/s Upflow Velocity")
plt.xlabel("Time (hours)")
plt.ylabel("Effluent Turbidity (NTU)")
plt.plot(elapsed_time, effluent_turbidity, "bo", markersize = 5)
plt.show()
```

####Old Tube Settler With Stacked Cylinder at 2mm/s Upflow Velocity
```python
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import numpy as np
import aguaclara.research.procoda_parser as pp

data_path = "2019 Spring/Raw Data/"
columns = pp.get_data_by_time(path=data_path, columns=[0, 2],
                              dates=["3-11-2019", "3-12-2019"], start_time="13:15", end_time="6:00")
time = columns[0]
effluent_turbidity = columns[1]
elapsed_time = (np.array(time)-time[0])*24

plt.title("Old Tube Settler With Stacked Cylinder at 2mm/s Upflow Velocity")
plt.xlabel("Time (hours)")
plt.ylabel("Effluent Turbidity (NTU)")
plt.ylim(4, 10)
plt.plot(elapsed_time, effluent_turbidity, "bo", markersize = 5)
plt.show()
```

####Baseline Experiment: New Tube Settler at 2mm/s Upflow Velocity
```python
#NEW TUBE SETTLER BASELINE AT 2mm/s UPFLOW VELOCITY
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import numpy as np
import aguaclara.research.procoda_parser as pp

data_path = "2019 Spring/Raw Data/"
columns = pp.get_data_by_time(path=data_path, columns=[0, 2],
                              dates=["4-13-2019", "4-14-2019"])
time = columns[0]
effluent_turbidity = columns[1]
elapsed_time = (np.array(time)-time[0])*24

plt.title("Baseline Experiment: New Tube Settler at 2mm/s Upflow Velocity")
plt.xlabel("Time (hours)")
plt.ylabel("Effluent Turbidity (NTU)")
plt.plot(elapsed_time, effluent_turbidity, "bo", markersize = 5)
plt.show()
```

####New Tube Settler With Linear Cylinder at 2mm/s Upflow Velocity
```python
#NEW TUBE SETTLER WITH LINCYL AT 2mm/s UPFLOW VELOCITY
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import numpy as np
import aguaclara.research.procoda_parser as pp

data_path = "2019 Spring/Raw Data/"
columns = pp.get_data_by_time(path=data_path, columns=[0, 2],
                              dates=["4-11-2019", "4-12-2019"], start_time="21:00", end_time="15:00")
time = columns[0]
effluent_turbidity = columns[1]
elapsed_time = (np.array(time)-time[0])*24

plt.title("New Tube Settler With Linear Cylinder at 2mm/s Upflow Velocity")
plt.xlabel("Time (hours)")
plt.ylabel("Effluent Turbidity (NTU)")
plt.plot(elapsed_time, effluent_turbidity, "bo", markersize = 5)
plt.show()
```

####Baseline Experiment: New Tube Settler at 3mm/s Upflow Velocity
```python
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import numpy as np
import aguaclara.research.procoda_parser as pp

data_path = "2019 Spring/Raw Data/"
columns = pp.get_data_by_time(path=data_path, columns=[0, 3],
                              dates=["4-19-2019", "4-20-2019"], start_time="20:00")
time = columns[0]
effluent_turbidity = columns[1]
elapsed_time = (np.array(time)-time[0])*24

plt.title("Baseline Experiment: New Tube Settler at 3mm/s Upflow Velocity")
plt.xlabel("Time (hours)")
plt.ylabel("Effluent Turbidity (NTU)")
plt.ylim(top=25)
plt.plot(elapsed_time, effluent_turbidity, "bo", markersize = 5)
plt.show()
```

```python
a=1
```
