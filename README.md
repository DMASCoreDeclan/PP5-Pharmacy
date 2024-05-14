![Phelans Pharmacy](/media/phelans-logo-high-cropped.png)



## Project Background

<details>

<summary>Overview</summary>

- This Django web development project is an extension of Code Institute, "Boutique Ado". 
- Phelans pharmacy already have a website: https://phelanspharmacy.com/.  While they are happy enough with it, the main problem which prevents them from leveraging it is that, Managing the Content just takes too long! In consultation with the owner, we decided that we would undertake a two epic, four persona revamp.


<details>
<summary>Epics:</summary>
 
- Epic 1: to replicate the site as is, not exactly, but enough to easily see the overlaps to appreciate the extra functionality provided in Epic 2.
- Epic 2: to add CRUD to Prescription (PX) Management, Product Management, Service Management and Article Managment.  Epic 2 would enable to team in Phelans Pharmacy to keep the site updated without having to engage the services of a Developer.
- Epic 3: Out of scope for this project, would be a Full Migration of all existing features in the current site and add a few more such as spcific reports to deal with increased PX and Product Orders
</details>

<details>
<summary>Personas:</summary>

- Persona 1: Site Owner AUX (is_superuser with access to /Admin)
- Persona 2: Team Member TUX (is_staff Access to CRUD on the frontend)
- Persona 3: Registered User RUX (Anonymous User with a Profile)
- Persona 4: Anonymous User UX (Access to view everything)


</details>

## READMEs

</details>

<details>
<summary>READMEs</summary>

 - [CART README](cart/_docs/README.md)
 - [CHECKOUT README](checkout/_docs/README.md)
 - [HOME README](home/_docs/README.md)
 - [PHARMACY README](pharmacy/_docs/README.md)
 - [PRESCRIPTION README](prescription/_docs/README.md)
 - [PRODUCTS README](products/_docs/README.md)
 - [PROFILES README](profiles/_docs/README.md)

</details>

## Agile Methodology

<summary>Personas</summary> 

-	Persona 1: Site Owner AUX (is_superuser with access to /Admin)
-	Persona 2: Team Member TUX (is_staff Access to CRUD on the frontend)
-	Persona 3: Registered User RUX (Anonymous User with a Profile)
-	Persona 4: Anonymous User UX (Access to view everything)

</details>

<details>
<summary>Github</summary> 
Github was used for Planning, Recording and Sharing of all aspects of the project:

The [Project Elements:](https://github.com/users/DMASCoreDeclan/projects/23)
- [Code Repository](https://github.com/DMASCoreDeclan/PP5-Pharmacy)
- [Version Control](https://github.com/DMASCoreDeclan/PP5-Pharmacy/commits/main/) was used for version control of the code.  Regular [commits](https://github.com/DMASCoreDeclan/PP5-Pharmacy/commits/main/) were created.  Where possible each commit was isolated to either a specific Issue but may have occassionally also included a minor change to some other part of the code
- [Epics](https://github.com/users/DMASCoreDeclan/projects/23/views/2)
- [User Stories](https://github.com/users/DMASCoreDeclan/projects/23/views/4)
- [Kanban](https://github.com/users/DMASCoreDeclan/projects/23)
- [Labels](https://github.com/DMASCoreDeclan/PP5-Pharmacy/labels)
- [MoSCow](https://github.com/users/DMASCoreDeclan/projects/23/views/3) Priorities are based on the MoSCoW method (Must have, Should have, Could have, Won't have)
</details>
</details>



## Wireframes Epic 2
[Designed with Balsamiq Wireframes for Desktop](https://balsamiq.com/wireframes/desktop/)

Epic 1 Wireframes were not prepared as the layout was determined by the [Phelans Pharmacy Site](https://phelanspharmacy.com)

Any vistor who has the URL can see the home screen [Phelans | the Friendliest Pharmacy Wateford](https://phelans-pharmacy-bf69b3045245.herokuapp.com/)

<details>
  <summary>Epic 2 Wireframes with corresponding URLs</summary> 

  <details>
  <summary>TUX Home Screen</summary>  
  
  [TUX Home Screen](https://phelans-pharmacy-bf69b3045245.herokuapp.com/)
  
  <img src="home/_docs/home.png">
  </details>

  <details>
  <summary>TUX Products</summary>  
  
  [Products](https://phelans-pharmacy-bf69b3045245.herokuapp.com/products/)
  
  <img src="products/_docs/Products.png">

  </details>

  <details>
  <summary>TUX Add Product</summary>  
  
  [Add Products](https://phelans-pharmacy-bf69b3045245.herokuapp.com/products/add/)

  <img src="products/_docs/Add Product.png">
  
  </details>

  <details>
  <summary>TUX Edit Products</summary>  
  
  [Edit Products](https://phelans-pharmacy-bf69b3045245.herokuapp.com/products/edit_products/)

  <img src="products/_docs/Edit Products.png">
  
  </details>


  <details>
  <summary>TUX Delete Products</summary>  
  
  [Delete Product](https://phelans-pharmacy-bf69b3045245.herokuapp.com/products/delete_products/)

  <img src="products/_docs/Delete Products.png">
  
  </details>

  <details>
  <summary>RUX Send Prescription</summary>  
  
  [Send Prescription](https://phelans-pharmacy-bf69b3045245.herokuapp.com/prescription/)

  <img src="prescription/_docs/Add PX.png">
  
  </details>



  <details>
  <summary>TUX View Prescriptions</summary>  
  
  [View Prescriptions](https://phelans-pharmacy-bf69b3045245.herokuapp.com/prescription/px_admin)

  <img src="prescription/_docs/PX Admin.png">
  
  </details>

  <details>
  <summary>TUX Update Prescriptions</summary>  
  
  [Update Prescriptions](https://phelans-pharmacy-bf69b3045245.herokuapp.com/prescription/edit_px_status/10)

  <img src="prescription/_docs/Edit PX.png">
  
  </details>




  <details>
  <summary>TUX Services</summary>  
  
  [Services](https://phelans-pharmacy-bf69b3045245.herokuapp.com/all_services/)
  
  <img src="home/_docs/Services.png">

  </details>

  <details>
  <summary>TUX Add Service</summary>  
  
  [Add Services](https://phelans-pharmacy-bf69b3045245.herokuapp.com/add_service/)

  <img src="home/_docs/Add Service.png">
  
  </details>

  <details>
  <summary>TUX Edit Services</summary>  
  
  [Edit Services](https://phelans-pharmacy-bf69b3045245.herokuapp.com/edit_services/)

  <img src="home/_docs/Edit Services.png">
  
  </details>


  <details>
  <summary>TUX Delete Services</summary>  
  
  [Delete Service](https://phelans-pharmacy-bf69b3045245.herokuapp.com/delete_services/)

  <img src="home/_docs/Delete Service.png">
  
  </details>

  <details>
  <summary>TUX Articles</summary>  
  
  [Articles](https://phelans-pharmacy-bf69b3045245.herokuapp.com/all_articles/)
  
  <img src="home/_docs/Articles.png">

  </details>

  <details>
  <summary>TUX Add Article</summary>  
  
  [Add Articles](https://phelans-pharmacy-bf69b3045245.herokuapp.com/add_article/

  <img src="home/_docs/Add Article.png">
  
  </details>

  <details>
  <summary>TUX Edit Articles</summary>  
  
  [Edit Articles](https://phelans-pharmacy-bf69b3045245.herokuapp.com/edit_article/)

  <img src="home/_docs/Edit Articles.png">
  
  </details>


  <details>
  <summary>TUX Delete Articles</summary>  
  
  [Delete Article](https://phelans-pharmacy-bf69b3045245.herokuapp.com/delete_articles/)

  <img src="home/_docs/Delete Article.png">
  
  </details>

</details>


<br>
<br>

</details>
 
## Entity Relationship Diagram
[Designed with Lucidchart](https://www.lucidchart.com/pages/)

<details>
<summary>ERD</summary>  <img src="_docs/PP5 ERD.png">
</details>

<details>
<summary>Project - Pharmacy</summary>
Pharmacy is the django Project. By default it uses SQLite but we're using PostgreSQL instead.  
There are six apps within the project:

1. cart
1. checkout
1. home
1. prescription
1. products
1. profiles
1. external apps

  <details>
  <summary>App - cart</summary>
  
  - `cart` views: `cartview`, `add_to_cart`, `adjust_cart`, `remove_from_cart` 
  - `cart` pages: `cartview.html`
  </details>

  <details>
  <summary>App - checkout</summary>

  - `checkout` models: `Order`, `OrderLineItem`
  - `checkout` forms: `OrderForm`, 
  - `checkout` views: `cache_checkout_data`, `checkout`, `checkout_success`
  - `checkout` pages: `checkout_success.html`, `checkout.html`
  </details>


  <details>
  
  <summary>App - home</summary>
  
  - `home` models: `CommunicationStatus`, `CommunicationType`, `CommunicationContent`, `Service`
  - `home` forms: `CommunicationForm`, `ServiceForm`, `PxChangeStatusForm`
  - `home` views: `index`, `subscribe`, `all_articles`, `add_article`, `edit_article`, `article_detail`, `delete_article`, `delete_articles`, `edit_articles`, `all_services`, `edit_service`, `edit_services`, `service_detail`, `delete_services`, `about`
  - `home` pages:  `custom_clearable_file_input.html`, `about.html`, `add_article.html`, `add_service.html`, `all_articles.html`, `all_services.html`, `article_detail.html`, `confirm_delete_article.html`, `confirm_delete_service.html`, `delete_articles.html`, `delete_services.html`, `edit_article.html`, `edit_articles.html`, `edit_service.html`, `edit_services.html`, `index.html`, `subscribe.html`, `service_detail.html`,  
  </details>

  <details>
  
  <summary>App - prescription</summary>
  
  - `prescription` models: `Prescription`
  - `prescription` forms: `PxForm`, `PxAdminForm`, `PxChangeStatusForm`,
  - `prescription` views: `order_px`, `px_admin`, `edit_px_status`
  - `prescription` pages:  `px_order.html`, `px_order.html`, `prescription_history.html`, `edit_px_status.html`, `custom_clearable_file_input.html`
  </details>

  <details>
  <summary>App - products</summary>
  
  - `products` models: `Category`, `Product`, `ProductBundle`, 
  - `products` forms: `ProductForm`
  - `products` views: `profiles`, `order_history`, `px_order_history`, `prescription_history` 
  - `products` pages:  `products.html`, `product_detail.html`, `edit_products.html`, `edit_product.html`, `delete_products.html`, `confirm_delete_product.html`, `add_product.html`, `quantity_input_script.html`, `product_bundle_picture.html`, `edit_product_bundle_picture.html`, `custom_rating_input_validation.html`, `custom_clearable_file_input.html`
  </details>



  <details>
  <summary>App - profiles</summary>

  - `profiles` models: `UserProfile`
  - `profiles` forms: `UserProfileForm`
  - `profiles` views: `profiles`, `order_history`, `px_order_history`, `prescription_history` 
  - `profiles` pages: `profile.html`
  </details>

</details>

  






## Deployment

<details>

### Local Deployment  
1. [Clone the repository from GitHub](https://github.com/DMASCoreDeclan/PP5-Pharmacy.git) by clicking the "Code" button and copying the URL.
2. Open your preferred IDE and open a terminal session in the directory you want to clone the repository to.
3. Type `git clone` followed by the URL you copied in step 1 and press enter.
4. Install the required dependencies by typing `pip install -r requirements.txt` in the terminal.
5. Note: The project is setup to use environment variables. You will need to set these up in your local environment. See [Environment Variables](_docs/env_sample.py) for more information.
6. Connect your database of choice and run the migrations by typing `python manage.py migrate` in the terminal.
7. Create a superuser by typing `python manage.py createsuperuser` in the terminal and following the prompts.  YOU MUST create a superuser called "Admin" to have the frontend features
8. Optional: Load blog articles `python manage.py loaddata products/fixtures/categories.json` and `python manage.py loaddata products/fixtures/products.json`.
9. Run the app by typing `python manage.py runserver` in the terminal and opening the URL in your browser.

### Heroku Deployment
1. Login to the Heroku dashboard and create a new app.
2. Connect your GitHub repository to your Heroku app.
3. In the Settings tab, ensure that the [Python Buildpack](_docs/heroku-config-vars.png) is added.  
4. Set environment variables in the Config Vars section of the Settings tab, detailed below.
5. In the Deploy tab, enable automatic deploys from your GitHub repository.
6. Click the "Deploy Branch" button to deploy the app.
7. Once the app has been deployed, click the "Open App" button to view the app.




###  Environment Variables
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

## Credits
<details>

**<summary>Credits</summary>**

- Antonio, my mentor 
- Code Institute for the foundation of Epic 1: "Boutique Ado!"

</details>


**May 16, 2024**