# Odoo_SimonLen

Odoo custom module which extends standard Odoo Sales module:
-------------------------
- By default, when a user creates a new Quotation, the "Test" field is filled with a random number.
- If the user changes the Quotes lines (products) or changes the Quotation Date, the value changes in realtime to text in the "Total - Date" format (example value: 8,287.50 - 02/06/2022 16:33:53)
- The new "Test" field is editable only if Quotes are at the Draft stage
- If the user manually enters a text longer than 50 characters, the message "The text length must be less than 50 characters!" appears.
- The value of the "Test" field, if it is not empty, then this field is displayed in the Print > Quotation / Order form, anywhere above the product table. If the "Test" field is empty, it is not displayed.


Getting started with Odoo for developers
-------------------------

For installation, administration and development please follow the <a href="https://www.odoo.com/documentation/15.0/index.html.">Getting started</a> from the documentation.



