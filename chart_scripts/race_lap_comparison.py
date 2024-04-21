import fastf1.plotting
import matplotlib
from matplotlib import pyplot as plt
import mplcursors

matplotlib.use('TkAgg')
fastf1.plotting.setup_mpl()


#%%
def laps_comparison_for_session(session, list_of_names):
    plt.figure(figsize=(10, 6))
    for name in list_of_names:
        laps = session.laps.pick_driver(name)
        plt.plot(laps.LapNumber, laps.LapTime, label=name, marker='o', markersize=2)
    mplcursors.cursor(hover=True, highlight=True)
    plt.legend()
    plt.title('Driver lap times')
    plt.xlabel('Lap Number')
    plt.ylabel('Time (MM:SS)')
    plt.ylim([1.5 / (24 * 60), 2 / (24 * 60)])

    plt.show()
