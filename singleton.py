print "Please enter the name of your singleton"
name = raw_input('-->').capitalize()

header = open(name + ".h", 'w')
implementation = open(name + ".m", 'w')

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
header.write("#import <Foundation/Foundation.h>\n\n")
header.write("@interface " + name + " : NSObject\n\n")

for var in variables:
    if "*" in var[0]:
        header.write("@property (nonatomic, strong) " + var[0] + " " + var[1] + ";\n")
    else:
        header.write("@property " + var[0] + " " + var[1] + ";\n")

header.write("\n+(" + name + " *)sharedInstance;\n\n")

for var in variables:
    header.write("+(" + var[0] + ")" + "get" + var[1].capitalize() + ";\n")
    header.write("+(void)set" + var[1].capitalize() + ":(" + var[0] + ")" + var[1] + ";\n")

header.write("\n@end")
header.close()

#Implementation file
implementation.write("#import \"" + name + ".h\"\n\n")
implementation.write("@implementation " + name + "\n\n")
implementation.write("static " + name + " *_" + name.lower() + ";\n\n")
implementation.write("+(" + name + " *)sharedInstance\n{\n")
implementation.write("\tstatic dispatch_once_t _singletonPredicate;\n")
implementation.write("\t\tdispatch_once(&_singletonPredicate), ^ {\n")
implementation.write("\t\t\t_" + name.lower() + " = [[self alloc] init];\n")
implementation.write("\t\t});\n")
implementation.write("\treturn _" + name.lower() + ";\n}\n\n")

for var in variables:
    implementation.write("+(" + var[0] + ")get" + var[1].capitalize() + "\n{\n")
    implementation.write("\treturn [[" + name + " sharedInstance] " + var[1] + "];\n}\n\n")
    implementation.write("+(void)set" + var[1].capitalize() + ":(" + var[0] + ")" + var[1] + "\n{\n")
    implementation.write("\t[[" + name + " sharedInstance] set" + var[1].capitalize() + ":" + var[1] + "];\n}\n\n")

implementation.write("@end\n")
implementation.close()
