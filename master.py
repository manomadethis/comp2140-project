#Python Code

import tkinter as tk

#Creating the master window
master_window = tk.Tk()
master_window.title("User Login")
master_window.configure(background='#FF9999')

#Setting up the user input lables
username_lbl = tk.Label(master_window, text='Username')
username_lbl.pack()
username_txt_box = tk.Entry(master_window)
username_txt_box.pack()
password_lbl = tk.Label(master_window, text="Password")
password_lbl.pack()
password_txt_box = tk.Entry(master_window, show='*')
password_txt_box.pack()

#Opening the credentials file
with open('credentials.txt', 'r') as file :
  users = dict( line.strip().split(':') for line in file )

def login():
  name = username_txt_box.get()
  pword = password_txt_box.get()

  if(name in users and users[name] == pword):
    master_window.destroy()
    record_management_system()
  else:
    response_lbl.configure(text='Invalid Username or Password. Try Again.',fg='red')

submit_btn = tk.Button(master_window, text='Login', command=login, bg='#005A9C')
submit_btn.pack()

response_lbl = tk.Label(master_window)
response_lbl.pack()

#Creating the record management system window
def record_management_system():
  record_window = tk.Tk()
  record_window.title('Records Management System')
  record_window.configure(background='#FF9999')

  #Creating a container for records
  records = []

  #Creating the add record label and button
  add_record_lbl = tk.Label(record_window, text="Add Record")
  add_record_lbl.pack()
  add_record_btn = tk.Button(record_window, text='Add Record', bg='#005A9C')
  add_record_btn.pack()

  #Creating functions for the add record button
  def add_data():
    #Creating the data entry window
    add_data_window = tk.Tk()
    add_data_window.title('Enter the user information')

    #Setting up the labels for each data entry field
    name_lbl = tk.Label(add_data_window, text='Name')
    name_lbl.pack()
    name_txt_box = tk.Entry(add_data_window)
    name_txt_box.pack()

    id_no_lbl = tk.Label(add_data_window, text="ID Number")
    id_no_lbl.pack()
    id_no_txt_box = tk.Entry(add_data_window)
    id_no_txt_box.pack()

    age_lbl = tk.Label(add_data_window, text="Age")
    age_lbl.pack()
    age_txt_box = tk.Entry(add_data_window)
    age_txt_box.pack()

    address_lbl = tk.Label(add_data_window, text="Address")
    address_lbl.pack()
    address_txt_box = tk.Entry(add_data_window)
    address_txt_box.pack()

    phone_no_lbl = tk.Label(add_data_window, text="Phone Number")
    phone_no_lbl.pack()
    phone_no_txt_box = tk.Entry(add_data_window)
    phone_no_txt_box.pack()

    #Creating a submit button
    submit_btn = tk.Button(add_data_window, text="Submit", bg='#005A9C')
    submit_btn.pack()

    response_lbl = tk.Label(add_data_window)
    response_lbl.pack()

    #Saving the data in a file
    def save_data():
      name = name_txt_box.get()
      age = age_txt_box.get()
      id_no = id_no_txt_box.get()
      address = address_txt_box.get()
      phone_no = phone_no_txt_box.get()

      if name != "" and age != "" and id_no != "" and address != "" and phone_no != "":
        records.append([name, age, id_no, address, phone_no])

        with open('records.txt', 'a+') as file:
           file.write(name + ":" + age + ":" + id_no + ":" + address + ":" + phone_no + "\n")

        response_lbl.configure(text="Record saved successfully!", fg='green')
        add_data_window.destroy()
      else:
        response_lbl.configure(text="Please enter all the information!", fg='red')

    #Binding the button to the save_data function
    submit_btn.configure(command=save_data)
  
  #Binding the button to the add_dataFunction
  add_record_btn.configure(command=add_data) 

  #Creating the search record label, entry and button
  search_record_lbl = tk.Label(record_window, text='Search Record')
  search_record_lbl.pack()
  search_record_txt_box = tk.Entry(record_window)
  search_record_txt_box.pack()
  search_record_btn = tk.Button(record_window, text='Search', bg='#005A9C')
  search_record_btn.pack()

  #Creating the function for searching records
  def search_data():
    #Opening the records file and appending it to the records list
    with open('records.txt','r') as file:
      for line in file:
        records.append(line.strip().split(':'))

    #Searching the records
    search_val = search_record_txt_box.get()

    for ele in records:
      if search_val in ele:
        #Opening a results window
        results_window = tk.Tk()
        results_window.title('Results Found')

        #Creating results label
        result_lbl = tk.Label(results_window, text=ele)
        result_lbl.pack()

  #Binding the button to the search_data function
  search_record_btn.configure(command=search_data)


  #Creating the sort record label and button
  sort_record_lbl = tk.Label(record_window, text="Sort Record")
  sort_record_lbl.pack()
  sort_record_btn = tk.Button(record_window, text="Sort Record", bg='#005A9C')
  sort_record_btn.pack()

  #Creating the function for sorting records
  def sort_data():
    #Opening the records file and appending it to the records list
    with open('records.txt','r') as file:
      for line in file:
        records.append(line.strip().split(':'))

    #Sorting the records 
    records.sort()

    #Opening a sort results window
    sort_results_window = tk.Tk()
    sort_results_window.title('Sorted Records')

    for ele in records:
      result_lbl = tk.Label(sort_results_window, text=ele)
      result_lbl.pack()

  #Binding the button to the sort_data function
  sort_record_btn.configure(command=sort_data) 

  #Creating the update record label, entry and button
  update_record_lbl = tk.Label(record_window, text="Update Record")
  update_record_lbl.pack()
  update_record_txt_box = tk.Entry(record_window)
  update_record_txt_box.pack()
  update_record_btn = tk.Button(record_window, text="Update Record", bg='#005A9C')
  update_record_btn.pack()

  #Creating the function for updating records
  def update_data():
    #Reading the records file
    with open('records.txt','r') as file:
      for line in file:
        records.append(line.strip().split(':'))
    
    #Getting the info from the search box
    search_val = update_record_txt_box.get()
    for ele in records:
      if search_val in ele:
        #Opening an update window
        update_window = tk.Tk()
        update_window.title('Update Record')

        #Creating the result label
        result_lbl = tk.Label(update_window, text=ele)
        result_lbl.pack()

        #Creating the update window fields
        name_lbl = tk.Label(update_window, text='Name')
        name_lbl.pack()
        name_txt_box = tk.Entry(update_window)
        name_txt_box.pack()

        id_no_lbl = tk.Label(update_window, text="ID Number")
        id_no_lbl.pack()
        id_no_txt_box = tk.Entry(update_window)
        id_no_txt_box.pack()

        age_lbl = tk.Label(update_window, text="Age")
        age_lbl.pack()
        age_txt_box = tk.Entry(update_window)
        age_txt_box.pack()

        address_lbl = tk.Label(update_window, text="Address")
        address_lbl.pack()
        address_txt_box = tk.Entry(update_window)
        address_txt_box.pack()

        phone_no_lbl = tk.Label(update_window, text="Phone Number")
        phone_no_lbl.pack()
        phone_no_txt_box = tk.Entry(update_window)
        phone_no_txt_box.pack()

        #Creating a save button
        save_btn = tk.Button(update_window, text="Save",bg='#005A9C')
        save_btn.pack()
        response_lbl = tk.Label(update_window)
        response_lbl.pack()

        #Creating a save data function
        def save_data():
          name = name_txt_box.get()
          age = age_txt_box.get()
          id_no = id_no_txt_box.get()
          address = address_txt_box.get()
          phone_no = phone_no_txt_box.get()

          if name != "" and age != "" and id_no != "" and address != "" and phone_no != "":
            with open('records.txt','w') as file:
              for row in records:
                if search_val not in row: 
                  file.write(row[0] + ":" + row[1] + ":" + row[2] + ":" +
                    row[3] + ":" + row[4] + "\n")
                else:
                  file.write(name + ":" + age + ":" +
                    id_no + ":" + address + ":" + phone_no + "\n")

            response_lbl.configure(text="Record updated successfully!", fg='green')
            update_window.destroy()
          else:
            response_lbl.configure(text="Please enter all the information!", fg='red')

        #Binding the button to the save_data function
        save_btn.configure(command=save_data)

  #Binding the button to the update_data function
  update_record_btn.configure(command=update_data)

  #Creating the delete record label, entry and button
  delete_record_lbl = tk.Label(record_window, text="Delete Record")
  delete_record_lbl.pack()
  delete_record_txt_box = tk.Entry(record_window)
  delete_record_txt_box.pack()
  delete_record_btn = tk.Button(record_window, text="Delete Record", bg='#005A9C')
  delete_record_btn.pack()

  #Creating the function for deleting records
  def delete_data():
    #Reading the records file
    with open('records.txt','r') as file:
      for line in file:
        records.append(line.strip().split(':'))
    search_val = delete_record_txt_box.get()

    #Opening a delete window
    delete_window = tk.Tk()
    delete_window.title('Delete Record')

    #Creating the save button
    save_btn = tk.Button(delete_window, text='Delete', bg='#005A9C')
    save_btn.pack()
    response_lbl = tk.Label(delete_window)
    response_lbl.pack() 

    #Creating the save data function
    def save_data():
      with open('records.txt','w') as file:
        for row in records:
          if search_val not in row: 
            file.write(row[0] + ":" + row[1] + ":" + row[2] + ":" +
            row[3] + ":" + row[4] + "\n")

      response_lbl.configure(text="Record deleted successfulyy!", fg='green')
      delete_window.destroy()

    #Binding the button to the save_data function
    save_btn.configure(command=save_data)

  #Binding the button to the delete_data function
  delete_record_btn.configure(command=delete_data)

# Keeping the main window running
master_window.mainloop()