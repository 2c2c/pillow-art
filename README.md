Randomly draw a geometric shape until it resembles the source image. Looks neat and is much easier than you'd think.

```
read source image source
make a blank image img1
make a blank image img2
get unique list of colors in source image
loop:
  draw shape using random color from colors to img1
  compare color distance between img1/img2 and source
  if img1 is worse revert to copy from img2
  if img1 is better make img2 a copy of img1
```

If you manually implement your own drawing algorithm you can get a 100x speedup by checking the color distance *before* drawing. This lets you work with one image (if the color distance is worse just dont apply the change). I wrote this to mess with Pillow so I wasn't really concerned with performance.

With enough iterations you can make any image look pretty using this method.

![lines](https://i.imgur.com/SQmNVvv.gif)

![ellipses](https://i.imgur.com/es8Z9mh.gif)