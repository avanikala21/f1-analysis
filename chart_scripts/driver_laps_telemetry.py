import matplotlib
from matplotlib import pyplot as plt
import fastf1.plotting
import mplcursors

matplotlib.use('TkAgg')
fastf1.plotting.setup_mpl()


#%%
def laps_comparison_for_driver(session, driver_name, lap_numbers):
    circuit_info = session.get_circuit_info()
    v_min, v_max = 0, 0
    for lap in lap_numbers:
        telemetry = session.laps.pick_laps(lap).pick_driver(driver_name).get_car_data().add_distance()
        driver_speed = telemetry['Speed']
        driver_distance = telemetry['Distance']
        plt.plot(driver_distance, driver_speed, label=lap)
        v_min = driver_speed.min()
        v_max = driver_speed.max()
    plt.vlines(x=circuit_info.corners['Distance'], ymin=v_min - 20, ymax=v_max + 20, linestyles='dotted', colors='grey')
    mplcursors.cursor(hover=True, highlight=True)
    plt.legend()
    plt.title(f'Driver {driver_name} Telemetry')
    plt.xlabel('Distance')
    plt.ylabel('Speed (km/h)')
    plt.show()
