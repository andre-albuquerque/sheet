from tkinter import filedialog as fd

def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    filename = fd.askdirectory(title='Selecione a pasta com os arquivos perdcomp.pdf')
    folder_path = filename
    return folder_path