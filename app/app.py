from flask import Flask, render_template
import plotly.express as px
import pandas as pd

app = Flask(__name__)

# Beispiel-Daten für das Dashboard
database_stats = {
    'total_users': 100,
    'active_users': 75,
    'total_databases': 50,
    'used_storage': 20,
    # Weitere relevante Daten hier hinzufügen
}

# Erstelle einen Beispiel-3D-Torten-Chart
# Erstelle einen Beispiel-3D-Torten-Chart
def create_pie_chart(data, title):
    df = pd.DataFrame({'Categories': list(data.keys()), 'Values': list(data.values())})
    fig = px.pie(df, names='Categories', values='Values', title=title)
    return fig.to_html(full_html=False)

@app.route('/')
def dashboard():
    # Beispiel-Daten für den 3D-Torten-Chart
    pie_data = {'Category A': 30, 'Category B': 50, 'Category C': 20}
    pie_chart = create_pie_chart(pie_data, 'Distribution of Categories')

    return render_template('dashboard.html', stats=database_stats, pie_chart=pie_chart)

if __name__ == '__main__':
    app.run(debug=True)
