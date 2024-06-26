![Phelans Pharmacy](/media/phelans-logo-high-cropped.png)

  * [Project Background](#project-background)
  * [Agile Methodology](#agile-methodology)
  * [Wireframes Epic 2](#wireframes-epic-2)
  * [Entity Relationship Diagram](#entity-relationship-diagram)
  * [Testing](#testing)
  * [SEO](#seo)
  * [Facebook](#facebook)
  * [Deployment](#deployment)
    + [Local Deployment](#local-deployment)
    + [Heroku Deployment](#heroku-deployment)
    + [Database](#database)
    + [Environment Variables](#environment-variables)
  * [READMEs](#readmes)
- [Technologies Used](#technologies-used)
  * [Core Development Technologies](#core-development-technologies)
  * [Python/Django Packages, Libraries, Frameworks and CDNs](#python-django-packages--libraries--frameworks-and-cdns)
  * [Infrastructural Technologies](#infrastructural-technologies)
  * [Credits](#credits)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


## Project Background

<details>

<summary>Overview</summary>

- This Django web development project is an extension of Code Institute, "Boutique Ado". 
- Phelans pharmacy, an independently owned pharmacy in Waterford, already have a website: https://phelanspharmacy.com/.  While they are happy enough with it as a source of information, the main problem which prevents them from leveraging it is that, Managing the Content just takes too long! In consultation with the owner, we decided that we would undertake a two epic, four persona revamp.
 - The overall objective is to develop the existing web-site to enable e-commerce functionality, allowing customers (users) to securely login, create a profile, select products to place in their cart, upload prescriptions, and make secure payments. In addition to being secure, the web-site will be user-friendly, conforming to the highest UX standards.  


<details>
<summary>Epics:</summary>
 
- [Epic 1](https://github.com/users/DMASCoreDeclan/projects/23/views/4?sliceBy%5Bvalue%5D=Epic+1+-+Frontend+Replica): to replicate the site as is, not exactly, but enough to easily see the overlaps to appreciate the extra functionality provided in Epic 2.
- [Epic 2](https://github.com/users/DMASCoreDeclan/projects/23/views/4?sliceBy%5Bvalue%5D=Epic+2+-+Backend+Features): to add CRUD to Prescription (PX) Management, Product Management, Service Management and Article Managment.  Epic 2 would enable the team in Phelans Pharmacy to keep the site updated without having to engage the services of a Developer.
- [Epic 3](https://github.com/users/DMASCoreDeclan/projects/23/views/4?sliceBy%5Bvalue%5D=Epic+3+-+Add+additional+Reports+and+Refactor+existing+code): Out of scope for this project, would be a Full Migration of all existing features in the current site and add a few more such as specific reports to deal with increased PX and Product Orders
</details>

<details>
<summary>Personas:</summary>

- Persona 1: Site Owner AUX (is_superuser with access to /Admin)
- Persona 2: Team Member TUX (is_staff Access to CRUD on the frontend)
- Persona 3: Registered User RUX (Anonymous User with a Profile)
- Persona 4: Anonymous User UX (Access to view everything)


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

  
## Testing


<details>

<summary>Test Case and Test Scenario</summary>

- All testing is manual.
- All testing took place on the deployed site in an incognito Chrome window.  A random selection of the tests were also carried out in Firefox and MS Edge to check the console.
- I logged into every URL and every Form as a UX, RUX, TUX and AUX.  After each action, I checked the console, and where appropriate, I checked the database in /admin, to ensure the backend did as expected.  
- I performed 64 [Unit Tests and Scenario Tests](https://github.com/DMASCoreDeclan/PP5-Pharmacy/blob/main/_docs/TESTING_REPORT.md) 
- During the testing
	1. **Easy** to fix, misspellings or obvious omissions, in .html/.py/.js/.css.  These fixed on the fly and captured in a commit
	1. **Substantial** and may or may not be fixed.  These have a [Bug Issue in Github](https://github.com/users/DMASCoreDeclan/projects/23/views/9?filterQuery=bug&sliceBy%5BcolumnId%5D=Status)

</details>

<details>

<summary>Responsiveness</summary>

- The website was viewed on a variety of devices such as Desktop, Laptop, iPhone 8, iPhone 11, iPad, and Androids to ensure responsiveness on various screen sizes. The website performed as intended. The responsive design was also checked using Chrome developer tools across multiple devices with structural integrity holding for the various sizes.
- Unfortunately, it seems that [AmIResponsive](https://ui.dev/amiresponsive?url=https://phelans-pharmacy-bf69b3045245.herokuapp.com/) and [Responsinator](http://www.responsinator.com/) can no longer check Heroku hosted apps.  
- Both sites yield the following Console Error: "chromewebdata/:1 Refused to display 'https://phelans-pharmacy-bf69b3045245.herokuapp.com/' in a frame because it set 'X-Frame-Options' to 'deny'."

</details>

<details>

<summary>Code CI Python Linter</summary>

[CI Python Linter](https://pep8ci.herokuapp.com/) showed several errors which have been remedied in [Commit 192](https://github.com/DMASCoreDeclan/PP5-Pharmacy/commit/1e14b7d6f93c62d667c7e2123326ddbf542c598e)
</details>

</details>

<details>

<summary>W3C CSS Validator Result</summary>
No errors were returned when passing through the official W3C CSS Validator

[W3C CSS Validator Result](https://jigsaw.w3.org/css-validator/validator?uri=https://phelans-pharmacy-bf69b3045245.herokuapp.com/)
</details>

</details>

<details>

<summary>W3C Markup Validator</summary>
Positive validation from Nu Html Checker

[About](https://validator.w3.org/nu/?showsource=yes&showoutline=yes&doc=https%3A%2F%2Fphelans-pharmacy-bf69b3045245.herokuapp.com%2Fabout%2F#l1c81694)

[Add a Product](https://validator.w3.org/nu/?showsource=yes&showoutline=yes&doc=https%3A%2F%2Fphelans-pharmacy-bf69b3045245.herokuapp.com%2Fproducts%2Fadd%2F#l1c81694)

[Add Article](https://validator.w3.org/nu/?showsource=yes&showoutline=yes&doc=https%3A%2F%2Fphelans-pharmacy-bf69b3045245.herokuapp.com%2Fadd_article%2F#l1c81694)

[Add Service](https://validator.w3.org/nu/?showsource=yes&showoutline=yes&doc=https%3A%2F%2Fphelans-pharmacy-bf69b3045245.herokuapp.com%2Fadd_service%2F)

[Cartview](https://validator.w3.org/nu/?showsource=yes&showoutline=yes&doc=https%3A%2F%2Fphelans-pharmacy-bf69b3045245.herokuapp.com%2Fcartview%2F#l303c12)

[Delete Products](https://validator.w3.org/nu/?showsource=yes&showoutline=yes&doc=https%3A%2F%2Fphelans-pharmacy-bf69b3045245.herokuapp.com%2Fproducts%2Fdelete_products%2F#l1c81694)

[Delete an Article](https://validator.w3.org/nu/?showsource=yes&showoutline=yes&doc=https%3A%2F%2Fphelans-pharmacy-bf69b3045245.herokuapp.com%2Fdelete_articles%2F)

[Delete a Service](https://validator.w3.org/nu/?showsource=yes&showoutline=yes&doc=https%3A%2F%2Fphelans-pharmacy-bf69b3045245.herokuapp.com%2Fdelete_services%2F)

[Delete Article Hairy-Mary](https://validator.w3.org/nu/?showsource=yes&showoutline=yes&doc=https%3A%2F%2Fphelans-pharmacy-bf69b3045245.herokuapp.com%2Fdelete_article%2Fhairy-mary)

[Delete Product 41](https://validator.w3.org/nu/?showsource=yes&showoutline=yes&doc=https%3A%2F%2Fphelans-pharmacy-bf69b3045245.herokuapp.com%2Fproducts%2Fdelete_product%2F41%2F#l1c81694)

[Delete Service 4](https://validator.w3.org/nu/?showsource=yes&showoutline=yes&doc=https%3A%2F%2Fphelans-pharmacy-bf69b3045245.herokuapp.com%2Fdelete_service%2F4)

[Edit Article Hairy-Mary](https://validator.w3.org/nu/?showsource=yes&showoutline=yes&doc=https%3A%2F%2Fphelans-pharmacy-bf69b3045245.herokuapp.com%2Fedit_article%2Fhairy#l1c81694)

[Edit Articles](https://validator.w3.org/nu/?showsource=yes&showoutline=yes&doc=https%3A%2F%2Fphelans-pharmacy-bf69b3045245.herokuapp.com%2Fedit_article%2F#l1c81694)

[Edit Product 42](https://validator.w3.org/nu/?showsource=yes&showoutline=yes&doc=https%3A%2F%2Fphelans-pharmacy-bf69b3045245.herokuapp.com%2Fproducts%2Fedit%2F42%2F#l1c81694)

[Edit Products](https://validator.w3.org/nu/?showsource=yes&showoutline=yes&doc=https%3A%2F%2Fphelans-pharmacy-bf69b3045245.herokuapp.com%2Fproducts%2Fedit_products%2F#l1c81694)

[Edit Service 4](https://validator.w3.org/nu/?showsource=yes&showoutline=yes&doc=https%3A%2F%2Fphelans-pharmacy-bf69b3045245.herokuapp.com%2Fedit_service%2F4)

[Edit Services](https://validator.w3.org/nu/?showsource=yes&showoutline=yes&doc=https%3A%2F%2Fphelans-pharmacy-bf69b3045245.herokuapp.com%2Fedit_services%2F)

[Home](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fphelans-pharmacy-bf69b3045245.herokuapp.com%2F#l303c12)

[Login](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fphelans-pharmacy-bf69b3045245.herokuapp.com%2Faccounts%2Flogin%2F%3Fnext%3D%2Fprescription%2F#l303c12)

[Logout](https://validator.w3.org/nu/?showsource=yes&showoutline=yes&doc=https%3A%2F%2Fphelans-pharmacy-bf69b3045245.herokuapp.com%2Faccounts%2Flogout%2F#l1c81694)

[My Profile](https://validator.w3.org/nu/?showsource=yes&showoutline=yes&doc=https%3A%2F%2Fphelans-pharmacy-bf69b3045245.herokuapp.com%2Fprofile%2F#l1c81694)

[Order Prescription](https://validator.w3.org/nu/?showsource=yes&showoutline=yes&doc=https%3A%2F%2Fphelans-pharmacy-bf69b3045245.herokuapp.com%2Fprescription%2F#l1c81694)

[Register](https://validator.w3.org/nu/?showsource=yes&showoutline=yes&doc=https%3A%2F%2Fphelans-pharmacy-bf69b3045245.herokuapp.com%2Faccounts%2Fsignup%2F#l303c12)

[Subscibe to Newsletter](https://validator.w3.org/nu/?showsource=yes&showoutline=yes&doc=https%3A%2F%2Fphelans-pharmacy-bf69b3045245.herokuapp.com%2Fsubscribe%2F#l303c12)

[View Articles](https://validator.w3.org/nu/?showsource=yes&showoutline=yes&doc=https%3A%2F%2Fphelans-pharmacy-bf69b3045245.herokuapp.com%2Fall_articles%2F#l1c81694)

[View Products](https://validator.w3.org/nu/?showsource=yes&showoutline=yes&doc=https%3A%2F%2Fphelans-pharmacy-bf69b3045245.herokuapp.com%2Fproducts%2F#l303c12)

[View Products (Category Cosmetics)](https://validator.w3.org/nu/?showsource=yes&showoutline=yes&doc=https%3A%2F%2Fphelans-pharmacy-bf69b3045245.herokuapp.com%2Fproducts%2F%3Fcategory%3Dcosmetics#l303c12)

[View Products (sorted by price low -> high)](https://validator.w3.org/nu/?showsource=yes&showoutline=yes&doc=https%3A%2F%2Fphelans-pharmacy-bf69b3045245.herokuapp.com%2Fproducts%2F%3Fsort%3Dprice%26direction%3Dasc#l303c12)

[View Products 42](https://validator.w3.org/nu/?showsource=yes&showoutline=yes&doc=https%3A%2F%2Fphelans-pharmacy-bf69b3045245.herokuapp.com%2Fproducts%2F42%2F#l303c12)

[View Service 1](https://validator.w3.org/nu/?showsource=yes&showoutline=yes&doc=https%3A%2F%2Fphelans-pharmacy-bf69b3045245.herokuapp.com%2Fservice_detail%2F1#l303c12)

[View Services](https://validator.w3.org/nu/?showsource=yes&showoutline=yes&doc=https%3A%2F%2Fphelans-pharmacy-bf69b3045245.herokuapp.com%2Fall_services%2F#l303c12)

</details>

<details>

<summary>Lighthouse</summary>

[SEO - Investigation](https://github.com/DMASCoreDeclan/PP5-Pharmacy/issues/50) is linked to each item below where it applies

[SEO won't be fixed - Investigation](https://github.com/DMASCoreDeclan/PP5-Pharmacy/issues/48) is linked to each item below where it applies

[Accessibility will be fixed in Epic 3 - Investigation](https://github.com/DMASCoreDeclan/PP5-Pharmacy/issues/49) is linked to each item below where it applies

[Performance Investigation](https://github.com/DMASCoreDeclan/PP5-Pharmacy/issues/36) is linked to each item below where it applies





<details>
<summary>lighthouse-about</summary>

<img src="_docs/lighthouse-about.png">
</details>
<details>
<summary>lighthouse-add-a-product</summary>

<img src="products/_docs/lighthouse-add-a-product.png">
</details>
<details>
<summary>lighthouse-add-article</summary>

[Performance Investigation](https://github.com/DMASCoreDeclan/PP5-Pharmacy/issues/36)

<img src="_docs/lighthouse-add-article.png">
</details>
<details>
<summary>lighthouse-add-service</summary>

<img src="_docs/lighthouse-add-service.png">
</details>
<details>
<summary>lighthouse-cartview</summary>

<img src="cart/_docs/lighthouse-cartview.png">
</details>
<details>
<summary>lighthouse-delete-a-products</summary>

[Performance Investigation](https://github.com/DMASCoreDeclan/PP5-Pharmacy/issues/36)

<img src="products/_docs/lighthouse-delete-a-products.png">
</details>
<details>
<summary>lighthouse-delete-an-article</summary>

[Performance Investigation](https://github.com/DMASCoreDeclan/PP5-Pharmacy/issues/36)
[SEO won't be fixed - Investigation](https://github.com/DMASCoreDeclan/PP5-Pharmacy/issues/48)


<img src="_docs/lighthouse-delete-an-article.png">
</details>
<details>
<summary>lighthouse-delete-a-service</summary>

[Performance Investigation](https://github.com/DMASCoreDeclan/PP5-Pharmacy/issues/36)
[SEO won't be fixed - Investigation](https://github.com/DMASCoreDeclan/PP5-Pharmacy/issues/48)


<img src="_docs/lighthouse-delete-a-service.png">
</details>
<details>
<summary>lighthouse-delete-article-hairy-mary</summary>

<img src="_docs/lighthouse-delete-article-hairy-mary.png">
</details>
<details>
<summary>lighthouse-delete-product-41</summary>

<img src="products/_docs/lighthouse-delete-product-41.png">
</details>
<details>
<summary>lighthouse-delete-service-4</summary>

<img src="_docs/lighthouse-delete-service-4.png">
</details>
<details>
<summary>lighthouse-edit-article-hairy-mary</summary>

[Performance Investigation](https://github.com/DMASCoreDeclan/PP5-Pharmacy/issues/36)

<img src="_docs/lighthouse-edit-article-hairy-mary.png">
</details>
<details>
<summary>lighthouse-edit-articles</summary>

[Performance Investigation](https://github.com/DMASCoreDeclan/PP5-Pharmacy/issues/36)

<img src="_docs/lighthouse-edit-articles.png">
</details>
<details>
<summary>lighthouse-edit-product-42</summary>

[SEO won't be fixed - Investigation](https://github.com/DMASCoreDeclan/PP5-Pharmacy/issues/48)

[Accessibility will be fixed in Epic 3 - Investigation](https://github.com/DMASCoreDeclan/PP5-Pharmacy/issues/49)

<img src="products/_docs/lighthouse-edit-product-42.png">


</details>
<details>
<summary>lighthouse-edit-products</summary>

[Performance Investigation](https://github.com/DMASCoreDeclan/PP5-Pharmacy/issues/36)


<img src="products/_docs/lighthouse-edit-products.png">
</details>
<details>
<summary>lighthouse-edit-service-4</summary>

[SEO won't be fixed - Investigation](https://github.com/DMASCoreDeclan/PP5-Pharmacy/issues/48)

[Accessibility will be fixed in Epic 3 - Investigation](https://github.com/DMASCoreDeclan/PP5-Pharmacy/issues/49)


<img src="_docs/lighthouse-edit-service-4.png">
</details>
<details>
<summary>lighthouse-edit-services</summary>

[SEO won't be fixed - Investigation](https://github.com/DMASCoreDeclan/PP5-Pharmacy/issues/48)


<img src="_docs/lighthouse-edit-services.png">
</details>
<details>
<summary>lighthouse-home</summary>

<img src="_docs/lighthouse-home.png">
</details>
<details>
<summary>lighthouse-prescription</summary>

<img src="prescription/_docs/lighthouse-prescription.png">
</details>
<details>
<summary>lighthouse-logout</summary>

<img src="_docs/lighthouse-logout.png">
</details>
<details>
<summary>lighthouse-my-profile</summary>

<img src="profiles/_docs/lighthouse-my-profile.png">
</details>
<details>
<summary>lighthouse-register</summary>

<img src="_docs/lighthouse-register.png">
</details>
<details>
<summary>lighthouse-subscibe-to-newsletter</summary>

<img src="_docs/lighthouse-subscibe-to-newsletter.png">
</details>
<details>
<summary>lighthouse-view-articles</summary>

[Performance Investigation](https://github.com/DMASCoreDeclan/PP5-Pharmacy/issues/36)


[SEO - Investigation](https://github.com/DMASCoreDeclan/PP5-Pharmacy/issues/50)

<img src="_docs/lighthouse-view-articles.png">
</details>
<details>
<summary>lighthouse-view-products</summary>

[Performance Investigation](https://github.com/DMASCoreDeclan/PP5-Pharmacy/issues/36)


<img src="products/_docs/lighthouse-view-products.png">
</details>
<details>
<summary>lighthouse-view-products-(category-cosmetics)</summary>

<img src="products/_docs/lighthouse-view-products-(category-cosmetics).png">
</details>
<details>
<summary>lighthouse-view-products-(sorted-by-price-low-->-high)</summary>

[Performance Investigation](https://github.com/DMASCoreDeclan/PP5-Pharmacy/issues/36)


<img src="products/_docs/lighthouse-view-products-(sorted-by-price-low-->-high).png">
</details>
<details>
<summary>lighthouse-view-products-42</summary>

<img src="products/_docs/lighthouse-view-products-42.png">
</details>
<details>
<summary>lighthouse-view-service-1</summary>

<img src="_docs/lighthouse-view-service-1.png">
</details>
<details>
<summary>lighthouse-view-services</summary>

[SEO - Investigation](https://github.com/DMASCoreDeclan/PP5-Pharmacy/issues/50)

<img src="_docs/lighthouse-view-services.png">
</details>


</details>



## SEO

<details>

<summary>Phelans Pharmacy Keyword Research</summary>

  <details>
  <summary>SEO High Level Strategy</summary>
  
 - Mention Waterford City, Waterford, Ireland
 - A Weekly Change – Edit/Add/Remove Product, Edit/Add/Remove Article, Add Newsletter
 - Link to Irish Pharmacy Page, Pharmacy Advertising Guidelines, Owners LinkedIn.  LinkedIn to Phelans Pharmacy, Social Media
 - In Products/Services/Articles links to product Brand and the Product name.  Have an Article on the Brands you stock, 
 - In Products/Services/Articles detail place the Brand Name and Products/Services/Articles Name in the TITLE
 - BOLD Brand Names
 - Make sure product details have title=”” and alt=”” wherever possible
 - Make the UX and content appealing to a human Google Rater

  </details>

  <details>
  <summary>Keyword Strategy</summary>
  
- The site is bound by the Pharmaceutical Advertising Laws and Regulations Ireland. In essence, we can only advertise our non medical products, services and our ability to deliver any service ie we are friendly.
- Social Media, Newsletters and Blog Articles would be the best.
- Our customers are not online social media users for Medicines, only for gifts and other non medical products and services.
- However, announcing a new service or the availability of a service should be marketed.  For example, a campaign saying “Latest Flu vaccine appointments are available from 25/10/5/, 09:00, book your appointment here . . .” would be allowed
- We want to rank highly for anything that we sell within a 15 mile radius.  
- We do not deliver non medical products, we DO deliver medical products.  
- All our services are consumed within the confines of the premises.  Our products are available either at a competing pharmacy or in the case of non medical products, in supermarkets.  There is nothing distinguishable about what we sell EXCEPT HOW we deliver it – Service.  
- We want to distinguish ourselves from our competitors, who are bound by the same constraints by:
 
  •	Being the preferred provider of services to be consumed on site
  
  •	Converting first time service customers to repeat medical product customers

![Keyword Research](_docs/keyword.png)


  </details>
  <details>
  <summary>Implementation</summary>
  
  •	Strategic use of semantics without keyword stuffing:

  •	Articles, Services and Product should be in < stong> H1 < /stong>> tags with < title > and < alt > being populated.

  •	Articles, Services and Products should have keyword decriptions URLs (Use Slugs instead of PKs/IDs)

  •	URLS to Images: descriptive-image-names.jpg.  (Using and image description in the model would have been more useful)

  •	Apply ARIA rules where possible

  •	META Data in < head >: < title >, < description > and < keywords > (Keywords should be stuffed)

  </details>

  
  <details>
  <summary>Newsletter</summary>

  Use mailchimp to create newsletter content to keep in touch with registered users.  Include Products, Services, Articles that have changed since the last newsletter

  </details>

</details>


## Facebook

<details>

<summary>Facebook</summary>

  <details>

  <summary>Facebook Original</summary>
  
  •	[Original Page - from Phelans Pharmacy](https://www.facebook.com/phelanspharmacywaterford/)

  </details>

  <details>
  
  <summary>Facebook Replica</summary>

  •	[Replica Page - from Phelans Pharmacy](https://www.facebook.com/profile.php?id=61558063517842)
  
  ![Replica Page - for Phelans Pharmacy](_docs/facebook-replica.png)

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

### Database
1. This app has been designed on sqlite which comes installed with django.  
2. PRD deployment would require a publically hosted DB.  The PRD version has been tested with PostgreSQL and deployed with [Code Institute](https://dbs.ci-dbs.net/).  
3. You can use any public PostgresSQL provider that has version 13 or above, such as [ElephantSQL](https://www.elephantsql.com/)

###  Environment Variables
- For local deployment, you will need to create a `.env` file in the root directory of the project and set the environment variables in this file. [sample env](_docs/env_sample.py)
- For Heroku deployment, you will need to set the environment variables through the Heroku CLI or through the Heroku dashboard under 'Config Vars'.  In addition, you will need an [AWS Account](https://eu-west-1.console.aws.amazon.com/s3/buckets?region=eu-west-1&bucketType=general&region=eu-west-1) to setup AWS Buckets, an [Email Account](https://support.google.com/mail/answer/56256?hl=en) for sending emails and a [Stripe Account](https://dashboard.stripe.com/apikeys) to connect to Stripe.  Setting up these Accounts and their components is beyond the scope of this README.  However should you have all of these accounts, you need to define the following variables:
  - If using a Postgres database:
    - `DATABASE_URL` - the URL for your Postgres database.
    - `AWS_ACCESS_KEY_ID` - AWS Keys to be obtained from your account and populated in Heroku
    - `AWS_SECRET_ACCESS_KEY` - AWS Keys to be obtained from your account and populated in Heroku
    - `USE_AWS` - False
    - `AWS_STORAGE_BUCKET_NAME` - AWS Keys to be obtained from your account and populated in Heroku
    - `AWS_S3_REGION_NAME` - AWS Keys to be obtained from your account and populated in Heroku
    - `AWS_S3_CUSTOM_DOMAIN` - AWS Keys to be obtained from your account and populated in Heroku
    Email Keys to be obtained from your account and populated in Heroku
    - `EMAIL_HOST_PASS` - Email Password
    - `EMAIL_HOST_USER` - Email Username
    - `SECRET_KEY` - DJANGO Key to be obtained from settings.py of your project and populated in Heroku
    Stripe Keys to be obtained from your account and populated in Heroku
    - `STRIPE_PUBLIC_KEY` - Stripe Keys to be obtained from your account and populated in Heroku
    - `STRIPE_PUBLIC_KEY_LIVE` - Stripe Keys to be obtained from your account and populated in Heroku
    - `STRIPE_SECRET_KEY` - Stripe Keys to be obtained from your account and populated in Heroku
    - `STRIPE_SECRET_KEY_LIVE` - Stripe Keys to be obtained from your account and populated in Heroku
    - `STRIPE_WH_SECRET` - Stripe Keys to be obtained from your account and populated in Heroku


</details>

## READMEs
<details>
<summary>Other READMEs</summary>

 - [CART README](https://github.com/DMASCoreDeclan/PP5-Pharmacy/blob/main/cart/_docs/README.md)
 - [CHECKOUT README](https://github.com/DMASCoreDeclan/PP5-Pharmacy/blob/main/checkout/_docs/README.md)
 - [HOME README](https://github.com/DMASCoreDeclan/PP5-Pharmacy/blob/main/home/_docs/README.md)
 - [PHARMACY README](https://github.com/DMASCoreDeclan/PP5-Pharmacy/blob/main/README.md)
 - [PRESCRIPTION README](https://github.com/DMASCoreDeclan/PP5-Pharmacy/blob/main/prescription/_docs/README.md)
 - [PRODUCTS README](https://github.com/DMASCoreDeclan/PP5-Pharmacy/blob/main/products/_docs/README.md)
 - [PROFILES README](https://github.com/DMASCoreDeclan/PP5-Pharmacy/blob/main/profiles/_docs/README.md)


</details>


# Technologies Used

This section outlines the various technologies used throughout the project and the purpose each serves.

## Core Development Technologies

<details>

- [Django](https://www.djangoproject.com/) used as a full-stack framework for developing the app.
- [JavaScript](https://www.ecma-international.org/publications-and-standards/standards/ecma-262/) used for client-side interaction and validation.
- [HTML](https://html.spec.whatwg.org/)
- [CSS](https://www.w3.org/Style/CSS/Overview.en.html) + [Django Template Language](https://docs.djangoproject.com/en/4.2/ref/templates/language/) used for building out site pages.

</details>

## Python/Django Packages, Libraries, Frameworks and CDNs

<details>

- [crispy-bootstrap5](https://django-crispy-forms.readthedocs.io/en/latest/) - Django-crispy-forms provides you with a |crispy filter and {% crispy %} tag that will let you control the rendering behavior of your Django forms in a very elegant and DRY way
- [dj-database-url](https://pypi.org/project/dj-database-url/) - This simple Django utility allows you to utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application.
- [dj3-cloudinary-storage](https://pypi.org/project/dj3-cloudinary-storage/) - Django Cloudinary Storage is a Django package that facilitates integration with Cloudinary by implementing Django Storage API
- [django-allauth](https://docs.allauth.org/en/latest/) - A fully integrated Django authentication app that allows for both local and social authentication, with flows that just work, beautifully!
- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) - Django-crispy-forms provides you with a |crispy filter and {% crispy %} tag that will let you control the rendering behavior of your Django forms in a very elegant and DRY way
- [django-summernote](https://pypi.org/project/django-summernote/) - Summernote is a JavaScript library that helps you create WYSIWYG editors online.
- [gunicorn](https://gunicorn.org/) - Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX
- [oauthlib](https://pypi.org/project/oauthlib/) - A generic, spec-compliant, thorough implementation of the OAuth request-signing logic
- [psycopg2](https://pypi.org/project/psycopg2/) - Psycopg is the most popular PostgreSQL database adapter for the Python programming language
- [PyJWT](https://pyjwt.readthedocs.io/) - Python library which allows you to encode and decode JSON Web Tokens (JWT)
- [FavIcon](https://favicon.io/) - Quickly generate your favicon from text, image, or choose from hundreds of emoji
- [Google Fonts](https://fonts.google.com/) - High-quality google fonts to use on your web site.
- [Font Awesome](https://fontawesome.com/) - Font Awesome is the Internet's icon library and toolkit, used by millions of designers, developers, and content creators
- [Bootstrap 4](https://getbootstrap.com/docs/4.4/getting-started/introduction/) - Get started with Bootstrap, the world’s most popular framework for building responsive, mobile-first sites
- [Tables Generator](https://www.tablesgenerator.com/markdown_tables) 
- [About](https://www.tablesgenerator.com/about)


</details>

## Infrastructural Technologies

<details>

- [PostgreSQL](https://www.postgresql.org/docs/12/) Current version provided by [Code Institute PostgresSQL](https://dbs.ci-dbs.net/)   (Originally on [ElephantSQL](https://www.elephantsql.com/) until v12 became unavailable.)  
- [Stripe](https://stripe.com/ie) - used for Credit Card Payments
- [Heroku](https://www.heroku.com/) - used for hosting the application.
- [Amazon S3](https://aws.amazon.com/s3/) - used for storing static files and media files.

</details>
</details>


<details>


## Credits
<details>

**<summary>Credits</summary>**

- Antonio, my mentor 
- Code Institute for the foundation of Epic 1: "Boutique Ado!"

</details>


**May 16, 2024**