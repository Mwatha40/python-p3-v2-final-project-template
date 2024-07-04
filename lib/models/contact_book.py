import click

# Define the contact class
class Contact:
    def __init__(self, name, address, phone_number, email_address):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email_address = email_address

    def __str__(self):
        return f"Name: {self.name}\nAddress: {self.address}\nPhone Number: {self.phone_number}\nEmail Address: {self.email_address}"

# Define the CLI commands
@click.group()
def cli():
    """A simple contact book CLI."""
    pass

@cli.command()
@click.option("--name", prompt="Name", help="The name of the contact")
@click.option("--address", prompt="Address", help="The address of the contact")
@click.option("--phone-number", prompt="Phone Number", help="The phone number of the contact")
@click.option("--email-address", prompt="Email Address", help="The email address of the contact")
def add(name, address, phone_number, email_address):
    """Add a new contact."""
    contact = Contact(name, address, phone_number, email_address)
    with open("contacts.txt", "a") as f:
        f.write(f"{contact}\n")
    click.echo(f"Contact {name} added successfully!")

@cli.command()
@click.argument("name", required=True)
def find(name):
    """Find a contact by name."""
    with open("contacts.txt", "r") as f:
        contacts = f.readlines()
    found = False
    for contact in contacts:
        if name in contact:
            click.echo(contact.strip())
            found = True
            break
    if not found:
        click.echo(f"No contact found with name {name}")

@cli.command()
def list():
    """List all contacts."""
    with open("contacts.txt", "r") as f:
        contacts = f.readlines()
    if not contacts:
        click.echo("No contacts in the contact book.")
    else:
        for contact in contacts:
            click.echo(contact.strip())
            click.echo()

@cli.command()
@click.argument("contact", required=True)
def delete(contact):
    """Delete a contact by name."""
    with open("contacts.txt", "r") as f:
        contacts = f.readlines()
    with open("contacts.txt", "w") as f:
        for contact in contacts:
            if contact not in contact:
                f.write(contact)
    click.echo(f"Contact {contact} deleted successfully!")

@cli.command()
@click.argument("name", required=True)
@click.option("--address", help="The new address of the contact")
@click.option("--phone-number", help="The new phone number of the contact")
@click.option("--email-address", help="The new email address of the contact")
def update(name, address, phone_number, email_address):
    """Update a contact by name."""
    with open("contacts.txt", "r") as f:
        contacts = f.readlines()
    with open("contacts.txt", "w") as f:
        for contact in contacts:
            if name in contact:
                lines = contact.split("\n")
                if address:
                    lines[1] = f"Address: {address}"
                if phone_number:
                    lines[2] = f"Phone Number: {phone_number}"
                if email_address:
                    lines[3] = f"Email Address: {email_address}"
                f.write("\n".join(lines) + "\n")
            else:
                f.write(contact)
    click.echo(f"Contact {name} updated successfully!")

# Run the CLI
if __name__ == "__main__":
    cli()