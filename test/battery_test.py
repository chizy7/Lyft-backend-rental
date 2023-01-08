from battery.battery_type.nubbing_battery import NubbingBattery
from battery.battery_type.splinder_battery import SplinderBattery

import unittest
import datetime


class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = datetime.datetime(2022, 7, 31)
        last_service_date = datetime.datetime(2019,1,27)
        battery = NubbingBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = datetime.datetime(2022, 7, 31)
        last_service_date = datetime.datetime(2021,1,10)
        battery = NubbingBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())


class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = datetime.datetime(2022, 7, 31)
        last_service_date = datetime.datetime(2017,1,25)
        battery = SplinderBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = datetime.datetime(2022, 7, 31)
        last_service_date = datetime.datetime(2021,1,10)
        battery = SplinderBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())