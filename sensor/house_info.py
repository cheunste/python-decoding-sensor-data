from datetime import date, datetime


class HouseInfo():
    def __init__(self, data):
        self.data = data

    def get_data_by_area(self, field, rec_area=0):
        # the valid field values are the column names of the data files in the datasets fodler
        field_data = []

        '''
            The self.data class variable is a list of dictionaries. The keys are equal to the columns
            names in the data file (when the field input is set to 'id' then the record[field] value correspond to the 'id' column
            values. This method, the rec_area variable maps to 'area' column values)
            '''

        for record in self.data:
            if rec_area == 0:
                field_data.append(record[field])
            elif rec_area == int(record['area']):
                field_data.append(record[field])
        return field_data

    def get_data_by_date(self, field, rec_date=date.today()):
        field_data = []
        for record in self.data:
            if rec_date.strftime("%m/%d/%y") == record['date']:
                field_data.append(record[field])
        return field_data
