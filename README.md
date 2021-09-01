# transfer

Application code for Django, in which users have, in addition to the main fields, 2 additional ones: 
- TIN (unique, TIN can start from zero) 
- Account value.
There is also a form consisting of fields:
- A drop-down list with all users in the system with the ability to select the user from whose account will be transfered money.
- A field for entering one or more TIN of users to whose accounts the money will be transferred.
- A field for specifying the amount to be transferred from one account to another.
 The specified amount is be debited from the account of the specified user and transferred to the accounts of users with the specified 
 TIN in equal parts.

 ## Creating new branch
