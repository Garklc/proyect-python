contacts.py

contacts = {}

def add_contact(name, phone, email):
    contacts[name] = {'phone': phone, 'email': email}
    print(f"Contacto {name} agregado.")

def view_contacts():
    if not contacts:
        print("No hay contactos registrados.")
    else:
        for name, info in contacts.items():
            print(f"Nombre: {name}")
            print(f"Teléfono: {info['phone']}")
            print(f"Email: {info['email']}")
            print("-" * 20)

def search_contact(name):
    if name in contacts:
        print(f"Nombre: {name}")
        print(f"Teléfono: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print(f"No se encontró el contacto {name}.")

if __name__ == "__main__":
    while True:
        print("\nAgenda de Contactos")
        print("1. Agregar contacto")
        print("2. Ver todos los contactos")
        print("3. Buscar contacto")
        print("4. Salir")
        choice = input("Elige una opción: ")

        if choice == '1':
            name = input("Nombre: ")
            phone = input("Teléfono: ")
            email = input("Email: ")
            add_contact(name, phone, email)
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            name = input("Nombre del contacto a buscar: ")
            search_contact(name)
        elif choice == '4':
            print("Saliendo...")
            break
        else:
            print("Opción no válida")
