from flask import Flask
from get_data_from_url import get_weather

app = Flask(__name__)


@app.route("/names")
def index():
    data = get_weather("http://api.data.mos.ru/v1/datasets/2009/rows")
    result = '<table><tr><th>Year</th><th>Month</th><th>Name</th></tr>'
    for x in data:
        # if x["Cells"]["Name"] == "Мария":
        cells_year = str(x["Cells"]["Year"])
        cells_month = str(x["Cells"]["Month"])
        cells_name = str(x["Cells"]["Name"])
        result += "<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format(cells_year, cells_month, cells_name)
    result += "</table>"
    return result


if __name__ == "__main__":
    app.run(port=5010, debug=True)


# <table><tr><th>Заголовок колонки 1</th><th>Заголовок колонки 2</th><th>Заголовок колонки 3</th></tr>
# <tr><td>Данные 1</td><td>Данные 2</td><td>Данные 3</td></tr>
# </table>
