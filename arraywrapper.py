import numpy as np
import array
class myarray(array.array):
    arraynumber1=np.array((1,2,3,4))
    arraynumber2=np.array([5,6,7,8])
    def arrar_addition(self):
        result=self.arraynumber1+self.arraynumber2
        return result
arrayobj=myarray('u')
#arrayobj.arraynumber1=np.array((1,3,5,7))
#arrayobj.arraynumber2=np.array([9,11,13,15])
print(arrayobj.arrar_addition())

