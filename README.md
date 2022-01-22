# Cologne Public Transport Stations

This repository contains all public transport stations in Cologne.

---

## Data

The file `stations.csv` contains the public transport stations. The file is a UTF-8 encoded text file and Comma Separated Value (CSV) formatted with, a comma `,` as delimiter of the fields. A semicolon `;` is used to delimitate the values for lists inside fields.

### Columns

Column Name | Notes
----------- | -----
`name` | Name of the station in German.
`latitude` | Coordinates as a decimal value.
`longitude` | Coordinates as a decimal value.
`bus` | Bus lines at the station as a semicolon-separated list.
`tram` | Tram (Straßenbahn) lines at the station as a semicolon-separated list.
`strain` | Suburban Train (S-Bahn) lines at the station as a semicolon-separated list.
`train` | Train (Regionalzüge) lines at the station as a semicolon-separated list.
`other` | Other lines at the station as a semicolon-separated list.

## Tests

The tests ensure the consistency of every station in the list. Content errors aren't covered with these tests. 

```bash
pip3 install -r requirements.txt 
python3 -m pytest -q tests/cvs_format_tests.py
```
