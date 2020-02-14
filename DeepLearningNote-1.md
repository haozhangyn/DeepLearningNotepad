### 多层感知机
  1. 多层感知机的基本知识
  2. 使用多层感知机图像分类的从零开始的实现
  3. 使用pytorch的简洁实现

感知机接收多个输入信号，输出一个信号。
### 激励函数
    全连接层只是对数据做仿射变换（affine transformation），而多个仿射变换的叠加仍然是一个仿射变换。解决问题的一个方法是引入非线性变换，例如对隐藏变量使用按元素运算的非线性函数进行变换，然后再作为下一个全连接层的输入。这个非线性函数被称为激活函数（activation function）。
#### Relu 函数
ReLU（rectified linear unit）函数提供了一个很简单的非线性变换。给定元素$x$
 则表示为 $$y = max(0,x) $$

**优点** ：Relu得到的SGD的收敛速度较快
**缺点**：训练的时候很容易‘die'了，对于小于0的值，这个神经元的梯度永远都会是0，在实际操错中，如果learning rate很大，很可能网络中较多的神经元都'dead'了，即使是较小的learning rate，这种情况也很有可能发生。

#### leakyRelu
数学表达式：$$ y = max(0, x) + leak*min(0,x) $$  （leak是一个很小的常数，这样保留了一些负轴的值，使得负轴的信息不会全部丢失）
也可表示为：

$$
Y =
\begin{cases}
x, & \text{ if x>0} \\[5ex]
x/\alpha, & \text{ if x<0}
\end{cases}
$$ 

``` python 
tensorflow
    tf.nn.leaky_relu(
        features,
        alpha=0.2,
        name=None
    )

```
 Args:
    features: A Tensor representing preactivation values. Must be one of the following types: float16, float32, float64, int32, int64.
    alpha: Slope of the activation function at x < 0.
    name: A name for the operation (optional).
    Returns:
    The activation value.
Source: [Rectifier Nonlinearities Improve Neural Network Acoustic Models.
  AL Maas, AY Hannun, AY Ng - Proc. ICML, 2013](https://ai.stanford.edu/~amaas/papers/relu_hybrid_icml2013_final.pdf).

  
#### Prelu
  
$$
 PRelu(X_i) =
\begin{cases}
x_i, & \text{ if x>0} \\[5ex]
\alpha _i x, & \text{ if x_i \le 0}
\end{cases}
$$ 

其中 $a_i$是可以学习的的。如果$a_i=0$，那么 PReLU 退化为ReLU；如果 $a_i$是一个很小的固定值（如 $a_i=0.01$），则 PReLU 退化为 Leaky ReLU（LReLU）。
PReLU 只增加了极少量的参数，也就意味着网络的计算量以及过拟合的危险性都只增加了一点点。特别的，当不同 channels 使用相同的$ a_i $时，参数就更少了。BP 更新$ a_i $时，采用的是带动量的更新方式（momentum）。

``` pytorch
>>> m = nn.ELU()
>>> input = autograd.Variable(torch.randn(2))
>>> print(input)
>>> print(m(input))
```

 
