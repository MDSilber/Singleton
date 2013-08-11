print "Please enter the name of your singleton"
name = raw_input('-->').capitalize()

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
    header += "+(" + var[0] + ")" + "get" + var[1].capitalize() + ";\n"
    header += "+(void)set" + var[1].capitalize() + ":(" + var[0] + ")" + var[1] + ";\n"

header += "\n@end"

#Implementation file
implementation += "#import \"" + name + ".h\"\n\n"
implementation += "@implementation " + name + "\n\n"
implementation += "static " + name + " *_" + name.lower() + ";\n\n"
implementation += "+(" + name + " *)sharedInstance\n{\n"
implementation += "\tstatic dispatch_once_t _singletonPredicate;\n"
implementation += "\t\tdispatch_once(&_singletonPredicate, ^ {\n"
implementation += "\t\t\t_" + name.lower() + " = [[self alloc] init];\n"
implementation += "\t\t});\n"
implementation += "\treturn _" + name.lower() + ";\n}\n\n"

for var in variables:
    implementation += "+(" + var[0] + ")get" + var[1].capitalize() + "\n{\n"
    implementation += "\treturn [[" + name + " sharedInstance] " + var[1] + "];\n}\n\n"
    implementation += "+(void)set" + var[1].capitalize() + ":(" + var[0] + ")" + var[1] + "\n{\n"
    implementation += "\t[[" + name + " sharedInstance] set" + var[1].capitalize() + ":" + var[1] + "];\n}\n\n"

implementation += "@end\n"

header_file = open(name + ".h", 'w')
header_file.write(header)
header_file.close()

implementation_file = open(name + ".m", 'w')
implementation_file.write(implementation)
implementation_file.close()
