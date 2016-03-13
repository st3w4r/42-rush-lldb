def mainrun(debugger, command, result, dct):
	debugger.HandleCommand("breakpoint set --name main")
	debugger.HandleCommand("process launch")

def pcfv(debugger, command, result, dct):
	debugger.HandleCommand("process continue")
	debugger.HandleCommand("frame variables")

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
