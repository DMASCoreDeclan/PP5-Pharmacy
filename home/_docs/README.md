![Phelans Pharmacy](/media/phelans-logo-high-cropped.png)

PRESCRIPTION ReadMe

The PRESCRIPTION APP replicates the original Phelans Parmacy functionality to take in Prescription Orders (PXs).  However, now only RUX Users can do this.  Instead of resulting in a mail, the PXs are captured in a table that allocaates the individual X to the RUXs Profile and centralises ALL PXs to a place where we can measure and mange their processing.  Epic 2 is about demonstrating the concept of centralised updating of PX Statuses, if it goes ahead, Epic 3 will look at sending messages to RUX when their Order sTATUS changes and capturing the TUX who changed the status.  Reports showing PXs processed per month/week/by person etc will be part of Epic 3.

Epic 1 Prescription app changes are not discussed here.

The Epic 2 Prescription app facilitates

TUXs to use PX Admin to View the order, compare its details to the scanned PX and contact the customer/Dr if clarification is required.
Once the details are verified, the PX should be prepared and the status cahnged from Being Processed to Processed.


Lighthouse performed on prescription.html. It yielded the following results and no further action has been taken:

![Lighthouse Results](/home/_docs/lighthouse-home.png)

[CI Python Linter](https://pep8ci.herokuapp.com/) showed several errors which have been remedied in [Commit 192](https://github.com/DMASCoreDeclan/PP5-Pharmacy/commit/1e14b7d6f93c62d667c7e2123326ddbf542c598e)

AFTER the code was written, it became very evident that a Class Based View should be created as the process is all but the same with the exception to the Model being referenced.  Creating, Updating and Deleting an Epic 3 issue has been created to do this
[Refactor: Refactor HOME App Code from multiple ADD/EDIT/DELETE to a Class Based View](https://github.com/DMASCoreDeclan/PP5-Pharmacy/issues/37)
**May 16, 2024**