![Phelans Pharmacy](/media/phelans-logo-high-cropped.png)

HOME ReadMe

The HOME APP is a replica of Code Institutes Home Page Layout.  Thereafter the functionality has been used to replicate a similarity to Phelans Pharmacy.  

Epic 1 Home app changes are not discussed here.

The Epic 2 Home app facilitates

- Products
  - Add Product
  - Edit Products
  - Delete Products
  - All Product (Customer View)

- Categories
- Prescriptions
  - PX Administration
- Services
  - Add Service
  - Edit Services
  - Delete Services
  - All Service (Customer View)

- Articles
  - Add Article
  - Edit Articles
  - Delete Articles
  - All Articles (Customer View)

AFTER the code was written, it became very evident that a Class Based View should be created as the process is all but the same with the exception to the Model being referenced.  Creating, Updating and Deleting an Epic 3 issue has been created to do this
[Refactor: Refactor HOME App Code from multiple ADD/EDIT/DELETE to a Class Based View](https://github.com/DMASCoreDeclan/PP5-Pharmacy/issues/37)


Lighthouse performed on index.html. It yielded the following results and no further action has been taken:

![Lighthouse Results](/_docs/lighthouse-home.png)

[CI Python Linter](https://pep8ci.herokuapp.com/) showed several errors which have been remedied in [Commit 192](https://github.com/DMASCoreDeclan/PP5-Pharmacy/commit/1e14b7d6f93c62d667c7e2123326ddbf542c598e)


**May 16, 2024**