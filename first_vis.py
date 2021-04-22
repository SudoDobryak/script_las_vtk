#!/usr/bin/env python

import vtk

from laspy.file import File
inFile = File("Avrora_Part.las", mode = "r")

# Количество точек
POINT_COUNT = 100
# Размер точек
POINT_SIZE = 5
# Обычный массив с точками
# pnt = []

# for k in range(POINT_COUNT):
#     pnt.append([inFile.x[k],inFile.y[k],inFile.z[k]])

# print(inFile.x[0],inFile.y[0],inFile.z[0])
# Create the geometry of a point (the coordinate)
points = vtk.vtkPoints()

# Create the topology of the point (a vertex)
vertices = vtk.vtkCellArray()

for k in range(POINT_COUNT):
    # id = points.InsertNextPoint(pnt[k])
    id = points.InsertNextPoint([inFile.x[k],inFile.y[k],inFile.z[k]])
    vertices.InsertNextCell(1)
    vertices.InsertCellPoint(id)

# Create a polydata object
point = vtk.vtkPolyData()

# Set the points and vertices we created as the geometry and topology of the polydata
point.SetPoints(points)
point.SetVerts(vertices)

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

camera = renderer.MakeCamera()
renderer.ResetCamera()
camera.SetPosition(13.55115266673536, -29.350476103164837, -1.3432727339253447)
camera.SetFocalPoint(43.55115266673536, -29.350476103164837, -1.3432727339253447)
renderer.SetActiveCamera(camera)

# camera.SetFocalPoint(0, 0, 0)

renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)
renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)
renderer.AddActor(actor)

# camera.SetViewUp(0, 0, 1)

renderWindow.Render()
renderWindowInteractor.Start()


