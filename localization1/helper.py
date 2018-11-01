import io

def show(robotmap, beliefs):
	buf1 = io.StringIO()
	print("     Map:", end='', file=buf1)
	print(*(map('{0[1]:^7.2}'.format, enumerate(robotmap))), sep="|", end='', file=buf1)
	s1 = buf1.getvalue()
	len1 = len(s1)

	buf2 = io.StringIO()
	print("Position:", end='', file=buf2)
	print(*(map('{0[1]:^7.2}'.format, enumerate(beliefs))), sep="|", end='', file=buf2)
	s2 = buf2.getvalue()
	len2 = len(s2)
	
	print('-'*max(len1, len2))
	print(s1)
	print(s2)
	print('-'*max(len1, len2))
    
def shift_list(l, n):
	from collections import deque
	d = deque(l)
	d.rotate(1)
	return list(d)

def show_diagram(robotmap, beliefs):
    import matplotlib.pyplot as plt
    import numpy as np
    
    assert len(robotmap) == len(beliefs)
    x_labels = []
    x_indices = []
    for index, cellcolor in enumerate(robotmap):
        x_labels.append(str(index+1) + ' - ' + cellcolor)
        x_indices.append(index)
    plt.xlabel('Position - Cell color')
    plt.ylabel('Probability')
    plt.title("Probability of Robot's Position")
    plt.bar(x_labels, beliefs, width=0.7, edgecolor='black')
    plt.xticks(np.arange(min(x_indices), max(x_indices)+1, 1))
    plt.show()
