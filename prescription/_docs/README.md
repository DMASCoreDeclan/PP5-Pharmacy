![Phelans Pharmacy](/media/phelans-logo-high-cropped.png)

PRESCRIPTION ReadMe

Prescription is commonly referred to as PX in the industry.  The prescription app was designed to accept information from an RUX, be validated on input, display a message upon successful completion, assign a px order number and then become part of PX ADMIN which ws designed for TUX/AUX members to process the PX.

You must be logged in as RUX to use this form.  UX are prompted to register.  TUX/AUX are not shown the link.  The form validation gives a successful message when completed correctly or returns you to the form, keeping the correct information and removing the incorrect field values, prompting you to try again.  Successful PX uploads are then sent to PX Admin.

PX Admin is a table which shows all PXs in the system.  The first column in the table is `update` which brings you to the edit_px_status.html.  Here you can change all fields. however, the site owner has expressed that TUX can only [change the STATUS](https://github.com/DMASCoreDeclan/PP5-Pharmacy/issues/47)

Previous orders are displayed in MY PROFILE of the logged in RUX.

Lighthouse was performed on PRESCRIPTION and it yielded the following results:

![Lighthouse Results](/prescription/_docs/lighthouse-prescription.png)

[CI Python Linter](https://pep8ci.herokuapp.com/) showed several errors which have been remedied in [Commit 192](https://github.com/DMASCoreDeclan/PP5-Pharmacy/commit/1e14b7d6f93c62d667c7e2123326ddbf542c598e)




**May 16, 2024**