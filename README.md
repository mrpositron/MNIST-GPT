# Can ChatGPT and GPT-4 classify MNIST digits (without images)?

> Not really. But it's fun to try.

## Introduction

Once upon a time, I was reading about GPT-3.5/4 and its capabilities. I was wondering if it can classify MNIST digits. I thought it would be interesting to see if it can do that. So, I decided to give it a try.

## Method

### Data
I took MNIST dataset (test split) and sampled 100 images. The size of each image is 28x28. Feeding these images to GPT might not be a good idea because 784-d input is a bit to large. Instead, I decided to return coordinates of non-zero pixels in each image. Then, I selected `k` distant pixels from each other. Finally, I converted these coordinates to a string and fed it to GPT.


Digit **(0)** is represented by the following string:
```
(5,20);(23,8);(18,19);(11,10);(4,13);(11,17);(17,7);(19,13);(13,21);(22,16);(7,16);(15,11);(15,16);(9,21);(23,12);(9,13);(4,17);(12,14);(14,8);(18,10);(20,6);
```
And you can see the sampled image below.

Original MNIST image | Sampled MNIST image
:---------------------:|:---------------------:
![Original MNIST](temp_1.png) | ![Sampled MNIST](temp_0.png)

### Prompt

Now, I needed to come up with a prompt. I decided to include some examples from the training set. The prompt is as follows:
```
Given (x, y) coordinates of non-zero pixels in a 28x28 grayscale image representing a digit, classify the digit between 0 and 9.  Input format: "(x0,y0);(x1,y1);(x2,y2);..." with coordinates sorted first in the x-axis and then in the y-axis. PLEASE RETURN ONLY the digit number in brackets, e.g., if the digit is 3, return "(3)".

Examples:
(0): (0,0); (0,1); ...
```

## Results
`k` = 20
|Model|Version|Accuracy|F1 Score|
|---|---|---|---|
|GPT-3.5|gpt-3.5-turbo-0125|0.2|0.18| 
|GPT-4|gpt-4-0125-preview|0.19|0.12| 
|   |gpt-4|0.15|0.13| 

Let's experiment with different values of k and see if we can improve the performance.

|k|Accuracy|F1 Score|
|---|---|---|
|10|0.16|0.15|
|20|0.2|0.18|
|40|0.18|0.15|

## Conclusion

GPT-3.5 and GPT-4 are not good at classifying MNIST digits. I thought GPT-s will have some spatial understanding, but it seems like they don't. The accuracy is around 20% and F1 score is around 0.18. It's not surprising because GPTs are not designed for this task. However, it was fun to try.
