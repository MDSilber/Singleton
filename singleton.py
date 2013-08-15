import readline

def capitalize_first_letter(s):
    return s[0].upper() + s[1:]

def lower_case_first_letter(s):
    return s[0].lower() + s[1:]

print "Please enter the name of your singleton"
name = capitalize_first_letter(raw_input('-->'))

header = ''
implementation = ''

variables = []

print "Input instance variables. When finished, enter a blank line"

#Get variables
while True:
    print "Input type of instance variable"
    var_type = raw_input('-->')
    print "Input name of instance variable"
    var_name = raw_input('-->')

    if var_type == '' or var_name == '':
        break
    else:
        variables.append((var_type, var_name))

#Header file
header += "#import <Foundation/Foundation.h>\n\n"
header += "@interface " + name + " : NSObject\n\n"

for var in variables:
    if "*" in var[0]:
        header += "@property (nonatomic, strong) " + var[0] + " " + var[1] + ";\n"
    else:
        header += "@property " + var[0] + " " + var[1] + ";\n"

header += "\n+(" + name + " *)sharedInstance;\n\n"

for var in variables:
    header += "+(" + var[0] + ")" + "get" + capitalize_first_letter(var[1]) + ";\n"
    header += "+(void)set" + capitalize_first_letter(var[1]) + ":(" + var[0] + ")" + var[1] + ";\n"

header += "\n@end"

#Implementation file
implementation += "#import \"" + name + ".h\"\n\n"
implementation += "@implementation " + name + "\n\n"
implementation += "static " + name + " *_" + lower_case_first_letter(name) + ";\n\n"
implementation += "+(" + name + " *)sharedInstance\n{\n"
implementation += "\tstatic dispatch_once_t _singletonPredicate;\n"
implementation += "\t\tdispatch_once(&_singletonPredicate, ^ {\n"
implementation += "\t\t\t_" + name.lower() + " = [[self alloc] init];\n"
implementation += "\t\t});\n"
implementation += "\treturn _" + name.lower() + ";\n}\n\n"

for var in variables:
    implementation += "+(" + var[0] + ")get" + capitalize_first_letter(var[1]) + "\n{\n"
    implementation += "\treturn [[" + name + " sharedInstance] " + var[1] + "];\n}\n\n"
    implementation += "+(void)set" + capitalize_first_letter(var[1]) + ":(" + var[0] + ")" + var[1] + "\n{\n"
    implementation += "\t[[" + name + " sharedInstance] set" + capitalize_first_letter(var[1]) + ":" + var[1] + "];\n}\n\n"

implementation += "@end\n"

header_file = open(name + ".h", 'w')
header_file.write(header)
header_file.close()

implementation_file = open(name + ".m", 'w')
implementation_file.write(implementation)
implementation_file.close()
