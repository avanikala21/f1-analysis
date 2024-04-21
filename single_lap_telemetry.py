import matplotlib
from matplotlib import pyplot as plt
import fastf1.plotting
import mplcursors

matplotlib.use('TkAgg')

#%%

fastf1.plotting.setup_mpl()
session = fastf1.get_session(2024, 'China', 'S')
session.load(telemetry=True, laps=True, weather=False)

#%%
circuit_info = session.get_circuit_info()


#%%
def driver_lap_telemetry(lap_number, driver_names):
    v_min, v_max = 0, 0
    for name in driver_names:
        telemetry = session.laps.pick_laps(lap_number).pick_driver(name).get_car_data().add_distance()
        driver_speed = telemetry['Speed']
        driver_distance = telemetry['Distance']
        plt.plot(driver_distance, driver_speed, label=name)
        v_min = driver_speed.min()
        v_max = driver_speed.max()
    plt.vlines(x=circuit_info.corners['Distance'], ymin=v_min - 20, ymax=v_max + 20, linestyles='dotted', colors='grey')
    mplcursors.cursor(hover=True, highlight=True)
    plt.legend()
    plt.title(f'Lap {lap_number} Telemetry')
    plt.xlabel('Distance')
    plt.ylabel('Speed (km/h)')
    plt.show()


#%%
driver_lap_telemetry(2, ['VER', 'LEC', 'NOR'])
#%%
