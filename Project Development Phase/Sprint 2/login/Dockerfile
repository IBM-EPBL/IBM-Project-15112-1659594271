FROM python
WORKDIR /app
ADD . .
ADD ./templates ./
ADD ./Static ./Static
RUN pip install -r requirements.txt
CMD ["python","app.py"]
EXPOSE 5000