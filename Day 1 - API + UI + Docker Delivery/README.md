**Day 1 - API + UI + Docker Delivery**

**Tasks Completed:**
-Developed a backend API with FastAPI, providing endpoints to convert currency using the exchangerate.host public API.
-*The frontend UI uses template code.* HTML + CSS + JavaScript frontend that calls the FastAPI backend to perform live conversions, offering a user-friendly interface.
-Isolated the Python environment using venv for local development, pinned dependencies in requirements.txt for reproducibility.
-Built a Docker image to containerize the app, ensuring consistent deployment across environments.
-Exposed the app via Uvicorn running on 0.0.0.0:8000
-Verified the app’s API and UI by running the container with docker run -d -p 8000:8000 <image> and testing endpoints in the browser.

**Screenshots:**
-Isolated Python environment + Installation of dependencies + File Structure
-Frontend UI template code
-Running API from VSC terminal + Currebcy app simulation
-Docker image creation + Container deployment
-Currency web app wokring from docker container on local host.
