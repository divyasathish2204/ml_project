from src.DimondPricePrediction.pipelines.prediction_pipeline import CustomData,PredictPipeline

from flask import Flask,request,render_template,jsonify

app = Flask(__name__)

@app.route('/')

def home_page():
    return render_template("index.html")
app.run(debug = True)

@app.route("/predict",methods=['GET','POST'])
def predict_datapoint():
    if request.method == "GET":
        return render_template("form.html")
    else:
        if request.method == "POST":
            data = CustomData(
                carat= float(request.form.get('carat')),
                depth= float(request.form.get("depth")),
                table = float(request.form.get("table")),
                x = float(request.form.get("x")),
                y = float(request.form.get("y")),
                z = float(request.form.get("z")),
                cut = str(request.form.get("cut")),
                color = str(request.form.get("color")),
                clarity = str(request.form.get("clarity"))
            )
            # this is my final data
            final_data = data.get_data_as_dataframe()
            predict_pipeline = PredictPipeline()
            pred =  predict_pipeline.predict(final_data)
            result = round(pred[0],2)
            return render_template("result.html",final_result = result)
        # execution begin

        if __name__ == "__main__":
            app.run(host = "0.0.0.0",port = 8080)




            







