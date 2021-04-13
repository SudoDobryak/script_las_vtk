#!/usr/bin/env python

import vtk
import numpy as np
from laspy.file import File
inFile = File("Avrora_Part.las", mode = "r")

# Количество точек
POINT_COUNT = 900000
# Размер точек
POINT_SIZE = 1

coords = np.vstack((inFile.x, inFile.y, inFile.z)).transpose()

print(coords[1000][0])
# Create the geometry of a point (the coordinate)
points = vtk.vtkPoints()

# Create the topology of the point (a vertex)
vertices = vtk.vtkCellArray()


#setup colors
Colors = vtk.vtkUnsignedCharArray()
Colors.SetNumberOfComponents(3)
Colors.SetName("Colors")

for k in range(POINT_COUNT):
    id = points.InsertNextPoint([coords[k][0], coords[k][1], coords[k][2]])
    vertices.InsertNextCell(1)
    vertices.InsertCellPoint(id)
    Colors.InsertNextTuple3(255, 255, 0)

# Create a polydata object
point = vtk.vtkPolyData()

# Set the points and vertices we created as the geometry and topology of the polydata
point.SetPoints(points)
point.SetVerts(vertices)
point.GetPointData().SetScalars(Colors)
# Visualize
mapper = vtk.vtkPolyDataMapper()
if vtk.VTK_MAJOR_VERSION <= 5:
    mapper.SetInput(point)
else:
    mapper.SetInputData(point)

actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.GetProperty().SetPointSize(POINT_SIZE)


renderer = vtk.vtkRenderer()
renderer.SetBackground(.1, .2, .3)
renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)
renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)

interactorStyle = vtk.vtkInteractorStyleFlight()

renderer.AddActor(actor)
interactorStyle.StartForwardFly()
renderWindow.Render()

renderWindowInteractor.Start()