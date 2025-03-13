# Architecture
## Layers
### Definition: What is a layer?
A **layer** in an artificial neural network is a group of neurons  that process and transform input data. Each layer takes input from the previous layer, performs computations, and sends its output to the next layer.
> **And in Keras?** Layers are the basic building blocks of neural networks in Keras. A layer consists of a tensor-in tensor-out computation function (the layer's call method) and some state, held in TensorFlow variables (the layer's weights).
### Different Types of layers : Input Layer - Hidden Layer - Output Layer
In Artificial Neural Networks data flows from the input layer to the output layer through one or more hidden layers. Each layer consists of neurons that receive input, process it, and pass the output to the next layer. The layers work together to extract features, transform data, and make predictions.

---
`Input layer`:
- First Layer: Receives the initial data.
- The number of neurons in this layer is equal to the features in the data
- Function: Passes data to the hidden layers
- Example: For an image, the input layer would have neurons for each pixel value.

---
`Hidden layers`
- Intermediate Layer(s): Perform computations and extract features from the input data.
- Each hidden layer applies a set of weights and biases to the input data, followed by an activation function to introduce non-linearity.

---
`Output layer`:
- final layer: Produces the final result or prediction.
- The number of neurons in this layer corresponds to the number of classes in a classification problem or the number of outputs in a regression problem.
> **And in Keras?** In Keras there are also different types of hidden layers: e.g. Preprocessing Layers (we've already learned the NormalizationLayer), Regularization Layers or Activation Layers (read more [here](https://keras.io/api/layers/)). You can even create your own layer!!
### How many hidden layers do we need?
|# of hidden layers|result|
|---|---|
|none|only capable of representing linear separable functions or decisions|
|1|Can approximate any function that contains a continuous mapping from one finite space to another|
|2|Can represent an arbitrary decision boundary to arbitrary accuracy with rational activation functions and can approcimate any smooth mapping to any accuracy|

For many problems, a single hidden layer is often enough. According to the Universal Approximation Theorem, a neural network with just one hidden layer can approximate any continuous function, as long as you have enough neurons. Adding a second hidden layer can allow the network to learn more complex patterns and hierarchical features.
**Neural networks with more layers can represent functions in more compact form**
## Neurons
### Definition: What is a Neuron?
A neuron in a neural network is a basic unit of computation that receives input, processes it, and produces an output. The input refers to the features of the dataset, which are the individual pieces of data (variables) that describe each observation.
### How many Neurons in the hidden layers?
| **Number of Neurons**   | **Capacity to Learn**                             | **Model Complexity**                        | **Risk of Overfitting**              | **Computational Cost**              |
|--------------------------|---------------------------------------------------|--------------------------------------------|--------------------------------------|-------------------------------------|
| **More Neurons**         | ↑ Higher capacity to learn complex patterns      | ↑ More parameters to train                | ↑ Risk of overfitting if data is small | ↑ Increased training time and memory usage |
---
There are many rule-of-thumb methods for determining the correct number of neurons to use in the hidden layers, such as the following:
- The number of hidden neurons should be between the size of the input layer and the size of the output layer.
- The number of hidden neurons should be 2/3 the size of the input layer, plus the size of the output layer.
- The number of hidden neurons should be less than twice the size of the input layer.
### Deep vs. wide ANN
- *Deeper Networks:* More hidden layers can model more complex relationships and hierarchical features. However, deeper networks are harder to train (they require more data and computational power) and are more prone to overfitting without proper regularization techniques. (**Warning: Overfitting!**)
- *Wider Networks*: Instead of adding more layers, increasing the number of neurons in a single layer (making it "wider") might help, especially for tasks that don't require deep representation
### Effect of number per type
| **Neuron Type**            | **Output Range**         | **Common Use**                            | **Effect of Number of Neurons**               | **High Number Effect**                       |
|----------------------------|--------------------------|-------------------------------------------|-----------------------------------------------|----------------------------------------------|
| **Perceptron**              | Binary (0 or 1)          | Basic models                            | More neurons may overfit                     | Limited improvement, higher risk of overfitting |
| **Sigmoid Neuron**          | (0, 1)                   | Binary classification                    | More neurons can overfit, capture patterns    | Can overfit, slower training due to saturation  |
| **ReLU Neuron**             | (0, ∞)                   | Deep networks, CNNs, MLPs                | More neurons improve features, but risk overfitting | Can speed up learning, but risk of overfitting and vanishing gradients in deep networks |
| **Tanh Neuron**             | (-1, 1)                  | RNNs, deep networks                      | More neurons can cause vanishing gradients   | Can increase saturation problems in deeper layers |
| **Softmax Neuron**          | (0, 1) (probabilities)   | Multi-class classification                | More neurons increase classification ability, complexity | More neurons allow for more classes, but increase computation and complexity |
| **Leaky ReLU Neuron**       | (negative, ∞)            | Prevents dead
___
## Epoch
- In ML: One complete pass of the entire training dataset
In mini-batches, the dataset is divided into batches, and an epoch completes when all batches have been processed.
In stochastic gradient descent (SGD), where you pick one random sample at a time, you need as many updates as there are rows before you count it as an epoch.
- In Neural networks: An epoch in a neural network is one complete pass of the entire training dataset through the network, ***during*** which the model's weights are updated to minimize the loss function
### Dynamics of Loss Function Over Time (Epochs) in Neural Networks:
- **Initial Epochs**:
  - High loss due to random weight initialization.
  - Rapid loss decrease as the model adjusts weights.
  - Strong gradient updates lead to significant improvements.
- **Middle Epochs**:
  - Loss reduction slows down as the model refines its learning.
  - Loss may fluctuate due to noisy updates (especially with SGD).
  - Encounter of local minima or saddle points can cause temporary plateaus.
- **Later Epochs**:
  - Loss slows further and may plateau as the model nears convergence.
  - Risk of overfitting as training loss keeps decreasing but validation loss may increase.
- **Very Late Epochs**:
  - Overfitting risk increases, with training loss continuing to decrease but validation loss rising.
  - **Early stopping** may be used to prevent overfitting.
### General Pattern:
1. Rapid loss decrease in early epochs.
2. Slower decrease in middle epochs.
3. Plateaus and potential overfitting in later epochs.
# Parameters of Epochs
| **Parameter**             | **Description**                                                 | **Effect on Training**                              |
|---------------------------|-----------------------------------------------------------------|-----------------------------------------------------|
| **Number of Epochs**      | Total number of times the entire dataset is passed through the model. | More epochs allow the model to learn better, but too many can lead to overfitting. |
| **Batch Size**            | Number of training examples processed in one forward/backward pass. | Affects how often the model weights are updated. Small batches can make updates noisier. |
| **Early Stopping**        | Stops training if the validation loss doesn't improve for a set number of epochs. | Prevents overfitting and saves training time by halting early when no improvements occur. |
| **Learning Rate Scheduling** | Adjusts the learning rate during training (e.g., decaying after certain epochs). | Helps improve convergence speed by lowering the learning rate gradually. |











Message Annette Manntschke, Katharina Baumgarter









---


## Common Loss Functions:

1. Mean Sqaured Error (MSE):
   - Application: Regression
   - Definition: Average Squared differences between predicted and actual values
   - Formula: ![MSE](/neural_networks/images/Screenshot%202025-03-13%20110138.png)
   - Characteristics: penalizes larger error more severely due to squaring, making it sensitive to outliers.
2. Mean Abosulute Error (MEA):
   - Application: Regression
   - Definition: Computes the average absolute differences between predicted and actual values.
   - Formula: ![MEA](/neural_networks/images/Screenshot%202025-03-13%20110644.png)]
   - Characteristics: provides a linear penalty for errors, offering robustness to outliers compared to MSE.
3. Zero-One Loss:
   - Application: Classification.
   - Definition: Assigns a loss of 1 for incorect predictions and 0 for correct ones.
   - Formula: ![Zero](/neural_networks/images/Screenshot%202025-03-13%20110933.png)
   - Characteristics: Measures the accuracy of predictions but is non-differentiable, making it less practical for gradient-based optimization method.
4. Cross-Entropy Loss (Log Loss):
   - Application: Classification.
   - Definition: Measures the dissimilarity between true labels and the predicted probability distributions.
   - Formula: For binary classification: ![](/neural_networks/images/Screenshot%202025-03-13%20111300.png)
   - Characteristics: Encourages the model to output probabilities close to the actual class labels, leading to more confident and accurate predictions.
5. Hinge Loss:
   - Application: Support Vector Machines (SVMs) for classification tasks.
   - Definition: MPenalizes predictions that are correct but not with a sufficient margin.
   - Formula: ![](/neural_networks/images/Screenshot%202025-03-13%20111628.png)
   - Characteristics: Focuses on maximizing the decision margin, promoting better generalization in classifiers.
6. Huber Loss:
   - Application: Regression tasks where robustness to outliers is desired.
   - Definition: Combines the properties of MSE and MAE; it is quadratic for small errors and linear for large errors.
   - Formula: ![](/neural_networks/images/Screenshot%202025-03-13%20111811.png)

   - Characteristics: Offers a balance between sensitivity to small errors and robustness to outliers.
  

