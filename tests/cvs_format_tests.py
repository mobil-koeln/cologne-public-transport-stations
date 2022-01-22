import csv


class TestCSVParsing:

    def test_csv_parsing(self):

        with open('stations.csv', newline='') as csvfile:
            stations = csv.DictReader(csvfile)
            for station in stations:
                assert station["name"] != None, f"Name is None in {station}"
                assert station["latitude"] != None, f"Latitude is None in {station}"
                assert station["longitude"] != None, f"Longitude is None in {station}"
                assert station["bus"] != None, f"Bus is None in {station}"
                assert station["tram"] != None, f"Tram is None in {station}"
                assert station["strain"] != None, f"STrain is None in {station}"
                assert station["train"] != None, f"Train is None in {station}"
                assert station["other"] != None, f"Other is None in {station}"
