import lldb
import time

def auto(debugger, command, result, internal_dict):
	args = command.split(" ")
	if not len(args) == 3:
		print "Usage: 3 numbers in arguments"
		exit()
	
	debugger.SetAsync(True)
	debugger.HandleCommand("breakpoint set --name main")
	time.sleep(0.5)
	debugger.HandleCommand("process launch")
	time.sleep(0.5)
	debugger.HandleCommand("breakpoint set --line 16 --one-shot")
	time.sleep(0.5)
	debugger.HandleCommand("breakpoint set --source-pattern-regexp 'std::cin|tmp /= max|return biggest;'")
	time.sleep(0.5)
	debugger.HandleCommand("process continue")
	time.sleep(0.5)
	debugger.HandleCommand("expression -- $rsi -= 4")
	time.sleep(0.5)
	debugger.HandleCommand("process continue")
	debugger.GetSelectedTarget().GetProcess().PutSTDIN(args[0]+'\n')
	time.sleep(0.5)
	debugger.HandleCommand("process continue")
	time.sleep(0.5)
	debugger.GetSelectedTarget().GetProcess().PutSTDIN(args[1]+'\n')
	time.sleep(0.5)
	debugger.HandleCommand("expression -- $rsi += 4")
	time.sleep(0.5)
	debugger.HandleCommand("process continue")
	time.sleep(0.5)
	debugger.GetSelectedTarget().GetProcess().PutSTDIN(args[2]+'\n')
	time.sleep(0.5)
	debugger.HandleCommand("expression -- count = 0")
	time.sleep(0.5)
	debugger.HandleCommand("process continue")
	time.sleep(0.5)
	debugger.HandleCommand("expression -- tmp = min[0] + min[1] + min[2]")
	time.sleep(0.5)
	debugger.HandleCommand("process continue")
	time.sleep(0.5)
	debugger.HandleCommand("expression -- biggest = ((min[0] >= min[1]) ? min[0] : (min[1] >= min[2] ? min[1] : min[2]))")
	time.sleep(0.5)
	debugger.HandleCommand("process continue")

def __lldb_init_module(debugger, internal_dict):
	debugger.HandleCommand('command script add -f auto.auto auto')

