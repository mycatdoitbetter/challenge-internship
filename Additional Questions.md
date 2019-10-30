1. Some Phone Cases may have cameras, buttons and other artifacts that can't be covered by the customization. What would you do to avoid that a customization would be plotted on top of one of those artifacts? A customization may be a name, but it can also be a picture or another complex element choosen by the client.

- Image processing methods like use filters such as Sobel, Canny or Prewitt can be used for detection of edges and artifacts that could disrupt printing. And after highlighting obstacles, you can resize or modify the object to be printed for a better fit.


2. Some people have small names and it would be interesting to use a larger font size. But other people have large names and it would be interesting to use a smaller font size. What would you change to handle this situation?

- Using the PX unit of measurement for a font size parameterization, we can get a clearer idea of ​​what will be plotted (name or image), because the PX unit, in most cases, returns the dimensions according to the device's fixed pixels.


3. Sometimes there's a problem with the generated preview. The colors seen by the client in his screen may be quiet diffent from the colors that come out of the printers. What would you do to handle the variation in colors between preview and printed product?

- For images with good resolution, methods like RGB to CMYK conversion (to ensure screen-to-print color fidelity) and ever keep the rasterization of the image even after the additions of effects and other changes
