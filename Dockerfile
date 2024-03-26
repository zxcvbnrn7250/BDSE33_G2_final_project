# 使用官方的 Python Docker 鏡像作為基礎
FROM python:3.11

LABEL maintainer='BDSE33_Group2'

# 切換工作目錄
WORKDIR /app

# 把目前目錄下的 ./app 複製到 /app
COPY ./app /app

# 安裝必要套件 (pip install -r 從檔案讀取要安裝的套件以及版本)
RUN pip install -r requirements.txt

# 啟動 Flask 應用程式
CMD ["python", "app.py"]
