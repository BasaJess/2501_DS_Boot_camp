[![Shipping files](https://github.com/neuefische/ds-gradient-descent/actions/workflows/workflow-02.yml/badge.svg?branch=main&event=workflow_dispatch)](https://github.com/neuefische/ds-gradient-descent/actions/workflows/workflow-02.yml)


# Gradient Descent

- Gradient descent is an optimization algorithm widely used  in various fields to minimize a function  and optimize parameters by iteratively moving towards the steepest descent, i.e., the direction of the negative gradient. It's widely employed in training machine learning models and neural networks to reduce errors between predicted and actual outcomes.

- The core idea involves starting with an initial guess and updating it iteratively:

 𝑥 𝑛 + 1 = 𝑥 𝑛 − 𝛾∇𝐹(𝑥𝑛


 - Here, 𝑥𝑛 represents the current point, 𝛾 is the learning rate (step size), and ∇𝐹(Xn) is the gradient of the function at 𝑥𝑛. The learning rate determines the size of the steps taken; if too large, the algorithm may overshoot the minimum, and if too small, convergence can be slow. 

 - An intuitive analogy is descending a foggy mountain: without visibility, you would feel the slope and step in the steepest downward direction, repeating this process to reach the base. 

 - Gradient descent has several variants:

   - Batch Gradient Descent: Uses the entire dataset to compute the gradient, which can be computationally intensive for large datasets.

   - Stochastic Gradient Descent (SGD): Uses a single data point to compute the gradient, leading to faster but noisier updates.

   - Mini-batch Gradient Descent: Balances the two by using a subset of data points, offering a trade-off between computation efficiency and convergence stability.
 
 - Choosing the appropriate variant and tuning the learning rate are crucial for the effective application of gradient descent in various optimization problems.
 ---
## when do I use it?
 - You would employ gradient descent in scenarios where you need to find the minimum of a function, particularly when dealing with large datasets or complex models where analytical solutions are impractical.
  - Common applications include:
    - Machine Learning and Deep Learning: Training models such as linear regression, logistic regression, support vector machines, and neural networks involves minimizing a cost function to improve predictive accuracy. Gradient descent iteratively adjusts model parameters to achieve this minimization
    - Natural Language Processing (NLP): Tasks like language translation, sentiment analysis, and text classification utilize models optimized through gradient descent to handle the complexities of human language.
    - Computer Vision: In image recognition and object detection, convolutional neural networks (CNNs) are trained using gradient descent to accurately interpret visual data.
    - Finance: Gradient descent aids in portfolio optimization by adjusting asset allocations to maximize returns while minimizing risk.
    - Engineering: Design optimization, such as refining the shape of an aircraft wing for better aerodynamics, employs gradient descent to fine-tune parameters for optimal performance.
- In essence, you would use gradient descent whenever you need an efficient method to find the minimum of a function, especially in high-dimensional spaces common in machine learning, engineering, and finance.
---
## How do I use it?
To apply gradient descent, follow these steps:
 1. Define the Objective Function: Determine the function 𝑓(𝑥)you aim to minimize. This function should be differentiable.

 2. Compute the Gradient: Calculate the gradient ∇𝑓(𝑥), which is a vector of partial derivatives indicating the function's slope with respect to each variable.

 3. Initialize Parameters: Choose initial values for the parameters 𝑥. Initialization can influence the convergence and outcome.

 4. Set Hyperparameters: Decide on the learning rate 𝛾(step size) and the number of iterations or a convergence criterion.

 5. Iterate Updates: Update the parameters iteratively using the rule: 𝑥𝑛+1=𝑥𝑛−𝛾∇𝑓(𝑥𝑛) Repeat this process until convergence or for a set number of iterations

---
The objective of ANY Machine Learning Model is to find parameters, weights or a structure that minimizes the Cost function.

A way to minimize the Cost function is Gradient Descent. We want to dive deep into this very basic ML method and try to understand Gradient Descent on a very granular level.

## Task

Please work through the notebooks in this particular order:

1. [Gradient_Descent](1_Gradient_Descent.ipynb)
2. [Gradient_Descent_Visuallization](2_Gradient_Descent_Visualization.ipynb)
3. [Gradient_Descent_Codealong](3_Gradient_Descent_Codealong.ipynb)
4. [Bonus_Classification](4_Bonus_Classification.ipynb)

In the first notebook, you will see the code that performs each step of the gradient descent. Try to understand what happens in each line and document each step. The second notebook shows you what gradient descent really looks like (visually), and in the third notebook it's your job to write the code for gradient descent from scratch. In the last notebook, you will see a simple classification example that will give you a little preview of what to expect in the next few days.


## Set up your Environment

Please make sure you have forked the repo and set up a new virtual environment. For this purpose you can use the following commands:

The added [requirements file](requirements.txt) contains all libraries and dependencies we need to execute the Gradient Descent notebooks.

*Note: If there are errors during environment setup, try removing the versions from the failing packages in the requirements file. M1 shizzle.*

### **`macOS`** type the following commands : 


- Install the virtual environment and the required packages by following commands:

    ```BASH
    pyenv local 3.11.3
    python -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    ```
### **`WindowsOS`** type the following commands :

- Install the virtual environment and the required packages by following commands.

   For `PowerShell` CLI :

    ```PowerShell
    pyenv local 3.11.3
    python -m venv .venv
    .venv\Scripts\Activate.ps1
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

    For `Git-Bash` CLI :
    ```
    pyenv local 3.11.3
    python -m venv .venv
    source .venv/Scripts/activate
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```
