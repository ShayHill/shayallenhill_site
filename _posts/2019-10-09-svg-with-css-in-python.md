---
layout: post

title: "SVG (with CSS) in Python"

date: 2019-10-09 12:28:21 -0500

tags:

categories: [programming]

author: Shay Hill

excerpt: It is straightforward and practical to create SVG graphics with Python.

post_image: "/assets/img/blog/svg-with-css-in-python/knot.png"
---

It’s easy to make this WAY harder than it has to be. Though it is straightforward and practical to create SVG graphics with Python, lxml is a little under documented, so it can be frustrating to get started.

The remainder of the article is split into four parts:

1. [Create SVG geometry in Python with the least possible friction ](#svg-geometry)(the straightforward part).
2. [Write the SVG geometry out to a file](#file-format) (the part you’ve been scouring the Net for).
3. [Enough lxml to get you started ](#etree)(it doesn’t take much to create an svg).
4. [Documentation for svg\_ultralight](#in-context) (my Python module to save 99% of the guesswork).

<div class="anchor" id="svg-geometry"></div>

# 1. SVG geometry in Python with the least possible friction

## First, you’ll need a “root” svg element

(You’ll have to install lxml to use most of the code here.)

~~~python
from lxml import etree

my_root_element = etree.Element(
    "svg", width=640, height=480, xmlns="http://www.w3.org/2000/svg"
)
~~~

## Add some geometry–the easy way

Lxml will translate Python-style keywords to valid xml. Here’s a nice shortcut for creating an xml/svg element.

~~~python
# let's draw a rectangle
my_rectangle = etree.Element(
    # the svg element type
    "rect",
    # any svg parameters that happen to be valid
    # Python attribute names
    x="13",
    y="14",
    width="500",
    height="200",
    rx="50",
    ry="100",
    stroke="blue",
)
~~~

So far, so good. But if you want to use CSS, you can pretty much guarantee one SVG parameter that *will not* be a valid Python attribute name (“class”). SVG also uses a lot of “this-that” names (Python of course reads “this-that” as “this minus that”). Here’s how you can deal with those.

~~~python
my_rectangle.set("class", "some-css-class")
my_rectangle.set("stroke-width", "10")
~~~

## Add some geometry–the easier way

SVG is it’s own language, and presumably you’re not trying to code SVG *through* Python unless you know both SVG and Python.

Why bother learning some pidgin wrapper between the two? Just code in SVG. Where you need to parameterize, use fstrings.

~~~python
my_rectangle = et.fromstring(
    f'<rect class="some-css-class" x="13" y="14" width="500" height="{height}" />'
)
~~~

## Add the element to your root

That’s easy too. Add the element to your SVG root element like this.

~~~python
my_root_element.append(my_rectangle)
~~~

<div class="anchor" id="file-format"></div>

# 2. Write the SVG geometry out to a file

This is where is starts to get a bit harder to guess your way through. You need to end up with an XML file that looks like this (importing a CSS stylesheet).

~~~xml
<?xml version='1.0' encoding='ASCII'?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<?xml-stylesheet href="path_to.css" type="text/css"?>
<svg width="640" height="480" xmlns="http://www.w3.org/2000/svg">
    <!-- some svg geometry -->
</svg>
~~~

… or this (CSS in a style block)

~~~xml
<?xml version='1.0' encoding='ASCII'?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg width="640" height="480" xmlns="http://www.w3.org/2000/svg">
    <style type="text/css"><![CDATA[ /** some CSS **/ ]]></style>
    <!-- some svg geometry -->
</svg>
~~~

Depending on your workflow, you may need to switch back and forth between these formats. Definitely keep your CSS in a separate file: you’ll most likely be editing your CSS long after you have your geometry worked out, and you can benefit from CSS syntax highlighting in your editor.

That being said, you may need to place your CSS and SVG in one file if you’d like to convert your SVG to other image formats with e.g. Gimp.

## Let’s start with the external CSS file

~~~xml
<?xml-stylesheet href="path_to.css" type="text/css"?>
~~~

The CSS stylesheet link is a “processing instruction” that exists outside your root element. Create it with

~~~python
my_root_element.addprevious(
    et.PI("xml-stylesheet", f'href="{path_to_css_file}" type="text/css"')
)
~~~

Then make sure it gets written to file by wrapping your root element in an ElementTree.

~~~python
# more context on this below

etree.tostring(etree.ElementTree(my_root_element))


~~~

## Alternately, you can create and insert a CSS style block

~~~xml
<style type="text/css"><![CDATA[ /** some CSS **/ ]]></style>
~~~

~~~python
style = etree.Element("style", type="text/css")
style.text = etree.CDATA("/** some CSS **/")
my_root_element.insert(0, style)
~~~

## Other SVG Context

You will also need

* an XML declaration
* an SVG doctype

~~~xml
<?xml version='1.0' encoding='ASCII'?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
~~~

Handle these with etree.tostring arguments.

~~~python
file_object.write(
    etree.tostring(
        etree.ElementTree(my_root_element),
        xml_declaration=True,
        doctype=(
            '<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"n'
            + '"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">'
        ),
    )
)
~~~

Those are all the sticking points. Here’s …

<div class="anchor" id="etree"></div>

# 3. Enough lxml to Get You Started

An xml element has three parts: a tag, some attributes, and (if a text object) some text.

~~~python
<tag attribute="string value"/>
# or
<tag attribute="string value">text</tag>
~~~

You know them already from svg. Here’s how to set and get them in the lxlm library.

Set the tag

~~~python
my_elem = etree.Element("tag")
# or
my_elem = etree.fromstring("<tag />")
# or
my_elem.tag = "tag"
~~~

get the tag

~~~python
print(my_elem.tag)
~~~

set an attribute

~~~python
my_elem = etree.Element("tag", attribute="always a string")
# or
my_elem = etree.fromstring('<tag attribute="always a string"/>')
# or
my_elem.set("attribute", "always a string")
# or
my_elem.attrib["attribute"] = "always a string"
~~~

set a namespace attribute

~~~python
my_elem.set(etree.QName("http://www.w3.org/1999/xlink", "href"), "value")
# with svg_ultralight
my_elem.set(etree.QName(NSMAP["xlink"], "href"), "value")
~~~

get an attribute

~~~python
print(my_elem.attrib["attribute"])
~~~

set text

~~~python
my_elem.text = "some text"
~~~

get text

~~~python
print(my_elem.text)
~~~

An svg file will have one parent defining the viewing area and multiple children (paths, text, etc.). To add children

~~~python
my_parent.append(my_child)
# or
my_parent.extend([child_1, child_2])
# or
my_parent.insert(0, child_0)
~~~

get children

~~~python
print(tuple(my_parent))
# or
print(my_parent[0])
~~~

<div class="anchor" id="in-context"></div>

# 4. Documentation for svg\_ultralight

To save the trouble of referencing this post every project, I’ve put the once-per-file, hard-to-remember details into a [Python module](https://github.com/ShayHill/svg_writer). Install with

~~~ powershell
pip install svg_ultralight
~~~

## svg\_ultralight

The most straightforward way to create SVG files with Python.

### Four principal functions

~~~ python
from svg_ultralight import new_svg_root, write_svg, write_png_from_svg, write_png
~~~

### One convenience

~~~ python
from svg_ultralight import NSMAP
~~~

### new\_svg\_root

~~~ python
x_: Optional[float],
y_: Optional[float],
width_: Optional[float],
height_: Optional[float],
pad_: float = 0
dpu_: float = 1
nsmap: Optional[Dict[str, str]] = None (svg_ultralight.NSMAP if None)
**attributes: Union[float, str],
-> etree.Element
~~~

Create an svg root element from viewBox style arguments and provide the necessary svg-specific attributes and namespaces. This is your window onto the scene.

Three ways to call:

1. The trailing-underscore arguments are the same you’d use to create a `rect` element (plus `pad_` and `dpu_`).
2. `new_svg_root` will infer `viewBox`, `width`, and `height` svg attributes from these values.
3. Use the svg attributes you already know: `viewBox`, `width`, `height`, etc. These will be written to the xml file.

Of course, you can combine 1. and 2. if you know what you’re doing.

See `namespaces` below.

* `x_`: x value in upper-left corner
* `y_`: y value in upper-left corner
* `width_`: width of viewBox
* `height_`: height of viewBox
* `pad_`: the one small convenience I’ve provided. Optionally increase viewBox by `pad` in all directions.
* `dpu_`: pixels per viewBox unit for output png images.
* `nsmap`: namespaces. (defaults to svg\_ultralight.NSMAP). Available as an argument should you wish to add additional namespaces. To do this, add items to NSMAP then call with `nsmap=NSMAP`.
* `**attributes`: the trailing-underscore arguments are an *optional* shortcut for creating a scene. The entire svg interface is available to you through kwargs. See `A few helpers` below for details on attribute-name translation between Python and xml (the short version: `this_name` becomes `this-name` and `this_` becomes `this`)

### namespaces (svg\_ultralight.NSMAP)

`new_svg_root` will create a root with several available namespaces.

* `"dc": "http://purl.org/dc/elements/1.1/"`
* `"cc": "http://creativecommons.org/ns#"`
* `"rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#"`
* `"svg": "http://www.w3.org/2000/svg"`
* `"xlink": "http://www.w3.org/1999/xlink"`
* `"sodipodi": "http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"`
* `"inkscape": "http://www.inkscape.org/namespaces/inkscape"`

I have made these available to you as `svg_ultralight.NSMAP`

### write\_svg

~~~ python
svg: str,
xml: etree.Element,
stylesheet: Optional[str] = None,
do_link_css: bool = False,
**tostring_kwargs,
-> str:
~~~

Write an xml element as an svg file. This will link or inline your css code and insert the necessary declaration, doctype, and processing instructions.

* `svg`: path to output file (include extension .svg)
* `param xml`: root node of your svg geometry (created by `new_svg_root`)
* `stylesheet`: optional path to a css stylesheet
* `do_link_css`: link to stylesheet, else (default) write contents of stylesheet into svg (ignored if `stylesheet` is None). If you have a stylesheet somewhere, the default action is to dump the entire contents into your svg file. Linking to the stylesheet is more elegant, but inlining *always* works.
* `**tostring_kwargs`: optional kwarg arguments for `lxml.etree.tostring`. Passing `xml_declaration=True` by itself will create an xml declaration with encoding set to UTF-8 and an svg DOCTYPE. These defaults can be overridden with keyword arguments `encoding` and `doctype`. If you don’t know what this is, you can probably get away without it.
* `returns`: for convenience, returns svg filename (`svg`)
* `effects`: creates svg file at `svg`

### write\_png\_from\_svg

~~~ python
inkscape_exe: str,
svg: str
png: Optional[str]
-> str
~~~

Convert an svg file to a png. Python does not have a library for this. That has an upside, as any library would be one more set of svg implementation idiosyncrasies we’d have to deal with. Inkscape will convert the file. This function provides the necessary command-line arguments.

* `inkscape_exe`: path to inkscape.exe
* `svg`: path to svg file
* `png`: optional path to png output (if not given, png name will be inferred from `svg`: `'name.svg'` becomes `'name.png'`)
* `return`: png filename
* `effects`: creates png file at `png` (or infers png path and filename from `svg`)

### write\_png

~~~ python
inkscape_exe: str,
png: str,
xml: etree.Element,
stylesheet: Optional[str] = None
-> str
~~~

Create a png without writing an initial svg to your filesystem. This is not faster (it may be slightly slower), but it may be important when writing many images (animation frames) to your filesystem.

* `inkscape_exe`: path to inkscape.exe
* `png`: path to output file (include extension .png)
* `param xml`: root node of your svg geometry (created by `new_svg_root`)
* `stylesheet`: optional path to a css stylesheet
* `returns`: for convenience, returns png filename (`png`)
* `effects`: creates png file at `png`

## A few helpers

~~~ python
from svg_ultralight.constructors import new_element, new_sub_element
~~~

I do want to keep this ultralight and avoid creating some pseudo scripting language between Python and lxml, but here are two very simple, very optional functions to save your having to `str()` every argument to `etree.Element`.

### constructors.new\_element

~~~ python
tag: str
**params: Union[str, float]
-> etree.Element
~~~

Python allows underscores in variable names; xml uses dashes.

Python understands numbers; xml wants strings.

This is a convenience function to swap `"_"` for `"-"` and `10.2` for `"10.2"` before creating an xml element.

Translates numbers to strings

~~~ python
>>> elem = new_element('line', x1=0, y1=0, x2=5, y2=5)
>>> etree.tostring(elem)
b'<line x1="0" y1="0" x2="5" y2="5"/>'
~~~

Translates underscores to hyphens

~~~ python
>>> elem = new_element('line', stroke_width=1)
>>> etree.tostring(elem)
b'<line stroke-width="1"/>'
~~~

Removes trailing underscores. You’ll almost certainly want to use reserved names like `class` as svg parameters. This can be done by passing the name with a trailing underscore.

~~~ python
>>> elem = new_element('line', class_='thick_line')
>>> etree.tostring(elem)
b'<line class="thick_line"/>'
~~~

Special handling for a ‘text’ argument. Places value between element tags.

~~~ python
>>> elem = new_element('text', text='please star my project')
>>> etree.tostring(elem)
b'<text>please star my project</text>'
~~~

### constructors.new\_sub\_element

~~~ python
parent: etree.Element
tag: str
**params: Union[str, float]
-> etree.Element
~~~

As above, but creates a subelement.

~~~ python
>>> parent = etree.Element('g')
>>> _ = new_sub_element('rect')
>>> etree.tostring(parent)
b'<g><rect/></g>'
~~~

### update\_element and deepcopy\_element

These are two more ways to add params with the above-described name and type conversion. Again unnecessary, but potentially helpful. Easily understood from the code or docstrings.

## Two extras

### query.map\_ids\_to\_bounding\_boxes

Python cannot parse an svg file. Python can *create* an svg file, and Inkscape can parse (and inspect) it. Inkscape has a command-line interface capable of reading an svg file and returning some limited information. This is the only way I know for a Python program to:

* create an svg file (optionally without writing to filesystem)
* query the svg file for bounding-box information
* create an adjusted svg file.

This would be necessary for, e.g., algorithmically fitting text in a box.

~~~ powershell
from svg_ultralight.queries import map_ids_to_bounding_boxes
~~~

You can get a tiny bit more sophisticated with Inkscape bounding-box queries, but not much. This will give you pretty much all you can get out of it.

### animate.write\_gif

Create an animated gif from a sequence of png filenames. This is a Pillow one-liner, but it’s convenient for me to have it, so it might be convenient for you.

~~~ python
from svg_ultralight.animate import write_gif
~~~

I hope I saved you a lot of time. (Gif created with svg\_ultralight).

{% include image.html url="/assets/img/blog/svg-with-css-in-python/animation\_1\_000.gif" description="SVG created with Python and svg\_writer" %}
