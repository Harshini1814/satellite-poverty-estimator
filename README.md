Poverty Estimation using Satellite Imagery

Introduction

Poverty estimation is a critical challenge for policymakers and humanitarian organizations, as traditional survey-based methods are often expensive, time-consuming, and limited in coverage.
By analyzing features such as nightlight intensity, infrastructure, vegetation cover, and land use patterns, machine learning models can predict socioeconomic conditions without requiring extensive field surveys. 
This approach not only improves decision-making in resource allocation but also helps governments and NGOs track economic growth, disaster impact, and urban development in low-income regions.

Problem Statement

Accurate poverty estimation is crucial for effective resource allocation and intervention strategies by governments, NGOs, and policymakers. However, traditional methods rely on costly and time-consuming surveys, making real-time poverty assessment challenging, especially in remote and developing regions. This project aims to develop a CNN-based model that leverages satellite imagery to estimate poverty levels by analyzing key socioeconomic indicators such as rooftop type, lighting sources, water proximity, agricultural areas, road networks, and industrial zones. By automating poverty estimation using AI, this approach enables real-time, scalable, and cost-effective assessments, aiding in better decision-making and targeted development efforts.


Objectives
1. To implement a CNN to estimate poverty levels using satellite imagery by learning temporal patterns in economic activity.
2. To  replace expensive and time-consuming traditional survey methods with an automated, AI-driven solution for continuous and real-time monitoring of economic conditions.
3. To identify and analyze key features such as rooftop type, lighting sources, water proximity, agricultural areas, road structures, and industrial zones to assess wealth distribution.
4. To provide accurate and actionable insights to governments, NGOs, and policymakers to assist in targeted resource allocation and poverty alleviation efforts.

Software Requirements

Anaconda IDE
1. Python 3.8
2. Deep Learning Libraries: TensorFlow Keras, PyTorch
3. Machine Learning Libraries: NumPy, Pandas, Matplotlib, OpenCV, Scikit-learn

Hardware Requirements

1. Hard Disk: Greater than 500 GB
2. RAM: Greater than 4 GB
3. Processor: I3 and Above

Proposed Method: Architecture Diagram
![image](https://github.com/user-attachments/assets/583cb7ca-1e79-4543-9091-4335b8105737)

Architecture Diagram: Description

1. Data Acquisition & Preprocessing: Satellite images are collected and preprocessed through geospatial mapping and normalization.
2. Feature Extraction & Model Training: Key features are extracted using ResNet-50 from torchvision.models and are used to train a Convolutional Neural Network (CNN) for pattern recognition.
3. Model Evaluation & Prediction: The trained model is evaluated and applied for poverty estimation.
4. Results & Visualization: Predictions are displayed, providing insights into poverty distribution.

Module Connectivity Diagram
![image](https://github.com/user-attachments/assets/163cc616-86bf-4a02-98b4-99194cdb4b93)

Class Diagram
![image](https://github.com/user-attachments/assets/c55a7c7f-0f05-4d6f-a0e7-1152e99fc5cc)

Sequence Diagram
![image](https://github.com/user-attachments/assets/7f26ad49-1951-4ae6-ad21-740a4b660021)



Output (screenshots) of Test Cases

Web Interface
![image](https://github.com/user-attachments/assets/a8760b82-51c5-4e87-ad23-535ab48bed89)

Wealth Index analysis for upto 10 images simultaneously:
![image](https://github.com/user-attachments/assets/82496bdc-3bb9-4384-9e0e-d22d5d3cbc60)

![image](https://github.com/user-attachments/assets/bcb9d942-2c75-429a-addc-aef5a4fc1b30)

   
Experimental Results in the Table Format

![image](https://github.com/user-attachments/assets/1bc55aea-9561-4321-ab12-99d1105c970c)
![image](https://github.com/user-attachments/assets/0de66873-feaf-459d-9e70-948b930ee57a)


Main Advantages of the Proposed Method

Cost-Effective Approach: Eliminates the need for expensive field surveys and data collection, significantly reducing costs while providing valuable insights.

High Precision & Accuracy: Extracts detailed features (like building density, roads, and vegetation) that closely correlate with socio-economic status, ensuring accurate poverty estimation


Conclusion

This project demonstrates an efficient approach to estimating poverty levels using satellite imagery and deep learning. By extracting key features like road networks, building density, vegetation cover, and water sources, the model provides valuable socioeconomic insights. The use of CNNs enhances feature extraction, allowing for a scalable and cost-effective solution compared to traditional survey-based methods. Additionally, the proposed wealth index calculation method standardizes poverty estimation, making it applicable across various regions. However, challenges such as varying image resolutions, generalization across diverse geographic areas, and potential biases in model training highlight the need for further improvements. 





