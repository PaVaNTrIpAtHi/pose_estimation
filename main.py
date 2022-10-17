from flask import *  
import os
import matplotlib.pyplot as plt
from angle_generator2 import get_points
# from werkzeug import secure_filename
app = Flask(__name__)


IMAGE_FOLDER = 'static/'
#PROCESSED_FOLDER = 'processed/'

app = Flask(__name__)  
app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER
#app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER

@app.route('/')  
def upload():
    return render_template("dhoni.html")  
 
@app.route('/success', methods = ['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'], f.filename)
        fc1,fc2,v1,v2 = get_points(full_filename)
        d = {}
        for x in range(v1.shape[1]):
            plt.figure(figsize=(7,3.6))
            v1.iloc[:,x].plot(label = "Dhoni"),v2.iloc[:,x].plot(label = "you")
            plt.title(v1.columns[x])
            plt.legend(loc="upper right")
            path = "static/graphs/"+v1.columns[x]+".jpg"
            plt.savefig(path, bbox_inches='tight')
            # plt.close(fig)
            # plt.show()
        for x in range(v1.shape[1]):
        #     print(df.iloc[:,x].corr(js.iloc[:,x]), "of ", df.columns[x])
            d[v1.columns[x]] = v1.iloc[:,x].corr(v2.iloc[:,x])
        sum = 0
        for x in d.values():
            sum = abs(x)*100 + sum
        print("you match player 1 by ",(sum/(v1.shape[1]))+25," %")
        txt = ""
        final_text = str(sum/(v1.shape[1])+25)
        return render_template("dhoni2.html", name = final_text)


@app.route('/info', methods = ['POST'])  
def info():
    return render_template("info.html")  


if __name__ == '__main__':  
    app.run(host="127.0.0.1",port=8080,debug=True)  






