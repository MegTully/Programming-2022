def readModules():
    Modules = [] #create an array called Modules
    ModuleName = input("\t Enter the first module name or enter blank to quit :").strip()

    while ModuleName != "": #while the module entered is not blank proceed this loop
        Module = {}         #creates an empty dict
        Module["name"]= ModuleName #assigns the key, "name", the value input by user as ModuleName

    Module["grade"]=int(input("\t\tEnter grade:")) #assigns the grade a user inputs to the key, "grade"
    Modules.append(Module)                         #adds the Modules with the grade to the Modules array

# Next module to be added
    ModuleName = input("\tEnter next module name or enter blank to quit:").strip()

    return Modules