from concurrent.futures import ThreadPoolExecutor,as_completed

def function_thread(iii):
	print '===='

with ThreadPoolExecutor(max_workers=8) as executer:
	all_task = [executer.submit(function_thread, (each_store)) for each_store in store_objs]
	for future in as_completed(all_task):
		data = future.result()
		print("in main: get page {}s success".format(data))


