To run this solution use Docker:
1. Before dockerizing create .flaskenv file and add this line:
PROJECT_REPO_PAT=Will provide via email
2. docker build -t healthjoy-ws:latest . --no-cache
3. docker run -d -p 5000:5000 healthjoy-ws