# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 22:29:08 2016
example of 3d bem program using the c++ solver
@author: mansour

 
require normals pointing outward. Gmsh can switch the normals. (see tutorial)
"""
import subprocess  
from mesh import Mesh
import boundary
import create

#name of the file
file = 'placa';
#boundary condition 0:temp 1:flux, not define is zero flux [1, 0] where [type, value]
surf_bc={4:[0,50],2:[1,-20]}

mymesh = Mesh() #criou objeto: instanciou a classe
#chamei o metodo do objeto
mymesh.read_msh(file + '.msh')
coord = mymesh.Verts
#get only the triangular elements [[physid],[nodes]] physid is the surf of the elem

#num_triangular = len(mymesh.Elmts[1][1]) + len(mymesh.Elmts[15][1])
elem = mymesh.Elmts[2][1]
surf = mymesh.Elmts[2][0]

#calculate the mean node and normal
#coord_med, normal = geometry.node_med(coord, elem)

# apply boundary condition
elem_bc = boundary.elem(surf_bc, surf, elem)

# run .exe
title = file + '\n'
create.preprocessing(elem, coord, elem_bc, title)
subprocess.call(['3D_Potential_CHBIE_FMM_64.exe'])

# read output.dat file and extract temperature and heat flux
[node, T, q] = create.postprocessing()

#write it back in the .msh file
create.add_to_msh([[T, 'temperature'],[q,'heat flux']],file)
#open gmsh
#NEED TO CHANGE DIRECTORY OF GMSH.EXE
subprocess.Popen(['gmsh', file+'_output.msh'])
