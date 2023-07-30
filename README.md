# Cherry Leaves Mildew Detection

[Link to the live project](https://ip-cherry-mildew-detection-e596dcba871a.herokuapp.com/)

## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
* The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.



## Business Requirements
The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute.  The company has thousands of cherry trees, located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.


* 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.


## Hypothesis and how to validate?
* We suspect cherry leaves infected with powdery mildew to have white powdery looking patches differentiating them from healthy green leaves. 
  * A average image study can help to investigate this.


## The rationale to map the business requirements to the Data Visualisations and ML tasks

* **Business Requirement 1**: Data Visualization 
	* As a Client I want to display the "mean" and "standard deviation" images for cherry leaves that are healthy and cherry leaves that contain powdery mildew, so that I can visually differentiate cherry leaves.
	* As a Client I want to display the difference between an average cherry leaf that is healthy and an average cherry leaf that contains powdery mildew, so that I can visually differentiate cherry leaves.
	* As a Client I want to display an image montage for cherry leaves that are healthy and cherry leaves that contain powdery mildew, so that I can visually differentiate cherry leaves.

* **Business Requirement 2**:  Classification
	* As a Client I want to predict if a given cherry leaf is healthy or contains powdery mildew, so that I can take appropriate action early to control the disease.
	* As a Client I want to build a machine learning model and generate reports, so that I can benefit from efficient and reliable verification if a tree is healthy or has powdery mildew.


## ML Business Case
* We want a ML model to predict if a cherry leaf has powdery mildew or not, based on historical image data. It is a supervised model, a 2-class, single-label, classification model.
* Our  desired outcome is to provide Farmy & Foods with a faster and reliable solution for detecting powdery mildew on cherry leaves.
* The model success metrics are:
	* We agreed with the Client a degree of 97% accuracy on the test set.
* The model output is defined as a flag, indicating if the cherry leaf has powdery mildew and the associated probability of being infected or not. An employee will upload the picture to the App. The prediction is made on the fly (not in batches).
* Heuristics: Currently, an employee spends around 30 minutes taking a few samples of leaves from each tree and verifying visually if the leaf tree is healthy or has powdery mildew. The company has thousands of cherry trees, located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.


## Agile methodology

* Agile approach has been applied to develop this application.
* GitHub [projects board](https://github.com/users/ip69719/projects/6/views/1) was used to create user stories and manage the work.
![](https://github.com/ip69719/ci-portfolio-five/blob/main/assets/images/agile_board.png)


## Dashboard Design

The application was designed using Streamlit framework. There is a sidebar menu with five menu options to choose from.

### Page 1: Quick Project Summary

This is a project summary page, showing the project dataset summary and the Client's requirements.

**General Information**

* The Client is facing a challenge where their cherry plantations have been presenting powdery mildew. The cherry plantation crop is one of the finest products in the portfolio and the company concerned about supplying the market with a product of compromised quality.
* Powdery mildew is a fungal disease that affects a wide range of plants.
* It is one of the easier plant diseases to identify, as its symptoms are quite distinctive.
* Infected plants display white powdery spots on the leaves.
* Visual criteria are used to verify if the tree leaf is healthy or has powdery mildew.

**Project Dataset**
* The available dataset contains over four thousand images taken from the Client's crop fields.
* The images show healthy cherry leaves and cherry leaves that have powdery mildew.

**Business Requirements**
* The project has two business requirements:
    * 1 - The Client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
    * 2 - The Client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

### Page 2: Cherry Leaf Visualiser

This page lists findings related to a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew. The content of this page will answer the business requirement 1.

* Checkbox 1 - Difference between average and variability images
* Checkbox 2 - Difference between average healthy leaf and average leaf with powdery mildew
* Checkbox 3 - Image montage

### Page 3: Mildew Detection

This page contains:
* A link to download a set of cherry leaf images for live prediction
* A User Interface with a file uploader widget giving the User the ability to upload multiple images. For each image, it will display the image and a prediction statement, indicating if a cherry leaf is healthy or contains powdery mildew and the probability associated with this statement.
* A table with the image name and prediction results, and a download button to download the table.

### Page 4: Project Hypothesis

This page states project hypothesis and how it was validated.

### Page 5: ML Performance Metrics

This is a technical page displaying the ML model performance.

* Train, Validation and Test Set: Labels Frequencies
* Model History
* Generalised Performance on Test Set


## Unfixed Bugs
* You will need to mention unfixed bugs and why they were unfixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable for consideration, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.


## Deployment
### Heroku

* [Link to the live project](https://ip-cherry-mildew-detection-e596dcba871a.herokuapp.com/)

* The project was deployed to Heroku using the following steps:
1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file. 


* Python version for this project is set to 3.8.12. This version is not supported by Heroku's current default stack, which at the time of deployment is Heroku-22. The stack for the app was changed from Heroku CLI and set to Heroku-20:
    * login to Heroku with `heroku login -i` command
    * run the following command `heroku stack:set heroku-20 --app APP` (APP is the Heroku app name)


## Technologies used

### Languages used

* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Main Data Analysis and Machine Learning Libraries

* [jupyter notebook](https://jupyter.org) was used for documenting and running the ML pipelines.
* [TensorFlow](https://www.tensorflow.org/overview) in conjuction with [Keras](https://keras.io/) were used for in image preprocessing and to create CNN model.
* [TensorFlow](https://www.tensorflow.org/overview) was used to fit the CNN model.
* [NumPy](https://numpy.org/) package was used  to convert images into arrays and for array manipulation.
* [pandas](https://pandas.pydata.org/) was used to structure and manipulate the data.
* [joblib](https://pypi.org/project/joblib/) for saving and loading image shapes and ML model outputs.
* [matplotlib](https://matplotlib.org/) was used for creating plots for data visualisation.
* [seaborn](https://seaborn.pydata.org/) was used in conjuction with matplotplib library for data visualisation.
* [plotly](https://plotly.com/python/) was used for ploting charts for data visualisation.
* [Streamlit](https://streamlit.io/) Python-based library was used to create the dashboard for the app.

### Other Frameworks, Libraries & Programs Used

* [Git](https://git-scm.com/) was used for version control by utilising the Gitpod terminal to commit to Git and Push to GitHub.
* [GitHub](https://github.com/) is used to store the project code after being pushed from Git.
* [Heroku](https://www.heroku.com/about) was used to deploy the app.
* [CI Python Linter](https://pep8ci.herokuapp.com/#) was used to validate Python code.

## Credits 

### Code

- Code to implement the project idea was taken from [this](https://github.com/Code-Institute-Org/WalkthroughProject01) Code Institute Walkthrough Project and [GyanShashwat1611](https://github.com/GyanShashwat1611/WalkthroughProject01/) github repository.

### Content 

- [Code Institute Mildew Detection GitHub Repository](https://github.com/Code-Institute-Solutions/milestone-project-mildew-detection-in-cherry-leaves) was forked and used as a template for the project.
- [CI Handbook: Mildew Detection in Cherry Leaves](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+PA_PAGPPF+2021_Q4/courseware/bde016cdbd184cdeafd341a73807e138/bd2104eb84de4e48a9df6f685773cbf2/) was referenced to implement the project and write parts of the README.md file.
- The content of the project summary page about powdery mildew was written with reference to [this](https://en.wikipedia.org/wiki/Powdery_mildew) Wikipedia article.
- Instructions on how to build a Streamlit multipage dashboard were taken from [this](https://learn.codeinstitute.net/courses/course-v1:code_institute+CI_DA_ML+2021_Q4/courseware/d186ae95191f48e9a2151559c7e6f85d/fc2f9892cfa44eee9cc8bf585c21df88/4?activate_block_id=block-v1%3Acode_institute%2BCI_DA_ML%2B2021_Q4%2Btype%40vertical%2Bblock%407636b337caeb4035bd7b5568404802f6) Code Institute Streamlit lesson.

### Media

* The icon used for Streamlit app pages was taken from [Emojipedia](https://emojipedia.org/leaf-fluttering-in-wind/)

## Acknowledgements
* Special thanks to my Mentor Rohit Sharma for support and guidance during this project.
