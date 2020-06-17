# Recurrent Neural Network
## Why RNN?
Take time factor into consideration.
RNN network seems to have **_memory_**, people use it to analyze videos, context and something else with relation to **time**.
## Application of RNN
- NLP (Natural Language Processing)
- Voice Recognition
- Image Capturing
- Text Similarity Analysis
- Recommendation System (Youtube, Ebay, TaoBao)
## How RNN get "memory"?
Like common NN, RNN is made up of **Input Layer**, **Hidden Layer**, **Output Layer**.
![alt text](https://github.com/wangruiling888/NN-learning/blob/master/RNN/pic1.png)
The differences between other NN and RNN is that: The hidden layer of RNN has a circle for accpeting input at different moment.
![alt text](https://github.com/wangruiling888/NN-learning/blob/master/RNN/pic2.png)
**t-1, t, t+1** stands for time series, **X** is input, **St** is the statement at time **t**, **U, W, V** are all weights:
- **U** is the weight for current input **Xt**.
- **W** is the weight of input for last time point
- **V** is weight of output
when t = 0, we have:
![alt text](https://github.com/wangruiling888/NN-learning/blob/master/RNN/pic3.png)
f(x) and g(x) are both **activation function**
We have output:
![alt text](https://github.com/wangruiling888/NN-learning/blob/master/RNN/pic4.png)
**Hidden layer: S = f(current statement + previous conclusion)**

