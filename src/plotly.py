import plotly.graph_objects as go
import space
import numpy as np

def draw_graph(space_objects, steps, actuness = 1):
    fig = go.Figure()
    config = dict({'ScrollZoom' : True})
    values = []
    for i in range(len(space_objects)):
        values.append([])

    for i in range(steps):
        for i in range(len(space_objects)):
            space_objects[i].move(float(1.0/actuness))
            values[i].append(space_objects[i].pos)
        
        for i in range(len(space_objects)):
            forces = np.array([0.0, 0.0])
            for objs in space_objects:
                if not space_objects[i] == objs:
                    forces = forces + objs.grav(space_objects[i].pos)

            space_objects[i].accelerate(forces, float(1.0/actuness))

    for v in values:
        fig.add_trace(go.Scatter(x=[x[0] for x in v], y=[y[1] for y in v]))

    fig.show(config=config)

'''
actuness = 512
steps = 12800

space_objects = []
space_objects.append(space.space_object(1, np.array([0.0, 0.0]), np.array([0.0, -0.5])))
#space_objects.append(space.space_object(0.1, np.array([0.0, -1.0]), np.array([0.0, -0.5])))
space_objects.append(space.space_object(1, np.array([-1.0, 0.0]), np.array([0.0, 0.8])))

draw_graph(space_objects, steps, actuness)
'''
