To run this solution use Docker:
Create .flaskenv file
docker build -t healthjoy-ws:latest . --no-cache
docker run -d -p 5000:5000 healthjoy-ws