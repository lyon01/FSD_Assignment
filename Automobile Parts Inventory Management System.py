#WONG JIE SHENG
#TP056464

def menu():
    while True:
        choice = int(input("1.Create parts \n2.Update parts \n3.Parts tracking \n4.Search \n5.Exit \nPlease enter your option number: "))
        if (choice == 1):
            savePartsCreation()
        elif (choice == 2):
            saveUpdateParts()
        elif (choice == 3):
            partsTracking()
        elif (choice == 4):
            search()
        elif (choice == 5):
            print('Have a nice day')
            break
        else:
            print('Invalid input')
        
def invalidInput(partId):
    valid = True
    pts = []
    for file in ['WBS.txt','WAY.txt','WBR.txt']:
        fileHandler = open(file,'r')
        data = fileHandler.readlines()
        for line in data:
            line = line.rstrip()
            newLine = line.split('\t')
            partIdInList = newLine[0]
            if partId == partIdInList:
                valid = False
                print('Part ID already existed')
                return 'existed'
            else:
                continue
        fileHandler.close()
    if valid == True:
        pts.append(partId)
    return pts

def partsCreation():
    pts = []
    # pts = [partId,partName,section,supplierCode,supplierName,supplierTelephone,supplierEmail,quantity,cost]
    partId = input('Enter the part ID: ')
    if invalidInput(partId) == 'existed':
        return
    pts.append(partId)
    partName = input('Enter the part\'s name: ')
    pts.append(partName)
    section = input('Enter the part\'s section(ES/BWS/AS): ')
    pts.append(section)
    supplierCode = input('Enter the supplier code: ')
    pts.append(supplierCode)
    supplierName = input('Enter the supplier\'s name: ')
    pts.append(supplierName)
    supplierTelephone = input('Enter the supplier\'s telephone number: ')
    pts.append(supplierTelephone)
    supplierEmail = input('Enter the supplier\'s email: ')
    pts.append(supplierEmail)
    quantity = input('Enter quantity: ')
    pts.append(quantity)
    cost = input('Enter the cost of the part: ')
    pts.append(cost)
    print('Part created successfully!')
    return pts

def writePartsCreation(fileName):
    fileHandler = open(fileName,'a')
    parts = partsCreation()
    if parts == None:
        return
    for pc in parts:
        fileHandler.write(pc)
        fileHandler.write('\t')
    fileHandler.write('\n')
    fileHandler.close()
    return

def savePartsCreation():
    warehouse = int(input('1.WBS \n2.WAY \n3.WBR \nPlease select a warehouse: '))
    if warehouse == 1:
        fileName = 'WBS.txt'
        writePartsCreation(fileName)

    elif warehouse == 2:
        fileName = 'WAY.txt'
        writePartsCreation(fileName)

    elif warehouse == 3:
        fileName = 'WBR.txt'
        writePartsCreation(fileName)

    else:
        print('Invalid input')
            

def updateFileData(data, quantity, action):
    '''
    data : accepts a list of strings (direct result of filehandler.readline())
    returns a list of lists with updated quantity
    '''
    textFileDataInList = [] # a list of lists [[]]

    for line in data: # format data into lists
        line = line.rstrip()
        dataList = line.split('\t') # convert the line of txt file to list 
        textFileDataInList.append(dataList)

    partChoice = input('Which part is sent/received? (Enter part ID): ')

    lineToChange = None
    for line in textFileDataInList: # check if the inputed part ID is in the text file data 
        if partChoice != line[0]:
            continue
        else:
            lineToChange = line
            textFileDataInList.remove(line)
            break 

    if lineToChange == None:
        print('Part is not available')
        return False 

    if action == 1:
        lineToChange[-2] = str(int(lineToChange[-2]) - quantity) #reduce quantity of the selected part ID 
    elif action == 2:
        lineToChange[-2] = str(int(lineToChange[-2]) + quantity) #add quantity of the selected part ID
    textFileDataInList.append(lineToChange)

    return textFileDataInList # modified part ID's quantity 

def saveUpdateParts():
    action = int(input('1.Send parts \n2.Receive parts \nPlease select an option: '))
    newQuantity = int(input('Sent/Received quantity: '))
    warehouse = int(input('1.WBS \n2.WAY \n3.WBR \nPlease select a warehouse: '))

    if warehouse == 1: # if choose bios 
        fileHandler = open('WBS.txt','r')
        data = fileHandler.readlines()
        fileHandler.close()

        newData = updateFileData(data, newQuantity, action)
        if newData == False:
            return
        
        fileHandler = open('WBS.txt','w')
        for line in newData:
            for element in line :
                fileHandler.write(element)
                fileHandler.write('\t')
            fileHandler.write('\n')
        fileHandler.close()
        print('Part quantity has been updated')
        return
    elif warehouse == 2: # if choose ambry
        fileHandler = open('WAY.txt','r')
        data = fileHandler.readlines()
        fileHandler.close()

        newData = updateFileData(data, newQuantity, action)
        if newData == False:
            return

        fileHandler = open('WAY.txt','w')
        for line in newData:
            for element in line :
                fileHandler.write(element)
                fileHandler.write('\t')
            fileHandler.write('\n')
        fileHandler.close()
        print('Part quantity has been updated')
        return
    elif warehouse == 3: # if choose barrier
        fileHandler = open('WBR.txt','r')
        data = fileHandler.readlines()
        fileHandler.close()

        newData = updateFileData(data, newQuantity, action)
        if newData == False:
            return

        fileHandler = open('WBR.txt','w')
        for line in newData:
            for element in line :
                fileHandler.write(element)
                fileHandler.write('\t')
            fileHandler.write('\n')
        fileHandler.close()
        print('Part quantity has been updated')
        return
    else:
        print('Invalid input')


def partsTrackingOne(fileName):
    parts = []
    fileHandler = open(fileName,'r')
    data = fileHandler.readlines()
    for line in data:
        line = line.rstrip()
        newLine = line.split('\t')
        parts.append(newLine[0])
    parts.sort()
    for l in parts:
        for line in data:
            line = line.rstrip()
            newLine = line.split('\t')
            if l == newLine[0]:
                print('Part ID:'+newLine[0],'Part Name:'+newLine[1],'Quantity:'+newLine[-2])
            else:
                continue
    fileHandler.close()
    return

def partsTrackingTwo(fileName):
    parts = []
    fileHandler = open(fileName,'r')
    data = fileHandler.readlines()
    for line in data:
        line = line.rstrip()
        newLine = line.split('\t')
        if int(newLine[-2]) < 10:
            print('Part ID:'+newLine[0],'Part Name:'+newLine[1],'Quantity:'+newLine[-2])
        else:
            continue
    fileHandler.close()
    return

def partsTrackingThree(fileName, section):
    parts = []
    fileHandler = open(fileName,'r')
    data = fileHandler.readlines()
    for line in data:
        line = line.rstrip()
        newLine = line.split('\t')
        if (newLine[2]) == section:
            print('Part ID:'+newLine[0],'Part Name:'+newLine[1],'Section:'+newLine[2],'Quantity:'+newLine[-2])
        else:
            continue
    fileHandler.close()
    return
            
def partsTracking():
    choice = int(input('1.All parts in selected warehouse \n2.Parts with quantity less than 10 by warehouse \n3.Parts supplied to each section \nPlease select an option: '))
    if choice == 1:
        warehouse = int(input('1.WBS \n2.WAY \n3.WBR \nPlease select a warehouse: '))
        if warehouse == 1:
            try:
                fileName = 'WBS.txt'
                partsTrackingOne(fileName)
            except:
                print('File cannot be opened')
                return
                
        elif warehouse == 2:  
            try:
                fileName = 'WAY.txt'
                partsTrackingOne(fileName)
            except:
                print('File cannot be opened')
                return

        elif warehouse == 3:       
            try:
                fileName = 'WBR.txt'
                partsTrackingOne(fileName)     
            except:
                print('File cannot be opened')
                return
        else:
            print('Invalid input')
           
            
    elif choice == 2:
        warehouse = int(input('1.WBS \n2.WAY \n3.WBR \nPlease select a warehouse: '))
        if warehouse == 1:
            try:
                fileName = 'WBS.txt'
                partsTrackingTwo(fileName)
            except:
                print('File cannot be opened')
                return
                
        elif warehouse == 2:
            try:
                fileName = 'WAY.txt'
                partsTrackingTwo(fileName)            
            except:
                print('File cannot be opened')
                return
                
        elif warehouse == 3:
            try:
                fileName = 'WBR.txt'
                partsTrackingTwo(fileName)              
            except:
                print('File cannot be opened')
                return
        else:
            print('Invalid input')
                
    elif choice == 3:
        section = int(input('1.ES \n2.BWS \n3.AS \nPlease select a section: '))
        if section == 1:
            try:
                fileName = 'WBS.txt'
                section = 'ES'
                partsTrackingThree(fileName, section)
                fileName = 'WAY.txt'
                section = 'ES'
                partsTrackingThree(fileName, section)
                fileName = 'WBR.txt'
                section = 'ES'
                partsTrackingThree(fileName, section)
                return              
            except:
                print('File cannot be opened')
                return
                
        elif section == 2:
            try:
                fileName = 'WBS.txt'
                section = 'BWS'
                partsTrackingThree(fileName, section)
                fileName = 'WAY.txt'
                section = 'BWS'
                partsTrackingThree(fileName, section)
                fileName = 'WBR.txt'
                section = 'BWS'
                partsTrackingThree(fileName, section)
                return              
            except:
                print('File cannot be opened')
                return
    
        elif section == 3:
            try:
                fileName = 'WBS.txt'
                section = 'AS'
                partsTrackingThree(fileName, section)
                fileName = 'WAY.txt'
                section = 'AS'
                partsTrackingThree(fileName, section)
                fileName = 'WBR.txt'
                section = 'AS'
                partsTrackingThree(fileName, section)
                return              
            except:
                print('File cannot be opened')
                return
        else:
            print('Invalid input')
    else:
        print('Invalid input')



def search():
    choice = int(input('1.Search part\'s record \n2.Supplier details of part \n3.Parts supplied by supplier \nPlease enter an option: '))
    if choice == 1:
        warehouse = int(input('1.WBS \n2.WAY \n3.WBR \nPlease select a warehouse: '))
        if warehouse == 1:
            fileHandler = open('WBS.txt','r')
        elif warehouse == 2:
            fileHandler = open('WAY.txt','r')
        elif warehouse == 3:
            fileHandler = open('WBR.txt','r')
        else:
            print('Invalid input')
            return
        
        data = fileHandler.readlines()
        partChoice = input('Enter part ID to search: ')
        for line in data:
            line = line.rstrip()
            newLine = line.split('\t')
            partId = newLine[0]
            if partChoice == partId:
                print('Part Name:'+newLine[1],'Section:'+newLine[2],'Quantity:'+newLine[-2],'Cost:'+newLine[-1])
                return
            else:
                continue
        print('Part is not found')
        return
        

    elif choice == 2:
        warehouse = int(input('1.WBS \n2.WAY \n3.WBR \nPlease select a warehouse: '))
        if warehouse == 1:
            fileHandler = open('WBS.txt','r')
        elif warehouse == 2:
            fileHandler = open('WAY.txt','r')
        elif warehouse == 3:
            fileHandler = open('WBR.txt','r')
        else:
            print('Invalid input')
            return
        
        data = fileHandler.readlines()
        partChoice = input('Enter part ID to search: ')
        for line in data:
            line = line.rstrip()
            newLine = line.split('\t')
            partId = newLine[0]
            if partChoice == partId:
                print('Supplier Code:'+newLine[3],'Supplier Name:'+newLine[4],'Telephone number:'+newLine[5],'Email:'+newLine[6])
                return
            else:
                continue
        print('Part is not found')
        return
        
    elif choice == 3:
        valid = False
        supplierChoice = input('Enter supplier ID to search: ')
        for file in ['WBS.txt','WAY.txt','WBR.txt']:
            fileHandler = open(file,'r')
            data = fileHandler.readlines()
            for line in data:
                line = line.rstrip()
                newLine = line.split('\t')
                supplierId = newLine[3]
                if supplierChoice == supplierId:
                    valid = True
                    print('Part ID:'+newLine[0],'Part Name:'+newLine[1],'Section:'+newLine[2],'Quantity:'+newLine[7],'Cost:'+newLine[8]) 
                else:
                    continue
        if valid == False:
            print('Part is not found')
        return
    else:
        print('Invalid input')
                  
menu()
    
             
