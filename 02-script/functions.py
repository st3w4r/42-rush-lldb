def mainrun(debugger, command, result, dct):
	debugger.HandleCommand("breakpoint set --name main")
	debugger.HandleCommand("process launch")

def pcfv(debugger, command, result, dct):
	debugger.HandleCommand("process continue")
	debugger.HandleCommand("frame variable")

def pcn(debugger, command, result, dct):
	args = command.split(" ")
	if len(args) is not 1:
		print "Usage: one argument, numbers of process repetition"
		return
	try:
		val = int(args[0])
	except ValueError:
		print "Usage: one argument, numbers of process repetition"
		return

	for i in range(0, int(args[0])):
		debugger.HandleCommand("process continue")

def colorR(debugger, command, result, dct):
	debugger.HandleCommand('script print "\033[31m"')

def colorG(debugger, command, result, dct):
	debugger.HandleCommand('script print "\033[32m"')

def colorB(debugger, command, result, dct):
	debugger.HandleCommand('script print "\033[34m"')

def colorW(debugger, command, result, dct):
	debugger.HandleCommand('script print "\033[39m"')

def colorT(debugger, command, result, dct):
	debugger.HandleCommand('script print "\033[36m"')

def info(debugger, command, result, dct):
	colorR(debugger, command, result, dct)
	debugger.HandleCommand("target list")
	colorG(debugger, command, result, dct)
	debugger.HandleCommand("disas")
	colorB(debugger, command, result, dct)
	debugger.HandleCommand("register read --all")
	colorT(debugger, command, result, dct)
	debugger.HandleCommand("frame select")
	colorW(debugger, command, result, dct)

def pc2(debugger, command, result, dct):
	debugger.HandleCommand("process continue")
	debugger.HandleCommand("process continue")

def pc3(debugger, command, result, dct):
	debugger.HandleCommand("process continue")
	debugger.HandleCommand("process continue")
	debugger.HandleCommand("process continue")

def __lldb_init_module(debugger, internal_dict):
	debugger.HandleCommand("command script add -f functions.mainrun mainrun")
	debugger.HandleCommand("command script add -f functions.pcfv pcfv")
	debugger.HandleCommand("command script add -f functions.pc2 pc2")
	debugger.HandleCommand("command script add -f functions.pc3 pc3")
	debugger.HandleCommand("command script add -f functions.pcn pcn")
	debugger.HandleCommand("command script add -f functions.colorR colorR")
	debugger.HandleCommand("command script add -f functions.colorG colorG")
	debugger.HandleCommand("command script add -f functions.colorB colorB")
	debugger.HandleCommand("command script add -f functions.colorW colorW")
	debugger.HandleCommand("command script add -f functions.colorT colorT")
	debugger.HandleCommand("command script add -f functions.info info")
