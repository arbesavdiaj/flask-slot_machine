from flask import Flask, request, render_template
from main import SlotMachine
import random

app = Flask(__name__)

# Your SlotMachine class here

@app.route('/', methods=['GET', 'POST'])
def slot_machine():
    if request.method == 'POST':
        # Instantiate SlotMachine and play
        slot_machine = SlotMachine()
        result = slot_machine.play()
        return render_template('result.html', result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
