# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 09:27:11 2016

@author: mansour
"""
import numpy as np
from numpy import linalg as LA

def node_med(coord, elem):
    # element half point - list
    coord_med = []
    normal = []
    # loop through elements
    for node1, node2, node3 in elem:
        # first node
        x1, y1, z1 = coord[node1]
    #    print(x1,y1)
        # second node
        x2, y2, z2 = coord[node2]
    #    print(x2,y2)
        # third node
        x3, y3, z3 = coord[node3]
        # font nodes
        coord_med.append([(x1 + x2 + x3)/3, (y1 + y2 + y3)/3, (z1 + z2 + z3)/3])    
        # print('element half points', node_med[line][0])    
        v1 = [x2 - x1, y2 - y1 , z2 - z1]
        v2 = [x3 - x2, y3 - y2 , z3 - z2]
        N = np.cross(v1, v2)
        normal.append(N/LA.norm(N))
    return coord_med, normal
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#def normal(node_font, node):
#    
#    xf, yf = node_font
#    x, y = node
#    # distance between the font point to the initial node and final node rad = [rx, ry]
#    # rad = (x - xd)i + (y - yd)j where (xd,yd) are the font node (nodes_med)
##    rad = [x-xf, y - yf]
#    # norm = rad/|rad|; norm = [nx, ny]
#    norm = [ (x - xf)/((x - xf)**2+(y - yf)**2)**0.5, (y - yf)/((x - xf)**2+(y - yf)**2)**0.5]
#
#    return norm
#        
#def length(nodes,nodes_bound_coord ):
#    # lengh elements
#    node1, node2 = nodes
#    # first node
#    x1, y1 = nodes_bound_coord[node1]
#    # print(x1,y1)
#    # second node
#    x2, y2 =nodes_bound_coord[node2]
#    # print(x2,y2)   
#    # lenght of the element between node1 and node2
#    length = np.sqrt((x2-x1)**2+(y2-y1)**2)
#    # print('element length', length)     
#    return length    
        

##  # radial vector - list
##    rad = []
##    # normal vector - list
##    norm = []
#
#    for node in node_med.values():
#        for xf, yf in node:
##            # temporary list
##            ltemp_rad = []
##            # temporary list
##            ltemp_norm = []
#        
#            for line, nodes in line_type.items():
#                 for node, _ in nodes:
#                     # first node
#                     x, y = nodes_bound_coord[node]
#                     # distance between the font point to the initial node and final node rad = [rx, ry]
#                     # rad = (x - xd)i + (y - yd)j where (xd,yd) are the font node (nodes_med)
#                     ltemp_rad.append([x-xf, y - yf]) 
#                     # norm = rad/|rad|; norm = [nx, ny]
#                     ltemp_norm.append([ (x-xf)/((x-xf)**2+(y - yf)**2)**0.5, (y-yf)/((x-xf)**2+(y - yf)**2)**0.5])
#                 #end for node, _ in nodes:
#                     
#            rad.append(ltemp_rad)
#            norm.append(ltemp_norm)
#            # end  for line, nodes in line_type.items():
#        # end for xf, yf in elem:
#    # end for elem in node_med.values():
#    return rad, norm
#        

#          # rad = (x - xd)i + (y - yd)j where (xd,yd) are the font node (nodes_med)
#            rad.append([x2 - node_med[line][0][0], y2 - node_med[line][0][1]])
#            print('rad', rad)
#          # norm = rad/|rad|; norm = [nx, ny]
#            norm.append([rad[0][0]/np.sqrt(rad[0][0]**2+rad[0][1]**2),rad[0][1]/np.sqrt(rad[0][0]**2+rad[0][1]**2)])
#          
    

            
    #        # rx*nx + ry*ny
    #        d = rad[0][0]*norm[0][0] + rad[0][1]*norm[0][1]
    #        # -rx*ny + ry*nx node 1
    #        t1 = -rad[0][0]*norm[0][1] + rad[0][1]*norm[0][0]
    #        # -rx*ny + ry*nx node 2
    #        t2 = -rad[1][0]*norm[0][1] + rad[1][1]*norm[0][0]
    #        print(d,t1,t2)  
    #        dtheta = np.tan(d*length)   
    