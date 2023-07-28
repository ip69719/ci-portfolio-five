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
* Our  desired outcome is provide Farmy & Foods with a faster and reliable solution for detecting powdery mildew on cherry leaves.
* The model success metrics are:
	* We agreed with the client a degree of 97% accuracy on the test set.
* The model output is defined as a flag, indicating if the cherry leaf has powdery mildew and the associated probability of being infected or not. An employee will upload the picture to the App. The prediction is made on the fly (not in batches).
* Heuristics: Currently, an employee spends around 30 minutes taking a few samples of leaves from each tree and verifying visually if the leaf tree is healthy or has powdery mildew. The company has thousands of cherry trees, located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.



## Dashboard Design
* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other items, that your dashboard library supports.
* Finally, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project, you were confident you would use a given plot to display an insight, but later, you chose another plot type).

### Page 1: Quick Project Summary

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

## Unfixed Bugs
* You will need to mention unfixed bugs and why they were unfixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable for consideration, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment
### Heroku

* [Link to the live project](https://ip-cherry-mildew-detection-e596dcba871a.herokuapp.com/)
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file. 


## Technologies used

### Languages used

* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Main Data Analysis and Machine Learning Libraries
* Here you should list the libraries used in the project and provide an example(s) of how you used these libraries.
* [Streamlit](https://streamlit.io/) Python-based library was used to create the dashboard for the app.

### Other Frameworks, Libraries & Programs Used
* [Git](https://git-scm.com/) was used for version control by utilising the Gitpod terminal to commit to Git and Push to GitHub.
* [GitHub](https://github.com/) is used to store the project code after being pushed from Git.
* [Heroku](https://www.heroku.com/about) was used to deploy the app. 

## Credits 

* In this section, you need to reference where you got your content, media and from where you got extra help. It is common practice to use code from other repositories and tutorials. However, it is necessary to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The content of the project summary page about powdery mildew was written with reference to [this](https://en.wikipedia.org/wiki/Powdery_mildew) Wikipedia article.
- Instructions on how to build a Streamlit multipage dashboard were taken from [this](https://learn.codeinstitute.net/courses/course-v1:code_institute+CI_DA_ML+2021_Q4/courseware/d186ae95191f48e9a2151559c7e6f85d/fc2f9892cfa44eee9cc8bf585c21df88/4?activate_block_id=block-v1%3Acode_institute%2BCI_DA_ML%2B2021_Q4%2Btype%40vertical%2Bblock%407636b337caeb4035bd7b5568404802f6) Code Institute Streamlit lesson.

### Media

- The photos used on the home and sign-up page are from This Open-Source site.
- The images used for the gallery page were taken from this other open-source site.



## Acknowledgements
* Special thanks to my Mentor Rohit Sharma for support and guidance during this project.
