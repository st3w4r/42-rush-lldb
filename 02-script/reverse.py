import lldb

def reverse(debugger, args, result, internal_dict):
	target = debugger.GetSelectedTarget()
	print "FT_"+str(target)[::-1]

def __lldb_init_module(debugger, internal_dict):
	debugger.HandleCommand('command script add -f reverse.reverse reverse')
