from house_info import HouseInfo
from datetime import date, datetime


class EnergyData (HouseInfo):
    ENERGY_PER_BULB = 0.2
    ENERGY_BITS = 0x0F0

    def _get_energy(self, rec):
        # energy_usage field comes as a 3 digit hex number (12 bits), but only the middle hex number (bit 4-7) gives the energy usage value
        # use bitwise oeprations to extract it
        energy = int(rec, base=16)
        energy &= self.ENERGY_BITS
        energy >> 4
        return energy

    def _convert_data(self, data):
        recs = []
        for rec in data:
            recs.append(self._get_energy(rec))
        return recs

    def get_data_by_area(self, rec_area=0):
        recs = super().get_data_by_area("energy_usage", rec_area)
        return self._convert_data(recs)

    def get_data_by_date(self, rec_date=date.today()):
        recs = super().get_data_by_date("energy_usage", rec_date)
        return self._convert_data(recs)

    def calculate_energy_usage(self, data):
        total_energy = sum([x for x in data if x == "field"])
