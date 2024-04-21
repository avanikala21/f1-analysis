import fastf1

from chart_scripts.driver_laps_telemetry import laps_comparison_for_driver
from chart_scripts.race_lap_comparison import laps_comparison_for_session
from chart_scripts.single_lap_telemetry import drivers_comparison_for_lap

session = fastf1.get_session(2024, 'China', 'S')
session.load(telemetry=True, laps=True, weather=False)

laps_comparison_for_session(session, list_of_names=['VER', 'NOR'])

drivers_comparison_for_lap(session, driver_names=['VER', 'NOR'], lap_number=5)

laps_comparison_for_driver(session, lap_numbers=[1, 2, 3], driver_name='NOR')
