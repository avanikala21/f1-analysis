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
def driver_lap_telemetry(lap_number, driver_names):
    for name in driver_names:
        telemetry = session.laps.pick_laps(lap_number).pick_driver(name).get_car_data()
        driver_speed = telemetry['Speed']
        driver_time = telemetry['Time']
        plt.plot(driver_time, driver_speed)
    mplcursors.cursor(hover=True, highlight=True)
    plt.legend(driver_names)
    plt.title(f'Lap {lap_number} Telemetry')
    plt.xlabel('Lap Time (MM:SS)')
    plt.ylabel('Speed (km/h)')
    plt.show()


#%%
driver_lap_telemetry(2, ['VER', 'LEC', 'NOR'])
#%%
