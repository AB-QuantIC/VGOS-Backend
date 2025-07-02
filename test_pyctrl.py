
from dbbc3.DBBC3 import DBBC3
from dbbc3.DBBC3Validation import ValidationFactory, ValidationReport
import logging

dbbc3 = DBBC3("192.168.190.92")

val = ValidationFactory().create(dbbc3)
# print (val.validateIFLevel("A"))
# print (val.validateIFLevel("B"))
# print (val.validateIFLevel("C"))
# print (val.validateIFLevel("D"))
# print (val.validateIFLevel("E"))
# print (val.validateIFLevel("F"))
# print (val.validateIFLevel("G"))
# print (val.validateIFLevel("H"))

# print (val.validateSamplerOffsets(0))

print(val.validateSynthesizerLock("A"))
print(val.validateSynthesizerFreq("A"))

# Analog power levels
print(val.validateIFLevel("A"))

# Sample statistics
print(val.validateSamplerPower("A"))
print(val.validateSamplerOffsets("A"))

# Multi IF sync check
print(val.validatePPS(100)) # PPS delay much be less than 100ns for all borads
print(val.validateSamplerPhases())



#                 validate.validateIFLevel('a')
#                 validate.validateIFLevel('b')
#                 validate.validateIFLevel('c')
#                 validate.validateIFLevel('d')

#                 validate.validateSamplerPhases()

#                 validate.validateSamplerPower(0)
#                 validate.validateSamplerPower(1)
#                 validate.validateSamplerPower('C')
#                 validate.validateSamplerPower('D')

#                 validate.validateSamplerOffsets(0)
#                 validate.validateSamplerOffsets(1)
#                 validate.validateSamplerOffsets('C')
#                 validate.validateSamplerOffsets('D')