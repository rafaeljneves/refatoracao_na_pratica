# test_donut.py



def donuts(count):	
	if count >=10:
		qtd = 'many'
	else:
		qtd = str(count)
	return 'Number of donuts: ' + qtd


def test_donuts():	
	assert donuts(1) == 'Number of donuts: 1'
	assert donuts(4) == 'Number of donuts: 4'
	assert donuts(10) == 'Number of donuts: many'
	assert donuts(90) == 'Number of donuts: many'

