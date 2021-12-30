from ipykernel.kernelapp import IPKernelApp
from .kernel import GroovyKernel
IPKernelApp.launch_instance(kernel_class=GroovyKernel)
