import os
from PyPDF2 import PdfReader

class Files():
    
    def __init__(self, path):
        self.path = path

    def getFiles(self):
        files = []
        try:
            for diretorio, subpastas, arquivos in os.walk(self.path):
                for arquivo in arquivos:
                    if arquivo.endswith('.pdf') or arquivo.endswith('.PDF'):
                        files.append(os.path.join(diretorio, arquivo))
        except:
             print("Arquivos não encontrados.")
        finally:
            return files

    def readFile(self, pathFile):

        try:
            pages = []
            filter = []
            reader = PdfReader(pathFile)

            for i in range(len(reader.pages)):
                #print(i)
                current = reader.pages[i].extract_text().splitlines()
                for line in current:
                    pages.append(line)

            """ for line in pages:
                split = line.split(" ")
                if "/" in split[0]:
                    i=1
                    print(pages[pages.index(line)])
                    filter.append(pages[pages.index(line)])
                    while "CFE" not in pages[pages.index(line)+i]:
                        linha = pages[pages.index(line)+i]
                        splitted = linha.split(" ")
                        #print(len(splitted[0]))
                        if "UN" in splitted[-1]:
                            print(linha)
                            filter.append(linha)

                        if "CFE" in pages[pages.index(line)+i]:
                            break

                        i += 1 """

            for i in range(len(pages)):
                split = pages[i].split(" ")
                if "/" in split[0]:
                    j=1
                    #print(pages[pages.index(pages[i])])
                    filter.append(pages[pages.index(pages[i])])
                    while "CFE" not in pages[pages.index(pages[i])+j]:
                        
                        linha = pages[pages.index(pages[i])+j]
                        splitted = linha.split(" ")
                        if "UN" in splitted[-1]:
                            #print(linha)
                            filter.append(linha)
                        elif "CFE" in pages[pages.index(pages[i])+j]:
                            j=1
                            break
                        print(pages.index(pages[pages.index(pages[i])+j]), len(pages), j)
                        j+=1
                        

        except Exception as e:
            print('\n')
            print(f"   Erro ao ler arquivo {pathFile.split('/')[-1]}", '\n')  
            print("  ", "Erro: ", e, '\n')
            print("  ", "Pulando arquivo...", '\n')
            