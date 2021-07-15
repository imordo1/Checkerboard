from flask import Flask, render_template
app = Flask(__name__)

# --------------- Level 1 (8x8) - This is the original ask to display in 8x8 checkerboard (use index2.html)----------------------------------

@app.route('/')
def  display8():
    return render_template('index2.html')

# --------------- Level 2 (8x4) 8x4checkerboard  (use index3.html)----------------------------------
@app.route('/4')
def  count():
    return render_template('index3.html')

# # --------------- Level 3 (x by y)  (use index.html)----------------------------------
@app.route('/<x>/<y>')
def  count_both(x,y):
    return render_template('index6.html', x=int(x), y=int(y)) 


@app.route('/<x>/<y>/<color1>/<color2>')
def  count_color(x,y,color1,color2):
    return render_template('index6.html', x=int(x), y=int(y), color1 = str(color1), color2=str(color2)) 



## Do not touch - always needed
if __name__ =="__main__":
	app.run(debug=True)