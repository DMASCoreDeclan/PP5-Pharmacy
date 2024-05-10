![Phelans Pharmacy](/workspace/PP5-Pharmacy/media/phelans-logo-high-cropped.png)

Welcom to my PP5 Code Institute submission

## Project Background

<details>

<summary>Overview</summary>

Phelans pharmacy already have a website: https://phelanspharmacy.com/.  While they are happy enough with it, the main problem which prevents them from leveraging it is that, Managing the Content just takes too long!  In consultation with the owner, we decided that we would undertake a two epic, four persona revamp.

<details>
<summary>Epics:</summary>
 
- Epic 1: to replicate the site as is, not exactly, but enough to easily see the overlaps to appreciate the extra functionality provided in Epic 2.
- Epic 2: to add CRUD to Prescription (PX) Management, Product Management, Service Management and Article Managment.  Epic 2 would enable to team in Phelans Pharmacy to keep the site updated without having to engage the services of a Developer.
- Epic 3: Out of scope for this project, would be a Full Migration of all existing features in the current site and add a few more such as spcific reports to deal with increased PX and Product Orders
</details>

<details>
<summary>Personas:</summary>

- Persona 1: Site Owner (is_superuser with access to /Admin)
- Persona 2: Team Member (is_staff Access to CRUD on the frontend)
- Persona 3: Anonymous User (Access to view everything)
- Persona 4: Registered User (Anonymous User with a Profile)

</details>

</details>

## Deployment

<details>

### Local Deployment  
1. [Clone the repository from GitHub](https://github.com/DMASCoreDeclan/PP5-Pharmacy.git) by clicking the "Code" button and copying the URL.
2. Open your preferred IDE and open a terminal session in the directory you want to clone the repository to.
3. Type `git clone` followed by the URL you copied in step 1 and press enter.
4. Install the required dependencies by typing `pip install -r requirements.txt` in the terminal.
5. Note: The project is setup to use environment variables. You will need to set these up in your local environment. See [Environment Variables](env_sample.py) for more information.
6. Connect your database of choice and run the migrations by typing `python manage.py migrate` in the terminal.
7. Create a superuser by typing `python manage.py createsuperuser` in the terminal and following the prompts.  YOU MUST create a superuser called "Admin" to have the frontend features
8. Optional: Load blog articles `python manage.py loaddata products/fixtures/categories.json` and `python manage.py loaddata products/fixtures/products.json`.
9. Run the app by typing `python manage.py runserver` in the terminal and opening the URL in your browser.

#### Heroku Deployment
1. Login to the Heroku dashboard and create a new app.
2. Connect your GitHub repository to your Heroku app.
3. In the Settings tab, ensure that the [Python Buildpack](_docs/heroku-config-vars.png) is added.  
4. Set environment variables in the Config Vars section of the Settings tab, detailed below.
5. In the Deploy tab, enable automatic deploys from your GitHub repository.
6. Click the "Deploy Branch" button to deploy the app.
7. Once the app has been deployed, click the "Open App" button to view the app.


####  Environment Variables
- For local deployment, you will need to create a `.env` file in the root directory of the project and set the environment variables in this file.
- For Heroku deployment, you will need to set the environment variables through the Heroku CLI or through the Heroku dashboard under 'Config Vars'.  In addition, you will need an [AWS Account](https://eu-west-1.console.aws.amazon.com/s3/buckets?region=eu-west-1&bucketType=general&region=eu-west-1) to setup AWS Buckets, an [Email Account](https://support.google.com/mail/answer/56256?hl=en) for sending emails and a [Stripe Account](https://dashboard.stripe.com/apikeys) to connect to Stripe.  Setting up these Accounts and their components is beyond the scope of this README.  However should you have all of these accounts, you need to define the following variables:
  - If using a Postgres database:
    - `DATABASE_URL` - the URL for your Postgres database.
    AWS Keys to be obtained from your account and poplated in Heroku
    - `AWS_ACCESS_KEY_ID` - 
    - `AWS_SECRET_ACCESS_KEY` -
    - `USE_AWS` - 
    - `AWS_STORAGE_BUCKET_NAME` - 
    - `AWS_S3_REGION_NAME` - 
    - `AWS_S3_CUSTOM_DOMAIN` - 
    Email Keys to be obtained from your account and poplated in Heroku
    - `EMAIL_HOST_PASS` - 
    - `EMAIL_HOST_USER` - 
    DJANGO Key to be obtained from settings.py of your project and poplated in Heroku
    - `SECRET_KEY` - 
    Stripe Keys to be obtained from your account and poplated in Heroku
    - `STRIPE_PUBLIC_KEY` - 
    - `STRIPE_PUBLIC_KEY_LIVE` - 
    - `STRIPE_SECRET_KEY` - 
    - `STRIPE_SECRET_KEY_LIVE` - 
    - `STRIPE_WH_SECRET` - 


</details>

<details>

**<summary>Credits</summary>**

- Antonio, my mentor 
- Code Institute for the foundation of Epic 1: "Boutique Ado!"

</details>


**May 16, 2024**