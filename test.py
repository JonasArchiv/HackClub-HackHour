from hackhour_api import HackHourManager

manager = HackHourManager()
stats = manager.get_stats()

if stats:
    print(stats)
