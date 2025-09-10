import fastf1.plotting
import matplotlib
from matplotlib import pyplot as plt
import mplcursors

matplotlib.use('TkAgg')
fastf1.plotting.setup_mpl()


#%%
def laps_comparison_for_session(session, list_of_names):
    plt.figure(figsize=(10, 6))
    all_lap_times = []
    
    for name in list_of_names:
        laps = session.laps.pick_driver(name)
        plt.plot(laps.LapNumber, laps.LapTime, label=name, marker='o', markersize=2)
        all_lap_times.extend(laps.LapTime.dropna())
    
    # Calculate dynamic y-limits with 5% padding
    min_time = min(all_lap_times)
    max_time = max(all_lap_times)
    padding = (max_time - min_time) * 0.05
    plt.ylim([min_time - padding, max_time + padding])
    
    mplcursors.cursor(hover=True, highlight=True)
    plt.legend()
    plt.title('Driver lap times')
    plt.xlabel('Lap Number')
    plt.ylabel('Time (MM:SS)')

    plt.show()
