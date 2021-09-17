import	glob,	re
for	msg	in	glob.glob('/tmp/'.txt'):
	filter	=	open((msg),'r')
	data	=	filter.read()
	message	=	re.findall(r'	message	(.'?)	/message ', data,re.DOTALL)
	print	"File	%s contains %s"	& (str(msg),message)
	filter.close()

