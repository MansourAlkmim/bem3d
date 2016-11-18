# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 19:04:56 2016
create the input file of the .exe 
@author: mansour
"""
def preprocessing(elem, coord, elem_bc, title):
    num_elem = len(elem)
    num_nodes = len(coord)
    pt_int = 0
    alpha=1;
    beta=-1;
    
    fid = open('input.dat', 'w')
    fid.write(title)
    fid.write('%d   %d   %d\n' % (num_elem, num_nodes, pt_int))
    fid.write('%10.6e  %10.6e\n' % (alpha, beta))
    fid.write('#Nodes:\n')
    for i, node_coord in enumerate(coord):
        fid.write(' %d     %20.12e     %20.12e  %20.12e  \n' % (i+1, node_coord[0], node_coord[1], node_coord[2]))
    
    fid.write('#Elements:\n')
    for i, node_elem in enumerate(elem):
        fid.write(' %d     %d    %d     %d  %d  %20.12e \n' % (i+1, node_elem[0], node_elem[1], node_elem[2], elem_bc[i][0]+1, elem_bc[i][1]))
        
    fid.close

def postprocessing():
     with open('output.dat', 'r') as output_file:
         data = [line.split() for line in output_file]
         output_data = {col[1]:list(col[2:]) for col in zip(*data)}
         # list to float
         Node = [float(x) for x in output_data['Node']]
         Potential = [float(x) for x in output_data['Potential']]  
         Normal = [float(x) for x in output_data['Normal']]  
                      
         return Node, Potential, Normal            

def add_to_msh(tag, title):
    with open(title +'.msh') as f:
        with open(title +'_output.msh', "w") as fid:
            for line in f:
                fid.write(line)
            fid.write('\n') 
    for data, var in tag:
        fid = open(title +'_output.msh', 'a')   
        fid.write('$ElementData\n')
        fid.write('1                      string tag:\n')
        fid.write('"%s"          the name of the view \n' % (var))
        fid.write('1                      one real tag:\n')
        fid.write('0.0                      the time value (0.0)\n')    
        fid.write('3                      integer tags:\n')
        fid.write('0                        the time step (0; time steps always start at 0)\n')
        fid.write('1                        1-component (scalar) field\n')
        fid.write('%d                        associated nodal values\n' % (len(data)) )
        for i, paramenter in enumerate(data):
            fid.write('%d %10.6e\n' % (i+1, paramenter))
        fid.write('$EndElementData\n')
    
#    for i, node_coord in enumerate(coord):
#        fid.write('%d %20.12e %20.12e %20.12e %20.12e\n' % (i+1, node_coord[0], node_coord[1], node_coord[2], var[i]))