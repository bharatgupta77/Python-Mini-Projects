import tkinter as t
import tkinter.ttk as tk


def currency_Converter_tool():
    # create the main window
    window = t.Tk(screenName=None, baseName=None, className='window', useTk=1)
    window.geometry("540x420")

    # since height and width is FALSE, window is not resizable
    window.resizable(height=False, width=False)

    '''
    widgets are added here
    '''
    title = t.Label(
        window, text="Welcome to Currency Converter tool ", pady=20)
    title.pack()

    parent_frame = t.Frame(window, bd=3,
                           relief="groove", pady=20)
    parent_frame.pack()

    child_frame = t.Frame(parent_frame)
    child_frame.pack()

    # this will create a label widget
    l1 = t.Label(child_frame, text="From")
    l2 = t.Label(child_frame, text="To")

    # grid method to arrange labels in respective
    # rows and columns as specified
    l1.grid(row=0, column=0, sticky="w", pady=2, padx=2)
    l2.grid(row=1, column=0, sticky="w", pady=2, padx=2)

    # this is the combobox for holding from_currencies
    e1 = tk.Combobox(child_frame, font=('Poppins 10 bold'))
    # this is the combobox for holding to_currencies
    e2 = tk.Combobox(child_frame, font=('Poppins 10 bold'))

    # this will arrange entry widgets
    e1.grid(row=0, column=1, pady=2)
    e2.grid(row=1, column=1, pady=2)

    convert_btn = t.Button(parent_frame, bg="red", text="Convert")
    convert_btn.pack()

    window.mainloop()


currency_Converter_tool()
