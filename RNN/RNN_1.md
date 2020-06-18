# Recurrent Neural Network
## Why RNN?
Take time factor into consideration.<br>
RNN network seems to have **_memory_**, people use it to analyze videos, context and something else with relation to **time**.
## Application of RNN
- NLP (Natural Language Processing)
- Voice Recognition
- Image Capturing
- Text Similarity Analysis
- Recommendation System (Youtube, Ebay, TaoBao)
## How RNN get "memory"?
Like common NN, RNN is made up of **Input Layer**, **Hidden Layer**, **Output Layer**.<br>
![alt text](https://github.com/wangruiling888/NN-learning/blob/master/RNN/pic1.png) <br>
The differences between other NN and RNN is that: The hidden layer of RNN has a circle for accpeting input at different moment.<br>
![alt text](https://github.com/wangruiling888/NN-learning/blob/master/RNN/pic2.png) <br>
**t-1, t, t+1** stands for time series, **X** is input, **St** is the statement at time **t**, **U, W, V** are all weights:
- **U** is the weight for current input **Xt**.
- **W** is the weight of input for last time point
- **V** is weight of output<br>
when t = 0, we have:<br>
![alt text](https://github.com/wangruiling888/NN-learning/blob/master/RNN/pic3.png) <br>
f(x) and g(x) are both **activation function**<br>
We have output:<br>
![alt text](https://github.com/wangruiling888/NN-learning/blob/master/RNN/pic4.png)<br>
**Hidden layer: S = f(current statement + previous conclusion)**<br>
## Back Propagation of RNN
Using Back Propagation through time. The mathematical theory is **_Gradient Descent_**.


