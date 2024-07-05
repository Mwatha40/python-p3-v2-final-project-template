
A simple Contact Book CLI
================

A simple command-line interface for managing a contact book.

**Features**

* Add new contacts with name, address, phone number, and email address
* Find contacts by name
* List all contacts
* Delete contacts by name
* Update contacts by name

**Usage**

### Add a new contact
`contact_book add`

This command will prompt you to enter the name, address, phone number, and email address of the new contact.

### Find a contact by name
`contact_book find <name>`

This command will search for a contact with the specified name and display their details if found.

### List all contacts
`contact_book list`

This command will display a list of all contacts in the contact book.

### Delete a contact by name
`contact_book delete <name>`

This command will delete the contact with the specified name from the contact book.

### Update a contact by name
`contact_book update <name> [--address <address>] [--phone-number <phone_number>] [--email-address <email_address>]`

This command will update the contact with the specified name. You can specify one or more of the following options to update:
* `--address <address>`: Update the address of the contact.
* `--phone-number <phone_number>`: Update the phone number of the contact.
* `--email-address <email_address>`: Update the email address of the contact.
**Installation**
------------
To use this contact book CLI, simply save the `contact_book.py` file to a directory on your system and run it using Python:

The contact book data will be stored in a file called `contacts.txt` in the same directory.

**Author:**
[Allan Mwatha]