

import gis.data_analysis as gis
import model.model_counting as usemodel

from flask import Flask, jsonify, render_template, request






app = Flask(__name__)


# 首頁顯示
@app.route("/")
def index():
    '''
    首頁 : 使用者輸入地址查詢
    '''

    return render_template("index.html")


# 在 Flask 新增頁面
@app.route("/page2.html")
def page2():
    '''
    儀錶板頁面
    '''



    return render_template("page2.html")


# 在你的 Flask 應用程式中新增這個路由
@app.route("/bi.html")
def bi():
    '''
    地區視覺化分析頁面
    '''

    return render_template("bi.html")


# 使用者輸入地址資料轉換
@app.route("/get_coordinates", methods=["GET", "POST"])
def get_coordinates():
    '''
    使用者地址 : 環域分析，合併地區資料
    '''

    data = request.json
    address = data["address"]
    # print(address)
    address_info = gis.buffer_analysis(address)
    # print(address_info)
    address_district_info = gis.user_district(address_info)

    user_full_data = gis.user_data(address_district_info)


    return jsonify(user_full_data)


# 接10大飲料店  (等csv)
@app.route("/top10_brand", methods=["POST"])
def top10_brand():
    '''
    前10大指標品牌 : 環域分析
    '''

    data = request.json
    address = data["address"]  
    top10_brand = gis.drink_top10_brand(address)

    return jsonify(top10_brand)


# 送到model接model資料
@app.route("/load_and_get_model", methods=["POST"])
def load_and_get_model():
    '''
    模型預測分數
    '''

    data = request.json
    address = data["address"]
    user_pred_point = usemodel.model_pred(address)
    return jsonify(user_pred_point)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
