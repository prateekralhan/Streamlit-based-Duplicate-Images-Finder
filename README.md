# Streamlit based Duplicate Images Finder 📷 [![Project Status: Active](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active) [![](https://img.shields.io/badge/Prateek-Ralhan-brightgreen.svg?colorB=ff0000)](https://prateekralhan.github.io/)

A streamlit based webapp to find duplicate images from single/multiple directories.

![demo1](https://user-images.githubusercontent.com/29462447/174408835-438234d9-5ff6-4159-a5e3-b908d885a8bc.gif)

![demo2](https://user-images.githubusercontent.com/29462447/174408842-5128838f-bf8f-43da-97d2-30a3264eb7af.gif)

## Installation:
* Simply run the command ***pip install -r requirements.txt*** to install the necessary dependencies.

## Usage:
1. Simply run the command: 
```
streamlit run app.py
```
2. Navigate to http://localhost:8501 in your web-browser.
3. By default, streamlit allows us to upload files of **max. 200MB**. If you want to have more size for uploading images, execute the command :
```
streamlit run app.py --server.maxUploadSize=1028
```

------------
## Results 
------------

| **Duplicate Images' Search within Single Directory**  | **Duplicate Images' Search within 2 Directories**  |
|---------------------|-----------------------|
| ![pic1](https://user-images.githubusercontent.com/29462447/174408690-a4e6cced-b8fc-4899-9585-de998ed5236f.png) | ![pic3](https://user-images.githubusercontent.com/29462447/174408698-a2c20a56-aeb9-49ee-a864-373fdd0914c9.png)  |
| ![pic2](https://user-images.githubusercontent.com/29462447/174408695-e6adf80f-a073-4c84-96e0-c43bb4cbd443.png) | ![pic4](https://user-images.githubusercontent.com/29462447/174408699-c4c6c6ce-243d-4320-becb-6dc906e13254.png)  |

### Running the Dockerized App
1. Ensure you have Docker Installed and Setup in your OS (Windows/Mac/Linux). For detailed Instructions, please refer [this.](https://docs.docker.com/engine/install/)
2. Navigate to the folder where you have cloned this repository ( where the ***Dockerfile*** is present ).
3. Build the Docker Image (don't forget the dot!! :smile: ): 
```
docker build -f Dockerfile -t app:latest .
```
4. Run the docker:
```
docker run -p 8501:8501 app:latest
```

This will launch the dockerized app. Navigate to ***http://localhost:8501/*** in your browser to have a look at your application. You can check the status of your all available running dockers by:
```
docker ps
```
