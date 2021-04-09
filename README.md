# Detecting Vairous products in A Retail Shop

### Challenges 
- Thousands of products and hundreds of vaients of different product
- Cannot label different products individually 
- Text is found in various fonts, orientation and sizes
- Each frame of video has to be processed 

### Strategy
- We to use written content on product
- We also use object classification of different images in imagenet 
- It would be possible to map the classification and text to product in a catalogue(for a real case scenario)

### Solutions
- Using imagenet trained model 
- Using CRAFT to read labels and texts on  each products

### Limitations 
- Difficult to use in realtime videos, as the CRAFT method is slow in CPU 
 

<img width="1000" alt="teaser" src="./figures/craft_example.gif">



