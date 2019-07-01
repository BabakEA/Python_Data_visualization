#!/usr/bin/env python
"""
Masked wordcloud
================

Using a mask you can generate wordclouds in arbitrary shapes.
"""

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

from wordcloud import WordCloud, STOPWORDS

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
text = open(path.join(d, 'AI.txt')).read()


Text_mask = np.array(Image.open(path.join(d, "canada.jpg")))

stopwords = set(STOPWORDS)
#stopwords.add("your words")

wc = WordCloud(background_color="white", max_words=2000, mask=Text_mask,
               stopwords=stopwords, contour_width=3, contour_color='steelblue')

# generate word cloud
wc.generate(text)

# store to file
wc.to_file(path.join(d, "result.png"))

# show
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.figure()
plt.imshow(Text_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.show()
