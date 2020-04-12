import flask
from flask import request, jsonify
import csv
import json
from json2html import *

app = flask.Flask(__name__)
app.config["DEBUG"] = True

data_file_dir = "C:/Users/anush/PycharmProjects/titanhacks/datafiles"

all_races = []
white_alone = []
white_not_hispanic = []
black_alone_or_in_combo = []
black_alone = []
asian_alone_or_in_combo = []
asian_and_pacific_islander = []
hispanic = []
min_max = []
percentage_data = []
degrees = []


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Income Trend Analysis By Race Across the US</h1><html>
    <body>
        <p><a href=/api/v1/resources/inequality_rates/degrees_by_race><input type=”button” value=Degrees_By_Race></a></p>
        <p><a href=/api/v1/resources/inequality_rates/income_by_race><input type=”button” value=Income_By_Race></a></p>
        <p><a href=/api/v1/resources/inequality_rates/min_max><input type=”button” value=Income-Min/Max></a></p>
        <p><a href=/api/v1/resources/inequality_rates/percentage_increase><input type=”button” value=Percentage_Increase></a></p>
        <p><a href=/api/v1/resources/inequality_rates/2008-2018><input type=”button” value=Income-2008/2018></a></p>
        <p><a href=/api/v1/resources/inequality_rates/comparison><input type=”button” value=Comparison></a></p>
    </body>
    </html>'''

#converts csv file of income statistics to an array
@app.route('/api/v1/resources/inequality_rates/income_by_race', methods=['GET'])
def api_income_by_race():
    csvfile = open(data_file_dir + '/household_income_by_race.csv', 'r')
    jsonfile = open('file.json', 'w')

    fieldnames = ("Year", "Num(thousands)", "MedianIncome(currentDollars)", "MedianIncome(2018dollars)", "MeanIncome(currentDollars)", "MeanIncome(2018dollars)", "Race")
    reader = csv.DictReader(csvfile, fieldnames)
    out = json.dumps([row for row in reader])
    jsonfile.write(out)
    with open('C:/Users/anush/PycharmProjects/titanhacks/file.json') as f:
        data = json.load(f)
    data = data[7:]

    #creates different lists for each race to make it easier to call for certain statistics
    a = 0
    for i in range(1):
        while True:
            try:
                x = int(data[a]["Year"][:1])
                a = a + 1
            except ValueError:
                a = a + 3
                break

    for i in range(2):
        while True:
            try:
                x = int(data[a]["Year"][:1])
                white_alone.append(data[a])
                a = a + 1
            except ValueError:
                a = a + 3
                break
    all_races.append(white_alone)

    for i in range(2):
        while True:
            try:
                x = int(data[a]["Year"][:1])
                white_not_hispanic.append(data[a])
                a = a + 1
            except ValueError:
                a = a + 3
                break
    all_races.append(white_not_hispanic)

    for i in range(1):
        while True:
            try:
                x = int(data[a]["Year"][:1])
                black_alone_or_in_combo.append(data[a])
                a = a + 1
            except ValueError:
                a = a + 3
                break
    all_races.append(black_alone_or_in_combo)

    for i in range(2):
        while True:
            try:
                x = int(data[a]["Year"][:1])
                black_alone.append(data[a])
                a = a + 1
            except ValueError:
                a = a + 3
                break
    all_races.append(black_alone)

    for i in range(1):
        while True:
            try:
                x = int(data[a]["Year"][:1])
                asian_alone_or_in_combo.append(data[a])
                a = a + 1
            except ValueError:
                a = a + 3
                break
    all_races.append(asian_alone_or_in_combo)

    for i in range(2):
        while True:
            try:
                x = int(data[a]["Year"][:1])
                asian_and_pacific_islander.append(data[a])
                a = a + 1
            except ValueError:
                a = a + 3
                break
    all_races.append(asian_and_pacific_islander)

    for i in range(1):
        while True:
            try:
                x = int(data[a]["Year"][:1])
                hispanic.append(data[a])
                a = a + 1
            except ValueError:
                break
    all_races.append(hispanic)


    return json2html.convert(json = all_races)


#finds minimum and maximum income values for all races
@app.route('/api/v1/resources/inequality_rates/min_max', methods=["GET"])
def api_minmax():
    api_income_by_race()
    result = ""
    max = 0
    max_year = 0
    min = 1000000
    min_year = 0
    for i in range(len(white_alone)):
        if int(white_alone[i]["MeanIncome(currentDollars)"]) > int(max):
            max = white_alone[i]["MeanIncome(currentDollars)"]
            max_year = white_alone[i]["Year"]
    for i in range(len(white_alone)):
        if int(white_alone[i]["MeanIncome(currentDollars)"]) < int(min):
            min = white_alone[i]["MeanIncome(currentDollars)"]
            min_year = white_alone[i]["Year"]
    min_max.append([max, min])

    result = result + ("<p>White Alone (max, min): " + str(max_year) + "-" + str(max) + ", " + str(min_year) + "-" + str(min))+ " " + white_alone[2]["MeanIncome(currentDollars)"] + "</p>"

    max = 0
    max_year = 0
    min = 1000000
    min_year = 0
    for i in range(len(white_not_hispanic)):
        if int(white_not_hispanic[i]["MeanIncome(currentDollars)"]) > int(max):
            max = white_not_hispanic[i]["MeanIncome(currentDollars)"]
            max_year = white_not_hispanic[i]["Year"]
    for i in range(len(white_not_hispanic)):
        if int(white_not_hispanic[i]["MeanIncome(currentDollars)"]) < int(min):
            min = white_not_hispanic[i]["MeanIncome(currentDollars)"]
            min_year = white_not_hispanic[i]["Year"]
    min_max.append([max, min])

    result = result + ("<p>White, Not Hispanic (max, min): " + str(max_year) + "-" + str(max) + ", " + str(min_year) + "-" + str(min)) + " " + white_not_hispanic[2]["MeanIncome(currentDollars)"] + "</p>"

    max = 0
    max_year = 0
    min = 1000000
    min_year = 0
    for i in range(len(black_alone_or_in_combo)):
        if int(black_alone_or_in_combo[i]["MeanIncome(currentDollars)"]) > int(max):
            max = black_alone_or_in_combo[i]["MeanIncome(currentDollars)"]
            max_year = black_alone_or_in_combo[i]["Year"]
    for i in range(len(black_alone_or_in_combo)):
        if int(black_alone_or_in_combo[i]["MeanIncome(currentDollars)"]) < int(min):
            min = black_alone_or_in_combo[i]["MeanIncome(currentDollars)"]
            min_year = black_alone_or_in_combo[i]["Year"]
    min_max.append([max, min])

    result = result + ("<p>Black Alone or in Combination (max, min): " + str(max_year) + "-" + str(max) + ", " + str(min_year) + "-" + str(min))+ "</p>"

    max = 0
    max_year = 0
    min = 1000000
    min_year = 0
    for i in range(len(black_alone)):
        if int(black_alone[i]["MeanIncome(currentDollars)"]) > int(max):
            max = black_alone[i]["MeanIncome(currentDollars)"]
            max_year = black_alone[i]["Year"]
    for i in range(len(black_alone)):
        if int(black_alone[i]["MeanIncome(currentDollars)"]) < int(min):
            min = black_alone[i]["MeanIncome(currentDollars)"]
            min_year = black_alone[i]["Year"]
    min_max.append([max, min])

    result = result + ("<p>Black Alone (max, min): " + str(max_year) + "-" + str(max) + ", " + str(min_year) + "-" + str(min))+ "</p>"

    max = 0
    max_year = 0
    min = 1000000
    min_year = 0
    for i in range(len(asian_alone_or_in_combo)):
        if int(asian_alone_or_in_combo[i]["MeanIncome(currentDollars)"]) > int(max):
            max = asian_alone_or_in_combo[i]["MeanIncome(currentDollars)"]
            max_year = asian_alone_or_in_combo[i]["Year"]
    for i in range(len(asian_alone_or_in_combo)):
        if int(asian_alone_or_in_combo[i]["MeanIncome(currentDollars)"]) < int(min):
            min = asian_alone_or_in_combo[i]["MeanIncome(currentDollars)"]
            min_year = asian_alone_or_in_combo[i]["Year"]
    min_max.append([max, min])

    result = result + ("<p>Asian Alone or in Conbination (max, min): " + str(max_year) + "-" + str(max) + ", " + str(min_year) + "-" + str(min))+ "</p>"

    max = 0
    max_year = 0
    min = 1000000
    min_year = 0
    for i in range(len(asian_and_pacific_islander)):
        if int(asian_and_pacific_islander[i]["MeanIncome(currentDollars)"]) > int(max):
            max = asian_and_pacific_islander[i]["MeanIncome(currentDollars)"]
            max_year = asian_and_pacific_islander[i]["Year"]
    for i in range(len(asian_and_pacific_islander)):
        if int(asian_and_pacific_islander[i]["MeanIncome(currentDollars)"]) < int(min):
            min = asian_and_pacific_islander[i]["MeanIncome(currentDollars)"]
            min_year = asian_and_pacific_islander[i]["Year"]
    min_max.append([max, min])

    result = result + ("<p>Asian and Pacific Islander (max, min): " + str(max_year) + "-" + str(max) + ", " + str(min_year) + "-" + str(min))+ "</p>"

    max = 0
    max_year = 0
    min = 1000000
    min_year = 0
    for i in range(len(hispanic)):
        if int(hispanic[i]["MeanIncome(currentDollars)"]) > int(max):
            max = hispanic[i]["MeanIncome(currentDollars)"]
            max_year = hispanic[i]["Year"]
    for i in range(len(hispanic)):
        if int(hispanic[i]["MeanIncome(currentDollars)"]) < int(min):
            min = hispanic[i]["MeanIncome(currentDollars)"]
            min_year = hispanic[i]["Year"]
    min_max.append([max, min])

    result = result + ("<p>Hispanic (max, min): " + str(max_year) + "-" + str(max) + ", " + str(min_year) + "-" + str(min))+ "</p>"
    return result

#Finds the percentage increase in income betweeen 2008 and 2018 for the races used in comparison
@app.route('/api/v1/resources/inequality_rates/percentage_increase', methods=['GET'])
def api_percentageIncrease():
    api_2008_2018()
    return ("<p>White, Not Hispanic Income Percentage Increase: " + str(100*(int(percentage_data[0]["2018"])-int(percentage_data[0]["2008"]))/int(percentage_data[0]["2008"])) + "%</p>" +
           "<p>Black Alone Percentage Increase: " + str(100*(int(percentage_data[1]["2018"])-int(percentage_data[1]["2008"]))/int(percentage_data[1]["2008"])) + "%</p>" +
           "<p>Asian Alone or In Combination Percentage Increase: " + str(100*(int(percentage_data[2]["2018"])-int(percentage_data[2]["2008"]))/int(percentage_data[2]["2008"])) + "%</p>" +
           "<p>Asian and Pacific Islander Percentage Increase: " + str(100*(int(percentage_data[3]["2018"])-int(percentage_data[3]["2008"]))/int(percentage_data[3]["2008"])) + "%</p>" +
           "<p>Hispanic Income Percentage Increase: " + str(100*(int(percentage_data[4]["2018"])-int(percentage_data[4]["2008"]))/int(percentage_data[4]["2008"])) + "%</p>")

#finds the 2008 and 2018 income stats to be used in the percentageIncrease function
@app.route('/api/v1/resources/inequality_rates/2008-2018', methods=['GET'])
def api_2008_2018():
    api_income_by_race()
    x = 0
    y = 0
    for i in range(len(white_not_hispanic)):
        cur_value = white_not_hispanic[i]
        cur_year = cur_value["Year"]
        if cur_year == "2018":
            x = cur_value["MeanIncome(currentDollars)"]
    for i in range(len(white_not_hispanic)):
        cur_value = white_not_hispanic[i]
        cur_year = cur_value["Year"]
        if cur_year == "2008":
            y = cur_value["MeanIncome(currentDollars)"]
    percentage_data.append({
        'Race': 'White, Not Hispanic',
        '2018': x,
        '2008': y})

    x = 0
    y = 0
    for i in range(len(black_alone)):
        cur_value = black_alone[i]
        cur_year = cur_value["Year"]
        if cur_year == "2018":
            x = cur_value["MeanIncome(currentDollars)"]
    for i in range(len(black_alone)):
        cur_value = black_alone[i]
        cur_year = cur_value["Year"]
        if cur_year == "2008":
            y = cur_value["MeanIncome(currentDollars)"]
    percentage_data.append({
        'Race': 'Black Alone',
        '2018': x,
        '2008': y})

    x = 0
    y = 0
    for i in range(len(asian_alone_or_in_combo)):
        cur_value = asian_alone_or_in_combo[i]
        cur_year = cur_value["Year"]
        if cur_year == "2018":
            x = cur_value["MeanIncome(currentDollars)"]
    for i in range(len(asian_alone_or_in_combo)):
        cur_value = asian_alone_or_in_combo[i]
        cur_year = cur_value["Year"]
        if cur_year == "2008":
            y = cur_value["MeanIncome(currentDollars)"]
    percentage_data.append({
        'Race': 'Asian Alone or In Combo',
        '2018': x,
        '2008': y})

    x = 0
    y = 0
    for i in range(len(asian_and_pacific_islander)):
        cur_value = asian_and_pacific_islander[i]
        cur_year = cur_value["Year"]
        if cur_year == "2018":
            x = cur_value["MeanIncome(currentDollars)"]
    for i in range(len(asian_and_pacific_islander)):
        cur_value = asian_and_pacific_islander[i]
        cur_year = cur_value["Year"]
        if cur_year == "2008":
            y = cur_value["MeanIncome(currentDollars)"]
    percentage_data.append({
        'Race': 'Asian and Pacific Islander',
        '2018': x,
        '2008': y})

    x = 0
    y = 0
    for i in range(len(hispanic)):
        cur_value = hispanic[i]
        cur_year = cur_value["Year"]
        if cur_year == "2018":
            x = cur_value["MeanIncome(currentDollars)"]
    for i in range(len(hispanic)):
        cur_value = hispanic[i]
        cur_year = cur_value["Year"]
        if cur_year == "2008":
            y = cur_value["MeanIncome(currentDollars)"]
    percentage_data.append({
        'Race': 'Hispanic',
        '2018': x,
        '2008': y})

    return json2html.convert(json = percentage_data)

#converts csv file with college degrees sorted by race into the same format as the income file
@app.route('/api/v1/resources/inequality_rates/degrees_by_race', methods=['GET'])
def api_degrees_by_race():
    csvfile = open(data_file_dir + '/degrees_by_race.csv', 'r')
    jsonfile = open('degrees_by_race.json', 'w')

    fieldnames = ("Race", "Year", "Some college/associate's degree", "Bachelor's degree", "Advanced degree")
    reader = csv.DictReader(csvfile, fieldnames)
    out = json.dumps([row for row in reader])
    jsonfile.write(out)
    with open('C:/Users/anush/PycharmProjects/titanhacks/degrees_by_race.json') as f:
        data = json.load(f)
    data = data[21:]

    x = []
    for i in range(len(data)):
        try:
            y = int(data[i]["Year"])
            x.append(data[i])
        except ValueError:
            if len(x)>1:
                degrees.append(x)
            x = []

    return json2html.convert(json = degrees)

#returns a table that shows income and degree statistics side by side in for comparison
@app.route('/api/v1/resources/inequality_rates/comparison', methods=['GET'])
def api_comparison():
    api_degrees_by_race()
    api_2008_2018()
    comparison = []

    x = degrees[1][0]
    y = degrees[1][len(degrees[1])-1]
    x['Income'] = percentage_data[0]["2018"]
    y['Income'] = percentage_data[0]["2008"]
    comparison.append(x)
    comparison.append(y)

    x = degrees[2][0]
    y = degrees[2][len(degrees[2])-1]
    x['Income'] = percentage_data[1]["2018"]
    y['Income'] = percentage_data[1]["2008"]
    comparison.append(x)
    comparison.append(y)

    x = degrees[3][0]
    y = degrees[3][len(degrees[3])-1]
    x['Income'] = percentage_data[3]["2018"]
    y['Income'] = percentage_data[3]["2008"]
    comparison.append(x)
    comparison.append(y)

    x = degrees[4][0]
    y = degrees[4][len(degrees[4])-1]
    x['Income'] = percentage_data[4]["2018"]
    y['Income'] = percentage_data[4]["2008"]
    comparison.append(x)
    comparison.append(y)

    return json2html.convert(json = comparison)

app.run()