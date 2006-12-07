# automatically generated by generate_docs.py.
doc="""Attributes supported by this class are:
plots(type:list) default="Used only internally by pychart.".
loc(type:(x,y)) default="The location of the bottom-left corner of the chart.
@cindex chart location
@cindex location, chart
".
y_grid_style(type:line_style.T) default="The style of vertical grid lines.".
y_grid_interval(type:Number or function) default="The vertical grid-line interval. See also x_grid_interval".
x_grid_over_plot(type:int) default="If True, grid lines are drawn over plots. Otherwise, plots are drawn over grid lines.".
x_range(type:(x,y)) default="Specifies the range of X values that are displayed in the
    chart. IF the value is None, both the values are computed
    automatically from the samples.  Otherwise, the value must be a
    tuple of format (MIN, MAX). MIN and MAX must be either None or a
    number. If None, the value is computed automatically from the
    samples. For example, if x_range = (None,5), then the minimum X
    value is computed automatically, but the maximum X value is fixed
    at 5.".
y_coord(type:coord.T) default="Set the Y coordinate system.".
    A linear coordinate system.
    
y_range(type:(x,y)) default="Specifies the range of Y values that are displayed in the
    chart. IF the value is None, both the values are computed
    automatically from the samples.  Otherwise, the value must be a
    tuple of format (MIN, MAX). MIN and MAX must be either None or a
    number. If None, the value is computed automatically from the
    samples. For example, if y_range = (None,5), then the minimum Y
    value is computed automatically, but the maximum Y value is fixed
    at 5.".
x_axis(type:axis.X) default="The X axis. <<axis>>.".
bg_style(type:fill_style.T) default="Background fill-pattern.".
x_coord(type:coord.T) default="Set the X coordinate system.".
    A linear coordinate system.
    
legend(type:legend.T) default="The legend of the chart.".
    a legend is by default displayed in the right-center of the
    chart.
    
y_grid_over_plot(type:int) default="See x_grid_over_plot.".
x_axis2(type:axis.X) default="The second X axis. This axis should be non-None either when you want to display plots with two distinct domains or when
    you just want to display two axes at the top and bottom of the chart.
    <<axis>>".
y_axis2(type:axis.Y) default="The second Y axis. This axis should be non-None either when you want to display plots with two distinct ranges or when
                you just want to display two axes at the left and right of the chart. <<axis>>".
x_grid_style(type:line_style.T) default="The style of horizontal grid lines.
@cindex grid lines".
y_axis(type:axis.Y) default="The Y axis. <<axis>>.".
border_line_style(type:line_style.T) default="Line style of the outer frame of the chart.".
x_grid_interval(type:Number or function) default="The horizontal grid-line interval.
                        A numeric value
                        specifies the interval at which
                        lines are drawn. If value is a function, it
                        takes two arguments, (MIN, MAX), that tells
                        the minimum and maximum values found in the
                        sample data. The function should return a list
                        of values at which lines are drawn.".
size(type:(x,y)) default="The size of the chart-drawing area, excluding axis labels,
              legends, tick marks, etc.
@cindex chart size
@cindex size, chart              
              ".
"""

