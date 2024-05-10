![Phelans Pharmacy](/media/phelans-logo-high-cropped.png)

PRODUCTS ReadMe

The basis of the Products APP is a replica of Code Institutes Boutique Ado Code.  The main changes are that in the original CI design, EDIT and DELETE functionality were based on the is_superuser.  EDIT and DELETE has been removed from the code and moved into seperate isolated pages based on the requirements of Epic 2 - The ability to use CRUD on the fontend, in the event that the logged on user is_superuser or is_staff.

In addition to the Tests performed site wide, the following tests and results are specific to the Products App

Lighthouse was performed on PRODUCTS and it yielded the following results:

![Lighthouse Results](products-lighthouse-results.png)

An Issue has been raised to resolve these errors
[Testing Bug: Lighthouse Performance Issue on products.html #36](https://github.com/DMASCoreDeclan/PP5-Pharmacy/issues/36)

[CI Python Linter](https://pep8ci.herokuapp.com/) showed several errors which have been remedied in [Commit 192](https://github.com/DMASCoreDeclan/PP5-Pharmacy/commit/1e14b7d6f93c62d667c7e2123326ddbf542c598e)




**May 16, 2024**