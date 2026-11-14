"""Build three code-native schematic SVGs. These are not application screenshots."""
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'phase-0-foundations/M01-data-and-variables/figures'

def text(x, y, value, size=18, fill='#172b43', bold=False):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" font-weight="{700 if bold else 400}">{escape(value)}</text>'

def panel(x, y, width, height, title):
    return (f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="12" fill="white" stroke="#b9c9da"/>'
            f'<path d="M {x+12} {y} H {x+width-12} Q {x+width} {y} {x+width} {y+12} V {y+48} H {x} V {y+12} Q {x} {y} {x+12} {y}" fill="#183b60"/>'
            + text(x+18, y+31, title,18,'white',True))

def grid(x,y,headers,rows,widths):
    parts=[]; height=38
    for rownum,row in enumerate([headers]+rows):
        left=x
        for colnum,cell in enumerate(row):
            parts.append(f'<rect x="{left}" y="{y+rownum*height}" width="{widths[colnum]}" height="{height}" fill="{("#e4eef8" if rownum==0 else "#fff")}" stroke="#bdcbd9"/>')
            parts.append(text(left+9,y+rownum*height+25,str(cell),16,bold=rownum==0)); left+=widths[colnum]
    return ''.join(parts)

def build():
    OUT.mkdir(exist_ok=True)
    configs={
        'excel-first-steps':('Excel: enter a table, then import CSV',
          [('1. Blank workbook',grid(45,135,['','A','B','C'],[['1','patient_id','age','temperature'],['2','1','24','36.8'],['3','2','51','37.2'],['4','3','38','38.1']],[35,125,75,155])+text(45,365,'B3 = age of patient 2 = 51',17)+text(45,400,'Select A1:C4 > Insert > Table',17)),
           ('2. Import an existing CSV',text(545,145,'Data > From Text/CSV',20,bold=True)+text(545,195,'File: M01_first_steps.csv',17)+text(545,240,'Delimiter: Comma',17)+grid(545,270,['patient_id','age','temperature'],[['1','24','36.8'],['2','51','37.2'],['3','38','38.1']],[120,70,165])+text(545,455,'Preview 3 columns > Load',17))]),
        'spss-first-steps':('SPSS: define columns, then enter people',
          [('1. Variable View',grid(45,135,['Name','Decimals','Measure'],[['patient_id','0','Nominal'],['age','0','Scale'],['temperature','1','Scale']],[170,105,115])+text(45,340,'Each row defines one data column.',16)+text(45,385,'Type = Numeric for these 3 columns.',16)),
           ('2. Data View',grid(545,135,['patient_id','age','temperature'],[['1','24','36.8'],['2','51','37.2'],['3','38','38.1']],[120,70,165])+text(545,340,'Each row now describes one person.',16)+text(545,385,'File > Save As > my_first_table.sav',16))]),
        'prism-first-steps':('Prism: choose Column, then enter temperatures',
          [('1. New Table & Graph',text(45,145,'Column',24,bold=True)+text(45,195,'Enter replicate values,',18)+text(45,225,'stacked into columns',18)+text(45,295,'Create',22,bold=True)+text(45,365,'Here, each row is a different person.',16)+text(45,400,'No statistical test in this step.',16)),
           ('2. Column data table',grid(545,135,['Row titles','Temperature (C)'],[['P1','36.8'],['P2','37.2'],['P3','38.1']],[130,225])+text(545,340,'Paste only Excel cells C2:C4.',16)+text(545,385,'Keep age in the original workbook.',16)+text(545,430,'File > Save As',17))])
    }
    for filename,(title,panels) in configs.items():
        parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="560" viewBox="0 0 1000 560" role="img" aria-labelledby="title desc">',
               f'<title id="title">{escape(title)}</title>',
               '<desc id="desc">Two schematic panels show the data-entry steps. Not a screenshot. Read the accompanying Persian guide for full steps.</desc>',
               '<rect width="1000" height="560" fill="#f3f7fc"/>',
               '<g font-family="DejaVu Sans, Arial, sans-serif">',text(25,40,title,23,bold=True)]
        for x,(heading,body) in zip([25,525],panels): parts += [panel(x,65,450,430,heading),body]
        parts += [text(25,535,'SCHEMATIC ONLY - menu positions vary by version.',16,fill='#50677f'),'</g></svg>']
        (OUT/f'{filename}.svg').write_text(''.join(parts),encoding='utf-8')



def render_png():
    """Render the SVG source with local librsvg/cairo for Markdown readers."""
    import ctypes as C
    from ctypes.util import find_library
    rsvg = C.CDLL(find_library('rsvg-2'))
    cairo = C.CDLL('/lib/x86_64-linux-gnu/libcairo.so.2')
    gobject = C.CDLL(find_library('gobject-2.0'))
    rsvg.rsvg_handle_new_from_file.argtypes = [C.c_char_p, C.c_void_p]
    rsvg.rsvg_handle_new_from_file.restype = C.c_void_p
    rsvg.rsvg_handle_render_cairo.argtypes = [C.c_void_p, C.c_void_p]
    rsvg.rsvg_handle_render_cairo.restype = C.c_int
    cairo.cairo_image_surface_create.argtypes = [C.c_int, C.c_int, C.c_int]
    cairo.cairo_image_surface_create.restype = C.c_void_p
    cairo.cairo_create.argtypes = [C.c_void_p]
    cairo.cairo_create.restype = C.c_void_p
    cairo.cairo_scale.argtypes = [C.c_void_p, C.c_double, C.c_double]
    cairo.cairo_surface_write_to_png.argtypes = [C.c_void_p, C.c_char_p]
    cairo.cairo_surface_write_to_png.restype = C.c_int
    cairo.cairo_destroy.argtypes = [C.c_void_p]
    cairo.cairo_surface_destroy.argtypes = [C.c_void_p]
    gobject.g_object_unref.argtypes = [C.c_void_p]
    for svg in OUT.glob('*.svg'):
        handle = rsvg.rsvg_handle_new_from_file(str(svg).encode(), None)
        if not handle: raise RuntimeError(f'Cannot load {svg}')
        surface = cairo.cairo_image_surface_create(0, 2000, 1120)
        context = cairo.cairo_create(surface)
        try:
            cairo.cairo_scale(context, 2.0, 2.0)
            if not rsvg.rsvg_handle_render_cairo(handle, context):
                raise RuntimeError(f'Cannot render {svg}')
            if cairo.cairo_surface_write_to_png(surface, str(svg.with_suffix('.png')).encode()) != 0:
                raise RuntimeError(f'Cannot save {svg}')
        finally:
            cairo.cairo_destroy(context)
            cairo.cairo_surface_destroy(surface)
            gobject.g_object_unref(handle)


if __name__ == '__main__':
    build()
    render_png()
