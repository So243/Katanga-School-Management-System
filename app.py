import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
from datetime import datetime
from PIL import ImageTk


def display_logo_frame(self):
    # Load your logo image
    # Replace with your image path
    logo_image_path = "/Users/mikekatanga/Documents/Work/Python/Project/KatangaManag/KATANGA SCHOOL MANAGEMEMNT SYSTEM/logo.png"
    logo_image = Image.open(logo_image_path)
    logo_image = logo_image.resize(
        (20, 20), Image.ANTIALIAS)  # Adjust the size as needed
    logo_image = ImageTk.PhotoImage(logo_image)

    # Create a label to display the logo
    logo_label = tk.Label(self.root, image=logo_image)
    logo_label.image = logo_image  # To prevent image from being garbage collected
    # Adjust the row and column as needed
    logo_label.grid(row=0, column=1, padx=10, pady=10)


class LoginWindow:
    def __init__(self, root, app):
        self.root = root
        self.app = app

        self.root.title("Connexion")
        self.root.configure(bg='#021024')

        # Calculate the center position
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_position = int((screen_width - 300) / 2)
        y_position = int((screen_height - 200) / 2)

        self.root.geometry(f"300x200+{x_position}+{y_position}")

        self.label_username = tk.Label(root, text="Nom d'utilisateur")
        self.label_username.pack(pady=5)
        self.entry_username = tk.Entry(root)
        self.entry_username.pack(pady=5)

        self.label_password = tk.Label(root, text="Mot de passe")
        self.label_password.pack(pady=5)
        self.entry_password = tk.Entry(root, show="*")
        self.entry_password.pack(pady=5)

        self.btn_login = tk.Button(root, text="Connexion", command=self.login)
        self.btn_login.pack(pady=10)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Check if the username and password are correct
        if (username == "Katanga" or username == "Katanga@1") and password == "123456":
            # Close the login window
            self.root.destroy()
            # Launch the main application
            self.app.launch_main_app()
        else:
            messagebox.showerror(
                "Échec de la connexion", "Nom d'utilisateur ou mot de passe invalide")


class HighSchoolManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Complexe Scolaire Katanga 2024 - 2025")
        self.root.configure(bg='#052659')

        # Calculate the center position
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_position = int((screen_width - 800) / 2)
        y_position = int((screen_height - 600) / 2)

        self.root.geometry(f"800x600+{x_position}+{y_position}")
        self.login_window = LoginWindow(tk.Toplevel(), self)

    def launch_main_app(self):
        self.login_window.root.destroy()

        self.db_connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Makabu01",
            database="sys"
        )
        # Title frame at the top

        # Title frame at the top

        self.create_database_table()


# ===================Details frame=======================
        # Create LabelFrame for entry widgets
        label_frame = ttk.LabelFrame(
            root, text="Informations de l'élève", padding=(20, 10))
        label_frame.grid(row=0, column=0, padx=10, pady=80, columnspan=1)

        # Labels and Entry Widgets inside the LabelFrame
        self.label_first_name = tk.Label(
            label_frame, text="Nom:", justify="center")
        self.label_first_name.grid(
            row=0, column=0, padx=10, pady=5, sticky=tk.E)

        self.entry_first_name = tk.Entry(label_frame, bg="lightgray")
        self.entry_first_name.grid(
            row=0, column=1, padx=10, pady=5, sticky=tk.W)

        self.label_middle_name = tk.Label(
            label_frame, text="Post-Nom:", justify="center")
        self.label_middle_name.grid(
            row=1, column=0, padx=10, pady=5, sticky=tk.E)

        self.entry_middle_name = tk.Entry(label_frame, bg="lightgray")
        self.entry_middle_name.grid(
            row=1, column=1, padx=10, pady=5, sticky=tk.W)

        self.label_last_name = tk.Label(
            label_frame, text="Prénom:", justify="center")
        self.label_last_name.grid(
            row=2, column=0, padx=10, pady=5, sticky=tk.E)

        self.entry_last_name = tk.Entry(label_frame, bg="lightgray")
        self.entry_last_name.grid(
            row=2, column=1, padx=10, pady=5, sticky=tk.W)

        # ====================== Combobox for Gender
        self.label_gender = tk.Label(label_frame, text="Genre:")
        self.label_gender.grid(row=3, column=0, padx=10, pady=5, sticky=tk.E)
        genders = ["Feminin", "Masculin"]
        self.combo_gender = ttk.Combobox(
            label_frame, values=genders, state="readonly")
        self.combo_gender.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)

        self.label_dob = tk.Label(label_frame, text="Date de naissance:")
        self.label_dob.grid(row=4, column=0, padx=10, pady=5, sticky=tk.E)

        self.entry_dob = tk.Entry(label_frame, bg="lightgray")
        self.entry_dob.grid(row=4, column=1, padx=10, pady=5, sticky=tk.W)

        self.label_pob = tk.Label(label_frame, text="Lieu de naissance:")
        self.label_pob.grid(row=5, column=0, padx=10, pady=5, sticky=tk.E)

        self.entry_pob = tk.Entry(label_frame, bg="lightgray")
        self.entry_pob.grid(row=5, column=1, padx=10, pady=5, sticky=tk.W)

        # ======================== Create a Combobox for the "Grade" field
        self.label_grade = tk.Label(label_frame, text="Classe:")
        self.label_grade.grid(row=6, column=0, padx=10, pady=5, sticky=tk.E)

        # ===================== Create a Combobox for the "Grade" field
        self.combo_grade = ttk.Combobox(
            label_frame, values=["1Primaire A", "1B", "2A", "2B", "3A", "3B", "4A", "4B", "5A", "5B", "6A", "6B", "7A", "7B", 8, 9, 10, 11, 12], state="readonly")
        self.combo_grade.grid(row=6, column=1, padx=10, pady=5, sticky=tk.W)

        self.label_father_name = tk.Label(label_frame, text="Père:")
        self.label_father_name.grid(
            row=0, column=2, padx=10, pady=5, sticky=tk.E)

        self.entry_father_name = tk.Entry(label_frame, bg="lightgray")
        self.entry_father_name.grid(
            row=0, column=3, padx=10, pady=5, sticky=tk.W)

        self.label_mother_name = tk.Label(label_frame, text="Mère:")
        self.label_mother_name.grid(
            row=1, column=2, padx=10, pady=5, sticky=tk.E)

        self.entry_mother_name = tk.Entry(label_frame, bg="lightgray")
        self.entry_mother_name.grid(
            row=1, column=3, padx=10, pady=5, sticky=tk.W)

        self.label_phone_number = tk.Label(label_frame, text="Telephone:")
        self.label_phone_number.grid(
            row=2, column=2, padx=10, pady=5, sticky=tk.E)

        self.entry_phone_number = tk.Entry(label_frame, bg="lightgray")
        self.entry_phone_number.grid(
            row=2, column=3, padx=10, pady=5, sticky=tk.W)

        self.label_email_address = tk.Label(
            label_frame, text="Email Addresse:")
        self.label_email_address.grid(
            row=3, column=2, padx=10, pady=5, sticky=tk.E)

        self.entry_email_address = tk.Entry(label_frame, bg="lightgray")
        self.entry_email_address.grid(
            row=3, column=3, padx=10, pady=5, sticky=tk.W)

        self.label_address = tk.Label(label_frame, text="Addresse:")
        self.label_address.grid(row=4, column=2, padx=10, pady=5, sticky=tk.E)

        self.entry_address = tk.Entry(label_frame, bg="lightgray")
        self.entry_address.grid(row=4, column=3, padx=10, pady=5, sticky=tk.W)

        self.label_province = tk.Label(
            label_frame, text="Province:")
        self.label_province.grid(
            row=5, column=2, padx=10, pady=5, sticky=tk.E)

        self.entry_province = tk.Entry(label_frame, bg="lightgray")
        self.entry_province.grid(
            row=5, column=3, padx=10, pady=5, sticky=tk.W)

        # --------------------- Add a small down border with copyright text
        copyright_label = tk.Label(
            self.root, text="© MightyCoorporation", font=("Helvetica", 8), bd=0, relief=tk.SOLID)
        copyright_label.grid(
            row=1, column=1, padx=10, pady=(0, 5), sticky=tk.W + tk.S)

        # ==========================Buttons frame=======================
        self.ButtonFrame = Frame(root, bd=20, relief=RIDGE)
        self.ButtonFrame.grid(row=1, column=0, pady=2, columnspan=1)

        self.btn_register = tk.Button(
            self.ButtonFrame, text="S'inscrire", command=self.register_student)
        self.btn_register.grid(row=0, column=0, padx=10)

        self.btn_clear = tk.Button(
            self.ButtonFrame, text="Effacer", command=self.clear_entries)
        self.btn_clear.grid(row=0, column=2, padx=10)

        self.btn_exit = tk.Button(
            self.ButtonFrame, text="Quitter", command=self.root.destroy)
        self.btn_exit.grid(row=0, column=3, padx=10)

        # Treeview to display student details with vertical and horizontal scrollbars
        self.tree = ttk.Treeview(root, columns=(
            'Nom', 'Post-Nom', 'Prènom', 'Genre', 'Date de Naissance', 'Lieu de Naissance',
            'Class', 'Père', 'Mère', 'Telephone', 'Email Addresse', 'Addresse', 'Province'))

        self.tree.heading('#0', text='ID')
        self.tree.heading('#1', text='First Name')
        self.tree.heading('#2', text='Middle Name')
        self.tree.heading('#3', text='Last Name')
        self.tree.heading('#4', text='Gender')
        self.tree.heading('#5', text='Date of Birth')
        self.tree.heading('#6', text='Place of Birth')
        self.tree.heading('#7', text='Grade')
        self.tree.heading('#8', text='Father Name')
        self.tree.heading('#9', text='Mother Name')
        self.tree.heading('#10', text='Phone Number')
        self.tree.heading('#11', text='Email Address')
        self.tree.heading('#12', text='Address')
        self.tree.heading('#13', text='Province')

        for col in self.tree["columns"]:
            self.tree.heading(col, text=col, anchor=tk.CENTER)
            # Adjust width as needed
            # self.tree.column(col, anchor=tk.CENTER, width=5)

        self.tree_scroll_y = ttk.Scrollbar(
            root, orient="vertical", command=self.tree.yview)
        self.tree_scroll_x = ttk.Scrollbar(
            root, orient="horizontal", command=self.tree.xview)

        self.tree.configure(
            yscrollcommand=self.tree_scroll_y.set, xscrollcommand=self.tree_scroll_x.set)

        self.tree.grid(row=3, column=0, columnspan=2, pady=20, sticky='nsew')
        self.tree_scroll_y.grid(row=3, column=2, pady=10, sticky='ns')
        self.tree_scroll_x.grid(
            row=4, column=0, columnspan=2, pady=10, sticky='ew')

        root.grid_rowconfigure(3, weight=1)
        root.grid_columnconfigure(0, weight=1)

        # Display students on application startup
        self.display_students()

    def create_database_table(self):
        cursor = self.db_connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INT (4) AUTO_INCREMENT PRIMARY KEY,
                first_name VARCHAR(255),
                middle_name VARCHAR(255),
                last_name VARCHAR(255),
                gender VARCHAR(10),
                date_of_birth DATE,
                place_of_birth VARCHAR(255),
                grade VARCHAR(10),  
                father_name VARCHAR(255),
                mother_name VARCHAR(255),
                phone_number VARCHAR(15),
                email_address VARCHAR(255),
                address VARCHAR(255),
                province VARCHAR(255)
            )
        ''')
        self.db_connection.commit()

    def display_students(self):
        self.tree.delete(*self.tree.get_children())
        cursor = self.db_connection.cursor()
        cursor.execute('SELECT * FROM students')
        students = cursor.fetchall()

        for student in students:
            # Convert date_of_birth to a formatted string
            formatted_dob = student[5].strftime(
                '%Y-%m-%d') if student[5] else ''

            # Insert the data into the Treeview widget with anchor set to CENTER
            self.tree.insert('', 'end', values=(
                student[0], student[1], student[2], student[3], student[4], formatted_dob,
                student[6], student[7], student[8], student[9], student[10], student[11], student[12], student[13]),
                anchor=tk.LEFT)

    def register_student(self):
        first_name = self.entry_first_name.get()
        middle_name = self.entry_middle_name.get()
        last_name = self.entry_last_name.get()
        gender = self.combo_gender.get()
        date_of_birth = self.entry_dob.get()
        place_of_birth = self.entry_pob.get()
        grade = self.combo_grade.get()
        father_name = self.entry_father_name.get()
        mother_name = self.entry_mother_name.get()
        phone_number = self.entry_phone_number.get()
        email_address = self.entry_email_address.get()
        address = self.entry_address.get()
        province = self.entry_province.get()

        if first_name and last_name and gender and date_of_birth and place_of_birth and grade:
            try:
                cursor = self.db_connection.cursor()
                cursor.execute('INSERT INTO students (first_name, middle_name, last_name, gender, date_of_birth, place_of_birth, grade, father_name, mother_name, phone_number, email_address, address, province) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (
                    first_name, middle_name, last_name, gender, date_of_birth, place_of_birth, grade, father_name, mother_name, phone_number, email_address, address, province))
                self.db_connection.commit()

                # Fetch the last inserted ID
                last_inserted_id = cursor.lastrowid

                # Retrieve the data of the newly inserted student
                cursor.execute(
                    'SELECT * FROM students WHERE id=%s', (last_inserted_id,))
                new_student = cursor.fetchone()

                # Insert the data into the Treeview widget
                self.tree.insert('', 'end', values=new_student)

                messagebox.showinfo(
                    "Success", "Student registered successfully!")
                self.clear_entries()
            except Exception as e:
                messagebox.showerror("Error", f"Error: {str(e)}")
        else:
            messagebox.showerror(
                "Error", "Please fill in all required fields.")

    def display_students(self):
        self.tree.delete(*self.tree.get_children())
        cursor = self.db_connection.cursor()
        cursor.execute('SELECT * FROM students')
        students = cursor.fetchall()

        for student in students:
            self.tree.insert('', 'end', values=student)

    def clear_entries(self):
        # Clear all entry widgets
        self.entry_first_name.delete(0, tk.END)
        self.entry_middle_name.delete(0, tk.END)
        self.entry_last_name.delete(0, tk.END)
        self.combo_gender.set('')  # Clear the selected gender
        self.entry_dob.delete(0, tk.END)
        self.entry_pob.delete(0, tk.END)
        self.combo_grade.set('')  # Clear the selected grade
        self.entry_father_name.delete(0, tk.END)
        self.entry_mother_name.delete(0, tk.END)
        self.entry_phone_number.delete(0, tk.END)
        self.entry_email_address.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)
        self.entry_province.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = HighSchoolManagementSystem(root)
    root.mainloop()
