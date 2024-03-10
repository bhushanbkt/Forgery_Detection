# Forgery Detection Streamlit App

## Overview
This repository contains the code for a Streamlit web application designed for forgery detection using YOLOv8 models. The application allows users to upload images and test them against three different trained models for detecting forgeries in various types of documents and logos.

## Features
- **Multi-model Detection**: The app is equipped with three different YOLOv8 models trained on different datasets, enabling detection of forgeries in Aadhar and PAN documents, logos, and real vs. fake documents.
- **User-friendly Interface**: The Streamlit interface provides an intuitive user experience with options to select the model and upload images for testing.
- **Real-time Results**: Results are displayed in real-time, providing immediate feedback to users.

## Dataset
The datasets used for training the models were collected from Roboflow and include images of Aadhar and PAN documents, logos, as well as real and fake documents.

## Pre-trained Models
You can download the pre-trained YOLOv8 models used in this project from the following Google Drive link:
[Download Models](https://drive.google.com/drive/folders/1uMpeEv0xmbZBVJm2qREMBp9rvt32hQd6?usp=drive_link)

## Dependencies
- Python 3.9
- Streamlit
- Ultralytics


## Usage
1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the Streamlit app using `streamlit run app.py`.
4. Select the desired model from the dropdown menu.
5. Upload an image for testing by clicking the "Browse Files" button.
6. View the detection results displayed on the app interface.

## Folder Structure
- `data/`: Contains datasets and other relevant data.
- `models/`: Stores the trained YOLOv8 models.
- `utils/`: Utility functions for image processing and model evaluation.
- `app.py`: Main file containing the Streamlit application code.
- `requirements.txt`: List of Python dependencies.

## Contribution
Contributions to this project are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
- We would like to thank the creators of Streamlit and YOLOv8 for their excellent tools and resources.

## Contact
For any inquiries or feedback, please contact [Bhushan Taksande](mailto:bhushant731@gmail.com).
