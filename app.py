from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Список для хранения данных пользователей
users = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Получение данных из формы
        name = request.form['name']
        age = request.form['age']
        city = request.form['city']
        hobby = request.form['hobby']

        # Добавление данных в список
        users.append({
            'name': name,
            'age': age,
            'city': city,
            'hobby': hobby
        })

        # Перенаправление на главную страницу для обновления данных
        return redirect(url_for('index'))

    # Отображение страницы с текущими данными
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
