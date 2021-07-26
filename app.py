from flask import *

app=Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method=='POST':
        red = int(request.form['red'])
        green = int(request.form['green'])
        blue = int(request.form['blue'])
        def rgb_to_hex(r, g, b):
            return ('{:X}{:X}{:X}').format(r, g, b)
        value = rgb_to_hex(red, green, blue)
        print(value)
        return render_template('index.html', value=f'#{value}')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
