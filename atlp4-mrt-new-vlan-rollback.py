# Load the jinja library's namespace into the current module.
import jinja2

# In this case, we will load templates off the filesystem.
# This means we must construct a FileSystemLoader object.
# 
# The search path can be used to make finding templates by
#   relative paths much easier.  In this case, we are using
#   absolute paths and thus set it to the filesystem root.
templateLoader = jinja2.FileSystemLoader( searchpath="templates/" )

# An environment provides the data necessary to read and
#   parse our templates.  We pass in the loader object here.
templateEnv = jinja2.Environment( loader=templateLoader )

# This constant string specifies the template file we will use.
TEMPLATE_FILE = "atlp4-mrt-new-vlan-rollback.jinja2"

# Read the template file using the environment object.
# This also constructs our Template object.
template = templateEnv.get_template( TEMPLATE_FILE )

# Ask the user what they want
VLAN_ID=raw_input("VLAN ID: ")
#VLAN_NAME=raw_input("VLAN Name: ")
#NETWORK=raw_input("Network (without CIDR): ")
#NETWORK_CIDR=raw_input("CIDR Mask: ")
#N7K_SVI_A=raw_input("7K SVI (A side): ")
#N7K_SVI_B=raw_input("7K SVI (B side): ")
#N7K_SVI_FLOAT=raw_input("7K SVI floating: ")
SRO_NUMBER=raw_input("SRO Number: ")

# Modify things that need CIDR
#N7K_SVI_A = N7K_SVI_A + "/" + NETWORK_CIDR
#N7K_SVI_B = N7K_SVI_B + "/" + NETWORK_CIDR
#NETWORK = NETWORK + "/" + NETWORK_CIDR

# Specify any input variables to the template as a dictionary.
templateVars = { #"network" : NETWORK,
                 "sro_number" : SRO_NUMBER,
                 "vlan_id" : VLAN_ID,
                # "n7k_svi_a" : N7K_SVI_A,
                 #"n7k_svi_b" : N7K_SVI_B,
                 #"n7k_svi_float" : N7K_SVI_FLOAT,
                  #"vlan_name" : VLAN_NAME
                  }


# Finally, process the template to produce our final text.
outputText = template.render( templateVars )

print outputText
