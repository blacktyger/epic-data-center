import datetime

import pytz
from bokeh.models import ColumnDataSource, FactorRange, NumeralTickFormatter, LinearAxis, DatetimeTickFormatter, \
    HoverTool, LabelSet, SingleIntervalTicker, FixedTicker, AdaptiveTicker
from bokeh.models import CustomJS, ColumnDataSource, HoverTool, NumeralTickFormatter
from bokeh.models.ranges import Range1d
from bokeh.embed import components
from bokeh.plotting import figure
from math import pi
import numpy
from django.utils.timezone import make_aware
from pytz import NonExistentTimeError, AmbiguousTimeError


from bokeh.models import ColumnDataSource, NumeralTickFormatter, LinearAxis, \
    DatetimeTickFormatter, HoverTool, SingleIntervalTicker
from bokeh.models.ranges import Range1d
from bokeh.embed import components
from bokeh.plotting import figure
import pandas as pd
from math import pi
import numpy
import bokeh
print(bokeh.__version__)

def sort_by_date(time, days=1):
    now = datetime.datetime.now(datetime.timezone.utc)
    difference = now - make_aware(datetime.datetime.fromtimestamp(time))

    if difference.days < days:
        return True
    else:
        return False

#
def t_s(timestamp):
    """ Convert different timestamps to datetime object"""
    try:
        if len(str(timestamp)) == 13:
            time = datetime.datetime.fromtimestamp(int(timestamp) / 1000)
        elif len(str(timestamp)) == 10:
            time = datetime.datetime.fromtimestamp(int(timestamp))
        elif len(str(timestamp)) == 16:
            time = datetime.datetime.fromtimestamp(int(timestamp / 1000000))
        elif len(str(timestamp)) == 12:
            time = datetime.datetime.fromtimestamp(int(timestamp.split('.')[0]))

    except (NonExistentTimeError, AmbiguousTimeError):
        timezone = pytz.timezone('Europe/London')
        time = timezone.localize(time, is_dst=False)
        return time

    except UnboundLocalError as er:
        return timestamp


def vitex_price(data):
    df = pd.DataFrame(data)
    # x_start = [t_s(x) for x in df.t if sort_by_date(x, days=4)]
    df['t'] = [t_s(d) for d in df['t']]

    df['adj_v'] = df.v / 2

    source = ColumnDataSource(df)
    DTF = DatetimeTickFormatter()
    DTF.hours = ["%H:%M"]
    DTF.days = ["%d/%m"]
    DTF.months = ["%d/%m/%Y"]
    DTF.years = ["%d/%m/%Y"]

    w100 = 1 * 60 * 60 * 1000  # half day in ms
    TOOLS = "pan,box_zoom,reset,save,xwheel_zoom"

    # FIGURE
    p = figure(x_axis_type="datetime", tools=TOOLS, plot_height=200,
               sizing_mode='stretch_both')

    p.toolbar.active_drag = None
    p.background_fill_color = None
    p.border_fill_color = None
    p.outline_line_color = None
    p.yaxis.visible = False
    p.xgrid.visible = False
    p.ygrid.visible = False
    p.toolbar_location = None

    # X STUFF
    # try:
    #     p.x_range = Range1d(x_start[0], x_start[-1])
    # except IndexError:
    #     pass
    p.xaxis[0].formatter = DTF

    p.xaxis.major_label_orientation = pi / 4
    p.xaxis[0].major_label_text_color = "white"
    p.xaxis[0].major_tick_line_color = "white"
    p.xaxis[0].axis_line_color = "white"
    p.xaxis[0].axis_line_alpha = 0.5

    # Y STUFF
    p.add_layout(LinearAxis(), 'right')
    p.y_range = Range1d(float(min(df.c)) * 0.5,
                        float(max(df.c)) * 1.2)
    p.yaxis[1].formatter = NumeralTickFormatter(format="0.00000000")
    p.yaxis[1].ticker.desired_num_ticks = 5
    p.yaxis[1].major_label_text_color = "white"
    p.yaxis[1].axis_line_color = "white"
    p.yaxis[1].axis_line_alpha = 0.4
    p.yaxis[1].major_tick_line_color = "white"
    p.yaxis[1].minor_tick_line_color = "white"

    price = p.line('t', y='c', source=source, line_width=3, alpha=1, color="white")

    p.rect(x='t', y='adj_v', width=w100, y_range_name="volume",
           source=source, alpha=0.7, height='v', color='#8DF0FF')

    p.extra_y_ranges = {'volume': Range1d(-100, max(df.v) * 3)}

    p.y_range = Range1d(float(min(df.c)) * 0.5,
                        float(max(df.p)) * 1.2)
    p.yaxis[1].ticker = SingleIntervalTicker(interval=0.00000500, num_minor_ticks=1)

    price_hover = HoverTool(renderers=[price],
                            tooltips=[
                                ("Date: ", "@t{%y-%m-%d}"),
                                ("Time: ", "@t{%H:%M}"),
                                ("Price: ", "@c{0.0000000f}"),
                                ("", ""),
                                ("Volume: ", "@v{0} EPIC"),
                                ],
                            formatters={"@t": "datetime"},
                            mode='vline')
    p.add_tools(price_hover)

    script, chart = components(p)
    return [script, chart]


def candle_chart(data):
    df = pd.DataFrame(data.candles)
    df["date"] = pd.to_datetime(df["date"])
    # x_start = [datetime.datetime.fromtimestamp(x) for x in df.date if sort_by_date(x, days=3)]

    df['adj_v'] = df.volume / 2

    source = ColumnDataSource(df)
    inc = df.close > df.open
    source_inc = ColumnDataSource(ColumnDataSource.from_df(df.loc[inc]))
    dec = df.open > df.close
    source_dec = ColumnDataSource(ColumnDataSource.from_df(df.loc[dec]))

    DTF = DatetimeTickFormatter()
    DTF.hours = ["%H:%M"]
    DTF.days = ["%d/%m"]
    DTF.months = ["%d/%m/%Y"]
    DTF.years = ["%d/%m/%Y"]

    # NOTE: list of colors one for each candlestick
    # df['colors'] = viridis()

    w = 0.8 * 60 * 60 * 1000  # half day in
    w100 = 1 * 60 * 60 * 1000  # half day in ms

    TOOLS = "pan,box_zoom,reset,save,xwheel_zoom"

    # FIGURE
    p = figure(x_axis_type="datetime", tools=TOOLS, plot_height=200,
               sizing_mode='scale_width', active_scroll='xwheel_zoom')

    p.toolbar.active_drag = None

    p.segment('date', 'high', 'date', 'low', source=source_inc, line_color="lawngreen")
    p.segment('date', 'high', 'date', 'low', source=source_dec, line_color="tomato")
    green_candle = p.vbar('date', w, 'open', 'close', source=source_inc, fill_color="lawngreen", line_width=0)
    red_candle = p.vbar('date', w, 'open', 'close', source=source_dec, fill_color="tomato", line_width=0)

    p.background_fill_color = None
    p.border_fill_color = None
    p.outline_line_color = None
    p.yaxis.visible = False

    # X STUFF
    # try:
    #     p.x_range = Range1d(x_start[0], x_start[-1])
    # except IndexError:
    #     pass
    p.xaxis[0].formatter = DTF

    p.xaxis.major_label_orientation = pi / 4
    p.xaxis[0].major_label_text_color = "#B3B8C6"
    p.xaxis.axis_line_color = "#323032"
    p.xaxis.major_tick_line_color = "#323032"

    p.grid.grid_line_alpha = 0.5
    p.grid.grid_line_color = "#323032"

    # Y STUFF
    p.add_layout(LinearAxis(), 'right')
    p.y_range = Range1d(float(min(df.close)) * 0.5,
                        float(max(df.open)) * 1.2)
    p.yaxis[1].formatter = NumeralTickFormatter(format="0.00000000")
    p.yaxis[1].ticker.desired_num_ticks = 5

    # p.yaxis[1].ticker = float(df.last_price[0])
    # p.yaxis[1].ticker = SingleIntervalTicker(interval=0.000005)
    # p.yaxis[1].ticker = FixedTicker(ticks=[last_price])

    p.yaxis[1].major_label_text_color = "gold"
    # p.yaxis[1].axis_label_text_color = "white"
    # p.yaxis[1].axis_label_text_font_style = "bold"
    # p.yaxis[1].axis_label = "Price in Bitcoin"
    p.yaxis[1].axis_line_color = "#323032"
    p.yaxis[1].major_tick_line_color = "#323032"
    p.yaxis[1].minor_tick_line_color = "#323032"

    p.line(df.date, y=float(data.price['btc']), line_width=2,
           alpha=0.7, color="gold", line_dash='dashed')

    # Y1 STUFF
    p.extra_y_ranges = {'volume': Range1d(-100, max(df.volume) * 3)}

    # p.add_layout(LinearAxis(y_range_name="volume"), place='left')
    p.y_range = Range1d(float(min(df.close)) * 0.5,
                        float(max(df.open)) * 1.2)
    # p.yaxis[1].ticker = SingleIntervalTicker(interval=500,
    #                                          num_minor_ticks=2)
    # p.yaxis[1].bounds = (0, 0)
    # p.yaxis[1].formatter = NumeralTickFormatter(format="0a")
    # df.v = df.v / 2
    # p.yaxis[1].ranges = Range1d(0, max(df.v))
    # p.yaxis[1].major_label_text_color = "#0AADC6"
    # p.yaxis[1].axis_label_text_color = "#0AADC6"
    # p.yaxis[1].axis_label_text_font_style = "bold"

    p.rect(x='date', y='adj_v', width=w100, y_range_name="volume",
           source=source, alpha=0.5, height='volume')

    p.line(df.date, y=numpy.mean(df.volume), y_range_name="volume", line_width=2,
           alpha=0.3, color="grey")

    # p.add_layout(LinearAxis(), 'right')
    # p.y_range = Range1d(float(min(df.c)) * 0.6,
    #                     float(max(df.p)) * 1.1)
    # p.yaxis[3].formatter = NumeralTickFormatter(format="0.00000000")
    # p.yaxis[3].ticker = FixedTicker(ticks=[last_price])
    # p.yaxis[3].major_label_text_color = "green"
    # p.yaxis[3].major_label_text_font_size = "13px"
    # p.yaxis[3].major_label_text_font_style = "bold"
    # p.yaxis[3].major_label_standoff = -5
    #
    # p.yaxis[3].axis_line_color = None
    # p.yaxis[3].major_tick_line_color = None
    # p.yaxis[3].minor_tick_line_color = None

    price_hover = HoverTool(renderers=[red_candle, green_candle],
                            tooltips=[
                                ("Date: ", "@t{%y-%m-%d}"),
                                ("Time: ", "@t{%H:%M}"),
                                ("Open: ", "@p{0.0000000f}"),
                                ("Close: ", "@c{0.0000000f}"),
                                ("High: ", "@h{0.0000000f}"),
                                ("Low: ", "@l{0.0000000f}"),
                                ("", ""),
                                ("Volume: ", "@v{0} EPIC"),


                                ],
                            formatters={"@t": "datetime"},
                            mode='vline')
    p.add_tools(price_hover)

    script, chart = components(p)
    return [script, chart]
