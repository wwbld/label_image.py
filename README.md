# label_image.py

1. Follow the instruction from https://codelabs.developers.google.com/codelabs/tensorflow-for-poets/#0 to be able to use tensorflow to classify images.
2. I modified the given file "label_image.py" in following ways:
   (1) To use this file, in Docker container, type "python label_image.py source destination", change the source and destination with proper names, the source is the directory name where you store images to be checked, the destination is the directory name where the recognized imaged will be copyed into with different sub-directories been built automatically.
   (2) The output on console will show that how many images have been processed.
   (3) However, in my laptop, it cannot handle images more than 30 or the laptop will stop working, so it still needs to be improved.
