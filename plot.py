from bokeh.plotting import figure

def first_plot():

    p = figure(plot_width=400, plot_height=400, responsive = True)
    p.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="navy", alpha=0.5)
    return p

def second_plot():

    p2 = figure(plot_width=400, plot_height=400, responsive = True)
    p2.square([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="olive", alpha=0.5)
    return p2
